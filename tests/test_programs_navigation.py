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
from build_navigation import build as navigation, text, link
from validate_extra import validate_inert_svg

class ProgramTests(unittest.TestCase):
    def setUp(self):
        self.rec=json.loads(next((ROOT/'data/programs').glob('*.json')).read_text())
        # These legacy/type fixtures deliberately omit the separately tested 1.4 scope extension.
        self.rec.pop('scope_context', None)
        self.schema=json.loads((ROOT/'schema/program.schema.json').read_text())
    def test_valid(self): validate_program(self.rec,self.schema)
    def test_program_type_is_optional_for_existing_versions(self):
        self.rec.pop('program_type',None)
        for version in ('1.1.0','1.2.0','1.3.0'):
            with self.subTest(version=version):
                self.rec['schema_version']=version
                validate_program(self.rec,self.schema)
    def test_program_type_requires_version_1_3(self):
        for version in ('1.1.0','1.2.0'):
            for value in ('paid_bounty','vulnerability_disclosure','unknown'):
                with self.subTest(version=version,value=value):
                    self.rec['schema_version']=version
                    self.rec['program_type']={'value':value,'summary':'Reviewed classification.','source_ids':[self.rec['sources'][0]['id']]}
                    with self.assertRaisesRegex(Invalid,'program type requires program record version 1.3.0'):
                        validate_program(self.rec,self.schema)
    def test_program_type_unknown_source(self):
        self.rec['program_type']={'value':'paid_bounty','summary':'Reviewed reward policy.','source_ids':['missing']}
        with self.assertRaises(Invalid): validate_program(self.rec,self.schema)
    def test_known_program_type_needs_evidence(self):
        for value in ('paid_bounty','vulnerability_disclosure'):
            with self.subTest(value=value):
                self.rec['program_type']={'value':value,'summary':'A classification without evidence.','source_ids':[]}
                with self.assertRaises(Invalid): validate_program(self.rec,self.schema)
    def test_unknown_program_type_may_have_no_evidence(self):
        self.rec['program_type']={'value':'unknown','summary':'Not established by the reviewed sources.','source_ids':[]}
        validate_program(self.rec,self.schema)
    def test_program_type_invalid_enum(self):
        self.rec['program_type']={'value':'free','summary':'Unsupported type.','source_ids':[self.rec['sources'][0]['id']]}
        with self.assertRaises(Invalid): validate_program(self.rec,self.schema)
    def test_program_type_invalid_shape(self):
        for value in (None,'paid_bounty',{'value':'paid_bounty','source_ids':[]}):
            with self.subTest(value=value):
                self.rec['program_type']=value
                with self.assertRaises(Invalid): validate_program(self.rec,self.schema)
    def test_program_type_independent_of_status_and_currency(self):
        self.rec['program_type']={'value':'paid_bounty','summary':'Advertised monetary bounty.','source_ids':[self.rec['sources'][0]['id']]}
        self.rec['submission_status'].update(value='paused',source_ids=[self.rec['sources'][0]['id']])
        self.rec['rewards'].update(currency=None,minimum=None,maximum=None)
        validate_program(self.rec,self.schema)
    def test_missing_program_type_export_preserves_legacy_record(self):
        self.rec.pop('program_type',None)
        self.rec['schema_version']='1.1.0'
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'schema').mkdir(); (root/'data/programs').mkdir(parents=True)
            (root/'schema/program.schema.json').write_text(json.dumps(self.schema))
            (root/'data/programs'/f"{self.rec['id']}.json").write_text(json.dumps(self.rec))
            result=programs(root)
        exported=json.loads(result['exports/programs.json'])['programs'][0]
        self.assertNotIn('program_type',exported)
        self.assertEqual(exported['schema_version'],'1.1.0')
        self.assertIn('Program type:** unknown.',result['docs/programs.md'])
    def test_program_type_export_retains_evidence(self):
        exported=json.loads(programs()['exports/programs.json'])
        self.assertEqual(exported['schema_version'],'1.4.0')
        canonical={json.loads(p.read_text())['id']:json.loads(p.read_text()) for p in (ROOT/'data/programs').glob('*.json')}
        for record in exported['programs']:
            with self.subTest(program=record['id']):
                self.assertEqual(record.get('program_type'),canonical[record['id']].get('program_type'))
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
    def test_official_link_needs_source(self):
        self.rec['official_program_links']=[{'url':'https://hackerone.com/example','source_ids':['missing'],'note':'Official link'}]
        with self.assertRaises(Invalid):validate_program(self.rec,self.schema)
    def test_duplicate_official_link(self):
        item={'url':'https://hackerone.com/example','source_ids':[self.rec['sources'][0]['id']],'note':'Official link'}
        self.rec['official_program_links']=[item,item]
        with self.assertRaises(Invalid):validate_program(self.rec,self.schema)
    def test_status_needs_evidence(self):
        self.rec['submission_status'].update(value='paused',source_ids=[])
        with self.assertRaises(Invalid): validate_program(self.rec,self.schema)
    def test_closed_status_supported(self):
        self.rec.pop('program_type',None)
        self.rec['schema_version']='1.2.0'
        self.rec['submission_status'].update(value='closed',source_ids=[self.rec['sources'][0]['id']])
        validate_program(self.rec,self.schema)
    def test_closed_status_supported_with_program_type(self):
        self.rec['schema_version']='1.3.0'
        self.rec['program_type']={'value':'paid_bounty','summary':'Reviewed bounty policy.','source_ids':[self.rec['sources'][0]['id']]}
        self.rec['submission_status'].update(value='closed',source_ids=[self.rec['sources'][0]['id']])
        validate_program(self.rec,self.schema)
    def test_closed_status_requires_new_version(self):
        self.rec.pop('program_type',None)
        self.rec['schema_version']='1.1.0'
        self.rec['submission_status'].update(value='closed',source_ids=[self.rec['sources'][0]['id']])
        with self.assertRaises(Invalid): validate_program(self.rec,self.schema)
    def test_closed_status_needs_evidence(self):
        self.rec.pop('program_type',None)
        self.rec['schema_version']='1.2.0'
        self.rec['submission_status'].update(value='closed',source_ids=[])
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
    def test_escape_link_destination(self):
        result=link("source", "https://example.invalid/\n><img src=x>")
        self.assertNotIn("<img",result);self.assertNotIn("\n",result)
        self.assertIn("%3E%3Cimg%20src=x%3E",result)
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
