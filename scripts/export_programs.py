#!/usr/bin/env python3
"""Validate and export public program-policy summaries offline, never target scopes."""
import argparse
import datetime as dt
import json
from validate import ROOT, Invalid, check_schema, normalize_url
from build_navigation import text, link


def validate_program(rec, schema):
    check_schema(rec, schema, schema)
    sources = {s['id']: s for s in rec['sources']}
    if len(sources) != len(rec['sources']): raise Invalid('duplicate program source ID')
    for field in ('rewards', 'eligibility', 'restrictions', 'submission_status'):
        if not set(rec[field]['source_ids']) <= set(sources): raise Invalid('unknown program claim source')
    if rec['submission_status']['value'] == 'closed' and rec['schema_version'] != '1.2.0':
        raise Invalid('closed status requires program record version 1.2.0')
    if rec['submission_status']['value'] != 'unknown' and not rec['submission_status']['source_ids']:
        raise Invalid('known submission status requires evidence')
    aliases=set()
    for alias in rec.get('official_program_links',[]):
        if not set(alias['source_ids']) <= set(sources): raise Invalid('unknown official program link source')
        normalized=normalize_url(alias['url'])
        if normalized in aliases: raise Invalid('duplicate official program link')
        aliases.add(normalized)
    urls = {normalize_url(s['url']) for s in sources.values()}
    required = [rec['program_url'], rec['policy_url'], *rec['announcement_urls']]
    if rec['change_log_url']: required.append(rec['change_log_url'])
    if not {normalize_url(u) for u in required} <= urls: raise Invalid('program link lacks reviewed source')
    reviewed = dt.datetime.fromisoformat(rec['last_verified_at'].replace('Z', '+00:00'))
    for s in sources.values():
        if dt.datetime.fromisoformat(s['retrieved_at'].replace('Z', '+00:00')) > reviewed:
            raise Invalid('source retrieval is after program verification')
    reward = rec['rewards']
    if reward['minimum'] is not None and reward['maximum'] is not None and reward['minimum'] > reward['maximum']:
        raise Invalid('reversed reward bounds')
    if (reward['minimum'] is not None or reward['maximum'] is not None) and reward['currency'] is None:
        raise Invalid('numeric rewards require verified currency')


def build(root=ROOT):
    schema = json.loads((root/'schema/program.schema.json').read_text())
    programs = []; identities = set(); urls = set()
    for path in sorted((root/'data/programs').glob('*.json')):
        rec = json.loads(path.read_text()); validate_program(rec, schema)
        url = normalize_url(rec['program_url'])
        if path.stem != rec['id'] or rec['id'] in identities or url in urls: raise Invalid('duplicate or mismatched program identity')
        identities.add(rec['id']); urls.add(url); programs.append(rec)
    export = {'schema_version':'1.2.0', 'content_scope':'public_program_policy_summary', 'counts':{'programs':len(programs)},
              'notice':'Advertised rewards are not report awards. This directory grants no authorization and omits asset inventories. Read the live official policy before any activity.',
              'rights':'Original summaries CC BY 4.0; linked sources and trademarks retain their own rights.', 'programs':programs}
    lines = ['# Public program directory', '', '[Library home](../README.md) · [Read reports](reports.md) · [Diagram gallery](diagram-gallery.md)', '',
             export['notice'], '', 'This is a small, manually reviewed starting directory, not a complete or continuously verified listing. Program metadata is separate from the USD 10,000 report inclusion threshold. Null values mean unverified or not established, not zero. Summaries are not legal advice or a substitute for the full terms.', '']
    for p in programs:
        lines += ['## '+text(p['name']), '', link('Official program',p['program_url'])+' · '+link('Policy',p['policy_url'])+' · '+link('Canonical record','../data/programs/'+p['id']+'.json'), '',
                  '**Platform:** '+text(p['platform'])+'  ', '**Last verified:** '+text(p['last_verified_at']), '',
                  '**Submission status:** '+text(p['submission_status']['value'].replace('_', ' '))+'. '+text(p['submission_status']['summary']), '',
                  '**Advertised rewards:** '+text(p['rewards']['summary']), '', '**Eligibility:** '+text(p['eligibility']['summary']), '',
                  '**Restrictions and exclusions:** '+text(p['restrictions']['summary']), '', '**Verification limits**', '']
        lines += ['- '+text(x) for x in p['limitations']]
        for alias in p.get('official_program_links',[]):
            lines += ['', link('Official linked program',alias['url'])+' — '+text(alias['note'])]
        lines += ['', '**Official evidence and updates**', '']
        lines += ['- '+link(s['title'],s['url'])+' — '+text(s['publisher'])+'; retrieved '+text(s['retrieved_at'])+'.' for s in p['sources']]
        lines += ['', 'Change-log link: '+(link('Official updates',p['change_log_url']) if p['change_log_url'] else 'No dedicated change-log URL verified; consult the current policy and linked announcements')+'.', '']
    lines += ['Original summaries: Security Research Library contributors, CC BY 4.0. Linked policies retain their own rights. [License scope](../LICENSE.md).', '']
    return {'exports/programs.json':json.dumps(export,indent=2,ensure_ascii=False)+'\n', 'docs/programs.md':'\n'.join(lines)}


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--check',action='store_true'); args=parser.parse_args()
    for name,content in build().items():
        path=ROOT/name
        if args.check:
            if not path.is_file() or path.read_text()!=content: raise SystemExit('Missing or stale program export: '+name)
        else: path.write_text(content)
    print('Program schema, evidence references and deterministic outputs validated (offline).')

if __name__=='__main__': main()
