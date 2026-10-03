"""Checks for the dated public bounty scope catalog."""

import json
from pathlib import Path
import re
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from export_public_bounties import build, load_captures
from export_program_discovery import build as build_discovery


class PublicBountyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.outputs = build()
        cls.catalog = json.loads(cls.outputs["exports/public-bounties.json"])
        cls.discovery_outputs = build_discovery()
        cls.discovery = json.loads(cls.discovery_outputs["exports/program-discovery.json"])

    def test_every_catalog_record_has_visual_and_json_scope(self):
        programs = self.catalog["programs"]
        self.assertEqual(len(programs), self.catalog["counts"]["observed_bounty_candidates"])
        self.assertEqual(len(programs), len({program["id"] for program in programs}))
        for program in programs:
            with self.subTest(program=program["id"]):
                page = "docs/public-bounties/" + program["platform"].lower() + "/" + program["id"] + ".md"
                self.assertIn(page, self.outputs)
                self.assertIn(program["program_url"], self.outputs[page])
                self.assertIn("In-scope entries", self.outputs[page])
                self.assertIn("Out-of-scope entries", self.outputs[page])
                if program["scope_status"] != "captured":
                    self.assertEqual(program["in_scope"], [])
                    self.assertEqual(program["out_of_scope"], [])

    def test_counts_match_asset_rows_and_review_states(self):
        programs = self.catalog["programs"]
        counts = self.catalog["counts"]
        self.assertEqual(counts["in_scope_entries"], sum(len(p["in_scope"]) for p in programs))
        self.assertEqual(counts["out_of_scope_entries"], sum(len(p["out_of_scope"]) for p in programs))
        self.assertEqual(counts["with_published_scope"], sum(p["scope_status"] == "captured" for p in programs))
        for program in programs:
            if program["policy_review_state"] == "scope_table_only":
                self.assertIsNone(program["verified_policy_id"])

    def test_hackerone_nonbounties_are_excluded(self):
        captures = {c["listing_id"]: c for c in json.loads(
            (ROOT / "data/public-bounty-scopes.json").read_text(encoding="utf-8"))["captures"]}
        selected = {program["id"] for program in self.catalog["programs"]}
        for listing_id, capture in captures.items():
            if capture["status"] == "not_paid_bounty":
                self.assertNotIn(listing_id, selected)

    def test_capture_identity_and_source_host_are_validated(self):
        listings = self.discovery["listings"]
        _, captures = load_captures(ROOT, listings)
        self.assertEqual(len(captures), len({c["listing_id"] for c in json.loads(
            (ROOT / "data/public-bounty-scopes.json").read_text(encoding="utf-8"))["captures"]}))
        self.assertGreater(len(captures), 0)

    def test_discovery_links_to_public_bounty_pages(self):
        for platform in ("Bugcrowd", "HackerOne", "Intigriti"):
            page = self.discovery_outputs["docs/program-discovery/" + platform.lower() + ".md"]
            for program in self.catalog["programs"]:
                if program["platform"] == platform:
                    self.assertIn("../public-bounties/" + platform.lower() + "/" + program["id"] + ".md", page)

    def test_generated_local_links_resolve(self):
        for output_path, content in self.outputs.items():
            if not output_path.endswith(".md"):
                continue
            for href in re.findall(r"\]\((?:<)?([^)>]+)(?:>)?\)", content):
                if href.startswith(("https://", "http://", "#")):
                    continue
                local_path = href.split("#", 1)[0]
                resolved = (ROOT / output_path).parent.joinpath(local_path).resolve()
                with self.subTest(page=output_path, href=href):
                    self.assertTrue(resolved.is_file() or str(resolved.relative_to(ROOT)).replace("\\", "/") in self.outputs)


if __name__ == "__main__":
    unittest.main()
