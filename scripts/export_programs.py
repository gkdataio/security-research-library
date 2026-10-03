#!/usr/bin/env python3
"""Validate and export public program-policy summaries offline, never target scopes."""
import argparse
import datetime as dt
import json
from urllib.parse import urlsplit
from validate import ROOT, Invalid, check_schema, normalize_url
from build_navigation import text, link


def scope_url_matches_source(url, source_url):
    """Match reviewed pages exactly; never manufacture a section anchor.

    A normalized spelling of a section URL is allowed only when its exact,
    nonempty fragment was recorded in the cited source URL. Query strings
    remain significant; ordinary program URL normalization alone is unsafe
    here because it discards fragments.
    """
    if url == source_url:
        return True
    fragment = urlsplit(url).fragment
    return bool(fragment and fragment == urlsplit(source_url).fragment
                and normalize_url(url) == normalize_url(source_url))


def validate_program(rec, schema):
    check_schema(rec, schema, schema)
    sources = {s['id']: s for s in rec['sources']}
    if len(sources) != len(rec['sources']): raise Invalid('duplicate program source ID')
    for field in ('rewards', 'eligibility', 'restrictions', 'submission_status'):
        if not set(rec[field]['source_ids']) <= set(sources): raise Invalid('unknown program claim source')
    program_type = rec.get('program_type')
    if program_type is not None:
        if rec['schema_version'] not in ('1.3.0', '1.4.0'):
            raise Invalid('program type requires program record version 1.3.0 or 1.4.0')
        if not set(program_type['source_ids']) <= set(sources): raise Invalid('unknown program type source')
        if program_type['value'] != 'unknown' and not program_type['source_ids']:
            raise Invalid('known program type requires evidence')
    if rec['submission_status']['value'] == 'closed' and rec['schema_version'] not in ('1.2.0','1.3.0','1.4.0'):
        raise Invalid('closed status requires program record version 1.2.0, 1.3.0 or 1.4.0')
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
    scope = rec.get('scope_context')
    if scope is not None:
        if rec['schema_version'] != '1.4.0':
            raise Invalid('scope context requires program record version 1.4.0')
        if not set(scope['source_ids']) <= set(sources):
            raise Invalid('unknown scope context source')
        scope_sources = [sources[source_id] for source_id in scope['source_ids']]
        scope_reviewed = dt.datetime.fromisoformat(scope['verified_at'].replace('Z', '+00:00'))
        if scope_reviewed > reviewed:
            raise Invalid('scope verification is after program verification')
        for source in scope_sources:
            if dt.datetime.fromisoformat(source['retrieved_at'].replace('Z', '+00:00')) > scope_reviewed:
                raise Invalid('source retrieval is after scope verification')
        scope_urls = set()
        for url in scope['policy_urls']:
            if any(char.isspace() for char in url):
                raise Invalid('scope policy URL contains whitespace')
            identity = (normalize_url(url), urlsplit(url).fragment)
            if identity in scope_urls:
                raise Invalid('duplicate scope policy URL')
            scope_urls.add(identity)
            if not any(scope_url_matches_source(url, source['url']) for source in scope_sources):
                raise Invalid('scope policy URL lacks a linked reviewed source or recorded fragment')
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
    scope_count = sum('scope_context' in p for p in programs)
    export = {'schema_version':'1.4.0', 'content_scope':'public_program_policy_summary',
              'counts':{'programs':len(programs), 'programs_with_scope_context':scope_count,
                        'programs_without_scope_context':len(programs)-scope_count},
              'notice':'Advertised rewards are not report awards. This directory grants no authorization and omits asset inventories. Read the live official policy before any activity.',
              'rights':'Original summaries CC BY 4.0; linked sources and trademarks retain their own rights.', 'programs':programs}
    lines = ['# Public program directory', '', '[Library home](../README.md) · [Read reports](reports.md) · [Diagram gallery](diagram-gallery.md)', '',
             export['notice'], '', 'This is a small, manually reviewed starting directory, not a complete or continuously verified listing. Program metadata is separate from the USD 10,000 report inclusion threshold. Null values mean unverified or not established, not zero. Summaries are not legal advice or a substitute for the full terms.', '',
             f'**Scope-context coverage:** {scope_count} of {len(programs)} records have separately reviewed high-level coverage and exclusion summaries. Missing context means not separately summarized, not unrestricted scope or an absence of exclusions. Even reviewed summaries can be incomplete or become outdated; the live official policy controls.', '']
    for p in programs:
        program_type = p.get('program_type', {'value':'unknown', 'summary':'Program type was not separately classified in this record.'})
        lines += ['## '+text(p['name']), '', link('Official program',p['program_url'])+' · '+link('Policy',p['policy_url'])+' · '+link('Canonical record','../data/programs/'+p['id']+'.json'), '',
                  '**Platform:** '+text(p['platform'])+'  ', '**Last verified:** '+text(p['last_verified_at']), '',
                  '**Program type:** '+text(program_type['value'].replace('_', ' '))+'. '+text(program_type['summary']), '',
                  '**Submission status:** '+text(p['submission_status']['value'].replace('_', ' '))+'. '+text(p['submission_status']['summary']), '',
                  '**Advertised rewards:** '+text(p['rewards']['summary']), '', '**Eligibility:** '+text(p['eligibility']['summary']), '',
                  '**Restrictions and exclusions:** '+text(p['restrictions']['summary']), '']
        scope = p.get('scope_context')
        if scope is not None:
            lines += ['**Scope context**', '', '**Included coverage:** '+text(scope['included_summary']), '',
                      '**Excluded coverage:** '+text(scope['excluded_summary']), '',
                      '**Scope verified:** '+text(scope['verified_at']), '',
                      'High-level context only; not an asset inventory, a completeness guarantee or authorization to test.', '',
                      '**Reviewed policy links**', '']
            lines += ['- '+link('Official policy '+str(index), url) for index, url in enumerate(scope['policy_urls'], 1)]
            by_id = {s['id']: s for s in p['sources']}
            lines += ['', '**Scope evidence:** '+', '.join(link(by_id[source_id]['title'], by_id[source_id]['url']) for source_id in scope['source_ids']), '']
        lines += ['**Verification limits**', '']
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
