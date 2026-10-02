import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate import Invalid, validate_library

class ReportIdentityTests(unittest.TestCase):
    def setUp(self):
        self.records=[json.loads((ROOT/f'data/reports/{id}.json').read_text()) for id in (
            'github-fork-collaboration-authorization-2021','github-fork-collaboration-consent-2021')]
    def check(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for d in ['schema','data/reports']:(root/d).mkdir(parents=True,exist_ok=True)
            for f in ['schema/report.schema.json','data/taxonomy.json']:(root/f).write_text((ROOT/f).read_text())
            for r in self.records:(root/f'data/reports/{r["id"]}.json').write_text(json.dumps(r))
            return validate_library(root)
    def test_distinct_shared_source_reports_accepted(self):
        self.assertEqual(len(self.check()[0]),2)
    def test_shared_source_missing_identity_rejected(self):
        del self.records[1]['report_identity']
        with self.assertRaises(Invalid):self.check()
    def test_duplicate_cve_rejected(self):
        self.records[1]['cve_ids']=self.records[0]['cve_ids'][:]
        self.records[1]['report_identity']['value']=self.records[0]['report_identity']['value']
        with self.assertRaises(Invalid):self.check()
    def test_different_url_cannot_recount_cve(self):
        self.records[1]['sources'][0]['url']='https://example.com/other-report'
        self.records[1]['cve_ids']=self.records[0]['cve_ids'][:]
        self.records[1]['report_identity']['value']=self.records[0]['report_identity']['value']
        with self.assertRaises(Invalid):self.check()
    def test_identity_needs_matching_cve(self):
        self.records[1]['report_identity']['value']='CVE-2021-99999'
        with self.assertRaises(Invalid):self.check()
    def test_identity_needs_primary_evidence(self):
        self.records[1]['report_identity']['source_id']='vendor-release'
        with self.assertRaises(Invalid):self.check()
    def test_identity_needs_cve_support(self):
        self.records[1]['sources'][0]['supports'].remove('cve')
        with self.assertRaises(Invalid):self.check()
    def test_identity_needs_new_schema(self):
        self.records[1]['schema_version']='1.0.0'
        with self.assertRaises(Invalid):self.check()
    def test_same_award_cannot_be_reused(self):
        self.records[1]['reward']['evidence_quote']=self.records[0]['reward']['evidence_quote']
        with self.assertRaises(Invalid):self.check()
    def test_shared_source_quotes_have_combined_limit(self):
        self.records[1]['reward']['evidence_quote']=' '.join(['word']*17)
        with self.assertRaises(Invalid):self.check()
    def test_fragment_is_not_a_report_discriminator(self):
        del self.records[1]['report_identity']
        self.records[1]['sources'][0]['url']+='#another-section'
        with self.assertRaises(Invalid):self.check()
    def test_shared_source_requires_award_date(self):
        self.records[1]['dates']['awarded']={'value':None,'precision':None,'basis':'not_reported','source_id':None,'note':None}
        with self.assertRaises(Invalid):self.check()
if __name__=='__main__':unittest.main()
