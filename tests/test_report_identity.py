import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate import Invalid, validate_library, check_schema
from export import build_export

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
class SourceLabelIdentityTests(ReportIdentityTests):
    # Fixtures are synthetic structural examples, not new research records.
    def setUp(self):
        super().setUp()
        for index, record in enumerate(self.records, 1):
            record['schema_version'] = '1.2.0'
            record['cve_ids'] = []
            record['report_identity'].update(
                kind='source_label', value=f'Report #{index}',
                evidence_location=f'Synthetic report heading {index}')
            record['sources'][0]['supports'].append('report_identity')

    # CVE-specific expectations are covered by the original class.
    def test_identity_needs_matching_cve(self):
        self.records[1]['report_identity']['kind'] = 'cve'
        self.records[1]['report_identity']['value'] = 'CVE-2021-99999'
        with self.assertRaises(Invalid): self.check()

    def test_identity_needs_cve_support(self):
        self.records[1]['sources'][0]['supports'].remove('report_identity')
        with self.assertRaises(Invalid): self.check()

    def test_duplicate_cve_rejected(self):
        for record in self.records:
            record['cve_ids'] = ['CVE-2021-99999']
        with self.assertRaises(Invalid): self.check()

    def test_different_url_cannot_recount_cve(self):
        self.records[1]['sources'][0]['url'] = 'https://example.com/other-report'
        for record in self.records:
            record['cve_ids'] = ['CVE-2021-99999']
        with self.assertRaises(Invalid): self.check()

    def test_duplicate_labels_rejected(self):
        self.records[1]['report_identity']['value'] = '  REPORT   #1  '
        with self.assertRaisesRegex(Invalid, 'distinct source-backed identities'): self.check()

    def test_blank_labels_rejected(self):
        for value in ('', ' ', '\t\n'):
            with self.subTest(value=value):
                self.records[1]['report_identity']['value'] = value
                with self.assertRaises(Invalid): self.check()

    def test_blank_identity_locator_rejected(self):
        self.records[1]['report_identity']['evidence_location'] = '  '
        with self.assertRaises(Invalid): self.check()

    def test_missing_identity_fields_rejected(self):
        original = copy.deepcopy(self.records[1]['report_identity'])
        for field in original:
            with self.subTest(field=field):
                self.records[1]['report_identity'] = {k:v for k,v in original.items() if k != field}
                with self.assertRaises(Invalid): self.check()

    def test_source_label_rejected_in_old_versions(self):
        for version in ('1.0.0', '1.1.0'):
            with self.subTest(version=version):
                self.records[1]['schema_version'] = version
                # Isolate identity-version check from new source support marker.
                self.records[1]['sources'][0]['supports'] = ['reward', 'dates', 'cve']
                with self.assertRaisesRegex(Invalid, 'schema version'): self.check()

    def test_missing_reward_or_date_support_rejected(self):
        original = self.records[1]['sources'][0]['supports'][:]
        for field in ('reward', 'dates'):
            self.records[1]['sources'][0]['supports'] = [s for s in original if s != field]
            with self.assertRaises(Invalid): self.check()

    def test_mixed_identity_kinds_rejected(self):
        self.records[1]['report_identity'].update(kind='cve', value='CVE-2021-99999')
        self.records[1]['cve_ids'] = ['CVE-2021-99999']
        with self.assertRaisesRegex(Invalid, 'cannot mix'): self.check()

    def test_shared_source_requires_report_date(self):
        self.records[1]['dates']['reported'] = dict(
            value=None, precision=None, basis='not_reported', source_id=None, note=None)
        with self.assertRaises(Invalid): self.check()

    def test_reused_award_location_rejected(self):
        self.records[1]['reward']['evidence_location'] = self.records[0]['reward']['evidence_location']
        with self.assertRaises(Invalid): self.check()

    def test_separate_award_source_rejected(self):
        source = copy.deepcopy(self.records[1]['sources'][0])
        source.update(id='other', url='https://example.com/other-award')
        self.records[1]['sources'].append(source)
        self.records[1]['reward']['source_id'] = 'other'
        with self.assertRaises(Invalid): self.check()

    def test_chain_scope_rejected(self):
        self.records[1]['reward']['scope'] = 'chain'
        with self.assertRaises(Invalid): self.check()

    def test_label_preserved_exactly(self):
        self.records[1]['report_identity']['value'] = 'Report  #2 (separate award)'
        before = copy.deepcopy(self.records)
        self.check()
        self.assertEqual(self.records, before)

class IdentityCompatibilityTests(unittest.TestCase):
    def test_export_version_and_legacy_records_preserved(self):
        records, _ = validate_library(ROOT)
        exported = build_export(ROOT)
        self.assertEqual(exported['schema_version'], '1.2.0')
        self.assertEqual({r['id']:r for r in records}, {r['id']:r for r in exported['reports']})

    def test_oneof_requires_exactly_one_match(self):
        for spec in ({'oneOf':[{'type':'integer'}, {'type':'number'}]},
                     {'oneOf':[{'type':'string'}, {'type':'null'}]}):
            with self.assertRaises(Invalid): check_schema(1, spec, spec)
        check_schema('label', {'oneOf':[{'type':'string'}, {'type':'null'}]}, {})

    def test_cve_identity_supported_in_new_version(self):
        fixture = ReportIdentityTests()
        fixture.setUp()
        for record in fixture.records: record['schema_version'] = '1.2.0'
        self.assertEqual(len(fixture.check()[0]), 2)

    def test_new_version_without_identity_is_valid(self):
        fixture = ReportIdentityTests()
        fixture.setUp()
        fixture.records = fixture.records[:1]
        fixture.records[0]['schema_version'] = '1.2.0'
        del fixture.records[0]['report_identity']
        self.assertEqual(len(fixture.check()[0]), 1)

    def test_new_support_marker_rejected_for_old_versions(self):
        for version in ('1.0.0', '1.1.0'):
            with self.subTest(version=version):
                fixture = ReportIdentityTests()
                fixture.setUp()
                fixture.records = fixture.records[:1]
                record = fixture.records[0]
                record['schema_version'] = version
                del record['report_identity']
                record['sources'][0]['supports'].append('report_identity')
                with self.assertRaisesRegex(Invalid, 'source support requires'): fixture.check()

    def test_cve_format_retained_in_schema(self):
        fixture = ReportIdentityTests()
        fixture.setUp()
        for record in fixture.records:
            record['schema_version'] = '1.2.0'
            record['report_identity']['value'] = 'not-a-cve'
            record['cve_ids'] = []
        with self.assertRaises(Invalid): fixture.check()

if __name__=='__main__':unittest.main()
