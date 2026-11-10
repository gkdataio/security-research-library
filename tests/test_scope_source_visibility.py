"""Historical rows, refresh health and independently reviewed transitions differ."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from scope_integrity import redacted_scope_row, redaction_warning
from scope_source_visibility import identity, load_visibility, visibility_lines
from export_scope_audit import build


class ScopeSourceVisibilityTests(unittest.TestCase):
    def item(self, name='example.test'):
        return {'program_url': 'https://hackerone.com/example?type=team',
                'scope_captured_at': '2026-11-01T00:00:00Z',
                'in_scope': [{'name': name, 'location': None}], 'out_of_scope': []}

    def test_masks_require_fully_hidden_name_and_location(self):
        for name in ('████', '▓▒░', '█ █'):
            self.assertTrue(redacted_scope_row({'name': name, 'location': None}))
            self.assertTrue(redacted_scope_row({'name': name, 'location': '  '}))
        for row in ({'name': '████', 'location': 'https://example.test'},
                    {'name': 'example█.test', 'location': None},
                    {'name': ' ', 'location': None}, {'name': 'example.test', 'location': None}):
            self.assertFalse(redacted_scope_row(row))
        self.assertIn('Every', redaction_warning([{'name': '████', 'location': None}]))
        self.assertIn('other rows', redaction_warning([{'name': '████'}, {'name': 'example.test'}]))

    def test_failure_does_not_replace_old_capture_and_later_success_clears_warning(self):
        item = self.item(); before = copy.deepcopy(item)
        key = identity(item['program_url'])
        outcome = {'status': 'failed', 'attempted_at': '2026-11-10T00:00:00Z', 'reason': 'HTTP 404; last-good scope retained'}
        lines = '\n'.join(visibility_lines(item, ({key: outcome}, {}), '../../../data/scope-refresh-status.json'))
        self.assertIn('Latest refresh failed', lines)
        self.assertIn('not a current scope verification', lines)
        self.assertEqual(item, before)
        outcome['status'] = 'refreshed'
        self.assertEqual(visibility_lines(item, ({key: outcome}, {}), 'audit.json'), [])
        outcome['status'] = 'failed'; item['scope_captured_at'] = '2026-11-11T00:00:00Z'
        self.assertEqual(visibility_lines(item, ({key: outcome}, {}), 'audit.json'), [])

    def test_deferred_date_and_exact_identity_no_unrelated_warning(self):
        item = self.item(); key = identity(item['program_url'])
        outcome = {'status': 'deferred', 'audit_completed_at': '2026-11-10T01:00:00Z', 'reason': 'Source access excluded'}
        lines = '\n'.join(visibility_lines(item, ({key: outcome}, {}), 'audit.json'))
        self.assertIn('Latest refresh deferred (2026-11-10T01:00:00Z)', lines)
        self.assertEqual(visibility_lines(item, ({key + '-other': outcome}, {}), 'audit.json'), [])
        self.assertNotEqual(identity(key + '?other=true'), key)

    def test_verified_transitions_are_dated_notes_not_scope_replacements(self):
        visibility = load_visibility(ROOT)
        reviews = visibility[1]
        self.assertGreaterEqual(len(reviews), 4)
        django = self.item(); django['program_url'] = 'https://hackerone.com/django?type=team'
        lines = '\n'.join(visibility_lines(django, visibility, 'audit.json'))
        self.assertIn('Existing HackerOne reports remain open', lines)
        self.assertIn('does not establish reward eligibility', lines)
        self.assertIn('https://www.djangoproject.com/weblog/2026/oct/08/django-security-reporting-update/', lines)
        for slug in ('cfpb-vdp', 'tva-vdp', 'usdot-vdp'):
            item = self.item(); item['program_url'] = 'https://bugcrowd.com/engagements/' + slug
            lines = '\n'.join(visibility_lines(item, visibility, 'audit.json'))
            self.assertIn('requires a separate Gov login', lines)
            self.assertIn('not a verified current scope or program closure', lines)

    def test_audit_separates_redacted_rows_without_changing_capture_history(self):
        audit = json.loads(build(ROOT)['exports/program-scope-audit.json'])
        counts = audit['counts']
        redacted = audit['redacted_only_programs']
        self.assertEqual(len(redacted), counts['distinct_redacted_only_programs'])
        self.assertEqual(len({row['id'] for row in redacted}), len(redacted))
        self.assertEqual(counts['distinct_with_non_redacted_scope_rows'] + len(redacted),
                         counts['distinct_scope_captured'])
        self.assertLessEqual(sum(row['captured_asset_rows'] for row in redacted),
                             counts['distinct_redacted_asset_rows'])
        self.assertTrue(all(row['captured_asset_rows'] > 0 for row in redacted))
        self.assertEqual(counts['distinct_scope_captured'] + counts['distinct_scope_gaps'],
                         counts['distinct_catalog_programs'])


if __name__ == '__main__':
    unittest.main()
