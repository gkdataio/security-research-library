"""Coverage checks for the current public Bugcrowd directory snapshot."""

import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from export_bugcrowd_programs import build, load_vdp_captures


class BugcrowdProgramTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.outputs = build()
        cls.catalog = json.loads(cls.outputs["exports/bugcrowd-programs.json"])

    def test_every_current_public_listing_has_scope_state_and_visual_page(self):
        latest = json.loads((ROOT / "data/program-discovery/bugcrowd-directory-2026-10-03.json").read_text(encoding="utf-8"))
        expected = {item["id"] for item in latest["entries"]}
        programs = self.catalog["programs"]
        self.assertEqual(len(expected), 516)
        self.assertEqual({item["id"] for item in programs}, expected)
        self.assertEqual(self.catalog["counts"]["bug_bounty_category"], 293)
        self.assertEqual(self.catalog["counts"]["vulnerability_disclosure"], 223)
        for item in programs:
            with self.subTest(program=item["id"]):
                page = self.outputs.get(item["visual_page"])
                if page is None:
                    path = ROOT / item["visual_page"]
                    self.assertTrue(path.is_file(), item["visual_page"])
                    page = path.read_text(encoding="utf-8")
                self.assertIn(item["program_url"], page)
                self.assertIn("In-scope entries", page)
                self.assertIn("Out-of-scope entries", page)
                if item["scope_status"] == "captured":
                    self.assertTrue(item["in_scope"] or item["out_of_scope"])
                    self.assertTrue(item["scope_source_urls"])
                else:
                    self.assertEqual(item["in_scope"], [])
                    self.assertEqual(item["out_of_scope"], [])

    def test_counts_and_vdp_capture_identity(self):
        programs = self.catalog["programs"]
        counts = self.catalog["counts"]
        self.assertEqual(counts["current_public_programs"], len(programs))
        self.assertEqual(counts["published_scope_captured"], 507)
        self.assertEqual(counts["by_scope_status"],
                         {"captured": 507, "fetch_failed": 2, "no_published_assets": 7})
        self.assertEqual(counts["published_scope_captured"], sum(p["scope_status"] == "captured" for p in programs))
        self.assertEqual(counts["scope_gaps"], sum(p["scope_status"] != "captured" for p in programs))
        self.assertEqual(counts["in_scope_entries"], sum(len(p["in_scope"]) for p in programs))
        self.assertEqual(counts["out_of_scope_entries"], sum(len(p["out_of_scope"]) for p in programs))
        current = {p["id"]: p for p in programs}
        captures = load_vdp_captures(ROOT, current, self.catalog["directory_snapshot_date"])
        self.assertEqual(len(captures), 223)

    def test_generated_local_links_resolve(self):
        for output_path, content in self.outputs.items():
            if not output_path.endswith(".md"):
                continue
            for href in re.findall(r"\]\((?:<)?([^)>]+)(?:>)?\)", content):
                if href.startswith(("https://", "http://", "#")):
                    continue
                resolved = (ROOT / output_path).parent.joinpath(href.split("#", 1)[0]).resolve()
                relative = str(resolved.relative_to(ROOT)).replace("\\", "/")
                with self.subTest(page=output_path, href=href):
                    self.assertTrue(resolved.is_file() or relative in self.outputs)


if __name__ == "__main__":
    unittest.main()
