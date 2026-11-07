"""Excluded sources stay offline across every existing scope collection path."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_program_changes as changes
import refresh_program_scopes as refresh
from source_access import (EXCLUDED_BUGCROWD_ENGAGEMENTS, EXCLUSION_REASON,
                           SourceAccessExcluded, excluded_source_reason)


SLUGS = ("fmshrc-vdp", "abmc-vdp", "oshrc-vdp")
URLS = tuple("https://bugcrowd.com/engagements/" + slug for slug in SLUGS)


def targets(urls):
    return {url: {"programs": ["listing:example"], "roles": ["scope_source"],
                  "platforms": ["Bugcrowd"]} for url in urls}


class SourceAccessTests(unittest.TestCase):
    def test_exact_exclusions_cover_aliases_and_children_not_nearby_identities(self):
        self.assertEqual(EXCLUDED_BUGCROWD_ENGAGEMENTS, frozenset(SLUGS))
        for slug in SLUGS:
            for host in ("bugcrowd.com", "www.bugcrowd.com", "BUGCROWD.COM"):
                for path in (f"/engagements/{slug}", f"/engagements/{slug}/",
                             f"/engagements/{slug}/changelog/old-version.json",
                             f"/engagements/{slug}?view=brief", f"/engagements/{slug}#scope",
                             f"/engagements/{slug.upper()}", f"/engagements/{slug}%2Fchangelog/a.json",
                             f"/engagements/other/../{slug}"):
                    with self.subTest(host=host, path=path):
                        self.assertEqual(excluded_source_reason("https://" + host + path), EXCLUSION_REASON)
            for url in (f"https://bugcrowd.com/engagements/{slug}-other",
                        f"https://bugcrowd.com/engagements/other-{slug}",
                        f"https://hackerone.com/{slug}",
                        f"https://example.com/engagements/{slug}"):
                self.assertIsNone(excluded_source_reason(url))
        self.assertIsNone(excluded_source_reason("https://bugcrowd.com/engagements"))

    def test_scope_http_client_never_opens_excluded_program_or_brief(self):
        client = refresh.PublicClient()
        client.opener = Mock()
        for base in URLS:
            for host_url in (base, base.replace("//bugcrowd.com", "//www.bugcrowd.com")):
                for url in (host_url, host_url + "/changelog/version.json"):
                    with self.subTest(url=url), patch.object(refresh.time, "sleep") as sleep:
                        with self.assertRaises(SourceAccessExcluded):
                            client.get(url)
                        sleep.assert_not_called()
        client.opener.open.assert_not_called()

    def test_brief_parser_never_calls_injected_fetcher_for_excluded_program(self):
        get = Mock(side_effect=AssertionError("Excluded brief requested"))
        for url in URLS:
            slug = url.rsplit("/", 1)[-1]
            page = json.dumps({"getBriefVersionDocument": f"/engagements/{slug}/changelog/version"})
            with self.assertRaises(SourceAccessExcluded):
                refresh.parse_brief(url, page, get)
        get.assert_not_called()

    def test_refresh_retains_all_overlapping_records_byte_for_byte(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data/programs").mkdir(parents=True)
            records = [{"program_url": url, "platform": "Bugcrowd", "captured_at": "old-capture",
                        "source_url": url + "/changelog/old.json", "assets": [{"name": "old", "scope": "in"}]}
                       for url in URLS]
            for name in refresh.CAPTURES:
                refresh.dump(root / name, {"captures": records})
            for index, row in enumerate(records):
                refresh.dump(root / f"data/programs/{index}.json",
                             {**row, "last_verified_at": "old-policy", "asset_scope": {"verified_at": "old-scope"}})
            before = {path: path.read_bytes() for path in (root / "data").rglob("*.json")}
            client = Mock()
            client.get.side_effect = AssertionError("Excluded source requested")
            audit = refresh.refresh(root, client)
            client.get.assert_not_called()
            self.assertEqual(audit["counts"], {"refreshed": 0, "failed": 0, "deferred": 3,
                                              "unsupported": 0, "total": 3, "attempted": 0})
            self.assertEqual({row["program_url"] for row in audit["results"]}, set(URLS))
            for row in audit["results"]:
                self.assertEqual(row["reason_code"], "source_excluded")
                self.assertEqual(row["verification_status"], "unknown")
                self.assertNotIn("attempted_at", row)
                self.assertNotIn("captured_at", row)
            for path, content in before.items():
                self.assertEqual(path.read_bytes(), content)

    def test_change_http_boundary_never_opens_excluded_program_or_brief(self):
        opener = Mock()
        for base in URLS:
            for url in (base, base + "/changelog/version.json",
                        base.replace("//bugcrowd.com", "//www.bugcrowd.com") + "/changelog/version.json"):
                observed = changes.fetch_official_page(url, opener=opener)
                self.assertEqual(observed["kind"], "deferred")
                self.assertEqual(observed["reason"], "source_excluded")
                self.assertEqual(observed["verification_status"], "unknown")
                self.assertNotIn("fingerprint", observed)
        opener.open.assert_not_called()

    def test_change_checks_and_plans_preserve_last_good_state_without_fetching(self):
        urls = [url + suffix for url in URLS for suffix in ("", "/changelog/old.json")]
        fetch = Mock(side_effect=AssertionError("Excluded source requested"))
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            state.write_text(json.dumps({"schema_version": "1.0.0", "pages": {
                url: {"checked_at": changes._now(), "fingerprint": {"sha256": "old"}} for url in urls}}))
            before = state.read_bytes()
            for plan in (False, True):
                for skip_recent_hours in (0, 12):
                    report = changes.check_live(targets(urls), state, plan=plan, fetcher=fetch,
                                                skip_recent_hours=skip_recent_hours, max_requests=0)
                    self.assertEqual(report["counts"]["deferred"], 6)
                    self.assertEqual(report["counts"]["requests"], 0)
                    self.assertEqual(len(report["signals"]), 6)
                    for row in report["signals"]:
                        self.assertEqual(row["reason"], "source_excluded")
                        self.assertEqual(row["verification_status"], "unknown")
                    self.assertEqual(state.read_bytes(), before)
            fetch.assert_not_called()

    def test_exclusions_do_not_consume_budget_for_permitted_sources(self):
        allowed = "https://bugcrowd.com/engagements/example"
        fetch = Mock(return_value={"kind": "observed", "fingerprint": {"sha256": "new"}})
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            report = changes.check_live(targets([*URLS, allowed]), state, fetcher=fetch, max_requests=1)
            self.assertEqual(report["counts"]["deferred"], 3)
            self.assertEqual(report["counts"]["requests"], 1)
            self.assertEqual(report["counts"]["baselined"], 1)
            self.assertEqual(fetch.call_args.args[0], allowed)
            self.assertEqual(set(json.loads(state.read_text())["pages"]), {allowed})

    def test_exclusions_remain_explicit_after_rate_limit_stop(self):
        allowed = "https://bugcrowd.com/engagements/example"
        fetch = Mock(return_value={"kind": "unavailable", "status": 429, "reason": "rate_limited"})
        with tempfile.TemporaryDirectory() as directory:
            report = changes.check_live(targets([allowed, *URLS, allowed + "-other"]),
                                        Path(directory) / "state.json", fetcher=fetch)
            self.assertEqual(report["counts"]["deferred"], 4)
            self.assertEqual(report["counts"]["requests"], 1)
            excluded = [row for row in report["signals"] if row.get("reason") == "source_excluded"]
            self.assertEqual({row["url"] for row in excluded}, set(URLS))


if __name__ == "__main__":
    unittest.main()
