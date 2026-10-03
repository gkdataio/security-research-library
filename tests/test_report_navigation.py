"""Offline regression coverage for the award-backed report category index."""
import copy
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from build_navigation import build, link, report_topic_page, text
from validate import validate_library


class ReportTopicNavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reports, cls.taxonomy = validate_library()
        cls.pages = build()

    def test_canonical_memberships_roles_counts_and_order(self):
        page = self.pages['docs/report-topics.md']
        self.assertIn(f'{len(self.reports)} distinct award-backed reports across {len(self.taxonomy["categories"])} taxonomy categories.', page)
        self.assertIn('overlapping memberships do not increase the distinct report count', page)
        self.assertIn('Category counts must not be added to count reports.', page)
        categories = sorted(self.taxonomy['categories'], key=lambda c: (c['title'].casefold(), c['id']))
        self.assertEqual(re.findall(r'<a id="category-([^"]+)"></a>', page), [c['id'] for c in categories])
        for category in categories:
            cid = category['id']
            with self.subTest(category=cid):
                section = page.split(f'<a id="category-{cid}"></a>', 1)[1].split('<a id=', 1)[0]
                expected = sorted((r for r in self.reports if cid in [r['category_id'], *r['secondary_category_ids']]),
                                  key=lambda r: (r['title'].casefold(), r['id']))
                self.assertEqual(re.findall(r'\]\(<reports/([^>]+)\.md>\)', section), [r['id'] for r in expected])
                count_label = f'{len(expected)} distinct '+('report.' if len(expected) == 1 else 'reports.')
                self.assertIn(count_label, section)
                self.assertIn(link(category['title'], '#category-'+cid)+' — '+count_label, page)
                for rec in expected:
                    role = 'primary' if rec['category_id'] == cid else 'secondary'
                    self.assertIn(link(rec['title'], 'reports/'+rec['id']+'.md')+' — '+text(rec['organization'])+'; '+role+' category.', section)
        for rec in self.reports:
            self.assertEqual(page.count('(<reports/'+rec['id']+'.md>)'), 1 + len(rec['secondary_category_ids']))

    def test_input_order_ties_empty_categories_and_no_mutation(self):
        records = [dict(id=rid, title=title, organization='Example', category_id='first',
                        secondary_category_ids=['second'])
                   for rid, title in [('z', 'Zulu'), ('b', 'Alpha'), ('a', 'alpha')]]
        taxonomy = {'categories': [{'id': 'second', 'title': 'Alpha'},
                                   {'id': 'empty', 'title': 'Zulu'},
                                   {'id': 'first', 'title': 'alpha'}]}
        originals = copy.deepcopy((records, taxonomy))
        page = report_topic_page(records, taxonomy)
        self.assertEqual(page, report_topic_page(list(reversed(records)), {'categories': list(reversed(taxonomy['categories']))}))
        self.assertEqual(re.findall(r'<a id="category-([^"]+)"></a>', page), ['first', 'second', 'empty'])
        self.assertEqual(re.findall(r'\]\(<reports/([^>]+)\.md>\)', page), ['a', 'b', 'z'] * 2)
        self.assertIn('3 distinct award-backed reports across 3 taxonomy categories.', page)
        self.assertIn('0 distinct reports.\n\nNo reports currently assigned to this category.', page)
        self.assertIn('0 distinct award-backed reports', report_topic_page([], taxonomy))
        self.assertEqual((records, taxonomy), originals)

    def test_navigation_links_resolve_and_anchors_remain_stable(self):
        self.assertIn('[Browse by topic](report-topics.md)', self.pages['docs/reports.md'])
        name = 'docs/report-topics.md'
        for target in re.findall(r'\]\(<?([^)>]+)>?\)', self.pages[name]):
            url = urlsplit(target)
            self.assertFalse(url.scheme)
            path = (ROOT/name).parent/unquote(url.path) if url.path else ROOT/name
            content = self.pages.get(str(path.relative_to(ROOT)))
            if content is None:
                self.assertTrue(path.is_file(), target)
                content = path.read_text()
            if url.fragment:
                self.assertIn(f'id="{url.fragment}"', content)
        taxonomy = copy.deepcopy(self.taxonomy)
        for category in taxonomy['categories']:
            category['title'] = 'Changed display title'
        changed = report_topic_page(self.reports, taxonomy)
        self.assertEqual(set(re.findall(r'<a id="([^"]+)"></a>', changed)),
                         set(re.findall(r'<a id="([^"]+)"></a>', self.pages[name])))

    def test_category_and_report_text_are_escaped(self):
        unsafe = '<script>[text](example) *literal* & "quoted"\nnew line'
        record = dict(id='safe-report', title=unsafe, organization=unsafe,
                      category_id='safe', secondary_category_ids=[])
        page = report_topic_page([record], {'categories': [{'id': 'safe', 'title': unsafe}]})
        self.assertEqual(page.count(text(unsafe)), 4)
        self.assertNotIn('<script>', page)
        self.assertNotIn('[text](example)', page)
        self.assertIn('(<reports/safe-report.md>)', page)

    def test_anchor_attribute_escapes_untrusted_category_id(self):
        cid = 'topic"<tag>\n'
        page = report_topic_page([], {'categories': [{'id': cid, 'title': 'Example'}]})
        anchor = 'category-topic%22%3Ctag%3E%0A'
        self.assertIn(f'<a id="{anchor}"></a>', page)
        self.assertIn('(<#'+anchor+'>)', page)
        self.assertNotIn('<tag>', page)

    def test_generated_page_matches_build_and_details_remain_present(self):
        self.assertEqual((ROOT/'docs/report-topics.md').read_text(), self.pages['docs/report-topics.md'])
        expected = {'docs/reports/'+r['id']+'.md' for r in self.reports}
        self.assertEqual(expected, {name for name in self.pages if name.startswith('docs/reports/')})
        for name in expected:
            self.assertEqual((ROOT/name).read_text(), self.pages[name])


if __name__ == '__main__':
    unittest.main()
