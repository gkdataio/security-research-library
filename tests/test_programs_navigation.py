import copy
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from urllib.parse import unquote, urlsplit
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from validate import Invalid
from export_programs import build as programs, validate_program
from build_navigation import build as navigation, text
from validate_extra import validate_inert_svg

class ProgramTests(unittest.TestCase):
    def setUp(self):
        self.rec=json.loads(next((ROOT/'data/programs').glob('*.json')).read_text())
        self.schema=json.loads((ROOT/'schema/program.schema.json').read_text())
    def test_valid(self): validate_program(self.rec,self.schema)
    def test_unknown_source(self):
        self.rec['rewards']['source_ids']=['unknown']
        with self.assertRaises(Invalid): validate_program(self.rec,self.schema)
    def test_scope_inventory_rejected(self):
        self.rec['targets']=['example.invalid']
        with self.assertRaises(Invalid): validate_program(self.rec,self.schema)
    def test_number_without_currency(self):
        self.rec['rewards'].update(currency=None,minimum=1)
        with self.assertRaises(Invalid): validate_program(self.rec,self.schema)
    def test_reversed_bounds(self):
        self.rec['rewards'].update(currency='USD',minimum=5,maximum=1)
        with self.assertRaises(Invalid): validate_program(self.rec,self.schema)
    def test_unreviewed_link(self):
        self.rec['policy_url']='https://example.invalid/policy'
        with self.assertRaises(Invalid): validate_program(self.rec,self.schema)
    def test_deterministic(self): self.assertEqual(programs(),programs())

class NavigationTests(unittest.TestCase):
    def test_deterministic(self): self.assertEqual(navigation(),navigation())
    def test_one_page_per_report(self):
        pages=navigation()
        self.assertEqual(len([p for p in pages if p.startswith('docs/reports/')]),len(list((ROOT/'data/reports').glob('*.json'))))
    def test_local_links_and_explicit_anchors(self):
        pages={**navigation(),**programs()}
        for name,content in pages.items():
            if not name.endswith('.md'):continue
            for target in re.findall(r'\]\(<?([^)>]+)>?\)',content):
                url=urlsplit(target)
                if url.scheme:continue
                path=(ROOT/name).parent/unquote(url.path)
                self.assertTrue(path.is_file(),f'{name}: {target}')
                if url.fragment:
                    self.assertIn(f'id="{url.fragment}"',path.read_text())
    def test_escape_untrusted_text(self):
        escaped=text('<script>[x](y)')
        self.assertNotIn('<script>',escaped);self.assertIn('\\[',escaped)

class StaticSvgTests(unittest.TestCase):
    def validate(self,body):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'test.svg';p.write_text('<svg xmlns="http://www.w3.org/2000/svg"><desc>Test</desc>'+body+'</svg>');validate_inert_svg(p)
    def test_static(self): self.validate('<text x="0" y="0">Test</text>')
    def test_active_and_references_rejected(self):
        for body in ['<script/>','<foreignObject/>','<animate/>','<a/>','<text onclick="test">X</text>','<image href="data:image/png;base64,AA"/>','<path fill="url(#x)"/>','<g style="display:block"/>']:
            with self.subTest(body=body),self.assertRaises(Invalid):self.validate(body)

if __name__=='__main__':unittest.main()
