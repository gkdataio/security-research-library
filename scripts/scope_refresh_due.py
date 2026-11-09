#!/usr/bin/env python3
"""Avoid repeat live collection when a completed daily audit is already published.

This reads the checked-out main branch only. A partial published refresh counts
as an attempt, not complete coverage: backup triggers must not retry access gaps.
Manual dispatch always requests a fresh authorized attempt.
"""
import datetime as dt
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def refresh_due(audit, event, now):
    if event != 'schedule':
        return True
    try:
        completed = dt.datetime.fromisoformat(audit['completed_at'].replace('Z', '+00:00'))
        if completed.tzinfo is None or completed > now:
            return True
        if not str(audit.get('workflow_run_id', '')).isdigit():
            return True
        results, counts = audit['results'], audit['counts']
        if not isinstance(results, list) or counts['total'] != len(results) or not results:
            return True
        return completed.astimezone(dt.timezone.utc).date() != now.astimezone(dt.timezone.utc).date()
    except (KeyError, TypeError, ValueError, AttributeError):
        return True


def main():
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
