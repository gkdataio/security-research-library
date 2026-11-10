#!/usr/bin/env python3
"""Avoid repeat live collection when a completed daily audit is already published.

This reads the checked-out main branch only. A partial published refresh counts
as an attempt, not complete coverage: backup triggers must not retry access gaps.
Manual dispatch always requests a fresh authorized attempt.
"""
import argparse
import datetime as dt
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUSES = ('refreshed', 'failed', 'deferred', 'unsupported')


def consistent_counts(results, counts):
    """Only a complete, internally consistent result list can suppress a run."""
    if not isinstance(results, list) or not results or not isinstance(counts, dict):
        return False
    expected = dict.fromkeys(STATUSES, 0)
    expected.update(total=len(results), attempted=0)
    for result in results:
        if not isinstance(result, dict) or result.get('status') not in STATUSES:
            return False
        expected[result['status']] += 1
        expected['attempted'] += 'attempted_at' in result
    return all(type(counts.get(key)) is int and counts[key] == value
               for key, value in expected.items())


def validate_audit(audit):
    if not isinstance(audit, dict) or not consistent_counts(audit.get('results'), audit.get('counts')):
        raise ValueError('scope refresh audit counts must exactly match recognized result rows and attempts')
    started = audit_timestamp(audit.get('started_at'))
    completed = audit_timestamp(audit.get('completed_at'))
    if started > completed:
        raise ValueError('scope refresh audit completion precedes its start')
    for field in ('workflow_run_id', 'workflow_run_attempt'):
        if field in audit and not valid_workflow_id(audit[field]):
            raise ValueError('scope refresh audit has an invalid ' + field)
    identities = set()
    for result in audit['results']:
        identity = result.get('program_url')
        if not isinstance(identity, str) or not identity.strip() or identity != identity.strip():
            raise ValueError('scope refresh audit requires nonempty program identities')
        if identity in identities:
            raise ValueError('scope refresh audit contains a duplicate program identity')
        identities.add(identity)
        attempted = result['status'] in ('refreshed', 'failed')
        if ('attempted_at' in result) != attempted:
            raise ValueError('scope refresh audit attempted timestamps do not match result statuses')
        if attempted and not started <= audit_timestamp(result['attempted_at']) <= completed:
            raise ValueError('scope refresh audit attempt is outside its run window')
    return audit['counts']


def audit_timestamp(value):
    try:
        if not isinstance(value, str):
            raise ValueError
        parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
        if parsed.tzinfo is None:
            raise ValueError
        return parsed.astimezone(dt.timezone.utc)
    except (ValueError, OverflowError):
        raise ValueError('scope refresh audit requires timezone-aware ISO timestamps') from None


def valid_workflow_id(value):
    return ((type(value) is int and value > 0) or
            (isinstance(value, str) and value.isascii() and value.isdecimal() and bool(value.strip('0'))))


def refresh_due(audit, event, now):
    if event != 'schedule':
        return True
    try:
        completed = audit_timestamp(audit['completed_at'])
        if completed > now:
            return True
        if not all(valid_workflow_id(audit.get(field)) for field in ('workflow_run_id', 'workflow_run_attempt')):
            return True
        validate_audit(audit)
        return completed.astimezone(dt.timezone.utc).date() != now.astimezone(dt.timezone.utc).date()
    except (KeyError, TypeError, ValueError, AttributeError, OverflowError):
        return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--validate-audit', type=Path,
                        help='Validate a newly produced audit offline; do not evaluate scheduling')
    args = parser.parse_args()
    if args.validate_audit:
        try:
            validate_audit(json.loads(args.validate_audit.read_text(encoding='utf-8')))
        except (OSError, ValueError) as error:
            raise SystemExit('Invalid scope refresh audit: ' + str(error)) from None
        print('Scope refresh audit counts match every result and attempted row.')
        return
    try:
        audit = json.loads((ROOT / 'data/scope-refresh-status.json').read_text())
    except (OSError, ValueError):
        audit = {}
    due = refresh_due(audit, os.environ.get('GITHUB_EVENT_NAME'), dt.datetime.now(dt.timezone.utc))
    message = ('No published attempt today; refresh is due.' if due else
               'A completed attempt is already published today; skipping duplicate collection. '
               'This does not mean complete scope or discovery coverage. Inspect the published audit.')
    print(message)
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        output.write(f'due={str(due).lower()}\n')
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
            summary.write(message + '\n')


if __name__ == '__main__':
    main()
