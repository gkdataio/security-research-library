"""Offline regression fixtures; no real program policy or scope claims."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from export_programs import build, validate_program
from validate import Invalid


class ScopeContextTests(unittest.TestCase):
    def setUp(self):
        self.schema = json.loads((ROOT / 'schema/program.schema.json').read_text())
        self.rec = {
            'schema_version': '1.4.0', 'id': 'example-policy', 'name': 'Example Policy',
            'operator': 'Example', 'platform': 'Direct',
            'program_url': 'https://example.invalid/policy',
            'policy_url': 'https://example.invalid/policy',
            'announcement_urls': [], 'change_log_url': None,
            'rewards': {'currency': None, 'minimum': None, 'maximum': None,
                        'basis': 'advertised_not_individual_award',
                        'summary': 'Reward terms not established by this synthetic fixture.',
                        'source_ids': ['policy']},
            'eligibility': {'summary': 'Eligibility remains subject to current terms.', 'source_ids': ['policy']},
            'restrictions': {'summary': 'Privacy and availability protections apply.', 'source_ids': ['policy']},
            'submission_status': {'value': 'unknown', 'summary': 'Not established.', 'source_ids': []},
            'last_verified_at': '2026-01-03T12:00:00Z',
            'limitations': ['Synthetic fixture; no real policy claim or authorization.'],
            'sources': [{'id': 'policy', 'title': 'Example policy',
                         'url': 'https://example.invalid/policy', 'publisher': 'Example',
                         'retrieved_at': '2026-01-01T12:00:00Z',
                         'provenance': 'official_primary', 'access_method': 'text'}],
            'content_scope': 'public_program_policy_summary',
            'rights': 'Original summary CC BY 4.0; linked sources and trademarks retain their own rights.',
            'scope_context': {
                'included_summary': 'Broad product categories are described by the reviewed policy; completeness is not established.',
                'excluded_summary': 'Excluded categories remain subject to current policy restrictions; no exhaustive claim is made.',
                'source_ids': ['policy'], 'policy_urls': ['https://example.invalid/policy'],
                'verified_at': '2026-01-02T12:00:00Z',
            },
        }

    def outputs(self, records):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'schema').mkdir()
            (root / 'data/programs').mkdir(parents=True)
            (root / 'schema/program.schema.json').write_text(json.dumps(self.schema))
            for rec in records:
                (root / 'data/programs' / (rec['id'] + '.json')).write_text(json.dumps(rec))
            first = build(root)
            self.assertEqual(first, build(root))
            return first

    def test_valid_scope(self):
        validate_program(self.rec, self.schema)

    def test_context_is_optional_in_all_versions(self):
        self.rec.pop('scope_context')
        for version in ('1.1.0', '1.2.0', '1.3.0', '1.4.0', '1.5.0'):
            with self.subTest(version=version):
                self.rec['schema_version'] = version
                validate_program(self.rec, self.schema)

    def test_context_requires_version_1_4(self):
        for version in ('1.1.0', '1.2.0', '1.3.0'):
            with self.subTest(version=version):
                self.rec['schema_version'] = version
                with self.assertRaisesRegex(Invalid, 'scope context requires program record version 1.4.0'):
                    validate_program(self.rec, self.schema)

    def test_program_type_supported_in_1_3_and_1_4(self):
        self.rec.pop('scope_context')
        self.rec['program_type'] = {'value': 'paid_bounty', 'summary': 'Synthetic classification.', 'source_ids': ['policy']}
        for version in ('1.3.0', '1.4.0', '1.5.0'):
            with self.subTest(version=version):
                self.rec['schema_version'] = version
                validate_program(self.rec, self.schema)

    def test_closed_supported_in_1_2_and_later(self):
        self.rec.pop('scope_context')
        self.rec['submission_status'].update(value='closed', source_ids=['policy'])
        for version in ('1.2.0', '1.3.0', '1.4.0', '1.5.0'):
            with self.subTest(version=version):
                self.rec['schema_version'] = version
                validate_program(self.rec, self.schema)

    def test_missing_required_context_fields(self):
        for field in self.rec['scope_context']:
            with self.subTest(field=field):
                rec = copy.deepcopy(self.rec)
                del rec['scope_context'][field]
                with self.assertRaises(Invalid):
                    validate_program(rec, self.schema)

    def test_invalid_context_shape(self):
        for value in (None, '', [], {}, True):
            with self.subTest(value=value):
                rec = copy.deepcopy(self.rec)
                rec['scope_context'] = value
                with self.assertRaises(Invalid):
                    validate_program(rec, self.schema)

    def test_empty_and_duplicate_evidence_rejected(self):
        for field in ('source_ids', 'policy_urls'):
            for value in ([], self.rec['scope_context'][field] * 2):
                with self.subTest(field=field, value=value):
                    rec = copy.deepcopy(self.rec)
                    rec['scope_context'][field] = value
                    with self.assertRaises(Invalid):
                        validate_program(rec, self.schema)

    def test_blank_summaries_rejected(self):
        for field in ('included_summary', 'excluded_summary'):
            for value in ('', ' \n\t'):
                with self.subTest(field=field, value=value):
                    rec = copy.deepcopy(self.rec)
                    rec['scope_context'][field] = value
                    with self.assertRaises(Invalid):
                        validate_program(rec, self.schema)

    def test_unknown_source_rejected(self):
        self.rec['scope_context']['source_ids'] = ['missing']
        with self.assertRaisesRegex(Invalid, 'unknown scope context source'):
            validate_program(self.rec, self.schema)

    def test_nonofficial_source_rejected(self):
        self.rec['sources'][0]['provenance'] = 'search_snippet'
        with self.assertRaises(Invalid):
            validate_program(self.rec, self.schema)

    def test_scope_url_requires_linked_source(self):
        self.rec['sources'].append(dict(self.rec['sources'][0], id='other', url='https://example.invalid/other-policy'))
        self.rec['scope_context']['policy_urls'] = ['https://example.invalid/other-policy']
        with self.assertRaisesRegex(Invalid, 'scope policy URL lacks a linked reviewed source'):
            validate_program(self.rec, self.schema)

    def test_unreviewed_urls_and_fragments_rejected(self):
        for url in ('https://example.invalid/unreviewed-policy',
                    'https://example.invalid/policy#invented',
                    'https://example.invalid/policy?unreviewed=1',
                    'http://example.invalid/policy'):
            with self.subTest(url=url):
                self.rec['scope_context']['policy_urls'] = [url]
                with self.assertRaises(Invalid):
                    validate_program(self.rec, self.schema)

    def test_exact_reviewed_fragment_supported(self):
        url = 'https://example.invalid/policy#coverage'
        self.rec['sources'][0]['url'] = url
        self.rec['scope_context']['policy_urls'] = [url]
        validate_program(self.rec, self.schema)

    def test_normalized_section_requires_same_recorded_fragment(self):
        self.rec['sources'][0]['url'] = 'https://example.invalid/policy#coverage'
        self.rec['scope_context']['policy_urls'] = ['https://EXAMPLE.invalid/policy/#coverage']
        validate_program(self.rec, self.schema)
        for url in ('https://example.invalid/policy#Coverage',
                    'https://example.invalid/policy?new=1#coverage',
                    'https://example.invalid/policy#exclusions',
                    'https://example.invalid/policy'):
            with self.subTest(url=url):
                self.rec['scope_context']['policy_urls'] = [url]
                with self.assertRaises(Invalid):
                    validate_program(self.rec, self.schema)

    def test_duplicate_normalized_section_rejected(self):
        self.rec['sources'][0]['url'] = 'https://example.invalid/policy#coverage'
        self.rec['scope_context']['policy_urls'] = [
            'https://example.invalid/policy#coverage', 'https://EXAMPLE.invalid/policy/#coverage']
        with self.assertRaisesRegex(Invalid, 'duplicate scope policy URL'):
            validate_program(self.rec, self.schema)

    def test_invalid_scope_timestamp_rejected(self):
        for value in ('not-a-date', '2026-02-30T12:00:00Z', '2026-01-02T12:00:00', '2026-01-02'):
            with self.subTest(value=value):
                self.rec['scope_context']['verified_at'] = value
                with self.assertRaises(Invalid):
                    validate_program(self.rec, self.schema)

    def test_scope_verification_cannot_be_after_overall_verification(self):
        self.rec['scope_context']['verified_at'] = '9999-01-01T00:00:00Z'
        with self.assertRaisesRegex(Invalid, 'scope verification is after program verification'):
            validate_program(self.rec, self.schema)

    def test_cited_source_cannot_be_after_scope_verification(self):
        self.rec['sources'][0]['retrieved_at'] = '2026-01-03T00:00:00Z'
        with self.assertRaisesRegex(Invalid, 'source retrieval is after scope verification'):
            validate_program(self.rec, self.schema)

    def test_source_cannot_be_after_overall_verification(self):
        self.rec['sources'][0]['retrieved_at'] = '9999-01-01T00:00:00Z'
        with self.assertRaisesRegex(Invalid, 'source retrieval is after program verification'):
            validate_program(self.rec, self.schema)

    def test_equal_timestamp_boundaries_and_timezones(self):
        self.rec['sources'][0]['retrieved_at'] = '2026-01-03T13:00:00+01:00'
        self.rec['scope_context']['verified_at'] = '2026-01-03T07:00:00-05:00'
        validate_program(self.rec, self.schema)

    def test_unrelated_later_source_does_not_reverify_scope(self):
        self.rec['sources'].append(dict(self.rec['sources'][0], id='later', retrieved_at='2026-01-03T00:00:00Z'))
        validate_program(self.rec, self.schema)

    def test_operational_structured_fields_rejected(self):
        for field in ('targets', 'assets', 'testing_instructions', 'endpoints'):
            with self.subTest(field=field):
                rec = copy.deepcopy(self.rec)
                rec['scope_context'][field] = ['Excluded structured content.']
                with self.assertRaises(Invalid):
                    validate_program(rec, self.schema)

    def test_legacy_export_preserves_records_and_coverage(self):
        records = []
        for version in ('1.1.0', '1.2.0', '1.3.0'):
            rec = copy.deepcopy(self.rec)
            rec.pop('scope_context')
            rec['schema_version'] = version
            rec['id'] += '-' + version.replace('.', '-')
            rec['program_url'] = rec['policy_url'] = rec['sources'][0]['url'] = 'https://example.invalid/' + rec['id']
            records.append(rec)
        outputs = self.outputs(records)
        exported = json.loads(outputs['exports/programs.json'])
        self.assertEqual(exported['schema_version'], '1.5.0')
        self.assertEqual(exported['programs'], records)
        self.assertEqual(exported['counts'], {'programs': 3, 'programs_with_scope_context': 0,
                                               'programs_without_scope_context': 3,
                                               'programs_with_asset_scope': 0, 'programs_without_asset_scope': 3,
                                               'in_scope_entries': 0, 'out_of_scope_entries': 0})
        self.assertIn('0 of 3 records', outputs['docs/programs.md'])
        self.assertEqual(outputs['docs/programs.md'].count('Missing context means'), 1)
        self.assertNotIn('**Scope context**', outputs['docs/programs.md'])

    def test_enriched_export_is_deterministic_and_retains_evidence(self):
        outputs = self.outputs([self.rec])
        exported = json.loads(outputs['exports/programs.json'])
        self.assertEqual(exported['programs'], [self.rec])
        self.assertEqual(exported['counts'], {'programs': 1, 'programs_with_scope_context': 1,
                                               'programs_without_scope_context': 0,
                                               'programs_with_asset_scope': 0, 'programs_without_asset_scope': 1,
                                               'in_scope_entries': 0, 'out_of_scope_entries': 0})
        page = outputs['docs/programs.md']
        for heading in ('**Scope context**', '**Included coverage:**', '**Excluded coverage:**',
                        '**Scope verified:**', '**Reviewed policy links**', '**Scope evidence:**'):
            self.assertIn(heading, page)
        self.assertIn('not an asset inventory, a completeness guarantee or authorization to test', page)
        self.assertIn('https://example.invalid/policy', page)

    def test_scope_summary_is_escaped_in_readable_output(self):
        self.rec['scope_context']['included_summary'] = '<script>[unsafe](link)</script>'
        page = self.outputs([self.rec])['docs/programs.md']
        self.assertNotIn('<script>', page)
        self.assertIn('&lt;script&gt;', page)


if __name__ == '__main__':
    unittest.main()
