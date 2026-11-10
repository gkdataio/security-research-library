"""Malformed local state must fail closed before any HTTP request or rewrite."""
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import check_program_changes as changes

URL = 'https://example.invalid/program'
TARGETS = {URL: {'programs': ['listing:example'], 'platforms': ['Independent'],
                 'roles': ['program_page']}}


class LocalStateTests(unittest.TestCase):
    def rejected(self, raw):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'state.json'
            path.write_text(raw, encoding='utf-8')
            original = path.read_bytes()
            fetcher = Mock(side_effect=AssertionError('No network permitted'))
            for plan in (True, False):
                with self.subTest(plan=plan), self.assertRaises(changes.Invalid):
                    changes.check_live(TARGETS, path, plan=plan, fetcher=fetcher)
                self.assertEqual(path.read_bytes(), original)
            fetcher.assert_not_called()

    def test_malformed_state_containers_and_json(self):
        for state in (None, [], 3, 'state', {}, {'schema_version': '1.0.0', 'pages': []}):
            with self.subTest(state=state):
                self.rejected(json.dumps(state))
        self.rejected('{broken-json')

    def test_malformed_page_entries_are_not_dropped(self):
        for entry in (None, [], 3, 'entry', {'fingerprint': []}, {'fingerprint': 'old'},
                      {'last_failure': True}, {'etag': 42}, {'last_modified': []}):
            with self.subTest(entry=entry):
                self.rejected(json.dumps({'schema_version': '1.0.0', 'pages': {URL: entry}}))

    def test_malformed_times_do_not_bypass_failure_cooldown(self):
        for field in ('checked_at', 'attempted_at'):
            for value in (None, False, 123, [], {}, '', 'bad', '2026-11-10T07:00:00',
                          '2026-11-10', '0001-01-01T00:00:00+23:00'):
                with self.subTest(field=field, value=value):
                    entry = {'fingerprint': {'status': 200, 'sha256': 'last-good'},
                             'last_failure': {'status': 429, 'reason': 'rate_limited'},
                             field: value}
                    self.rejected(json.dumps({'schema_version': '1.0.0', 'pages': {URL: entry}}))

    def test_failure_without_attempt_timestamp_cannot_be_retried(self):
        for checked in (None, '2020-01-01T00:00:00Z'):
            entry = {'last_failure': {'status': 429, 'reason': 'rate_limited'}}
            if checked:
                entry['checked_at'] = checked
            self.rejected(json.dumps({'schema_version': '1.0.0', 'pages': {URL: entry}}))

    def test_entire_state_is_validated_before_selected_targets_are_requested(self):
        self.rejected(json.dumps({'schema_version': '1.0.0', 'pages': {
            URL: {'checked_at': '2020-01-01T00:00:00Z'},
            'https://other.invalid/program': {'attempted_at': 42}}}))

    def test_valid_offset_timestamps_preserve_most_recent_attempt(self):
        now = dt.datetime(2026, 11, 10, 14, 0, tzinfo=dt.timezone.utc)
        entry = {'checked_at': '2020-01-01T00:00:00Z',
                 'attempted_at': '2026-11-10T05:00:00-08:00'}
        self.assertTrue(changes._recent(entry, 12, now))
        self.assertFalse(changes._recent(entry, 0, now))
        self.assertFalse(changes._recent(entry, 0.5, now))

    def test_cli_returns_a_clear_error_without_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'state.json'
            path.write_text(json.dumps({'schema_version': '1.0.0', 'pages': {
                URL: {'attempted_at': 42}}}))
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/check_program_changes.py'),
                                     '--live', '--plan', '--state', str(path)],
                                    capture_output=True, text=True, check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('invalid local program-change timestamp', result.stderr)
            self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
