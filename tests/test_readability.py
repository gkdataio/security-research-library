"""Keep reading order useful without losing evidence or source attribution."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from build_navigation import build, link, text
from validate import validate_library
from validate_extra import validate_all


class ReadabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reports, _ = validate_library()
        cls.resources, _, _ = validate_all()
        cls.pages = build()

    def test_reports_start_with_primary_source_and_takeaway(self):
        for rec in self.reports:
            with self.subTest(report=rec['id']):
                page = self.pages['docs/reports/'+rec['id']+'.md']
                source = next(s for s in rec['sources'] if s['id'] == rec['primary_source_id'])
                original = link('Read the original source', source['url'])
                self.assertLess(page.index(original), page.index('## Main takeaway'))
                self.assertLess(page.index(text(rec['summary'])), page.index('**Organization:**'))
                self.assertLess(page.index(text(rec['summary'])), page.index('Publication window:'))
                for value in [rec['root_cause'], rec['impact'], *rec['defensive_takeaways'],
                              *rec['verification']['limitations'], rec['verification']['reviewed_at']]:
                    self.assertIn(text(value), page)
                for anchor in ('what-the-evidence-establishes', 'root-cause', 'bounded-impact'):
                    self.assertIn('id="'+anchor+'"', page)

    def test_resources_put_takeaway_before_catalog_metadata(self):
        for rec in self.resources:
            with self.subTest(resource=rec['id']):
                page = self.pages['docs/resources/'+rec['id']+'.md']
                source = link('Official resource', rec['primary_url'])
                self.assertLess(page.index(source), page.index('## Main takeaway'))
                self.assertLess(page.index(text(rec['summary'])), page.index('**Publisher:**'))
                self.assertLess(page.index(text(rec['defensive_use'])), page.index('**Publisher:**'))
                self.assertIn('id="original-summary"', page)
                for value in [*rec['prerequisites'], *rec['caveats']]:
                    self.assertIn(text(value), page)

    def test_indexes_offer_direct_original_sources(self):
        for rec in self.reports:
            source = next(s for s in rec['sources'] if s['id'] == rec['primary_source_id'])
            self.assertIn(link('Original source', source['url']), self.pages['docs/reports.md'])
        for rec in self.resources:
            self.assertIn(link('Original source', rec['primary_url']), self.pages['docs/resource-index.md'])

    def test_build_is_deterministic_and_does_not_rewrite_records(self):
        paths = [*sorted((ROOT/'data/reports').glob('*.json')),
                 *sorted((ROOT/'data/resources').glob('*.json'))]
        before = {p: p.read_bytes() for p in paths}
        self.assertEqual(build(), self.pages)
        self.assertEqual(before, {p: p.read_bytes() for p in paths})


if __name__ == '__main__':
    unittest.main()
