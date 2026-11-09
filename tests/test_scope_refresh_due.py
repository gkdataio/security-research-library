import copy
import datetime as dt
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from scope_refresh_due import refresh_due


class DailyRefreshDueTests(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime(2026, 11, 9, 14, 23, tzinfo=dt.timezone.utc)
        self.audit = {'completed_at': '2026-11-09T07:10:00Z', 'workflow_run_id': '123',
                      'results': [{'status': 'failed'}], 'counts': {'total': 1, 'failed': 1}}

    def test_completed_partial_attempt_is_not_retried(self):
        self.assertFalse(refresh_due(self.audit, 'schedule', self.now))

    def test_manual_dispatch_always_runs(self):
        self.assertTrue(refresh_due(self.audit, 'workflow_dispatch', self.now))

    def test_stale_audit_runs(self):
        self.audit['completed_at'] = '2026-11-08T23:59:59Z'
        self.assertTrue(refresh_due(self.audit, 'schedule', self.now))

    def test_invalid_or_unpublished_audit_runs(self):
        for field, value in [('completed_at', 'bad'), ('completed_at', '2026-11-09T07:00:00'),
                             ('completed_at', '2026-11-10T07:00:00Z'), ('workflow_run_id', None),
                             ('counts', {'total': 2}), ('results', [])]:
            with self.subTest(field=field, value=value):
                audit = copy.deepcopy(self.audit)
                audit[field] = value
                self.assertTrue(refresh_due(audit, 'schedule', self.now))
        self.assertTrue(refresh_due({}, 'schedule', self.now))

    def test_workflow_gates_network_and_publication(self):
        workflow = (Path(__file__).resolve().parents[1] / '.github/workflows/daily-scope-refresh.yml').read_text()
        self.assertIn("cron: '23 6,10,14 * * *'", workflow)
        self.assertIn('cancel-in-progress: false', workflow)
        for step in ('Report new-program discovery coverage', 'Refresh supported public scope tables',
                     'Record workflow identity', 'Regenerate and validate',
                     'Publish validated snapshots and audit', 'Surface incomplete supported coverage'):
            self.assertIn(f"- name: {step}\n        if: steps.freshness.outputs.due == 'true'", workflow)
        self.assertIn("subprocess.check_output(['git', 'rev-parse', 'HEAD']", workflow)

    def test_timezone_is_compared_in_utc(self):
        self.audit['completed_at'] = '2026-11-08T23:30:00-08:00'
        self.assertFalse(refresh_due(self.audit, 'schedule', self.now))


if __name__ == '__main__':
    unittest.main()
