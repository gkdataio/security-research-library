"""Offline contract, provenance and deterministic output checks for recognition."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from export_recognition import build_export, build_page, load_records, validate_record
from validate import Invalid


class RecognitionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / 'schema/recognition.schema.json').read_text())
        cls.records = load_records(ROOT)

    def record(self):
        return copy.deepcopy(self.records[0])

    def test_records_validate_and_keep_stable_ids(self):
        for record in self.records:
            validate_record(record, self.schema)
            self.assertTrue((ROOT / 'data/recognition' / (record['id'] + '.json')).is_file())

    def test_unknown_source_is_rejected(self):
        record = self.record()
        record['reporting']['source_ids'] = ['missing']
        with self.assertRaisesRegex(Invalid, 'unknown recognition source'):
            validate_record(record, self.schema)

    def test_url_must_belong_to_field_evidence(self):
        record = self.record()
        record['recognition']['url'] = 'https://example.org/unreviewed'
        with self.assertRaisesRegex(Invalid, 'missing from linked evidence'):
            validate_record(record, self.schema)

    def test_duplicate_source_ids_are_rejected(self):
        record = self.record()
        record['sources'].append(copy.deepcopy(record['sources'][0]))
        with self.assertRaisesRegex(Invalid, 'duplicate recognition source'):
            validate_record(record, self.schema)

    def test_source_cannot_postdate_review(self):
        record = self.record()
        record['sources'][0]['retrieved_at'] = '2099-01-01T00:00:00Z'
        with self.assertRaisesRegex(Invalid, 'after recognition review'):
            validate_record(record, self.schema)

    def test_timezone_required(self):
        record = self.record()
        record['reviewed_at'] = '2026-10-11T00:00:00'
        with self.assertRaises(Invalid):
            validate_record(record, self.schema)

    def test_asset_inventory_is_not_a_schema_field(self):
        record = self.record()
        record['asset_scope'] = {}
        with self.assertRaisesRegex(Invalid, 'unexpected keys'):
            validate_record(record, self.schema)

    def test_payment_and_submission_are_not_inferred(self):
        record = self.record()
        record['submission_availability'] = 'open'
        with self.assertRaises(Invalid):
            validate_record(record, self.schema)
        record = self.record()
        record['rewards']['status'] = 'paid'
        with self.assertRaises(Invalid):
            validate_record(record, self.schema)

    def test_non_https_url_is_rejected(self):
        record = self.record()
        record['sources'][0]['url'] = 'http://example.org'
        with self.assertRaises(Invalid):
            validate_record(record, self.schema)

    def test_empty_or_duplicate_field_evidence_rejected(self):
        for refs in ([], ['recognition', 'recognition']):
            record = self.record()
            record['recognition']['source_ids'] = refs
            with self.assertRaises(Invalid):
                validate_record(record, self.schema)

    def test_duplicate_organizations_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'schema').mkdir()
            (root / 'data/recognition').mkdir(parents=True)
            (root / 'schema/recognition.schema.json').write_text(json.dumps(self.schema))
            record = self.record()
            (root / 'data/recognition' / (record['id'] + '.json')).write_text(json.dumps(record))
            record['id'] += '-duplicate'
            (root / 'data/recognition' / (record['id'] + '.json')).write_text(json.dumps(record))
            with self.assertRaisesRegex(Invalid, 'duplicate recognition page or organization'):
                load_records(root)

    def test_export_current(self):
        saved = (ROOT / 'exports/recognition.json').read_text()
        expected = json.dumps(build_export(self.records), ensure_ascii=False, indent=2) + '\n'
        self.assertEqual(saved, expected)
        self.assertEqual(build_export(self.records)['counts']['organizations'], len(self.records))

    def test_page_current_and_contains_all_source_urls(self):
        page = build_page(self.records)
        self.assertEqual((ROOT / 'docs/direct-disclosure.md').read_text(), page)
        for record in self.records:
            self.assertIn('id="' + record['id'] + '"', page)
            for source in record['sources']:
                self.assertIn(source['url'], page)

    def test_no_bounty_label_preserves_policy_distinction(self):
        record = self.record()
        record['rewards']['status'] = 'no_bounty'
        record['rewards']['summary'] = 'No bug bounty program is currently offered.'
        page = build_page([record])
        self.assertIn('No-bounty policy', page)
        self.assertIn('No bug bounty program is currently offered', page)
        self.assertNotIn('Policy says no monetary rewards', page)

    def test_mixed_route_note_is_preserved(self):
        record = next(record for record in self.records if record['id'] == 'bosch-security-recognition')
        self.assertEqual(record['reporting']['route'], 'direct_email')
        self.assertIn('Bugcrowd is preferred for websites', record['reporting']['summary'])
        self.assertIn('Bugcrowd is preferred for websites', build_page([record]))

    def test_page_preserves_boundaries_and_escapes_content(self):
        record = self.record()
        record['organization'] = '<script>alert(1)</script> | [name]'
        page = build_page([record])
        self.assertNotIn('<script>', page)
        self.assertIn('&lt;script&gt;', page)
        self.assertIn('Recognition does not imply payment or permission to test.', page)
        self.assertIn('Submission availability: not tested.', page)


if __name__ == '__main__':
    unittest.main()
