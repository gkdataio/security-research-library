import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from validate import Invalid, validate_library
from validate_extra import validate_all, validate_resource, validate_diagram
from export_resources import build_export, latest_review_date

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
    def test_resource_timestamp_formats_rejected(self):
        for field in ('reviewed_at','retrieved_at'):
            for value in ('2026-10-03T05:00:00','2026-10-03','not-a-date',
                          '2026-02-30T05:00:00Z','2026-10-03T25:00:00Z'):
                with self.subTest(field=field,value=value):
                    rec=copy.deepcopy(self.rec)
                    if field=='reviewed_at':rec['freshness'][field]=value
                    else:rec['sources'][0][field]=value
                    with self.assertRaisesRegex(Invalid,'invalid date-time'):
                        validate_resource(rec,self.rs,self.tax,self.skills)
    def test_resource_retrieval_chronology_accepts_earlier_or_equal_instants(self):
        for reviewed,retrieved in (
            ('2026-10-03T05:00:00Z','2026-10-03T04:59:59Z'),
            ('2026-10-03T05:00:00Z','2026-10-03T05:00:00Z'),
            ('2026-10-03T05:00:00Z','2026-10-03T07:00:00+02:00'),
            ('2026-10-03T00:30:00+02:00','2026-10-02T22:00:00Z'),
            ('2026-10-03T05:00:00Z','2026-10-03T06:00:00+02:00'),
            ('2026-10-03T05:00:00Z','2026-10-03T00:00:00-05:00'),
        ):
            with self.subTest(reviewed=reviewed,retrieved=retrieved):
                rec=copy.deepcopy(self.rec)
                rec['freshness']['reviewed_at']=reviewed
                for source in rec['sources']:source['retrieved_at']=retrieved
                validate_resource(rec,self.rs,self.tax,self.skills)
    def test_resource_retrieval_after_review_rejected(self):
        for reviewed,retrieved in (
            ('2026-10-03T05:00:00Z','2026-10-03T05:00:01Z'),
            ('2026-10-03T05:00:00Z','2026-10-03T05:00:00.000001Z'),
            ('2026-10-03T05:00:00Z','2026-10-03T04:30:00-01:00'),
            ('2026-10-03T00:30:00+02:00','2026-10-02T23:00:00Z'),
        ):
            with self.subTest(reviewed=reviewed,retrieved=retrieved):
                rec=copy.deepcopy(self.rec)
                rec['freshness']['reviewed_at']=reviewed
                for source in rec['sources']:source['retrieved_at']=retrieved
                with self.assertRaisesRegex(Invalid,'source retrieval is after resource review'):
                    validate_resource(rec,self.rs,self.tax,self.skills)
    def test_resource_chronology_checks_every_source(self):
        self.rec['freshness']['reviewed_at']='2026-10-03T05:00:00Z'
        for source in self.rec['sources']:source['retrieved_at']='2026-10-03T05:00:00Z'
        extra=copy.deepcopy(self.rec['sources'][0])
        extra.update(id='secondary',url='https://example.com/secondary',retrieved_at='2026-10-03T05:00:01Z')
        self.rec['sources'].append(extra)
        with self.assertRaisesRegex(Invalid,'source retrieval is after resource review'):
            validate_resource(self.rec,self.rs,self.tax,self.skills)
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
    def test_export_date_uses_latest_review(self):
        self.assertEqual(latest_review_date([{'freshness': {'reviewed_at': '2026-10-03T01:00:00Z'}}], [{'reviewed_at': '2026-10-02T20:00:00Z'}]), '2026-10-03')
    def test_export_date_normalizes_utc(self):
        self.assertEqual(latest_review_date([{'freshness': {'reviewed_at': '2026-10-03T00:30:00+02:00'}}], [{'reviewed_at': '2026-10-02T23:00:00Z'}]), '2026-10-02')
    def test_resources_export_deterministic(self):
        self.assertEqual(build_export(),build_export())
    def test_resources_are_separate_from_awards(self):
        data=build_export();self.assertNotIn('reports',data);self.assertNotIn('reward',data['resources'][0])

if __name__=='__main__':unittest.main()
