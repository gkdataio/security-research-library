"""Reader routes connect existing content without changing its classification."""
import json
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from build_navigation import build, link
from validate_extra import validate_all


class ReaderNavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resources, _, cls.taxonomy = validate_all()
        cls.skills = json.loads((ROOT/'data/taxonomy.json').read_text())
        cls.pages = build()

    def test_resource_memberships_link_to_existing_groups(self):
        types = {r['id']: r['title'] for r in self.taxonomy['resource_types']}
        topics = {r['id']: r['title'] for r in self.taxonomy['topics']}
        skills = {r['id']: r['title'] for r in self.skills['skillsets']}
        for rec in self.resources:
            page = self.pages['docs/resources/'+rec['id']+'.md']
            groups = [('Resource type', 'resource-types.md', 'type', types, [rec['resource_type_id']]),
                      ('Topics', 'resource-topics.md', 'topic', topics, rec['topic_ids']),
                      ('Defensive skills', 'skillsets.md', 'skill', skills, rec['skillset_ids'])]
            for label, index, prefix, titles, ids in groups:
                with self.subTest(resource=rec['id'], label=label):
                    expected = '; '.join(link(titles[rid], '../'+index+'#'+prefix+'-'+rid) for rid in ids)
                    self.assertIn('**'+label+':** '+expected, page)
                    for rid in ids:
                        self.assertIn('id="'+prefix+'-'+rid+'"', self.pages['docs/'+index])

    def test_learning_guide_contents_match_unchanged_sections(self):
        page = (ROOT/'docs/learning-guide.md').read_text()
        self.assertIn('[Library home](../README.md)', page)
        headings = re.findall(r'^## (.+)$', page, re.M)
        self.assertEqual(len(headings), 14)
        for heading in headings:
            slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
            self.assertIn('['+heading+'](#'+slug+')', page)

    def test_guides_route_readers_to_pages_that_retain_json(self):
        for name, collection, minimum in [('learning-guide.md', 'reports', 5),
                                          ('research-methodology.md', 'resources', 11)]:
            page = (ROOT/'docs'/name).read_text()
            self.assertNotIn('../data/'+collection+'/', page)
            targets = re.findall(r'\]\(('+collection+r'/[^()]+\.md)\)', page)
            self.assertGreaterEqual(len(targets), minimum)
            for target in targets:
                with self.subTest(guide=name, target=target):
                    record_id = Path(target).stem
                    rendered = self.pages['docs/'+target]
                    self.assertIn(link('Canonical JSON', '../../data/'+collection+'/'+record_id+'.json'), rendered)
                    self.assertTrue((ROOT/'data'/collection/(record_id+'.json')).is_file())

    def test_guide_local_paths_and_fragments_resolve(self):
        for name in ['learning-guide.md', 'research-methodology.md']:
            page = (ROOT/'docs'/name).read_text()
            for target in re.findall(r'\]\(<?([^)>]+)>?\)', page):
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    continue
                path = (ROOT/'docs'/unquote(parsed.path)).resolve() if parsed.path else ROOT/'docs'/name
                self.assertTrue(path.is_file(), (name, target))
                if parsed.fragment:
                    content = path.read_text()
                    headings = re.findall(r'^#{1,6} (.+)$', content, re.M)
                    slugs = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                    explicit = set(re.findall(r'<a id="([^"]+)"', content))
                    self.assertIn(unquote(parsed.fragment), slugs | explicit, (name, target))


if __name__ == '__main__':
    unittest.main()
