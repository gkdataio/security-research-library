import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from validate import Invalid, validate_library
from validate_extra import validate_all, validate_resource, validate_diagram
from export_resources import build_export

class ResourceTests(unittest.TestCase):
    def setUp(self):
        resources,diagrams,self.tax=validate_all()
        self.resources={r['id']:r for r in resources};self.rec=copy.deepcopy(resources[0]);self.diagram=copy.deepcopy(diagrams[0])
        reports,tax=validate_library();self.reports={r['id']:r for r in reports};self.skills={s['id'] for s in tax['skillsets']}
        self.rs=json.loads((ROOT/'schema/resource.schema.json').read_text());self.ds=json.loads((ROOT/'schema/diagram.schema.json').read_text())
    def test_collections_valid(self):
        resources,diagrams,_=validate_all();self.assertGreaterEqual(len(resources),6);self.assertGreaterEqual(len(diagrams),3)
    def test_resource_unknown_type_rejected(self):
        self.rec['resource_type_id']='unknown'
        with self.assertRaises(Invalid):validate_resource(self.rec,self.rs,self.tax,self.skills)
    def test_resource_unknown_skill_rejected(self):
        self.rec['skillset_ids']=['unknown']
        with self.assertRaises(Invalid):validate_resource(self.rec,self.rs,self.tax,self.skills)
    def test_resource_future_publication_rejected(self):
        self.rec['dates']['published']={'value':'2030-01-01','precision':'day','basis':'explicit','source_id':'primary','note':None}
        with self.assertRaises(Invalid):validate_resource(self.rec,self.rs,self.tax,self.skills)
    def test_unlinked_diagram_source_rejected(self):
        self.diagram['evidence_urls'].append('https://example.com/unreviewed')
        with self.assertRaises(Invalid):validate_diagram(self.diagram,self.ds,self.reports,self.resources)
    def test_unknown_diagram_node_rejected(self):
        self.diagram['source_graph']['edges'][0]['to']='unknown'
        with self.assertRaises(Invalid):validate_diagram(self.diagram,self.ds,self.reports,self.resources)
    def test_unsafe_asset_path_rejected(self):
        self.diagram['files']['svg']='../outside.svg'
        with self.assertRaises(Invalid):validate_diagram(self.diagram,self.ds,self.reports,self.resources)
    def test_rendering_provenance_preserved(self):
        self.assertFalse(self.diagram['rendering']['mermaid_engine_executed'])
        self.assertEqual(self.diagram['rendering']['visual_qa'],'passed')
    def test_resources_export_deterministic(self):
        self.assertEqual(build_export(),build_export())
    def test_resources_are_separate_from_awards(self):
        data=build_export();self.assertNotIn('reports',data);self.assertNotIn('reward',data['resources'][0])

if __name__=='__main__':unittest.main()
