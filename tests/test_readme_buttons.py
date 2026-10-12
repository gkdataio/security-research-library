"""Offline checks for accessible, deterministic GitHub README navigation images."""
import copy
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import tempfile
import unittest
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from render_readme_buttons import ASSET_DIR, GROUPS, HEIGHT, block, build, svg_button
from validate import Invalid
from validate_extra import validate_inert_svg


class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.images = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'a': self.links.append(values)
        if tag == 'img': self.images.append(values)


class ReadmeButtonTests(unittest.TestCase):
    def test_exact_button_destinations_and_accessible_click_targets(self):
        expected = []
        for group, (_, buttons) in GROUPS.items():
            parser = Links(); parser.feed(block(group))
            self.assertEqual(len(parser.links), len(buttons))
            self.assertEqual(len(parser.images), len(buttons))
            for button, anchor, image in zip(buttons, parser.links, parser.images):
                slug, label, href, width, description = button
                self.assertTrue(description.startswith(label+':'))
                self.assertEqual(anchor, {'href': href, 'title': description})
                self.assertEqual(image, {'src': ASSET_DIR+'/'+slug+'.svg', 'width': str(width), 'height': str(HEIGHT), 'alt': description})
                self.assertLessEqual(width, 240)
                self.assertGreaterEqual(HEIGHT, 44)
                expected.append(href)
        self.assertEqual(len(expected), len(set(expected)))
        self.assertEqual(len(expected), 8)

    def test_svg_safety_palette_dimensions_and_visible_labels(self):
        ns = '{http://www.w3.org/2000/svg}'
        for group, (_, buttons) in GROUPS.items():
            for button in buttons:
                path = ROOT/ASSET_DIR/(button[0]+'.svg')
                validate_inert_svg(path)
                root = ET.parse(path).getroot()
                self.assertEqual(root.attrib['role'], 'img')
                self.assertEqual(root.attrib['aria-label'], button[4])
                self.assertEqual(root.attrib['height'], '44')
                self.assertEqual(root.find(ns+'title').text, button[1])
                self.assertEqual(root.find(ns+'text').text, button[1])
                self.assertEqual(root.find(ns+'rect').attrib['fill'], '#EAC87A' if group == 'vulnerabilities' else '#090F12')
                self.assertEqual(root.find(ns+'text').attrib['fill'], '#090F12' if group == 'vulnerabilities' else '#F0F3E8')

    def test_button_text_is_escaped_and_active_svg_is_rejected(self):
        sample = ('test', '<Example & "label">', 'docs/resources.md', 180, 'Read <example> & "description"')
        result = svg_button(sample)
        root = ET.fromstring(result)
        self.assertEqual(root.find('{http://www.w3.org/2000/svg}title').text, sample[1])
        self.assertNotIn('<Example', result)
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/'test.svg'; p.write_text(result); validate_inert_svg(p)
            for body in ('<script>example</script>', '<image href="https://example.com/pixel"/>', '<foreignObject/>'):
                p.write_text(result.replace('</svg>', body+'</svg>'))
                with self.assertRaises(Invalid): validate_inert_svg(p)

    def test_destinations_and_anchors_exist(self):
        for _, buttons in GROUPS.values():
            for _, _, href, _, _ in buttons:
                url = urlsplit(href)
                self.assertFalse(url.scheme or url.netloc)
                path = (ROOT/unquote(url.path)).resolve()
                self.assertTrue(path.is_relative_to(ROOT))
                self.assertTrue(path.is_file())
                if url.fragment:
                    self.assertIn('id="'+url.fragment+'"', path.read_text())

    def test_deterministic_assets_and_readme_regions(self):
        original = copy.deepcopy(GROUPS)
        outputs = build()
        self.assertEqual(outputs, build())
        self.assertEqual(GROUPS, original)
        for name, content in outputs.items(): self.assertEqual((ROOT/name).read_text(), content)
        expected = {button[0]+'.svg' for _, buttons in GROUPS.values() for button in buttons}
        self.assertEqual({p.name for p in (ROOT/ASSET_DIR).glob('*.svg')}, expected)
        readme = outputs['README.md']
        self.assertLess(readme.index('BEGIN README BUTTONS: vulnerabilities'), readme.index('BEGIN README BUTTONS: learning'))
        self.assertLess(readme.index('BEGIN README BUTTONS: learning'), readme.index('BEGIN README BUTTONS: browse'))
        self.assertIn('**Learning lanes**', readme)
        self.assertIn('**Browse across collections**', readme)

    def test_regeneration_preserves_content_outside_marked_regions(self):
        source = (ROOT/'README.md').read_text()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = 'Preserve this user introduction.\n'+source+'\nPreserve this user footer.\n'
            (root/'README.md').write_text(source)
            rendered = build(root)['README.md']
            self.assertEqual(rendered, source)
            for broken in ('missing', 'duplicate'):
                changed = source.replace('<!-- BEGIN README BUTTONS: learning -->', '') if broken == 'missing' else source+'\n'+block('learning')
                (root/'README.md').write_text(changed)
                with self.assertRaises(ValueError): build(root)

    def test_existing_readme_ui_and_policy_entry_points_remain(self):
        readme = (ROOT/'README.md').read_text()
        for image in ('hero.gif', 'hero-static.png', 'hero-mobile.gif', 'hero-mobile-static.png',
                      'collection-reports.svg', 'collection-programs.svg', 'collection-learning.svg',
                      'collection-diagrams.svg', 'collection-data.svg', 'collection-maintenance.svg',
                      'diagram-ai.svg', 'diagram-browser.svg', 'diagram-build.svg',
                      'evidence.gif', 'workbench.png'):
            self.assertIn('docs/assets/readme/'+image, readme)
        for target in ('DATA_POLICY.md', 'LICENSE.md#educational-content-cc-by-40', 'LICENSE.md#software-mit', '#report-index', '#check-program-changes'):
            self.assertIn(target, readme)
        self.assertIn('Quick links: [Cross-site scripting (XSS)]', readme)
        self.assertIn('### Explore by topic', readme)


if __name__ == '__main__':
    unittest.main()
