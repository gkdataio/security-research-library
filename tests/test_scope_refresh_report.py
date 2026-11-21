"""Reporting and its actual CI entry points use local synthetic evidence only."""
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import scope_refresh_evidence as evidence
import scope_refresh_report as report

IDENTITY = {'workflow_run_id': '123', 'workflow_run_attempt': '2'}
START = '2026-11-21T06:00:00Z'
COMPLETED = '2026-11-21T06:30:00Z'
END = '2026-11-21T07:00:00Z'
COMMAND = [sys.executable, str(ROOT / 'scripts/scope_refresh_report.py')]


def scope(rows):
    rows = copy.deepcopy(rows)
    counts = dict.fromkeys(('refreshed', 'failed', 'deferred', 'unsupported'), 0)
    counts.update(total=len(rows), attempted=0)
    for index, row in enumerate(rows):
        row.setdefault('program_url', f'https://example.invalid/program-{index}')
        row.setdefault('platform', 'Bugcrowd')
        counts[row['status']] += 1
        if row['status'] in ('refreshed', 'failed'):
            row['attempted_at'] = START
            counts['attempted'] += 1
    return {'started_at': START, 'completed_at': COMPLETED, **IDENTITY,
            'results': rows, 'counts': counts}


def discovery():
    return {'completed_at': COMPLETED, **IDENTITY, 'status': 'incomplete',
            'counts': {'platforms_completed': 0, 'new_programs': None, 'validated_candidates': 0},
            'platforms': [{'platform': platform, 'status': 'needs_browser', 'new_count': None,
                           'observed_count': None, 'candidates': []} for platform in report.PLATFORMS]}


def excluded():
    return {'status': 'deferred', 'reason_code': 'source_excluded', 'verification_status': 'unknown',
            'program_url': 'https://bugcrowd.com/engagements/fmshrc-vdp'}


class ScopeGateTests(unittest.TestCase):
    def gate_cli(self, audit):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'audit.json'
            path.write_text(json.dumps(audit))
            before = path.read_bytes()
            result = subprocess.run(COMMAND + ['--check-coverage', str(path)],
                                    capture_output=True, text=True, check=False)
            self.assertEqual(before, path.read_bytes())
            self.assertNotIn('Traceback', result.stderr)
            return result

    def test_exclusion_alone_passes_gate_but_remains_deferred_and_incomplete(self):
        audit = scope([excluded()])
        summary = report.scope_summary(audit)
        self.assertEqual(summary['gate'], 'passed')
        self.assertEqual(summary['status'], 'incomplete')
        self.assertEqual(summary['counts']['deferred'], 1)
        self.assertEqual(summary['explicit_exclusions'], 1)
        result = self.gate_cli(audit)
        self.assertEqual(result.returncode, 0)
        self.assertIn('::warning::Coverage remains incomplete', result.stdout)

    def test_known_review_failures_are_never_normalized(self):
        for reason in report.REVIEW_REASONS:
            with self.subTest(reason=reason):
                audit = scope([excluded(), {'status': 'failed', 'reason_code': reason}])
                result = self.gate_cli(audit)
                self.assertEqual(result.returncode, 1)
                self.assertEqual(report.scope_summary(audit)['blocking_failures'], 1)

    def test_unknown_http_and_internal_errors_remain_blocking(self):
        for fields in ({}, {'reason_code': 'internal_error'}, {'reason_code': []},
                       {'reason_code': 'http_error', 'http_status': 404},
                       {'reason_code': 'http_error', 'http_status': 503}):
            with self.subTest(fields=fields):
                self.assertEqual(self.gate_cli(scope([{'status': 'failed', **fields}])).returncode, 1)

    def test_unknown_and_mislabelled_deferrals_block_even_with_exclusions(self):
        for row in ({'status': 'deferred'},
                    {'status': 'deferred', 'reason_code': 'budget_exhausted'},
                    {'status': 'deferred', 'reason_code': 'source_excluded', 'verification_status': 'unknown'},
                    {**excluded(), 'verification_status': 'verified'},
                    {**excluded(), 'reason_code': 'other'}):
            with self.subTest(row=row):
                audit = scope([row])
                self.assertEqual(self.gate_cli(audit).returncode, 1)
        audit = scope([excluded(), {'status': 'deferred'}])
        self.assertEqual(report.scope_summary(audit)['blocking_deferrals'], 1)
        self.assertEqual(self.gate_cli(audit).returncode, 1)

    def test_unsupported_is_visible_not_verified(self):
        summary = report.scope_summary(scope([{'status': 'unsupported'}]))
        self.assertEqual(summary['gate'], 'passed')
        self.assertEqual(summary['status'], 'incomplete')
        self.assertEqual(summary['counts']['refreshed'], 0)

    def test_malformed_count_identity_or_timestamp_cannot_pass(self):
        original = scope([excluded()])
        bad = copy.deepcopy(original)
        bad['counts']['deferred'] = 0
        duplicate = scope([excluded(), excluded()])
        malformed = scope([{'status': 'failed'}])
        malformed['results'][0]['attempted_at'] = 'bad'
        for audit in (bad, duplicate, malformed, None, []):
            with self.subTest(audit=audit):
                self.assertEqual(self.gate_cli(audit).returncode, 1)


class OutcomeReportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        self.packet = Path(self.temp.name) / 'packet'
        self.summary = Path(self.temp.name) / 'github-summary.md'
        self.write(report.SCOPE, scope([{'status': 'refreshed'}]))
        self.write(report.DISCOVERY, discovery())
        evidence.start(self.root, self.packet, IDENTITY, 'a' * 40, START)
        # The changed timestamp distinguishes current output from checkout bytes.
        for name in evidence.AUDITS:
            audit = json.loads((self.root / name).read_text())
            audit['completed_at'] = '2026-11-21T06:40:00Z'
            self.write(name, audit)

    def write(self, name, audit):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(audit))

    def finish(self, **overrides):
        outcomes = dict.fromkeys((*report.STEPS, 'coverage'), 'success')
        outcomes.update(overrides)
        return evidence.finish(self.root, self.packet, IDENTITY, outcomes, END)

    def cli(self):
        before = {name: (self.root / name).read_bytes() for name in evidence.AUDITS}
        env = {**os.environ, 'GITHUB_RUN_ID': '123', 'GITHUB_RUN_ATTEMPT': '2',
               'GITHUB_STEP_SUMMARY': str(self.summary)}
        result = subprocess.run(COMMAND + ['--directory', str(self.packet)],
                                env=env, capture_output=True, text=True, check=False)
        self.assertNotIn('Traceback', result.stderr)
        for name, raw in before.items():
            self.assertEqual(raw, (self.root / name).read_bytes())
        self.assertEqual((self.packet / 'outcome.md').read_text(), self.summary.read_text())
        return result, json.loads((self.packet / 'outcome.json').read_text())

    def test_process_success_does_not_claim_discovery_or_overall_coverage(self):
        self.finish()
        result, output = self.cli()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(output['operational_status'], 'succeeded')
        self.assertEqual(output['discovery']['status'], 'incomplete')
        self.assertIsNone(output['discovery']['new_programs'])
        self.assertIn('unknown (not zero)', result.stdout)
        self.assertNotIn('Scope coverage: complete', result.stdout)

    def test_excluded_only_complete_pipeline_reports_incomplete_without_failure(self):
        self.write(report.SCOPE, scope([excluded()]))
        self.finish()
        result, output = self.cli()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(output['scope']['status'], 'incomplete')
        self.assertEqual(output['scope']['explicit_exclusions'], 1)

    def test_published_partial_is_not_reported_as_pipeline_failure(self):
        self.write(report.SCOPE, scope([{'status': 'refreshed'}, {'status': 'failed',
                                  'reason_code': 'redirect_requires_review'}]))
        self.finish(coverage='failure')
        result, output = self.cli()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(output['operational_status'], 'succeeded')
        self.assertEqual(output['steps']['publication'], 'success')
        self.assertEqual(output['scope']['gate'], 'blocked')
        self.assertIn('source_review', result.stdout)

    def test_coverage_step_cannot_silently_accept_a_failed_row(self):
        self.write(report.SCOPE, scope([{'status': 'failed'}]))
        self.finish(coverage='success')
        result, _ = self.cli()
        self.assertEqual(result.returncode, 1)

    def test_validation_and_publication_failure_are_never_called_success(self):
        for step in ('validation', 'publication'):
            with self.subTest(step=step):
                # Packaging is intentionally a one-shot operation.
                evidence.write_manifest(self.packet, {'evidence_status': 'started', **IDENTITY,
                    'started_at': START, 'baseline_audits': {}})
                self.finish(**{step: 'failure', 'coverage': 'skipped'})
                output = report.build_report(self.packet, IDENTITY)
                self.assertEqual(output['operational_status'], 'failed_or_incomplete')
                self.assertIsNotNone(output['scope'])
                self.assertEqual(output['evidence_errors'], [])

    def test_publication_failure_report_cli_does_not_create_another_red_step(self):
        self.finish(publication='failure', coverage='skipped')
        result, output = self.cli()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(output['steps']['publication'], 'failure')
        self.assertEqual(output['operational_status'], 'failed_or_incomplete')

    def test_early_failure_never_uses_checkout_audit(self):
        self.finish(tests='failure', discovery='skipped', collector='skipped',
                    identity='skipped', validation='skipped', publication='skipped', coverage='skipped')
        result, output = self.cli()
        self.assertEqual(result.returncode, 0)
        self.assertIsNone(output['scope'])
        self.assertIsNone(output['discovery'])
        self.assertEqual(output['steps']['tests'], 'failure')
        self.assertIn('Scope coverage: unknown', result.stdout)
        self.assertNotIn('total: 1', result.stdout)

    def test_current_discovery_survives_interrupted_collector(self):
        self.finish(collector='failure', identity='skipped', validation='skipped',
                    publication='skipped', coverage='skipped')
        _, output = self.cli()
        self.assertIsNone(output['scope'])
        self.assertIsNotNone(output['discovery'])

    def test_missing_bad_or_foreign_manifest_is_explicit(self):
        for manifest in (None, [], {}, {'step_outcomes': {}, **IDENTITY, 'workflow_run_attempt': '1'}):
            with self.subTest(manifest=manifest):
                path = self.packet / evidence.MANIFEST
                if manifest is None:
                    path.unlink(missing_ok=True)
                else:
                    path.write_text(json.dumps(manifest))
                output = report.build_report(self.packet, IDENTITY)
                self.assertIsNone(output['scope'])
                self.assertTrue(output['evidence_errors'])

    def test_tampered_artifact_hash_does_not_show_counts(self):
        self.finish()
        (self.packet / report.SCOPE).write_text('{}')
        result, output = self.cli()
        self.assertEqual(result.returncode, 1)
        self.assertIsNone(output['scope'])
        self.assertTrue(output['evidence_errors'])

    def test_even_matching_hash_cannot_admit_stale_foreign_or_invalid_counts(self):
        self.finish()
        path = self.packet / report.SCOPE
        original = json.loads(path.read_text())
        for mutation in ({'completed_at': '2026-11-20T06:30:00Z'}, {'workflow_run_id': '99'},
                         {'counts': {'total': 0}}):
            with self.subTest(mutation=mutation):
                raw = json.dumps({**original, **mutation}).encode()
                path.write_bytes(raw)
                manifest_path = self.packet / evidence.MANIFEST
                manifest = json.loads(manifest_path.read_text())
                manifest['audits'][report.SCOPE]['sha256'] = hashlib.sha256(raw).hexdigest()
                manifest['audits'][report.SCOPE]['completed_at'] = mutation.get('completed_at', original['completed_at'])
                manifest_path.write_text(json.dumps(manifest))
                self.assertIsNone(report.build_report(self.packet, IDENTITY)['scope'])

    def test_reason_and_platform_text_cannot_inject_summary_or_workflow_commands(self):
        self.write(report.SCOPE, scope([{'status': 'failed', 'reason': '\n::error::injected',
                         'reason_code': '<script>', 'platform': '\n::error::injected'}]))
        self.finish(coverage='failure')
        result, _ = self.cli()
        self.assertNotIn('injected', result.stdout)
        self.assertNotIn('<script>', result.stdout)

    def test_discovery_counts_must_preserve_unknowns(self):
        audit = discovery()
        audit['counts']['new_programs'] = 0
        with self.assertRaises(ValueError):
            report.discovery_summary(audit)
        audit = discovery()
        audit['platforms'][1]['platform'] = 'Bugcrowd'
        with self.assertRaises(ValueError):
            report.discovery_summary(audit)

    def test_complete_visible_discovery_is_not_called_universal_discovery(self):
        audit = discovery()
        for row in audit['platforms']:
            row.update(status='complete_visible_listing', new_count=0, observed_count=1)
        audit.update(status='complete_visible_listings')
        audit['counts'].update(platforms_completed=3, new_programs=0)
        self.assertEqual(report.discovery_summary(audit)['status'], 'complete_visible_listings')

    def test_workflow_preserves_gates_and_reports_even_after_failure_without_live_push(self):
        workflow = (ROOT / '.github/workflows/daily-scope-refresh.yml').read_text()
        self.assertNotIn('  push:', workflow)
        self.assertNotIn('continue-on-error', workflow)
        self.assertIn("cron: '23 6,10,14 * * *'", workflow)
        self.assertIn('  workflow_dispatch:', workflow)
        self.assertIn('permissions:\n  contents: write', workflow)
        self.assertIn('cancel-in-progress: false', workflow)
        summary = workflow.split('- name: Summarize collection, publication and coverage')[1]
        self.assertIn("if: always() && steps.freshness.outputs.due == 'true'", summary.split('- name:')[0])
        self.assertLess(workflow.index('- name: Finish run evidence manifest'),
                        workflow.index('- name: Summarize collection, publication and coverage'))
        self.assertLess(workflow.index('- name: Summarize collection, publication and coverage'),
                        workflow.index('- name: Upload run evidence'))
        self.assertIn('--step coverage=${{ steps.coverage.outcome }}', workflow)


if __name__ == '__main__':
    unittest.main()
