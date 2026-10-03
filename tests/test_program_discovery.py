import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from validate import Invalid
from export_program_discovery import identity_url,validate_batch,build

class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.schema=json.loads((ROOT/'schema/program-discovery.schema.json').read_text())
        self.batch={'schema_version':'1.0.0','id':'test-listing','platform':'HackerOne','reviewed_at':'2026-10-02T21:30:00Z','review_state':'directory_listing_only','coverage':{'completeness':'partial','filters':'Example visible filter','pagination_note':'First page','continuation_note':'Continue observed pagination','limitations':['Policy not reviewed']},'sources':[{'id':'directory','url':'https://hackerone.com/directory','observed_at':'2026-10-02T21:29:00Z','access_method':'browser','page_label':'First page'}],'entries':[{'id':'example','name':'Example','program_url':'https://hackerone.com/example?type=team','program_type':'unknown','submission_status':'unknown','source_ids':['directory'],'evidence_note':'Directory listing only'}],'content_scope':'public_program_listing_metadata','rights':'Original selection and commentary CC BY 4.0; facts, linked sources and trademarks retain their own rights.'}
    def test_valid(self):validate_batch(self.batch,self.schema)
    def test_display_query_dedup(self):self.assertEqual(identity_url('https://hackerone.com/example?type=team'),identity_url('https://hackerone.com/example/'))
    def test_unknown_query_preserved(self):self.assertNotEqual(identity_url('https://hackerone.com/example?a=1'),identity_url('https://hackerone.com/example?a=2'))
    def test_no_target_inventory(self):
        self.batch['entries'][0]['targets']=['example.invalid']
        with self.assertRaises(Invalid):validate_batch(self.batch,self.schema)
    def test_nonplatform_url(self):
        self.batch['entries'][0]['program_url']='https://example.invalid/'
        with self.assertRaises(Invalid):validate_batch(self.batch,self.schema)
    def test_report_url_not_program(self):
        self.batch['entries'][0]['program_url']='https://hackerone.com/reports/123'
        with self.assertRaises(Invalid):validate_batch(self.batch,self.schema)
    def test_missing_provenance(self):
        self.batch['entries'][0]['source_ids']=['unobserved']
        with self.assertRaises(Invalid):validate_batch(self.batch,self.schema)
    def test_duplicate_page_identity(self):
        other=copy.deepcopy(self.batch['entries'][0]);other.update(id='second',program_url='https://hackerone.com/example');self.batch['entries'].append(other)
        with self.assertRaises(Invalid):validate_batch(self.batch,self.schema)
    def test_no_future_source(self):
        self.batch['sources'][0]['observed_at']='2027-01-01T00:00:00Z'
        with self.assertRaises(Invalid):validate_batch(self.batch,self.schema)
    def test_export_deterministic(self):self.assertEqual(build(),build())
    def test_overlap_not_counted_as_pending(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'data/program-discovery').mkdir(parents=True);(root/'data/programs').mkdir();(root/'schema').mkdir()
            (root/'schema/program-discovery.schema.json').write_text(json.dumps(self.schema));(root/'data/program-discovery/test-listing.json').write_text(json.dumps(self.batch));(root/'data/programs/example.json').write_text(json.dumps({'id':'existing-policy','program_url':'https://hackerone.com/example'}))
            data=json.loads(build(root)['exports/program-discovery.json']);self.assertEqual(data['counts']['unique_program_page_listings'],1);self.assertEqual(data['counts']['already_has_verified_policy'],1);self.assertEqual(data['counts']['awaiting_policy_review'],0)
            self.assertEqual(data['counts']['verified_with_asset_scope'],0)
    def test_verified_scope_links_back_to_readable_directory(self):
        output=build()
        data=json.loads(output['exports/program-discovery.json'])
        linked=[item for item in data['listings'] if item['verified_asset_scope']]
        self.assertEqual(len(linked),data['counts']['verified_with_asset_scope'])
        for item in linked:
            with self.subTest(program=item['verified_policy_id']):
                self.assertIn('program-'+item['verified_policy_id'],output['docs/program-discovery/'+item['platform'].lower()+'.md'])
                self.assertGreater(item['verified_asset_scope']['in_scope_entries'],0)

if __name__=='__main__':unittest.main()
