"""Offline completeness, date provenance and escaping checks for learning browse views."""
import copy
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from build_navigation import build, link, text
from category_navigation import memberships, validate_config
from learning_navigation import learning_pages, publication_year, publication_year_page, resource_type_page
from validate import Invalid, check_schema, validate_library
from validate_extra import validate_all


class LearningNavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reports, cls.taxonomy = validate_library()
        cls.resources, cls.diagrams, cls.resource_taxonomy = validate_all()
        cls.pages = learning_pages(cls.reports, cls.resources, cls.taxonomy, cls.resource_taxonomy, text, link)

    def test_type_index_lists_every_resource_once_with_exact_groups(self):
        page = self.pages['docs/resource-types.md']
        ids = re.findall(r'\]\(<resources/([^>]+)\.md>\)', page)
        self.assertEqual(sorted(ids), sorted(r['id'] for r in self.resources))
        for item in self.resource_taxonomy['resource_types']:
            section = page.split('<a id="type-'+item['id']+'"></a>')[1].split('<a id=')[0]
            actual = re.findall(r'\]\(<resources/([^>]+)\.md>\)', section)
            self.assertEqual(set(actual), {r['id'] for r in self.resources if r['resource_type_id'] == item['id']})

    def test_skill_index_preserves_exact_collection_memberships(self):
        page = self.pages['docs/skillsets.md']
        for skill in self.taxonomy['skillsets']:
            section = page.split('<a id="skill-'+skill['id']+'"></a>')[1].split('<a id=')[0]
            for collection, records in [('reports', self.reports), ('resources', self.resources)]:
                actual = re.findall(r'\]\(<'+collection+r'/([^>]+)\.md>\)', section)
                self.assertEqual(set(actual), {r['id'] for r in records if skill['id'] in r['skillset_ids']})
                self.assertEqual(len(actual), len(set(actual)))

    def test_year_index_is_complete_once_per_collection(self):
        page = self.pages['docs/publication-years.md']
        for collection, records in [('reports', self.reports), ('resources', self.resources)]:
            actual = re.findall(r'\]\(<'+collection+r'/([^>]+)\.md>\)', page)
            self.assertEqual(sorted(actual), sorted(r['id'] for r in records))
            for year in {publication_year(r) for r in records}:
                section = page.split('<a id="year-'+(year or 'unknown')+'"></a>')[1].split('<a id=')[0]
                actual = re.findall(r'\]\(<'+collection+r'/([^>]+)\.md>\)', section)
                self.assertEqual(set(actual), {r['id'] for r in records if publication_year(r) == year})

    def test_partial_and_unknown_publication_dates_never_use_fallbacks(self):
        records = [
            {'id': 'unknown', 'title': 'Unknown', 'dates': {'published': {'value': None, 'precision': None, 'basis': 'not_reported'}, 'source_displayed': {'value': '2026-10-12'}, 'version_released': {'value': '2025-01-01'}}, 'freshness': {'reviewed_at': '2026-10-12T18:00:00Z'}},
            {'id': 'partial', 'title': 'Partial', 'dates': {'published': {'value': '2024', 'precision': 'year', 'basis': 'explicit'}}},
            {'id': 'month', 'title': 'Month', 'dates': {'published': {'value': '2025-03', 'precision': 'month', 'basis': 'url_date'}}},
        ]
        page = publication_year_page([], records, text, link)
        self.assertIsNone(publication_year(records[0]))
        self.assertNotIn('year-2026', page)
        self.assertIn('publication: 2024; precision: year; basis: explicit.', page)
        self.assertIn('publication: 2025-03; precision: month; basis: url date.', page)
        self.assertLess(page.index('<a id="year-2025"'), page.index('<a id="year-2024"'))
        self.assertLess(page.index('<a id="year-2024"'), page.index('<a id="year-unknown"'))

    def test_deterministic_no_mutation_and_current_generated_files(self):
        original = copy.deepcopy((self.reports, self.resources, self.taxonomy, self.resource_taxonomy))
        result = learning_pages(list(reversed(self.reports)), list(reversed(self.resources)), self.taxonomy, self.resource_taxonomy, text, link)
        self.assertEqual(result, self.pages)
        self.assertEqual(original, (self.reports, self.resources, self.taxonomy, self.resource_taxonomy))
        complete = build()
        for name, content in self.pages.items():
            self.assertEqual(complete[name], content)
            self.assertEqual((ROOT/name).read_text(), content)

    def test_empty_types_and_html_markdown_escaping(self):
        page = resource_type_page([{'id':'example','title':'<script>[Bad](link)','publisher':'<b>Publisher</b>','resource_type_id':'example'}],
                                  {'resource_types':[{'id':'empty','title':'Empty'}, {'id':'example','title':'Example'}]}, text, link)
        self.assertIn('No resources currently assigned to this type.', page)
        self.assertIn('&lt;script&gt;', page)
        self.assertNotIn('<script>', page)

    def test_taxonomy_anchor_ids_are_encoded_even_for_empty_groups(self):
        unsafe = 'x" onmouseover="example'
        taxonomy = {'resource_types': [{'id': unsafe, 'title': 'Example'}]}
        page = resource_type_page([], taxonomy, text, link)
        self.assertIn('id="type-x%22%20onmouseover%3D%22example"', page)
        self.assertIn('#type-x%22%20onmouseover%3D%22example', page)
        self.assertNotIn(' onmouseover="', page)
        pages = learning_pages([], [], {'skillsets': [{'id': unsafe, 'title': 'Example', 'defensive_objective': 'Example'}]}, taxonomy, text, link)
        self.assertIn('id="skill-x%22%20onmouseover%3D%22example"', pages['docs/skillsets.md'])
        self.assertNotIn(' onmouseover="', pages['docs/skillsets.md'])

    def test_explicit_crosswalks_are_narrow_validated_and_deduplicated(self):
        config = json.loads((ROOT/'data/category-navigation.json').read_text())
        schema = json.loads((ROOT/'schema/category-navigation.schema.json').read_text())
        validate_config(config, schema, self.taxonomy, self.resource_taxonomy, self.resources)
        for cid in ('client-security', 'server-request-trust', 'information-exposure'):
            category = next(c for c in config['categories'] if c['id'] == cid)
            self.assertTrue(category['resource_ids'])
            self.assertNotIn('web-foundations', category['resource_topic_ids'])
        for bad in ('unknown', 'version', 'duplicate'):
            changed = copy.deepcopy(config)
            entry = next(c for c in changed['categories'] if c.get('resource_ids'))
            if bad == 'unknown': entry['resource_ids'].append('missing-resource')
            if bad == 'version': changed['schema_version'] = '1.0.0'
            if bad == 'duplicate': entry['resource_ids'].append(entry['resource_ids'][0])
            with self.subTest(bad=bad), self.assertRaises(Invalid):
                validate_config(changed, schema, self.taxonomy, self.resource_taxonomy, self.resources)
        version_mismatch = copy.deepcopy(config); version_mismatch['schema_version'] = '1.0.0'
        with self.assertRaises(Invalid):
            check_schema(version_mismatch, schema, schema)
        legacy = copy.deepcopy(config); legacy['schema_version'] = '1.0.0'
        for category in legacy['categories']: category.pop('resource_ids', None)
        validate_config(legacy, schema, self.taxonomy, self.resource_taxonomy, self.resources)
        selected = {'id':'selected','title':'Selected','topic_ids':['web-foundations']}
        broad = {'id':'broad','title':'Broad','topic_ids':['web-foundations']}
        result = memberships({'id':'family','resource_topic_ids':[],'resource_ids':['selected']}, [], [selected,broad], [])
        self.assertEqual(result, ([], [(selected, [], [])], []))

    def test_practice_stays_educational_and_lanes_exist(self):
        topics = {t['id'] for t in self.resource_taxonomy['topics']}
        self.assertTrue({'ctf-and-practice','api-security','browser-security','server-client-frameworks'} <= topics)
        self.assertNotIn('ctf-and-practice', {c['id'] for c in self.taxonomy['categories']})
        practice = [r for r in self.resources if 'ctf-and-practice' in r['topic_ids']]
        self.assertGreaterEqual(len(practice), 6)
        self.assertTrue(all(r['resource_type_id'] == 'training-lab' for r in practice))


if __name__ == '__main__':
    unittest.main()
