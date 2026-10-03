"""Offline checks for sourced, dated program asset scope snapshots."""

import copy
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from export_programs import build, validate_program
from validate import Invalid


class AssetScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / 'schema/program.schema.json').read_text(encoding='utf-8'))
        cls.records = [json.loads(path.read_text(encoding='utf-8'))
                       for path in sorted((ROOT / 'data/programs').glob('*.json'))]

    def setUp(self):
        self.rec = copy.deepcopy(self.records[0])

    def test_every_verified_program_has_sourced_assets(self):
        self.assertGreater(len(self.records), 0)
        for rec in self.records:
            with self.subTest(program=rec['id']):
                self.assertEqual(rec['schema_version'], '1.5.0')
                self.assertIn('asset_scope', rec)
                self.assertTrue(rec['asset_scope']['in_scope'])
                validate_program(rec, self.schema)

    def test_export_counts_match_canonical_rows(self):
        exported = json.loads(build()['exports/programs.json'])
        counts = exported['counts']
        self.assertEqual(counts['programs_with_asset_scope'], len(self.records))
        self.assertEqual(counts['in_scope_entries'], sum(len(r['asset_scope']['in_scope']) for r in self.records))
        self.assertEqual(counts['out_of_scope_entries'], sum(len(r['asset_scope']['out_of_scope']) for r in self.records))
        self.assertIn('No explicit asset entry was captured', build()['docs/programs.md'])

    def test_assets_require_new_version(self):
        self.rec['schema_version'] = '1.4.0'
        with self.assertRaisesRegex(Invalid, 'asset scope requires program record version 1.5.0'):
            validate_program(self.rec, self.schema)

    def test_unknown_asset_source_rejected(self):
        self.rec['asset_scope']['in_scope'][0]['source_ids'] = ['missing']
        with self.assertRaisesRegex(Invalid, 'asset cites unknown or unrelated source'):
            validate_program(self.rec, self.schema)

    def test_late_asset_source_rejected(self):
        asset_source_id = self.rec['asset_scope']['source_ids'][0]
        next(s for s in self.rec['sources'] if s['id'] == asset_source_id)['retrieved_at'] = '9999-01-01T00:00:00Z'
        with self.assertRaisesRegex(Invalid, 'asset source retrieval is after asset verification'):
            validate_program(self.rec, self.schema)

    def test_duplicate_asset_rejected(self):
        self.rec['asset_scope']['in_scope'].append(copy.deepcopy(self.rec['asset_scope']['in_scope'][0]))
        with self.assertRaises(Invalid):
            validate_program(self.rec, self.schema)

    def test_untrusted_asset_label_is_escaped(self):
        self.rec['asset_scope']['in_scope'][0]['name'] = '<script>|[unsafe](url)</script>'
        validate_program(self.rec, self.schema)
        # Render the asset cell using the same escaping function used by the exporter.
        from build_navigation import text
        rendered = text(self.rec['asset_scope']['in_scope'][0]['name'])
        self.assertNotIn('<script>', rendered)
        self.assertIn('\\|', rendered)


if __name__ == '__main__':
    unittest.main()
