#!/usr/bin/env python3
"""Package only this workflow run's completed audits, with explicit provenance.

This is an offline evidence writer, not a collector. Prior checked-in audits are
identified by hash in the manifest, never relabeled or copied as current output.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess

from scope_refresh_due import validate_audit

ROOT = Path(__file__).resolve().parents[1]
AUDITS = {'data/scope-refresh-status.json': 'collector',
          'data/program-discovery-status.json': 'discovery'}
MANIFEST = 'run-manifest.json'


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00', 'Z')


def timestamp(value):
    parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('missing timezone')
    return parsed.astimezone(dt.timezone.utc)


def digest(path):
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def write_manifest(directory, manifest):
    directory.mkdir(parents=True, exist_ok=True)
    (directory / MANIFEST).write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')


def start(root, directory, identity, baseline_commit, started_at=None):
    # A rerun has its own directory; refuse to reuse an existing evidence packet.
    directory.mkdir(parents=True, exist_ok=False)
    manifest = {'schema_version': '1.0.0', **identity, 'baseline_commit': baseline_commit,
                'started_at': started_at or now(), 'evidence_status': 'started',
                'baseline_audits': {name: digest(root / name) for name in AUDITS},
                'notice': 'Run evidence is not proof of publication or complete coverage.'}
    write_manifest(directory, manifest)
    return manifest


def finish(root, directory, identity, outcomes, recorded_at=None):
    recorded_at = recorded_at or now()
    # A failed/repeated packaging invocation must not retain earlier copies.
    for name in AUDITS:
        (directory / name).unlink(missing_ok=True)
    try:
        manifest = json.loads((directory / MANIFEST).read_text(encoding='utf-8'))
        if (not isinstance(manifest, dict) or manifest.get('evidence_status') != 'started'
                or any(manifest.get(key) != value for key, value in identity.items())
                or not isinstance(manifest.get('baseline_audits'), dict)):
            raise ValueError('invalid run start')
        started = timestamp(manifest['started_at'])
        finished = timestamp(recorded_at)
        if started > finished:
            raise ValueError('invalid run times')
    except (OSError, ValueError, KeyError, TypeError, AttributeError, OverflowError):
        # Still give a current identity and step outcomes if initialization failed.
        # No audit can be attributed safely without the matching start manifest.
        manifest = {'schema_version': '1.0.0', **identity,
                    'evidence_status': 'initialization_missing_or_invalid',
                    'recorded_at': recorded_at, 'step_outcomes': outcomes, 'audits': {},
                    'notice': 'No audit files included: a matching run-start manifest was unavailable.'}
        write_manifest(directory, manifest)
        return manifest

    manifest.update(evidence_status='finished', recorded_at=recorded_at,
                    step_outcomes=outcomes, audits={})
    for name, producer in AUDITS.items():
        path = root / name
        entry = {'producer_step': producer, 'producer_outcome': outcomes.get(producer, 'unknown'),
                 'sha256': digest(path), 'included': False}
        manifest['audits'][name] = entry
        if entry['sha256'] is None:
            entry['attribution'] = 'missing_or_unreadable'
            continue
        if entry['sha256'] == manifest['baseline_audits'].get(name):
            entry['attribution'] = 'unchanged_from_checkout'
            continue
        entry['attribution'] = 'modified_but_not_verified_as_current'
        if entry['producer_outcome'] != 'success':
            continue
        try:
            raw = path.read_bytes()
            audit = json.loads(raw)
            if name == 'data/scope-refresh-status.json':
                validate_audit(audit)
            completed = timestamp(audit['completed_at'])
            if not started <= completed <= finished:
                continue
            if any(key in audit and str(audit[key]) != value for key, value in identity.items()):
                continue
        except (OSError, ValueError, KeyError, TypeError, AttributeError, OverflowError):
            continue
        destination = directory / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)
        entry.update(attribution='produced_this_run', included=True,
                     completed_at=audit['completed_at'],
                     sha256=hashlib.sha256(raw).hexdigest())
    write_manifest(directory, manifest)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--start', action='store_true')
    mode.add_argument('--finish', action='store_true')
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--step', action='append', default=[], metavar='NAME=OUTCOME')
    args = parser.parse_args()
    identity = {'workflow_run_id': os.environ['GITHUB_RUN_ID'],
                'workflow_run_attempt': os.environ['GITHUB_RUN_ATTEMPT']}
    if args.start:
        baseline = subprocess.check_output(['git', '-C', str(args.root), 'rev-parse', 'HEAD'],
                                           text=True).strip()
        start(args.root, args.directory, identity, baseline)
    else:
        finish(args.root, args.directory, identity, dict(step.split('=', 1) for step in args.step))


if __name__ == '__main__':
    main()
