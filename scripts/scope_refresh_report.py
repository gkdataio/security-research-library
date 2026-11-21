#!/usr/bin/env python3
"""Offline CI outcome report. Never collect, alter audits, or infer fresh scope.

The coverage gate still blocks every failed row and every unrecognized deferral.
An enforced source exclusion is a coverage gap, not a failed collection attempt.
The summary reads only hash-verified current-run evidence, never checkout audits.
"""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path

from scope_refresh_due import audit_timestamp, valid_workflow_id, validate_audit
from source_access import excluded_source_reason

SCOPE = 'data/scope-refresh-status.json'
DISCOVERY = 'data/program-discovery-status.json'
STEPS = ('tests', 'discovery', 'collector', 'identity', 'validation', 'publication')
OUTCOMES = ('success', 'failure', 'cancelled', 'skipped', 'unknown')
PLATFORMS = ('Bugcrowd', 'HackerOne', 'Intigriti')
REVIEW_REASONS = {
    'redirect_requires_review': 'Redirect refused; source identity needs review',
    'bugcrowd_scope_redacted': 'Public scope redacted',
    'bugcrowd_scope_empty': 'Empty public scope table',
    'hackerone_scope_empty': 'Empty public scope table',
    'scope_removal_guard': 'Large removal blocked by safeguard',
}


def is_explicit_exclusion(row):
    # A reason label alone must not excuse a new or unknown deferral.
    return (row['status'] == 'deferred' and row.get('reason_code') == 'source_excluded'
            and row.get('verification_status') == 'unknown'
            and excluded_source_reason(row['program_url']) is not None)


def scope_summary(audit):
    counts = dict(validate_audit(audit))
    exclusions = sum(is_explicit_exclusion(row) for row in audit['results'])
    blocking_deferred = counts['deferred'] - exclusions
    groups = Counter()
    for row in audit['results']:
        if row['status'] == 'refreshed':
            continue
        platform = row.get('platform')
        platform = platform if platform in PLATFORMS else 'Other'
        code = row.get('reason_code')
        if row['status'] == 'unsupported':
            category, label = 'unsupported', 'No validated unattended coverage for this record'
        elif is_explicit_exclusion(row):
            category, label = 'excluded', 'Enforced source exclusion; no request made'
        elif row['status'] == 'deferred':
            category, label = 'collection_error', 'Unrecognized or operational deferral'
        elif isinstance(code, str) and code in REVIEW_REASONS:
            category, label = 'source_review', REVIEW_REASONS[code]
        elif code == 'http_error':
            category = 'source_error'
            status = row.get('http_status')
            label = f'HTTP {status}' if type(status) is int and 100 <= status <= 599 else 'HTTP error'
        else:
            category, label = 'collection_error', 'Unclassified collection or validation failure'
        groups[(category, platform, label)] += 1
    return {
        'completed_at': audit_timestamp(audit['completed_at']).isoformat(),
        'status': 'incomplete' if any(counts[key] for key in ('failed', 'deferred', 'unsupported'))
                  else 'recorded_scope_tables_refreshed',
        'counts': counts, 'explicit_exclusions': exclusions,
        'blocking_failures': counts['failed'], 'blocking_deferrals': blocking_deferred,
        'gate': 'blocked' if counts['failed'] or blocking_deferred else 'passed',
        'groups': [{'category': category, 'platform': platform, 'reason': label, 'count': count}
                   for (category, platform, label), count in sorted(groups.items())],
    }


def discovery_summary(audit):
    """Reconcile summary fields without claiming more than visible listings."""
    rows, counts = audit['platforms'], audit['counts']
    if (not isinstance(rows, list) or len(rows) != len(PLATFORMS)
            or {row['platform'] for row in rows} != set(PLATFORMS)):
        raise ValueError('invalid discovery platforms')
    completed = 0
    candidates = 0
    for row in rows:
        if row['status'] == 'complete_visible_listing':
            if (type(row['new_count']) is not int or row['new_count'] < 0
                    or type(row['observed_count']) is not int
                    or row['observed_count'] < row['new_count']
                    or not isinstance(row['candidates'], list)
                    or len(row['candidates']) != row['new_count']):
                raise ValueError('invalid discovery counts')
            completed += 1
            candidates += row['new_count']
        elif row['status'] in ('needs_browser', 'invalid_observation'):
            if row['new_count'] is not None or row['observed_count'] is not None or row['candidates'] != []:
                raise ValueError('unknown discovery must remain unknown')
        else:
            raise ValueError('unknown discovery status')
    complete = completed == len(PLATFORMS)
    expected_status = 'complete_visible_listings' if complete else 'incomplete'
    if (audit['status'] != expected_status
            or type(counts['platforms_completed']) is not int or counts['platforms_completed'] != completed
            or type(counts['validated_candidates']) is not int or counts['validated_candidates'] != candidates
            or (complete and (type(counts['new_programs']) is not int or counts['new_programs'] != candidates))
            or (not complete and counts['new_programs'] is not None)):
        raise ValueError('inconsistent discovery summary')
    return {'completed_at': audit_timestamp(audit['completed_at']).isoformat(),
            'status': expected_status, 'platforms_completed': completed,
            'platforms_total': len(PLATFORMS), 'new_programs': candidates if complete else None}


def current_audit(directory, manifest, name, producer, identity):
    entry = manifest['audits'][name]
    if (entry['included'] is not True or entry['attribution'] != 'produced_this_run'
            or entry['producer_step'] != producer or entry['producer_outcome'] != 'success'
            or manifest['step_outcomes'].get(producer) != 'success'):
        raise ValueError('no current audit')
    raw = (directory / name).read_bytes()
    if hashlib.sha256(raw).hexdigest() != entry['sha256']:
        raise ValueError('audit hash mismatch')
    audit = json.loads(raw)
    completed = audit_timestamp(audit['completed_at'])
    if (not audit_timestamp(manifest['started_at']) <= completed <= audit_timestamp(manifest['recorded_at'])
            or entry['completed_at'] != audit['completed_at']
            or any(key in audit and str(audit[key]) != value for key, value in identity.items())):
        raise ValueError('audit attribution mismatch')
    return audit


def build_report(directory, identity):
    safe_identity = {key: value if valid_workflow_id(value) else None for key, value in identity.items()}
    report = {'schema_version': '1.0.0', **safe_identity, 'operational_status': 'failed_or_incomplete',
              'steps': dict.fromkeys((*STEPS, 'coverage'), 'unknown'),
              'scope': None, 'discovery': None, 'evidence_errors': [],
              'notice': 'Process success is not complete coverage, policy verification, or testing authorization.'}
    try:
        manifest = json.loads((directory / 'run-manifest.json').read_text(encoding='utf-8'))
        if (not all(valid_workflow_id(value) for value in identity.values())
                or any(str(manifest.get(key)) != value for key, value in identity.items())
                or not isinstance(manifest.get('step_outcomes'), dict)):
            raise ValueError('invalid manifest identity or outcomes')
        report['steps'] = {step: manifest['step_outcomes'].get(step, 'unknown')
                           if manifest['step_outcomes'].get(step) in OUTCOMES else 'unknown'
                           for step in report['steps']}
        if (manifest.get('evidence_status') != 'finished'
                or any(outcome == 'unknown' for outcome in report['steps'].values())
                or audit_timestamp(manifest['started_at']) > audit_timestamp(manifest['recorded_at'])):
            raise ValueError('no completed evidence manifest')
    except (OSError, ValueError, TypeError, KeyError, AttributeError, OverflowError):
        report['evidence_errors'].append('Run evidence unavailable or invalid; no checkout audit used.')
        return report
    for key, name, producer, summarize in (
            ('scope', SCOPE, 'collector', scope_summary),
            ('discovery', DISCOVERY, 'discovery', discovery_summary)):
        try:
            report[key] = summarize(current_audit(directory, manifest, name, producer, identity))
        except (OSError, ValueError, TypeError, KeyError, AttributeError, OverflowError):
            # A failed/skipped producer is expected not to have a completed audit.
            # Report the known step failure without inventing a second failure.
            if report['steps'][producer] == 'success':
                report['evidence_errors'].append(f'Current {key} audit unavailable or invalid despite producer success; '
                                                 'no checkout audit used.')
    if all(report['steps'][step] == 'success' for step in STEPS) and not report['evidence_errors']:
        report['operational_status'] = 'succeeded'
    if (report['scope'] is not None and report['scope']['gate'] == 'blocked'
            and report['steps']['coverage'] == 'success'):
        report['evidence_errors'].append('Coverage gate reported success despite blocking records.')
    return report


def render(report):
    lines = ['# Public scope refresh outcome', '',
             f"Run: {report['workflow_run_id'] or 'unknown'}; attempt: {report['workflow_run_attempt'] or 'unknown'}.", '',
             f"Collection pipeline: **{report['operational_status']}**.", '',
             '| Step | Outcome |', '| --- | --- |']
    lines += [f'| {step} | {outcome} |' for step, outcome in report['steps'].items()]
    lines += ['', 'Process success does not mean all records were refreshed. Publication is a separate step;',
              'an artifact alone does not prove publication. Hard runner termination may prevent this report.', '']
    scope = report['scope']
    if scope is None:
        lines += ['## Scope coverage: unknown', '', 'No verified current-run scope audit is available.', '']
    else:
        counts = scope['counts']
        lines += [f"## Scope coverage: {scope['status']}", '',
                  f"Audit completed: {scope['completed_at']}.", '',
                  '; '.join(f'{key}: {counts[key]}' for key in
                            ('total', 'attempted', 'refreshed', 'failed', 'deferred', 'unsupported')) + '.', '',
                  f"Supported coverage gate: **{scope['gate']}**. "
                  f"Blocking failures: {scope['blocking_failures']}; "
                  f"blocking deferrals: {scope['blocking_deferrals']}; "
                  f"enforced exclusions: {scope['explicit_exclusions']}.", '',
                  '| Category | Platform | Reason | Records |', '| --- | --- | --- | ---: |']
        lines += [f"| {g['category']} | {g['platform']} | {g['reason']} | {g['count']} |" for g in scope['groups']]
        lines += ['', 'Source-review rows are protective refusals, not proof that records are current. '
                  'They remain failures. Unknown errors and unrecognized deferrals remain blocking. '
                  'Exclusions remain unverified and are never retried by this report.', '']
    discovery = report['discovery']
    if discovery is None:
        lines += ['## New-program discovery: unknown', '', 'No verified current-run discovery audit is available.', '']
    else:
        new = 'unknown (not zero)' if discovery['new_programs'] is None else str(discovery['new_programs'])
        lines += [f"## New-program discovery: {discovery['status']}", '',
                  f"Audit completed: {discovery['completed_at']}.", '',
                  f"Complete visible listings: {discovery['platforms_completed']}/{discovery['platforms_total']}; "
                  f"new programs absent from the historical baseline: {new}.", '',
                  'The workflow imports observations; it does not perform live directory discovery. '
                  'Complete visible listings do not mean complete platform coverage.', '']
    lines += ['## Next action', '',
              '- If tests, collection, validation, or publication failed, inspect that step before trusting updates.',
              '- Review source identity, redaction, empty tables, and removal safeguards separately. '
              'Do not bypass gates, follow alternate routes, or overwrite last-good records.',
              '- Discovery needs a separate authorized, complete observation pass. Missing observations remain unknown.',
              '- Read run-manifest.json and the attributed raw audits in this run artifact for exact evidence.', '']
    lines += ['- ' + error for error in report['evidence_errors']]
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check-coverage', type=Path, help='Offline gate for a newly generated scope audit')
    mode.add_argument('--directory', type=Path, help='Completed current-run evidence directory')
    args = parser.parse_args()
    if args.check_coverage:
        try:
            summary = scope_summary(json.loads(args.check_coverage.read_text(encoding='utf-8')))
        except (OSError, ValueError, TypeError, KeyError, AttributeError, OverflowError):
            print('::error::Scope audit invalid; coverage cannot be established.')
            return 1
        print(json.dumps(summary, indent=2))
        if summary['gate'] == 'blocked':
            print('::error::Supported coverage incomplete: failed records or operational deferrals remain. '
                  'This does not mean collection, validation, or publication failed; see the outcome summary.')
            return 1
        if summary['status'] == 'incomplete':
            print('::warning::Coverage remains incomplete; enforced exclusions and unsupported records are unverified.')
        return 0
    identity = {key: os.environ.get(env, '') for key, env in
                (('workflow_run_id', 'GITHUB_RUN_ID'), ('workflow_run_attempt', 'GITHUB_RUN_ATTEMPT'))}
    report = build_report(args.directory, identity)
    markdown = render(report)
    args.directory.mkdir(parents=True, exist_ok=True)
    (args.directory / 'outcome.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    (args.directory / 'outcome.md').write_text(markdown, encoding='utf-8')
    print(markdown)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with Path(os.environ['GITHUB_STEP_SUMMARY']).open('a', encoding='utf-8') as output:
            output.write(markdown)
    # This step reports existing failures; it must not create a redundant red
    # step for accurately reported partial coverage or failed prior operations.
    return int(bool(report['evidence_errors']))


if __name__ == '__main__':
    raise SystemExit(main())
