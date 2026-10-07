"""Offline regression checks for a source-reviewed reporting-guide promotion."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_navigation import build
from export_resources import build_export
from validate import validate_library
from validate_extra import validate_all


class ReportingGuidePromotionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rid = 'google-understanding-security-vulnerability-reports'
        resources, _, _ = validate_all()
        cls.resources = {r['id']: r for r in resources}
        cls.record = cls.resources[cls.rid]

    def test_promotion_preserves_identity_and_resolved_retrieval_history(self):
        candidates = json.loads((ROOT / 'data/resource-candidates.json').read_text())['candidates']
        self.assertNotIn(self.rid, {r['id'] for r in candidates})
        self.assertIn('hackerone-quality-vulnerability-reports', self.resources)
        self.assertEqual(self.record['sources'][0]['url'], self.record['primary_url'])
        self.assertEqual(self.record['sources'][0]['provenance'], 'official_primary')
        note = self.record['freshness']['note']
        for qualifier in ('candidate', 'indexed text', 'browser-rendered primary text',
                          'HackerOne Quality Reports', 'same candidate ID'):
            self.assertIn(qualifier, note)

    def test_general_guidance_keeps_unknown_dates_and_no_award_claim(self):
        self.assertEqual(self.record['resource_type_id'], 'reporting-guide')
        self.assertEqual(self.record['topic_ids'], ['reporting'])
        self.assertEqual(self.record['skillset_ids'], ['defensive-evidence-writing'])
        self.assertEqual(self.record['authors'], [])
        self.assertIsNone(self.record['version'])
        for date in self.record['dates'].values():
            self.assertIsNone(date['value'])
            self.assertIsNone(date['precision'])
            self.assertEqual(date['basis'], 'not_reported')
            self.assertIsNone(date['source_id'])
        self.assertEqual(self.record['prerequisites_basis'], 'editorial_guidance')
        self.assertNotIn('reward', self.record)
        reports, _ = validate_library()
        self.assertNotIn(self.rid, {r['id'] for r in reports})
        self.assertIn('no individual incident', ' '.join(self.record['caveats']))
        self.assertIn("video's date does not establish", ' '.join(self.record['caveats']))

    def test_promotion_reaches_export_and_reporting_navigation_once(self):
        exported = build_export()
        self.assertEqual([r for r in exported['resources'] if r['id'] == self.rid],
                         [self.record])
        pages = build()
        target = 'resources/' + self.rid + '.md'
        self.assertIn('docs/' + target, pages)
        for page in ('docs/resource-index.md', 'docs/resource-topics.md'):
            self.assertEqual(pages[page].count('(<' + target + '>)'), 1)
        reporting = pages['docs/resource-topics.md'].split('<a id="topic-reporting"></a>')[1]
        reporting = reporting.split('<a id=', 1)[0]
        self.assertIn('(<' + target + '>)', reporting)


if __name__ == '__main__':
    unittest.main()
