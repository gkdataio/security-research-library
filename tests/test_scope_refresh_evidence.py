"""Run evidence packaging is tested entirely with local synthetic audit files."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import scope_refresh_evidence as evidence

IDENTITY = {'workflow_run_id': '123', 'workflow_run_attempt': '2'}
START = '2026-11-10T14:00:00Z'
END = '2026-11-10T15:00:00Z'
CURRENT = '2026-11-10T14:30:00Z'


class RunEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        self.packet = Path(self.temp.name) / 'evidence'
        for name in evidence.AUDITS:
            self.write_audit(name, {'completed_at': '2026-11-09T14:00:00Z',
                                    'workflow_run_id': '100', 'workflow_run_attempt': '1'})
        self.original = {name: (self.root / name).read_bytes() for name in evidence.AUDITS}
        evidence.start(self.root, self.packet, IDENTITY, 'baseline-commit', START)

    def write_audit(self, name, audit):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(audit), encoding='utf-8')

    def finish(self, **outcomes):
        manifest = evidence.finish(self.root, self.packet, IDENTITY, outcomes, END)
        self.assertEqual(manifest, json.loads((self.packet / evidence.MANIFEST).read_text()))
        self.assertEqual(manifest['workflow_run_id'], '123')
        self.assertEqual(manifest['workflow_run_attempt'], '2')
        return manifest

    def test_early_test_failure_includes_manifest_but_no_prior_audits(self):
        manifest = self.finish(tests='failure', collector='skipped', discovery='skipped',
                               publication='skipped')
        self.assertEqual(manifest['baseline_commit'], 'baseline-commit')
        self.assertEqual(manifest['step_outcomes']['tests'], 'failure')
        for name in evidence.AUDITS:
            entry = manifest['audits'][name]
            self.assertEqual(entry['attribution'], 'unchanged_from_checkout')
            self.assertFalse(entry['included'])
            self.assertFalse((self.packet / name).exists())
            self.assertEqual((self.root / name).read_bytes(), self.original[name])

    def test_interrupted_collector_only_includes_current_discovery(self):
        discovery = 'data/program-discovery-status.json'
        self.write_audit(discovery, {'completed_at': CURRENT, 'status': 'incomplete'})
        manifest = self.finish(discovery='success', collector='failure', identity='skipped')
        self.assertEqual(manifest['audits'][discovery]['attribution'], 'produced_this_run')
        self.assertEqual((self.packet / discovery).read_bytes(), (self.root / discovery).read_bytes())
        self.assertFalse((self.packet / 'data/scope-refresh-status.json').exists())

    def test_current_audits_remain_evidence_if_validation_or_publication_fails(self):
        for name in evidence.AUDITS:
            self.write_audit(name, {'started_at': START, 'completed_at': CURRENT, **IDENTITY,
                                    'results': [{'program_url': 'https://example.invalid/one', 'status': 'deferred'}],
                                    'counts': {'total': 1, 'attempted': 0, 'refreshed': 0,
                                               'failed': 0, 'deferred': 1, 'unsupported': 0}})
        manifest = self.finish(discovery='success', collector='success', identity='success',
                               validation='failure', publication='skipped')
        for name in evidence.AUDITS:
            self.assertTrue(manifest['audits'][name]['included'])
            self.assertEqual(manifest['audits'][name]['sha256'], evidence.digest(self.packet / name))
        self.assertEqual(manifest['step_outcomes']['publication'], 'skipped')

    def test_current_scope_audit_with_inconsistent_counts_is_not_included(self):
        name = 'data/scope-refresh-status.json'
        self.write_audit(name, {'completed_at': CURRENT, **IDENTITY,
                                'results': [{'status': 'failed'}],
                                'counts': {'total': 1, 'attempted': 0, 'refreshed': 1,
                                           'failed': 0, 'deferred': 0, 'unsupported': 0}})
        manifest = self.finish(collector='success')
        self.assertFalse(manifest['audits'][name]['included'])
        self.assertFalse((self.packet / name).exists())

    def test_modified_file_from_failed_step_is_not_attributed_to_this_run(self):
        for name in evidence.AUDITS:
            self.write_audit(name, {'completed_at': CURRENT})
        manifest = self.finish(discovery='failure', collector='cancelled')
        for name in evidence.AUDITS:
            self.assertEqual(manifest['audits'][name]['attribution'], 'modified_but_not_verified_as_current')
            self.assertFalse((self.packet / name).exists())

    def test_modified_stale_foreign_or_invalid_audits_are_not_included(self):
        name = 'data/scope-refresh-status.json'
        for audit in ({'completed_at': '2026-11-09T14:00:00Z'},
                      {'completed_at': '2026-11-11T14:00:00Z'},
                      {'completed_at': '2026-11-10T14:30:00'},
                      {'completed_at': 42}, {}, [],
                      {'completed_at': CURRENT, 'workflow_run_id': '100'},
                      {'completed_at': CURRENT, **{**IDENTITY, 'workflow_run_attempt': '1'}}):
            with self.subTest(audit=audit):
                # Restore the start record between independent finish attempts.
                (self.packet / evidence.MANIFEST).write_text(json.dumps({
                    'evidence_status': 'started', **IDENTITY, 'started_at': START,
                    'baseline_audits': {}}))
                self.write_audit(name, audit)
                manifest = self.finish(collector='success')
                self.assertFalse(manifest['audits'][name]['included'])
                self.assertFalse((self.packet / name).exists())

    def test_missing_audit_is_explicit(self):
        name = 'data/scope-refresh-status.json'
        (self.root / name).unlink()
        manifest = self.finish(collector='failure')
        self.assertEqual(manifest['audits'][name]['attribution'], 'missing_or_unreadable')

    def test_missing_or_foreign_start_manifest_does_not_retain_old_artifact_files(self):
        for bad_start in (None, {}, {'evidence_status': 'started', **IDENTITY,
                                    'workflow_run_attempt': '1', 'baseline_audits': {}}):
            with self.subTest(bad_start=bad_start):
                path = self.packet / evidence.MANIFEST
                if bad_start is None:
                    path.unlink(missing_ok=True)
                else:
                    path.write_text(json.dumps(bad_start))
                for name in evidence.AUDITS:
                    target = self.packet / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text('old packet contents')
                manifest = self.finish(collector='success', discovery='success')
                self.assertEqual(manifest['evidence_status'], 'initialization_missing_or_invalid')
                self.assertEqual(manifest['audits'], {})
                self.assertFalse(any((self.packet / name).exists() for name in evidence.AUDITS))

    def test_start_refuses_an_existing_packet(self):
        with self.assertRaises(FileExistsError):
            evidence.start(self.root, self.packet, IDENTITY, 'baseline', START)

    def test_workflow_packages_only_run_directory_after_outcomes_are_known(self):
        workflow = (ROOT / '.github/workflows/daily-scope-refresh.yml').read_text()
        self.assertLess(workflow.index('- name: Start run evidence manifest'),
                        workflow.index('- name: Test collectors before network access'))
        self.assertLess(workflow.index('- name: Surface incomplete supported coverage'),
                        workflow.index('- name: Finish run evidence manifest'))
        self.assertLess(workflow.index('- name: Finish run evidence manifest'),
                        workflow.index('- name: Upload run evidence even on failure'))
        self.assertIn('--start --directory "$RUNNER_TEMP/$SCOPE_EVIDENCE_NAME"', workflow)
        self.assertIn('--finish --directory "$RUNNER_TEMP/$SCOPE_EVIDENCE_NAME"', workflow)
        upload = workflow.split('- name: Upload run evidence even on failure')[1]
        self.assertIn("if: always() && steps.freshness.outputs.due == 'true'", upload)
        self.assertIn('path: ${{ runner.temp }}/${{ env.SCOPE_EVIDENCE_NAME }}', upload)
        self.assertNotIn('data/scope-refresh-status.json', upload)
        self.assertIn('name: scope-refresh-${{ github.run_id }}-${{ github.run_attempt }}', upload)


if __name__ == '__main__':
    unittest.main()
