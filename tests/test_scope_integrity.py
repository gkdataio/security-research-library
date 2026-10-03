"""Reject repeated scope rows and sources bound to another program."""

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from export_bugcrowd_programs import load_vdp_captures
from export_programs import validate_program
from export_public_bounties import build as build_bounties, load_captures
from export_scope_audit import build as build_scope_audit
from scope_integrity import source_belongs_to_program
from validate import Invalid


class ScopeIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bounty_data = json.loads((ROOT / "data/public-bounty-scopes.json").read_text(encoding="utf-8"))
        cls.vdp_data = json.loads((ROOT / "data/bugcrowd-vdp-scopes.json").read_text(encoding="utf-8"))
        cls.listings = {item["id"]: item for item in json.loads(
            (ROOT / "exports/program-discovery.json").read_text(encoding="utf-8"))["listings"]}
        cls.program_schema = json.loads((ROOT / "schema/program.schema.json").read_text(encoding="utf-8"))

    def check_bounty(self, capture):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            (root / "schema").mkdir()
            (root / "schema/public-bounty-scopes.schema.json").write_text(
                (ROOT / "schema/public-bounty-scopes.schema.json").read_text(encoding="utf-8"), encoding="utf-8")
            (root / "data/public-bounty-scopes.json").write_text(json.dumps({
                "schema_version": "1.0.0", "directory_snapshot_date": "2026-10-03",
                "captures": [capture]}), encoding="utf-8")
            return load_captures(root, [self.listings[capture["listing_id"]]])

    def check_vdp(self, capture):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            (root / "schema").mkdir()
            (root / "schema/bugcrowd-vdp-scopes.schema.json").write_text(
                (ROOT / "schema/bugcrowd-vdp-scopes.schema.json").read_text(encoding="utf-8"), encoding="utf-8")
            (root / "data/bugcrowd-vdp-scopes.json").write_text(json.dumps({
                "schema_version": "1.0.0", "directory_snapshot_date": "2026-10-03",
                "captures": [capture]}), encoding="utf-8")
            return load_vdp_captures(root, {capture["listing_id"]: self.listings[capture["listing_id"]]},
                                     "2026-10-03")

    def test_bounty_duplicate_row_rejected(self):
        capture = copy.deepcopy(next(item for item in self.bounty_data["captures"]
                                     if item["name"] == "MetaMask"))
        capture["assets"].append(copy.deepcopy(capture["assets"][0]))
        capture["published_asset_count"] += 1
        with self.assertRaisesRegex(Invalid, "duplicate scope row"):
            self.check_bounty(capture)

    def test_distinct_hackerone_bounty_eligibility_is_preserved(self):
        capture = copy.deepcopy(next(item for item in self.bounty_data["captures"]
                                     if item["name"] == "MetaMask"))
        different = copy.deepcopy(capture["assets"][0])
        different["bounty_eligible"] = not different["bounty_eligible"]
        capture["assets"].append(different)
        capture["published_asset_count"] += 1
        self.check_bounty(capture)

    def test_bounty_same_host_sibling_source_rejected(self):
        capture = copy.deepcopy(next(item for item in self.bounty_data["captures"]
                                     if item["name"] == "MetaMask"))
        capture["source_url"] = "https://hackerone.com/paypal/policy_scopes"
        with self.assertRaisesRegex(Invalid, "different program"):
            self.check_bounty(capture)

    def test_gap_review_must_point_to_same_program(self):
        capture = copy.deepcopy(next(item for item in self.bounty_data["captures"]
                                     if item["name"] == "Django"))
        capture["gap_review"]["policy_url"] = "https://hackerone.com/paypal/policy_scopes"
        with self.assertRaisesRegex(Invalid, "not this program policy"):
            self.check_bounty(capture)

    def test_vdp_duplicate_and_sibling_source_rejected(self):
        capture = copy.deepcopy(next(item for item in self.vdp_data["captures"]
                                     if item["status"] == "captured"))
        capture["assets"].append(copy.deepcopy(capture["assets"][0]))
        with self.assertRaisesRegex(Invalid, "duplicate scope row"):
            self.check_vdp(capture)
        capture["assets"].pop()
        capture["source_url"] = "https://bugcrowd.com/engagements/another-program/changelog/version.json"
        with self.assertRaisesRegex(Invalid, "different program"):
            self.check_vdp(capture)

    def test_collapsed_vdp_rows_reconcile_with_original_count(self):
        capture = copy.deepcopy(next(item for item in self.vdp_data["captures"]
                                     if item.get("duplicate_source_rows")))
        self.check_vdp(capture)
        capture["published_asset_count"] += 1
        with self.assertRaisesRegex(Invalid, "published VDP asset count"):
            self.check_vdp(capture)

    def test_verified_platform_source_is_bound_to_program(self):
        record = json.loads((ROOT / "data/programs/1password-bug-bounty.json").read_text(encoding="utf-8"))
        source_id = record["asset_scope"]["source_ids"][0]
        next(s for s in record["sources"] if s["id"] == source_id)["url"] = \
            "https://hackerone.com/paypal/policy_scopes"
        with self.assertRaisesRegex(Invalid, "different program"):
            validate_program(record, self.program_schema)

    def test_verified_distinct_eligibility_allowed_but_repeat_rejected(self):
        record = json.loads((ROOT / "data/programs/1password-bug-bounty.json").read_text(encoding="utf-8"))
        duplicate = copy.deepcopy(record["asset_scope"]["in_scope"][0])
        record["asset_scope"]["in_scope"].append(duplicate)
        with self.assertRaisesRegex(Invalid, "duplicate scope row"):
            validate_program(record, self.program_schema)
        record["asset_scope"]["in_scope"][-1]["bounty_eligible"] = False
        validate_program(record, self.program_schema)

    def test_platform_specific_routes_and_similar_prefixes(self):
        cases = [
            ("Bugcrowd", "https://bugcrowd.com/engagements/alpha",
             "https://www.bugcrowd.com/engagements/alpha/changelog/v1.json", "bugcrowd_scope", True),
            ("Bugcrowd", "https://eu.bugcrowd.net/engagements/alpha",
             "https://eu.bugcrowd.net/engagements/alpha/changelog/v1.json", "bugcrowd_scope", True),
            ("Bugcrowd", "https://bugcrowd.com/engagements/alpha",
             "https://bugcrowd.com/engagements/alpha-extra/changelog/v1.json", "bugcrowd_scope", False),
            ("HackerOne", "https://hackerone.com/alpha?type=team",
             "https://hackerone.com/alpha/policy_scopes", "hackerone_scope", True),
            ("HackerOne", "https://hackerone.com/alpha?type=team",
             "https://hackerone.com/alpha", "hackerone_program", True),
            ("HackerOne", "https://hackerone.com/alpha?type=team",
             "https://hackerone.com/alpha-extra/policy_scopes", "hackerone_scope", False),
            ("Intigriti", "https://app.intigriti.com/programs/org/alpha",
             "https://app.intigriti.com/programs/org/alpha/detail", "intigriti_detail", True),
            ("Intigriti", "https://app.intigriti.com/programs/org/alpha",
             "https://app.intigriti.com/programs/org/alpha/preview/detail", "intigriti_preview", True),
            ("Intigriti", "https://app.intigriti.com/programs/org/alpha",
             "https://app.intigriti.com/programs/org/alpha/tac/detail", "intigriti_terms", True),
            ("Intigriti", "https://app.intigriti.com/programs/org/alpha",
             "https://app.intigriti.com/programs/org/alpha-other/detail", "intigriti_detail", False),
        ]
        for platform, program, source, kind, expected in cases:
            with self.subTest(platform=platform, source=source):
                self.assertEqual(source_belongs_to_program(platform, program, source, kind), expected)

    def test_scope_audit_reconciles_overlapping_catalogs(self):
        audit = json.loads(build_scope_audit()["exports/program-scope-audit.json"])
        counts = audit["counts"]
        self.assertEqual((counts["bugcrowd_public_listings"], counts["cross_platform_bounty_candidates"],
                          counts["catalog_overlap"], counts["distinct_catalog_programs"]),
                         (516, 627, 293, 850))
        self.assertEqual((counts["distinct_scope_captured"], counts["distinct_scope_gaps"],
                          counts["duplicate_source_rows_collapsed"]), (808, 42, 77))
        self.assertEqual(len(audit["unresolved_gaps"]), 42)

    def test_scope_audit_rejects_page_row_count_drift(self):
        outputs = build_bounties()
        page = next(name for name in outputs if name.startswith("docs/public-bounties/hackerone/")
                    and name.endswith(".md"))
        modified = dict(outputs)
        modified[page] = modified[page].replace("In-scope entries (", "In-scope entries (999", 1)
        with patch("export_scope_audit.build_bounties", return_value=modified):
            with self.assertRaisesRegex(Invalid, "generated in-scope heading differs"):
                build_scope_audit()


if __name__ == "__main__":
    unittest.main()
