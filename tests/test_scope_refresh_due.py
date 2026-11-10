import copy
import datetime as dt
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from scope_refresh_due import refresh_due, validate_audit


class DailyRefreshDueTests(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime(2026, 11, 9, 14, 23, tzinfo=dt.timezone.utc)
        self.audit = {'started_at': '2026-11-09T07:00:00Z',
                      'completed_at': '2026-11-09T07:10:00Z',
                      'workflow_run_id': '123', 'workflow_run_attempt': '1',
                      'results': [{'program_url': 'https://example.invalid/one',
                                   'status': 'failed', 'attempted_at': '2026-11-09T07:00:00Z'}],
                      'counts': {'total': 1, 'attempted': 1, 'failed': 1, 'refreshed': 0,
                                 'deferred': 0, 'unsupported': 0}}

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

    def test_each_count_must_match_the_results_exactly(self):
        for key in self.audit['counts']:
            for value in (None, True, False, -1, 1.0, '1', 99):
                with self.subTest(key=key, value=value):
                    audit = copy.deepcopy(self.audit)
                    audit['counts'][key] = value
                    self.assertTrue(refresh_due(audit, 'schedule', self.now))
            audit = copy.deepcopy(self.audit)
            del audit['counts'][key]
            self.assertTrue(refresh_due(audit, 'schedule', self.now))

    def test_result_statuses_and_shapes_must_be_valid(self):
        for result in (None, [], 'failed', {}, {'status': 'unknown'}, {'status': []},
                       {'status': 'failed'}):
            with self.subTest(result=result):
                audit = copy.deepcopy(self.audit)
                audit['results'] = [result]
                self.assertTrue(refresh_due(audit, 'schedule', self.now))

    def test_mixed_completed_partial_attempt_is_not_retried(self):
        self.audit['results'] = [
            {'status': 'refreshed', 'attempted_at': '2026-11-09T07:00:00Z'},
            {'status': 'failed', 'attempted_at': '2026-11-09T07:01:00Z'},
            {'status': 'deferred'}, {'status': 'unsupported'}]
        self.audit['counts'] = {'total': 4, 'attempted': 2, 'refreshed': 1,
                                'failed': 1, 'deferred': 1, 'unsupported': 1}
        for index, result in enumerate(self.audit['results']):
            result['program_url'] = f'https://example.invalid/{index}'
        self.assertFalse(refresh_due(self.audit, 'schedule', self.now))

    def test_invalid_audit_container_runs(self):
        for audit in (None, [], 'audit', 12):
            self.assertTrue(refresh_due(audit, 'schedule', self.now))

    def test_new_audit_validation_rejects_inconsistency(self):
        self.assertEqual(validate_audit(self.audit), self.audit['counts'])
        self.audit['counts']['failed'] = 0
        with self.assertRaisesRegex(ValueError, 'counts must exactly match'):
            validate_audit(self.audit)

    def test_timestamps_must_be_aware_and_ordered(self):
        for value in (None, 42, '', 'bad', '2026-11-09T07:05:00',
                      '2026-11-09T06:59:00Z', '2026-11-09T07:11:00Z'):
            with self.subTest(value=value):
                audit = copy.deepcopy(self.audit)
                audit['results'][0]['attempted_at'] = value
                with self.assertRaises(ValueError):
                    validate_audit(audit)
                self.assertTrue(refresh_due(audit, 'schedule', self.now))
        for field, value in (('started_at', None), ('started_at', '2026-11-09T08:00:00Z'),
                             ('completed_at', '2026-11-09T07:00:00')):
            audit = copy.deepcopy(self.audit)
            audit[field] = value
            with self.assertRaises(ValueError):
                validate_audit(audit)

    def test_program_identities_must_be_nonempty_and_unique(self):
        for identity in (None, 42, '', ' ', ' https://example.invalid/one'):
            with self.subTest(identity=identity):
                audit = copy.deepcopy(self.audit)
                audit['results'][0]['program_url'] = identity
                with self.assertRaises(ValueError):
                    validate_audit(audit)
        self.audit['results'] *= 2
        self.audit['counts'].update(total=2, failed=2, attempted=2)
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            validate_audit(self.audit)

    def test_attempt_timestamp_must_match_status_semantics(self):
        for status in ('deferred', 'unsupported'):
            audit = copy.deepcopy(self.audit)
            audit['results'][0]['status'] = status
            audit['counts'].update(failed=0, **{status: 1})
            with self.assertRaisesRegex(ValueError, 'result statuses'):
                validate_audit(audit)
        for status in ('refreshed', 'failed'):
            audit = copy.deepcopy(self.audit)
            audit['results'][0]['status'] = status
            del audit['results'][0]['attempted_at']
            audit['counts'].update(failed=0, attempted=0)
            audit['counts'][status] = 1
            with self.assertRaisesRegex(ValueError, 'result statuses'):
                validate_audit(audit)

    def test_workflow_identity_requires_positive_integer_ids(self):
        for field in ('workflow_run_id', 'workflow_run_attempt'):
            for value in (None, 0, True, '0', '-1', '1.5', '\u0661', ''):
                with self.subTest(field=field, value=value):
                    audit = copy.deepcopy(self.audit)
                    audit[field] = value
                    with self.assertRaises(ValueError):
                        validate_audit(audit)
                    self.assertTrue(refresh_due(audit, 'schedule', self.now))

    def test_validation_cli_fails_before_workflow_can_publish(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'audit.json'
            command = [sys.executable, str(Path(__file__).resolve().parents[1] /
                                          'scripts/scope_refresh_due.py'), '--validate-audit', str(path)]
            for valid in (True, False):
                with self.subTest(valid=valid):
                    audit = copy.deepcopy(self.audit)
                    if not valid:
                        audit['counts']['failed'] = 0
                    path.write_text(json.dumps(audit))
                    result = subprocess.run(command, capture_output=True, text=True, check=False)
                    self.assertEqual(result.returncode == 0, valid)
                    self.assertNotIn('Traceback', result.stderr)

    def test_workflow_gates_network_and_publication(self):
        workflow = (Path(__file__).resolve().parents[1] / '.github/workflows/daily-scope-refresh.yml').read_text()
        self.assertIn("cron: '23 6,10,14 * * *'", workflow)
        self.assertIn('cancel-in-progress: false', workflow)
        for step in ('Report new-program discovery coverage', 'Refresh supported public scope tables',
                     'Record workflow identity', 'Regenerate and validate',
                     'Publish validated snapshots and audit', 'Surface incomplete supported coverage'):
            self.assertIn(f"- name: {step}\n        if: steps.freshness.outputs.due == 'true'", workflow)
        self.assertIn("subprocess.check_output(['git', 'rev-parse', 'HEAD']", workflow)
        check = 'python scripts/scope_refresh_due.py --validate-audit data/scope-refresh-status.json'
        validation = workflow.split('- name: Regenerate and validate')[1].split('- name:')[0]
        publication = workflow.split('- name: Publish validated snapshots and audit')[1].split('- name:')[0]
        coverage = workflow.split('- name: Surface incomplete supported coverage')[1].split('- name:')[0]
        self.assertLess(validation.index(check), validation.index('python scripts/export_programs.py'))
        self.assertLess(publication.index(check), publication.index('git add'))
        self.assertLess(publication.index(check), publication.index('git push'))
        self.assertIn('counts = validate_audit(audit)', coverage)

    def test_timezone_is_compared_in_utc(self):
        self.audit['started_at'] = '2026-11-08T23:00:00-08:00'
        self.audit['completed_at'] = '2026-11-08T23:30:00-08:00'
        self.assertFalse(refresh_due(self.audit, 'schedule', self.now))


if __name__ == '__main__':
    unittest.main()
