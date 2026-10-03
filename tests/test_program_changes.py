"""Program comparison and official-page monitoring stay bounded and evidence-aware."""

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_program_changes import (NoRedirect, check_live, compare_inventories,
                                   fetch_official_page, inventory, official_targets, _load_current)


def fixture():
    return {
        "discovery": {"listings": [{
            "id": "hackerone-example", "name": "Example", "platform": "HackerOne",
            "program_url": "https://hackerone.com/example?type=team",
            "program_type": "paid_bounty", "submission_status": "unknown",
            "directory_card": None, "evidence_note": "", "verified_policy_id": None,
        }]},
        "programs": {"programs": []},
        "bounty_captures": {"captures": [{
            "listing_id": "hackerone-example", "platform": "HackerOne", "status": "captured",
            "source_url": "https://hackerone.com/example/policy_scopes",
            "captured_at": "2026-10-03T00:00:00Z",
            "assets": [{"scope": "in", "name": "https://asset.example.invalid",
                        "asset_type": "domain", "location": None, "group": None,
                        "bounty_eligible": True}],
        }]},
        "vdp_captures": {"captures": []},
    }


class ProgramChangeTests(unittest.TestCase):
    def test_all_stored_programs_are_included_once(self):
        current = _load_current(ROOT)
        records = inventory(current)
        listings = current["discovery"]["listings"]
        policies = current["programs"]["programs"]
        linked = {item["verified_policy_id"] for item in listings if item["verified_policy_id"]}
        self.assertEqual(sum(key.startswith("listing:") for key in records), len(listings))
        self.assertEqual(sum(key.startswith("policy:") for key in records), len(policies) - len(linked))
        targets = official_targets(current)
        expected_urls = {item["program_url"] for item in listings}
        expected_urls.update(item["program_url"] for item in policies)
        expected_urls.update(item["policy_url"] for item in policies)
        expected_urls.update(item["source_url"] for name in ("bounty_captures", "vdp_captures")
                             for item in current[name]["captures"] if item.get("source_url"))
        for policy in policies:
            sources = {item["id"]: item["url"] for item in policy["sources"]}
            if policy.get("asset_scope"):
                expected_urls.update(sources[ident] for ident in policy["asset_scope"]["source_ids"])
        self.assertEqual(set(targets), expected_urls)

    def test_review_time_and_duplicate_cleanup_do_not_raise_program_change(self):
        before = fixture()
        after = copy.deepcopy(before)
        after["bounty_captures"]["captures"][0]["captured_at"] = "2026-10-04T00:00:00Z"
        before["bounty_captures"]["captures"][0]["assets"].append(
            copy.deepcopy(before["bounty_captures"]["captures"][0]["assets"][0]))
        after["bounty_captures"]["captures"][0]["duplicate_source_rows"] = 1
        after["bounty_captures"]["captures"][0]["published_asset_count"] = 2
        self.assertEqual(compare_inventories(inventory(before), inventory(after)), [])

    def test_scope_and_bounty_eligibility_changes_are_reported(self):
        before = fixture()
        after = copy.deepcopy(before)
        after["bounty_captures"]["captures"][0]["assets"][0]["bounty_eligible"] = False
        changes = compare_inventories(inventory(before), inventory(after))
        self.assertEqual(len(changes), 1)
        self.assertEqual(changes[0]["fields"][0]["field"], "capture.in_scope")
        self.assertTrue(changes[0]["fields"][0]["added"])
        self.assertTrue(changes[0]["fields"][0]["removed"])

    def test_latest_directory_absence_is_a_signal_not_closure(self):
        before = fixture()
        before["discovery"]["batches"] = [{"id": "day-one", "platform": "HackerOne",
                                            "reviewed_at": "2026-10-03T00:00:00Z"}]
        before["discovery"]["listings"][0]["observations"] = [{"batch_id": "day-one"}]
        after = copy.deepcopy(before)
        after["discovery"]["batches"].append({"id": "day-two", "platform": "HackerOne",
                                                 "reviewed_at": "2026-10-04T00:00:00Z"})
        changes = compare_inventories(inventory(before), inventory(after))
        self.assertEqual(changes[0]["fields"][0]["field"],
                         "listing.observed_in_latest_directory_batch")
        self.assertEqual((changes[0]["fields"][0]["before"], changes[0]["fields"][0]["after"]),
                         (True, False))

    def test_reviewed_policy_reward_change_is_reported(self):
        policy = json.loads((ROOT / "data/programs/1password-bug-bounty.json").read_text(encoding="utf-8"))
        before = fixture()
        before["programs"]["programs"].append(policy)
        after = copy.deepcopy(before)
        after["programs"]["programs"][0]["last_verified_at"] = "2026-10-04T00:00:00Z"
        self.assertEqual(compare_inventories(inventory(before), inventory(after)), [])
        after["programs"]["programs"][0]["rewards"]["maximum"] += 1
        changes = compare_inventories(inventory(before), inventory(after))
        self.assertEqual(changes[0]["key"], "policy:1password-bug-bounty")
        self.assertIn("policy.rewards.maximum", [item["field"] for item in changes[0]["fields"]])

    def test_live_targets_never_use_asset_row_names(self):
        targets = official_targets(fixture())
        self.assertEqual(set(targets), {"https://hackerone.com/example?type=team",
                                        "https://hackerone.com/example/policy_scopes"})
        self.assertNotIn("https://asset.example.invalid", targets)

    def test_live_baseline_then_change_without_network(self):
        targets = official_targets(fixture())
        serial = {"value": 1}

        def fake_fetch(url, prior, **kwargs):
            return {"kind": "observed", "fingerprint": {"status": 200, "sha256": str(serial["value"])},
                    "etag": None, "last_modified": None}

        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            first = check_live(targets, state, fetcher=fake_fetch, interval=0, skip_recent_hours=0)
            self.assertEqual(first["counts"]["baselined"], 2)
            serial["value"] = 2
            second = check_live(targets, state, fetcher=fake_fetch, interval=0, skip_recent_hours=0)
            self.assertEqual(second["counts"]["changed"], 2)
            self.assertEqual(len(second["signals"]), 2)
            self.assertEqual(len(json.loads(state.read_text(encoding="utf-8"))["pages"]), 2)

    def test_plan_honors_limit_without_fetching_or_writing(self):
        targets = official_targets(fixture())

        def fail_fetch(url, prior, **kwargs):
            raise AssertionError("plan attempted a request")

        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            result = check_live(targets, state, plan=True, max_requests=1, fetcher=fail_fetch)
            self.assertEqual(result["counts"]["planned"], 1)
            self.assertEqual(result["counts"]["deferred"], 1)
            self.assertEqual(result["counts"]["requests"], 0)
            self.assertFalse(state.exists())

    def test_rate_limit_stops_remaining_requests(self):
        targets = official_targets(fixture())
        calls = []

        def rate_limit(url, prior, **kwargs):
            calls.append(url)
            return {"kind": "unavailable", "status": 429, "reason": "rate_limited"}

        with tempfile.TemporaryDirectory() as directory:
            result = check_live(targets, Path(directory) / "state.json", fetcher=rate_limit,
                                interval=0, skip_recent_hours=0)
            self.assertEqual(len(calls), 1)
            self.assertEqual(result["counts"]["rate_limited"], 1)
            self.assertEqual(result["counts"]["deferred"], 1)

    def test_unavailable_pages_are_skipped_during_resume(self):
        targets = official_targets(fixture())
        calls = []

        def unavailable(url, prior, **kwargs):
            calls.append(url)
            return {"kind": "unavailable", "status": 403, "reason": "access_or_server_error"}

        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            first = check_live(targets, state, fetcher=unavailable, interval=0)
            second = check_live(targets, state, fetcher=unavailable, interval=0)
            self.assertEqual(first["counts"]["unavailable"], 2)
            self.assertEqual(second["counts"]["skipped_unavailable"], 2)
            self.assertEqual(second["counts"]["requests"], 0)
            self.assertEqual(len(calls), 2)

    def test_live_fetch_is_bounded_and_does_not_follow_redirects(self):
        self.assertIsNone(NoRedirect().redirect_request(None, None, 302, "Found", {},
                                                        "https://asset.example.invalid"))

        class Response:
            code = 200
            headers = {"Content-Type": "text/html"}

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return None

            def read(self, limit):
                self.requested_limit = limit
                return b"x" * limit

        class Opener:
            def __init__(self):
                self.response = Response()

            def open(self, request, timeout):
                self.url = request.full_url
                return self.response

        opener = Opener()
        result = fetch_official_page("https://hackerone.com/example", max_bytes=4, opener=opener)
        self.assertEqual(result["reason"], "response_too_large")
        self.assertEqual(opener.response.requested_limit, 5)


if __name__ == "__main__":
    unittest.main()
