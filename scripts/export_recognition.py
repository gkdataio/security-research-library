#!/usr/bin/env python3
"""Validate and export first-party recognition references; local files only."""
import argparse
import datetime as dt
import html
import json
import re
from pathlib import Path
from urllib.parse import quote

from validate import ROOT, Invalid, check_schema, normalize_url


def timestamp(value):
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00'))


def validate_record(record, schema):
    check_schema(record, schema, schema)
    sources = {source['id']: source for source in record['sources']}
    if len(sources) != len(record['sources']):
        raise Invalid('duplicate recognition source ID')
    for field in ('recognition', 'reporting', 'rewards'):
        evidence = record[field]
        if not set(evidence['source_ids']) <= sources.keys():
            raise Invalid('unknown recognition source reference')
        if 'url' in evidence and evidence['url'] not in {
                sources[ref]['url'] for ref in evidence['source_ids']}:
            raise Invalid('recognition/reporting URL missing from linked evidence')
    reviewed = timestamp(record['reviewed_at'])
    if any(timestamp(source['retrieved_at']) > reviewed for source in sources.values()):
        raise Invalid('source retrieval is after recognition review')


def load_records(root=ROOT):
    schema = json.loads((root / 'schema/recognition.schema.json').read_text())
    records, ids, urls, organizations = [], set(), set(), set()
    for path in sorted((root / 'data/recognition').glob('*.json')):
        record = json.loads(path.read_text())
        validate_record(record, schema)
        url = normalize_url(record['recognition']['url'])
        organization = ' '.join(record['organization'].split()).casefold()
        if path.stem != record['id'] or record['id'] in ids:
            raise Invalid('duplicate or mismatched recognition identity')
        if url in urls or organization in organizations:
            raise Invalid('duplicate recognition page or organization')
        ids.add(record['id'])
        urls.add(url)
        organizations.add(organization)
        records.append(record)
    if not records:
        raise Invalid('no recognition records')
    return sorted(records, key=lambda rec: (rec['organization'].casefold(), rec['id']))


def text(value):
    value = html.escape(str(value), quote=False).replace('\n', ' ')
    return re.sub(r'([\\`*_{}\[\]()#+.!|])', r'\\\1', value)


def link(label, url):
    return '[' + text(label) + '](<' + quote(str(url), safe='/:#?&=@!$\'()*+,;%-._~') + '>)'


def build_export(records):
    return {
        'schema_version': '1.0.0',
        'dataset': 'security-research-library-recognition',
        'as_of': max(timestamp(rec['reviewed_at']).astimezone(dt.timezone.utc)
                     for rec in records).date().isoformat(),
        'repository_url': 'https://github.com/gkdataio/security-research-library',
        'scope': 'First-party recognition pages and direct reporting guidance; separate from program-policy and award records.',
        'limitations': [
            'A small editorial selection, not a traffic ranking or exhaustive directory.',
            'Recognition does not imply a monetary bounty or testing authorization.',
            'Submission flows were not exercised; current official terms control.'
        ],
        'counts': {'organizations': len(records)},
        'records': records,
    }


def build_page(records):
    export = build_export(records)
    lines = [
        '# First-party recognition and direct disclosure', '',
        '[Library home](../README.md) · [Canonical records](../data/recognition/) · '
        '[JSON export](../exports/recognition.json) · [Evidence policy](../DATA_POLICY.md#first-party-recognition-and-direct-disclosure)', '',
        f"{len(records)} organizations; latest source review: {export['as_of']}.", '',
        'A small selection of prominent organizations with their own public recognition pages and official direct reporting guidance. '
        'This is not a measured traffic ranking, an exhaustive directory or a claim that every reporting option avoids external services. '
        'The linked route is the first-party route documented by the organization.', '',
        '**Recognition does not imply payment or permission to test.** '
        'Read the current official policy. No submission flows were exercised, researcher names copied, or target assets catalogued. '
        'These references are separate from reviewed program-policy records and award-backed reports.', '',
        '## Quick directory', '',
        '| Organization | Recognition | Reporting guidance | Reward distinction |',
        '|---|---|---|---|',
    ]
    labels = {'separate_bounty_policy': 'Separate bounty policy', 'no_bounty': 'Policy says no monetary rewards', 'unknown': 'Payment not established'}
    for rec in records:
        lines.append('| ' + link(rec['organization'], '#' + rec['id']) + ' | ' +
                     link('Official recognition page', rec['recognition']['url']) + ' | ' +
                     link(rec['reporting']['route'].replace('_', ' ').capitalize(), rec['reporting']['url']) + ' | ' +
                     labels[rec['rewards']['status']] + ' |')
    for rec in records:
        lines += ['', f'<a id="{rec["id"]}"></a>', '## ' + text(rec['organization']), '',
                  link('Canonical record', '../data/recognition/' + rec['id'] + '.json'), '']
        source_by_id = {source['id']: source for source in rec['sources']}
        for field in ('recognition', 'reporting', 'rewards'):
            evidence = rec[field]
            citations = ' · '.join(link(source_by_id[ref]['title'], source_by_id[ref]['url'])
                                   for ref in evidence['source_ids'])
            lines += ['**' + field.capitalize() + ':** ' + text(evidence['summary']) + ' ' + citations, '']
        lines += ['**Limits:**', *['- ' + text(note) for note in rec['limitations']], '',
                  '**Reviewed:** ' + text(rec['reviewed_at']) + '. Submission availability: not tested.', '',
                  '**Source provenance:**']
        for source in rec['sources']:
            lines.append('- ' + link(source['title'], source['url']) + ' — ' + text(source['publisher']) +
                         '; official primary source, text reviewed ' + text(source['retrieved_at']) + '.')
        lines += ['', text(rec['rights'])]
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        records = load_records(args.root)
        outputs = {
            'exports/recognition.json': json.dumps(build_export(records), ensure_ascii=False, indent=2) + '\n',
            'docs/direct-disclosure.md': build_page(records),
        }
        for path, content in outputs.items():
            target = args.root / path
            if args.check:
                if not target.is_file() or target.read_text() != content:
                    raise Invalid(f'{path} missing or stale')
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content)
    except (Invalid, OSError, json.JSONDecodeError, KeyError, ValueError) as exc:
        parser.exit(1, f'Recognition validation/export failed: {exc}\n')
    print(f'Validated {len(records)} recognition records; outputs ' +
          ('current and deterministic.' if args.check else 'regenerated (offline).'))


if __name__ == '__main__':
    main()
