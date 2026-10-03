"""Offline coverage for readable resource records and generated-file checks."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from build_navigation import build, check_generated_page_sets, link, resource_pages, text
from validate_extra import validate_all


class ResourceNavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resources, cls.diagrams, cls.taxonomy = validate_all()
        cls.skills = json.loads((ROOT/'data/taxonomy.json').read_text())
        cls.pages = build()

    def render(self, records):
        return resource_pages(records, self.diagrams, self.taxonomy, self.skills)

    def test_exactly_one_page_per_resource(self):
        expected = {'docs/resources/'+r['id']+'.md' for r in self.resources}
        self.assertEqual(expected, {p for p in self.pages if p.startswith('docs/resources/')})
        self.assertIn('docs/resource-index.md', self.pages)
        self.assertNotIn('docs/resources.md', self.pages)

    def test_index_has_every_record_once(self):
        index = self.pages['docs/resource-index.md']
        for rec in self.resources:
            self.assertEqual(index.count('(<'+'resources/'+rec['id']+'.md'+'>)'), 1)

    def test_record_content_and_provenance_preserved(self):
        for rec in self.resources:
            with self.subTest(resource=rec['id']):
                page = self.pages['docs/resources/'+rec['id']+'.md']
                for value in [rec['summary'], rec['defensive_use'], *rec['prerequisites'], *rec['caveats'], rec['freshness']['note'], rec['freshness']['reviewed_at']]:
                    self.assertIn(text(value), page)
                self.assertIn(text(rec['prerequisites_basis'].replace('_', ' ')), page)
                self.assertIn(link('Canonical JSON', '../../data/resources/'+rec['id']+'.json'), page)
                self.assertIn(link('Official resource', rec['primary_url']), page)
                for date in rec['dates'].values():
                    self.assertIn(text(date['value'] or 'Unknown'), page)
                    self.assertIn('precision: '+text(date['precision'] or 'unknown'), page)
                    self.assertIn('basis: '+text(date['basis'].replace('_', ' ')), page)
                    if date['note']:
                        self.assertIn(text(date['note']), page)
                    if date['source_id']:
                        self.assertIn('source ID: '+text(date['source_id']), page)
                for source in rec['sources']:
                    self.assertIn(link(source['title'], source['url']), page)
                    self.assertIn(text(source['retrieved_at']), page)
                    self.assertIn('supports: '+text(', '.join(source['supports'])), page)

    def test_rendering_independent_of_input_record_order(self):
        self.assertEqual(self.render(self.resources), self.render(list(reversed(self.resources))))

    def test_unknowns_and_empty_lists_do_not_invent_claims(self):
        rec = copy.deepcopy(self.resources[0])
        rec.update(authors=[], version=None, prerequisites=[], caveats=[])
        rec['access']['note'] = None
        rec['prerequisites_basis'] = 'publisher_explicit'
        for date in rec['dates'].values():
            date.update(value=None, precision=None, basis='not_reported', source_id=None, note=None)
        page = self.render([rec])['docs/resources/'+rec['id']+'.md']
        self.assertIn('Not identified in the reviewed record', page)
        self.assertIn('Not established in the reviewed record', page)
        self.assertIn('No prerequisites recorded; this does not establish that none are needed.', page)
        self.assertIn('No additional caveats recorded', page)
        self.assertIn('publisher explicit', page)
        self.assertEqual(page.count('; precision: unknown; basis: not reported; source: Not recorded.'), 3)
        self.assertNotIn('None', page)

    def test_record_text_is_escaped(self):
        rec = copy.deepcopy(self.resources[0])
        unsafe = '<script>[text](example) *literal*'
        rec['summary'] = unsafe
        rec['sources'][0]['title'] = unsafe
        page = self.render([rec])['docs/resources/'+rec['id']+'.md']
        self.assertIn(text(unsafe), page)
        self.assertNotIn('<script>', page)

    def test_committed_pages_match_build(self):
        for name, expected in self.pages.items():
            with self.subTest(page=name):
                self.assertEqual((ROOT/name).read_text(), expected)
        check_generated_page_sets(ROOT, self.pages)

    def test_stale_resources_and_reports_rejected_without_deletion(self):
        for collection in ('resources', 'reports'):
            with self.subTest(collection=collection), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                path = root/'docs'/collection/'obsolete.md'
                path.parent.mkdir(parents=True)
                path.write_text('Keep this for manual review.')
                with self.assertRaisesRegex(SystemExit, 'Unexpected generated '+collection+' pages'):
                    check_generated_page_sets(root, {})
                self.assertTrue(path.is_file())

    def test_no_curated_guide_overwrite(self):
        guide = (ROOT/'docs/resources.md').read_text()
        self.assertIn('[Browse all readable resource records](resource-index.md)', guide)
        self.assertIn('## Modern webapp research and guidance', guide)


if __name__ == '__main__':
    unittest.main()
