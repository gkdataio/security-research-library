"""HTTP monitoring guards use only synthetic responses and local state."""

import hashlib
from http.client import IncompleteRead
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_program_changes as changes


URL = "https://example.invalid/program?type=team"
TARGETS = {URL: {"programs": ["listing:example"], "platforms": ["Independent"],
                 "roles": ["program_page"]}}


class Response:
    def __init__(self, code=200, headers=None, body=b"hello", error=None):
        self.code = code
        self.headers = {"Content-Type": "text/html", **(headers or {})}
        self.body = body
        self.error = error
        self.read_limits = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return None

    def read(self, limit):
        self.read_limits.append(limit)
        if self.error:
            raise self.error
        return self.body[:limit]


def fetch(response, prior=None, **kwargs):
    opener = Mock()
    opener.open.return_value = response
    result = changes.fetch_official_page(URL, prior, opener=opener, **kwargs)
    opener.open.assert_called_once()
    # Display redaction must not change a legitimate request's URL identity.
    assert opener.open.call_args.args[0].full_url == URL
    return result


class RedirectPrivacyTests(unittest.TestCase):
    def test_redirect_discards_userinfo_and_raw_paths_queries_and_fragments(self):
        location = ("https://synthetic-user:synthetic-password@example.invalid:8443/"
                    "arbitrary/synthetic-path-token?code=synthetic-query-token#synthetic-fragment")
        result = fetch(Response(code=302, headers={"Location": location}))
        target = result["fingerprint"]["redirect_to"]
        self.assertEqual(target, {
            "origin": "https://example.invalid:8443",
            "path_sha256": hashlib.sha256(b"/arbitrary/synthetic-path-token").hexdigest(),
        })
        self.assertNotIn("synthetic-", json.dumps(result))

    def test_relative_redirects_keep_path_identity_without_plaintext(self):
        first = changes._safe_redirect(URL, "/program/one?code=first#scope")
        equivalent = changes._safe_redirect(URL, "/program/one?code=second#other")
        second = changes._safe_redirect(URL, "/program/two")
        self.assertEqual(first, equivalent)
        self.assertNotEqual(first, second)
        self.assertEqual(first["origin"], "https://example.invalid")
        self.assertNotIn("/program/", json.dumps([first, second]))
        ipv6 = changes._safe_redirect(URL, "https://user:password@[2001:db8::1]:8443/program")
        self.assertEqual(ipv6["origin"], "https://[2001:db8::1]:8443")

    def test_malformed_and_non_web_redirects_do_not_raise_or_retain_text(self):
        for location in (None, "", "https://[invalid", "https://example.invalid:bad/path",
                         "javascript:synthetic-token", "data:text/plain,synthetic-token",
                         "https://example.invalid/\nsynthetic-token",
                         "https://example.invalid\\synthetic-token/path",
                         "https://example.invalid%2Fsynthetic-token/path",
                         "https://[::1%25synthetic-token]/path",
                         "https://example.invalid/\ud800"):
            with self.subTest(location=location):
                self.assertIsNone(changes._safe_redirect(URL, location))

    def test_legacy_redirects_are_sanitized_in_state_and_change_reports(self):
        location = "https://synthetic-user:synthetic-password@example.invalid/arbitrary/synthetic-path-token"
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            state.write_text(json.dumps({"schema_version": "1.0.0", "pages": {URL: {
                "fingerprint": {"status": 302, "redirect_to": location},
                "checked_at": "2020-01-01T00:00:00Z",
            }}}))
            observed = fetch(Response(code=302, headers={"Location": "/other"}))
            report = changes.check_live(TARGETS, state, fetcher=Mock(return_value=observed), interval=0)
            self.assertEqual(report["counts"]["changed"], 1)
            self.assertNotIn("synthetic-", state.read_text() + json.dumps(report))
            self.assertEqual(set(json.loads(state.read_text())["pages"]), {URL})

    def test_legacy_redaction_alone_is_not_a_destination_change(self):
        location = "https://example.invalid/program/unchanged"
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            state.write_text(json.dumps({"schema_version": "1.0.0", "pages": {URL: {
                "fingerprint": {"status": 302, "redirect_to": location},
                "checked_at": "2020-01-01T00:00:00Z",
            }}}))
            observed = fetch(Response(code=302, headers={"Location": location}))
            report = changes.check_live(TARGETS, state, fetcher=Mock(return_value=observed), interval=0)
            self.assertEqual(report["counts"]["unchanged"], 1)
            self.assertEqual(report["signals"], [])

    def test_legacy_redaction_is_persisted_without_requests_but_plan_is_read_only(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            state.write_text(json.dumps({"schema_version": "1.0.0", "pages": {URL: {
                "fingerprint": {"status": 302, "redirect_to": URL + "/synthetic-path-token"},
                "checked_at": changes._now(),
            }}}))
            original = state.read_bytes()
            no_fetch = Mock(side_effect=AssertionError("unexpected request"))
            changes.check_live(TARGETS, state, plan=True, fetcher=no_fetch)
            self.assertEqual(state.read_bytes(), original)
            report = changes.check_live(TARGETS, state, fetcher=no_fetch)
            self.assertEqual(report["counts"]["requests"], 0)
            self.assertNotIn("synthetic-path-token", state.read_text())
            no_fetch.assert_not_called()


class CompleteResponseTests(unittest.TestCase):
    def test_declared_length_must_match_body(self):
        for length in ("100", "4"):
            with self.subTest(length=length):
                result = fetch(Response(headers={"Content-Length": length}))
                self.assertEqual(result, {"kind": "unavailable", "status": 200,
                                          "reason": "incomplete_response"})

    def test_malformed_lengths_are_unavailable_not_baselines(self):
        for length in ("bad", "-5", "+5", "5, 5", "", "5.0", "\u0665"):
            with self.subTest(length=length):
                result = fetch(Response(headers={"Content-Length": length}))
                self.assertEqual(result["reason"], "invalid_content_length")
                self.assertNotIn("fingerprint", result)

    def test_complete_bounded_bodies_still_have_fingerprints(self):
        for headers in ({}, {"Content-Length": "5"}, {"Content-Length": " 5 "}):
            with self.subTest(headers=headers):
                response = Response(headers=headers)
                result = fetch(response, max_bytes=5)
                self.assertEqual(result["kind"], "observed")
                self.assertEqual(result["fingerprint"]["sha256"], hashlib.sha256(b"hello").hexdigest())
                self.assertEqual(response.read_limits, [6])

    def test_oversized_declared_body_is_rejected_without_reading(self):
        response = Response(headers={"Content-Length": "100"})
        result = fetch(response, max_bytes=5)
        self.assertEqual(result["reason"], "response_too_large")
        self.assertEqual(response.read_limits, [])

    def test_read_errors_preserve_last_good_state_without_error_text(self):
        for error in (IncompleteRead(b"synthetic-partial-body", 10),
                      OSError("synthetic-error-value"), TimeoutError("synthetic-timeout-value")):
            with self.subTest(error=type(error).__name__), tempfile.TemporaryDirectory() as directory:
                state = Path(directory) / "state.json"
                prior = {"fingerprint": {"status": 200, "sha256": "last-good"}, "etag": "old-etag",
                         "checked_at": "2020-01-01T00:00:00Z"}
                state.write_text(json.dumps({"schema_version": "1.0.0", "pages": {URL: prior}}))
                result = fetch(Response(error=error), prior)
                self.assertEqual(result["kind"], "unavailable")
                report = changes.check_live(TARGETS, state, fetcher=Mock(return_value=result), interval=0)
                after = json.loads(state.read_text())["pages"][URL]
                self.assertEqual(after["fingerprint"], prior["fingerprint"])
                self.assertEqual(after["etag"], prior["etag"])
                self.assertNotIn("synthetic-", state.read_text() + json.dumps(report))

    def test_short_body_never_replaces_last_good_hash_or_cache_headers(self):
        result = fetch(Response(headers={"Content-Length": "100", "ETag": "new-etag"}))
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            prior = {"fingerprint": {"status": 200, "sha256": "last-good"}, "etag": "old-etag",
                     "checked_at": "2020-01-01T00:00:00Z"}
            state.write_text(json.dumps({"schema_version": "1.0.0", "pages": {URL: prior}}))
            report = changes.check_live(TARGETS, state, fetcher=Mock(return_value=result), interval=0)
            after = json.loads(state.read_text())["pages"][URL]
            self.assertEqual(report["counts"]["unavailable"], 1)
            self.assertEqual(after["fingerprint"], prior["fingerprint"])
            self.assertEqual(after["etag"], prior["etag"])


class RateLimitResumeTests(unittest.TestCase):
    def test_rate_limit_failure_is_persisted_before_stopping_and_skipped_on_resume(self):
        for existing in (False, True):
            with self.subTest(existing=existing), tempfile.TemporaryDirectory() as directory:
                state = Path(directory) / "state.json"
                prior = {"fingerprint": {"status": 200, "sha256": "last-good"}, "etag": "old-etag",
                         "checked_at": "2020-01-01T00:00:00Z"}
                if existing:
                    state.write_text(json.dumps({"schema_version": "1.0.0", "pages": {URL: prior}}))
                limited = Mock(return_value={"kind": "unavailable", "status": 429, "reason": "rate_limited"})
                first = changes.check_live(TARGETS, state, fetcher=limited, interval=0)
                self.assertEqual(first["counts"]["rate_limited"], 1)
                stored = json.loads(state.read_text())["pages"][URL]
                self.assertTrue(stored["attempted_at"])
                self.assertEqual(stored["last_failure"], {"status": 429, "reason": "rate_limited"})
                if existing:
                    self.assertEqual(stored["fingerprint"], prior["fingerprint"])
                    self.assertEqual(stored["etag"], prior["etag"])
                second = changes.check_live(TARGETS, state, fetcher=limited, interval=0)
                self.assertEqual(second["counts"]["skipped_unavailable"], 1)
                self.assertEqual(second["counts"]["requests"], 0)
                limited.assert_called_once()
                # Preserve the documented, explicit recheck option.
                changes.check_live(TARGETS, state, fetcher=limited, interval=0, skip_recent_hours=0)
                self.assertEqual(limited.call_count, 2)


if __name__ == "__main__":
    unittest.main()
