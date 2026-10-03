"""Offline tests for cross-collection category navigation."""
import copy
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from build_navigation import build, check_generated_page_sets, link, text
from category_navigation import category_pages, collection_counts, memberships, validate_config
from validate import Invalid, validate_library
from validate_extra import validate_all


class CategoryNavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reports, cls.taxonomy = validate_library()
        cls.resources, cls.diagrams, cls.resource_taxonomy = validate_all()
        cls.config = json.loads((ROOT/'data/category-navigation.json').read_text())
        cls.schema = json.loads((ROOT/'schema/category-navigation.schema.json').read_text())
        cls.pages = build()

    def test_config_rejects_unknown_missing_duplicate_and_unsafe_values(self):
        validate_config(self.config, self.schema, self.taxonomy, self.resource_taxonomy)
        for change in ('missing', 'duplicate', 'unknown', 'topic', 'kind', 'path', 'extra'):
            config = copy.deepcopy(self.config)
            if change == 'missing': config['categories'].pop()
            if change == 'duplicate': config['categories'].append(config['categories'][0])
            if change == 'unknown': config['categories'][0]['id'] = 'unknown'
            if change == 'topic': config['categories'][0]['resource_topic_ids'] = ['unknown']
            if change == 'kind': config['categories'][0]['kind'] = 'exploit'
            if change == 'path': config['categories'][0]['id'] = '../escape'
            if change == 'extra': config['categories'][0]['new_field'] = True
            with self.subTest(change=change), self.assertRaises(Invalid):
                validate_config(config, self.schema, self.taxonomy, self.resource_taxonomy)

    def test_exact_report_membership_roles_and_complete_coverage(self):
        seen = set()
        for category in self.config['categories']:
            cid = category['id']
            page = self.pages['docs/categories/'+cid+'.md']
            expected = {r['id'] for r in self.reports
                        if cid in [r['category_id'], *r['secondary_category_ids']]}
            actual = re.findall(r'\]\(<../reports/([^>]+)\.md>\)', page)
            self.assertEqual(set(actual), expected)
            self.assertEqual(len(actual), len(expected))
            for report in self.reports:
                if report['id'] in expected:
                    role = 'primary' if report['category_id'] == cid else 'secondary'
                    self.assertIn(link(report['title'], '../reports/'+report['id']+'.md')+' — '+text(report['organization'])+'; '+role+' category.', page)
            seen.update(actual)
        self.assertEqual(seen, {r['id'] for r in self.reports})

    def test_learning_and_diagrams_have_only_explicit_relationships(self):
        for category in self.config['categories']:
            reports, learning, diagrams = memberships(category, self.reports, self.resources, self.diagrams)
            report_ids = {r['id'] for r in reports}
            expected_diagrams = {d['id'] for d in self.diagrams if report_ids.intersection(d['linked_report_ids'])}
            self.assertEqual({d['id'] for d in diagrams}, expected_diagrams)
            expected_resources = {r['id'] for r in self.resources
                                  if set(r['topic_ids']).intersection(category['resource_topic_ids'])
                                  or any(r['id'] in d['linked_resource_ids'] for d in diagrams)}
            self.assertEqual({r['id'] for r, _, _ in learning}, expected_resources)
            self.assertEqual(len(learning), len(expected_resources))
            for resource, topics, diagram_ids in learning:
                self.assertEqual(set(topics), set(resource['topic_ids']) & set(category['resource_topic_ids']))
                self.assertEqual(set(diagram_ids), {d['id'] for d in diagrams if resource['id'] in d['linked_resource_ids']})
            page = self.pages['docs/categories/'+category['id']+'.md']
            self.assertIn(collection_counts(reports, learning, diagrams), page)

    def test_deterministic_order_and_no_mutation(self):
        original = copy.deepcopy((self.reports, self.resources, self.diagrams, self.taxonomy, self.resource_taxonomy))
        expected = category_pages(ROOT, *original, text, link)
        shuffled = tuple(list(reversed(x)) if isinstance(x, list) else x for x in original)
        actual = category_pages(ROOT, *shuffled, text, link)
        self.assertEqual(actual, expected)
        self.assertEqual(original, (self.reports, self.resources, self.diagrams, self.taxonomy, self.resource_taxonomy))

    def test_local_links_anchors_and_generated_files(self):
        names = ['docs/vulnerability-types.md'] + [n for n in self.pages if n.startswith('docs/categories/')]
        for name in names:
            content = self.pages[name]
            self.assertEqual((ROOT/name).read_text(), content)
            for target in re.findall(r'\]\(<?([^)>]+)>?\)', content):
                url = urlsplit(target)
                self.assertFalse(url.scheme)
                path = ((ROOT/name).parent/unquote(url.path)).resolve() if url.path else ROOT/name
                self.assertTrue(path.is_relative_to(ROOT))
                self.assertTrue(path.is_file(), target)
                if url.fragment:
                    self.assertIn('id="'+url.fragment+'"', path.read_text())
        self.assertIn(f'**{len(self.reports)} distinct reports · {len(self.resources)} learning resources · {len(self.diagrams)} conceptual diagrams**', self.pages['docs/vulnerability-types.md'])

    def test_obsolete_category_pages_rejected_without_deletion(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root/'docs/categories/obsolete.md'
            path.parent.mkdir(parents=True)
            path.write_text('Keep for review.')
            with self.assertRaisesRegex(SystemExit, 'Unexpected generated categories pages'):
                check_generated_page_sets(root, {})
            self.assertTrue(path.is_file())

    def test_empty_relationships_and_learning_do_not_add_reports(self):
        category = {'id': 'example', 'resource_topic_ids': ['topic']}
        resources = [{'id': 'resource', 'title': 'Example', 'topic_ids': ['topic']}]
        diagrams = [{'id': 'diagram', 'title': 'Example', 'linked_report_ids': ['unrelated'], 'linked_resource_ids': ['resource']}]
        reports, learning, related = memberships(category, [], resources, diagrams)
        self.assertEqual(reports, [])
        self.assertEqual(related, [])
        self.assertEqual(learning, [(resources[0], ['topic'], [])])


if __name__ == '__main__':
    unittest.main()
