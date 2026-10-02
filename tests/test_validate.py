import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate import Invalid, validate_library, validate_record, normalize_url
from export import build_export

class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.schema=json.loads((ROOT/'schema/report.schema.json').read_text())
        self.taxonomy=json.loads((ROOT/'data/taxonomy.json').read_text())
        self.record=json.loads((ROOT/'data/reports/google-cloud-build-approval-toctou-2025.json').read_text())
    def check(self):
        return validate_record(self.record,self.taxonomy,self.schema)
    def test_library_is_valid(self):
        records,_=validate_library(ROOT)
        self.assertGreaterEqual(len(records),1)
    def test_below_threshold_rejected(self):
        self.record['reward']['amount']=9999
        with self.assertRaises(Invalid):self.check()
    def test_boolean_amount_rejected(self):
        self.record['reward']['amount']=True
        with self.assertRaises(Invalid):self.check()
    def test_non_usd_rejected_from_qualified_data(self):
        self.record['reward']['currency']='EUR'
        with self.assertRaises(Invalid):self.check()
    def test_aggregate_reward_rejected(self):
        self.record['reward']['scope']='program_total'
        with self.assertRaises(Invalid):self.check()
    def test_unknown_fields_rejected(self):
        self.record['exploit_steps']=['not permitted']
        with self.assertRaises(Invalid):self.check()
    def test_undefined_taxonomy_rejected(self):
        self.record['skillset_ids']=['unregistered']
        with self.assertRaises(Invalid):self.check()
    def test_false_vendor_attribution_rejected(self):
        self.record['reward']['evidence_level']='vendor_confirmed'
        with self.assertRaises(Invalid):self.check()
    def test_unknown_source_rejected(self):
        self.record['dates']['reported']['source_id']='missing'
        with self.assertRaises(Invalid):self.check()
    def test_date_order_rejected(self):
        self.record['dates']['reported']['value']='2026-01-01'
        with self.assertRaises(Invalid):self.check()
    def test_impossible_date_rejected(self):
        self.record['dates']['reported']['value']='2024-02-31'
        with self.assertRaises(Invalid):self.check()
    def test_future_date_rejected(self):
        self.record['dates']['published']['value']='2027-01-01'
        with self.assertRaises(Invalid):self.check()
    def test_partial_date_precision_rejected(self):
        self.record['dates']['reported']['value']='2024-11'
        with self.assertRaises(Invalid):self.check()
    def test_partial_date_with_precision_accepted(self):
        self.record['dates']['reported']['value']='2024-11'
        self.record['dates']['reported']['precision']='month'
        self.check()
    def test_null_date_invariants(self):
        self.record['dates']['paid']['precision']='day'
        with self.assertRaises(Invalid):self.check()
    def test_inference_requires_note(self):
        self.record['dates']['reported']['basis']='inferred'
        self.record['dates']['reported']['note']=None
        with self.assertRaises(Invalid):self.check()
    def test_recency_requires_evidence(self):
        self.record['recency']['within_preferred_window']=True
        with self.assertRaises(Invalid):self.check()
    def test_quote_length_rejected(self):
        self.record['reward']['evidence_quote']=' '.join(['word']*26)
        with self.assertRaises(Invalid):self.check()
    def test_duplicate_source_rejected(self):
        self.record['sources'].append(copy.deepcopy(self.record['sources'][0]))
        with self.assertRaises(Invalid):self.check()
    def test_source_url_normalization(self):
        self.assertEqual(normalize_url('https://EXAMPLE.com/article/#section'),normalize_url('https://example.com/article'))
    def test_duplicate_primary_url_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for d in ['schema','data/reports']: (root/d).mkdir(parents=True,exist_ok=True)
            (root/'schema/report.schema.json').write_text(json.dumps(self.schema))
            (root/'data/taxonomy.json').write_text(json.dumps(self.taxonomy))
            for id_ in ['copy-one','copy-two']:
                rec=copy.deepcopy(self.record);rec['id']=id_
                (root/f'data/reports/{id_}.json').write_text(json.dumps(rec))
            with self.assertRaises(Invalid):validate_library(root)
    def test_export_deterministic(self):
        self.assertEqual(build_export(ROOT),build_export(ROOT))
    def test_competition_type_preserved(self):
        out=build_export(ROOT)
        pg=next(r for r in out['reports'] if r['id']=='postgresql-multibyte-validation-cve-2026-2006')
        self.assertEqual(pg['reward']['type'],'competition_award')
        self.assertIsNone(pg['dates']['paid']['value'])
    def test_unknown_amount_candidates_excluded(self):
        out=build_export(ROOT)
        self.assertFalse(any(r['id'].startswith('dependabot') for r in out['reports']))

if __name__=='__main__':unittest.main()
