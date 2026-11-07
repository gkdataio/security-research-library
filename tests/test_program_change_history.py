"""Offline retention checks; no official pages or asset URLs are requested."""
import copy
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest

from test_program_changes import fixture
from check_program_changes import append_history, inventory, validate_history, Invalid, HISTORY_PATH


class ProgramHistoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'history.json'
        self.before = inventory(fixture())
        changed = fixture()
        changed['bounty_captures']['captures'][0]['assets'][0]['scope'] = 'out'
        self.after = inventory(changed)

    def record(self, before=None, after=None, timestamp='2026-11-07T00:00:00Z'):
        return append_history(self.path, 'a' * 40,
                              self.before if before is None else before,
                              self.after if after is None else after, timestamp)

    def test_scope_move_retained_and_retry_idempotent(self):
        history, added = self.record()
        self.assertTrue(added)
        fields = history['entries'][0]['changes'][0]['fields']
        self.assertEqual({f['field'] for f in fields}, {'capture.in_scope', 'capture.out_of_scope'})
        original = self.path.read_bytes()
        self.assertFalse(self.record(timestamp='2026-11-08T00:00:00Z')[1])
        self.assertEqual(self.path.read_bytes(), original)
        validate_history(history)

    def test_no_change_does_not_erase_prior_batches(self):
        self.record()
        original = self.path.read_bytes()
        self.assertFalse(self.record(after=self.before)[1])
        self.assertEqual(self.path.read_bytes(), original)

    def test_distinct_change_appends_without_mutating_old_entry(self):
        history, _ = self.record()
        old = copy.deepcopy(history['entries'][0])
        history, added = self.record(before=self.after, after=self.before)
        self.assertTrue(added)
        self.assertEqual(len(history['entries']), 2)
        self.assertEqual(history['entries'][0], old)

    def test_added_and_removed_programs_retain_scope_snapshot(self):
        for before, after, kind in (({}, self.before, 'added'), (self.before, {}, 'removed')):
            history, _ = self.record(before=before, after=after)
            event = history['entries'][-1]['changes'][0]
            self.assertEqual(event['kind'], kind)
            self.assertTrue(event['snapshot']['capture']['in_scope'])

    def test_corrupt_or_modified_history_is_not_overwritten(self):
        for raw in ('{', '{}'):
            self.path.write_text(raw)
            with self.assertRaises(Invalid):
                self.record()
            self.assertEqual(self.path.read_text(), raw)
        self.path.unlink()
        history, _ = self.record()
        history['entries'][0]['current_digest'] = 'tampered'
        self.path.write_text(json.dumps(history))
        original = self.path.read_bytes()
        with self.assertRaises(Invalid):
            self.record()
        self.assertEqual(self.path.read_bytes(), original)

    def test_active_writer_blocks_without_losing_history(self):
        self.record()
        original = self.path.read_bytes()
        self.path.with_suffix('.json.lock').touch()
        with self.assertRaises(Invalid):
            self.record()
        self.assertEqual(self.path.read_bytes(), original)

    def test_committed_feed_is_valid(self):
        root = Path(__file__).resolve().parents[1]
        validate_history(json.loads((root / HISTORY_PATH).read_text()))

    def test_initial_no_change_creates_empty_feed_not_fake_event(self):
        history, added = self.record(after=self.before)
        self.assertFalse(added)
        self.assertEqual(history['entries'], [])

    def test_cli_protects_retained_history_and_separates_live_signals(self):
        root = Path(__file__).resolve().parents[1]
        for options in (("--record-history", "--live"),
                        ("--json-out", str(root / HISTORY_PATH)),
                        ("--state", str(root / HISTORY_PATH))):
            result = subprocess.run([sys.executable, str(root / "scripts/check_program_changes.py"),
                                     *options], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn("error:", result.stderr)
