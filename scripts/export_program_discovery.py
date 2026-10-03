#!/usr/bin/env python3
"""Validate and export observed official program listings. No network or target scope."""
import argparse
import datetime as dt
import json
import re
from collections import Counter, defaultdict
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from validate import ROOT, Invalid, check_schema
from build_navigation import link, text


def identity_url(url):
    parts=urlsplit(url)
    query=[(k,v) for k,v in parse_qsl(parts.query,keep_blank_values=True) if not (parts.hostname=='hackerone.com' and k=='type' and v=='team')]
    return urlunsplit((parts.scheme.lower(),parts.netloc.lower(),parts.path.rstrip('/'),urlencode(query),''))


def validate_batch(batch,schema):
    check_schema(batch,schema,schema)
    sources={s['id']:s for s in batch['sources']}
    if len(sources)!=len(batch['sources']):raise Invalid('duplicate discovery source')
    reviewed=dt.datetime.fromisoformat(batch['reviewed_at'].replace('Z','+00:00'))
    for s in sources.values():
        if dt.datetime.fromisoformat(s['observed_at'].replace('Z','+00:00'))>reviewed:raise Invalid('listing observed after review')
    allowed={'HackerOne':{'hackerone.com'},'Bugcrowd':{'bugcrowd.com','eu.bugcrowd.net','gov.bugcrowd.net'},'Intigriti':{'app.intigriti.com','www.intigriti.com'}}
    ids=set();urls=set()
    for entry in batch['entries']:
        if 'directory_card' in entry and batch['platform']!='Bugcrowd':raise Invalid('Bugcrowd directory card on another platform')
        if not set(entry['source_ids'])<=set(sources):raise Invalid('unknown listing source')
        url=identity_url(entry['program_url']);p=urlsplit(url)
        if p.hostname not in allowed[batch['platform']]:raise Invalid('program URL must use official platform host')
        if batch['platform']=='HackerOne' and not re.fullmatch(r'/[a-zA-Z0-9_-]+',p.path):raise Invalid('expected program page, not report or asset')
        if batch['platform']=='Bugcrowd' and not re.fullmatch(r'/(?:engagements/)?[a-zA-Z0-9_-]+',p.path):raise Invalid('expected engagement page')
        if batch['platform']=='Intigriti' and not p.path.startswith('/programs/'):raise Invalid('expected Intigriti program page')
        if entry['id'] in ids or url in urls:raise Invalid('duplicate listing identity in batch')
        ids.add(entry['id']);urls.add(url)


def build(root=ROOT):
    schema=json.loads((root/'schema/program-discovery.schema.json').read_text(encoding='utf-8'));batches=[]
    policy_records=[json.loads(p.read_text(encoding='utf-8')) for p in (root/'data/programs').glob('*.json')]
    policies={identity_url(r['program_url']):r['id'] for r in policy_records}
    policy_assets={r['id']:r.get('asset_scope') for r in policy_records}
    policy_types={r['id']:r.get('program_type',{}).get('value') for r in policy_records}
    capture_path=root/'data/public-bounty-scopes.json'
    captures={r['listing_id']:r for r in json.loads(capture_path.read_text(encoding='utf-8'))['captures']} if capture_path.is_file() else {}
    vdp_path=root/'data/bugcrowd-vdp-scopes.json'
    vdp_captures={r['listing_id']:r for r in json.loads(vdp_path.read_text(encoding='utf-8'))['captures']} if vdp_path.is_file() else {}
    if set(captures)&set(vdp_captures):raise Invalid('same listing captured in bounty and VDP data')
    for path in (root/'data/programs').glob('*.json'):
        record=json.loads(path.read_text(encoding='utf-8'))
        for alias in record.get('official_program_links',[]):
            key=identity_url(alias['url'])
            if key in policies and policies[key]!=record['id']:raise Invalid('conflicting verified program identity')
            policies[key]=record['id']
    entries={};names=defaultdict(set);global_ids={}
    for path in sorted((root/'data/program-discovery').glob('*.json')):
        batch=json.loads(path.read_text(encoding='utf-8'));validate_batch(batch,schema)
        if path.stem!=batch['id']:raise Invalid('discovery filename mismatch')
        batches.append(batch)
        for entry in batch['entries']:
            key=identity_url(entry['program_url'])
            if entry['id'] in global_ids and global_ids[entry['id']]!=key:raise Invalid('listing ID reused for different program URLs')
            global_ids[entry['id']]=key
            if key not in entries:
                policy_id=policies.get(key)
                asset_scope=policy_assets.get(policy_id)
                capture=captures.get(entry['id'])
                vdp_capture=vdp_captures.get(entry['id'])
                entries[key]={**entry,'platform':batch['platform'],'review_state':'directory_listing_only',
                              'verified_policy_id':policy_id,
                              'verified_asset_scope':({'verified_at':asset_scope['verified_at'],
                                                       'capture_status':asset_scope['capture_status'],
                                                       'in_scope_entries':len(asset_scope['in_scope']),
                                                       'out_of_scope_entries':len(asset_scope['out_of_scope'])}
                                                      if asset_scope else None),
                              'public_bounty_capture':({'status':capture['status'], 'captured_at':capture['captured_at'],
                                                        'in_scope_entries':sum(a['scope']=='in' for a in capture.get('assets',[])),
                                                        'out_of_scope_entries':sum(a['scope']=='out' for a in capture.get('assets',[]))}
                                                       if capture else None),
                              'public_vdp_capture':({'status':vdp_capture['status'], 'captured_at':vdp_capture['captured_at'],
                                                     'in_scope_entries':sum(a['scope']=='in' for a in vdp_capture.get('assets',[])),
                                                     'out_of_scope_entries':sum(a['scope']=='out' for a in vdp_capture.get('assets',[]))}
                                                    if vdp_capture else None),
                              'observations':[]}
            else:
                # Conflicting observations are retained, never silently overwritten.
                for field in ('program_type','submission_status'):
                    if entries[key][field]!=entry[field]:entries[key][field]='unknown'
            entries[key]['observations'].append({'batch_id':batch['id'],'source_ids':entry['source_ids'],'observed_at':batch['reviewed_at'],'program_type':entry['program_type'],'submission_status':entry['submission_status']})
            if 'directory_card' in entry:
                entries[key]['directory_card']=entry['directory_card']
                entries[key]['observations'][-1]['directory_card']=entry['directory_card']
            for field in ('name','evidence_note'):
                if entries[key][field]!=entry[field]:entries[key]['observations'][-1][field]=entry[field]
            names[re.sub(r'[^a-z0-9]','',entry['name'].lower())].add(key)
    records=sorted(entries.values(),key=lambda r:(r['platform'],r['name'].casefold(),r['program_url']))
    groups=[sorted(urls) for urls in names.values() if len(urls)>1]
    counts={'unique_program_page_listings':len(records),'already_has_verified_policy':sum(r['verified_policy_id'] is not None for r in records),
            'verified_with_asset_scope':sum(r['verified_asset_scope'] is not None for r in records),
            'public_scope_tables_captured':sum(any(r[field] is not None and r[field]['status']=='captured'
                                                   for field in ('public_bounty_capture','public_vdp_capture')) for r in records),
            'awaiting_policy_review':sum(r['verified_policy_id'] is None for r in records),'batches':len(batches)}
    counts['by_platform']={platform:sum(r['platform']==platform for r in records) for platform in sorted({r['platform'] for r in records})}
    counts['by_program_type']=dict(sorted(Counter(r['program_type'] for r in records).items()))
    counts['by_submission_status']=dict(sorted(Counter(r['submission_status'] for r in records).items()))
    counts['possible_identity_review_groups']=len(groups)
    export={'schema_version':'1.0.0','notice':'Directory observations alone are not verified policies or testing authorization. Linked scope-table captures have separate dates and do not establish complete rules, current submission availability or bounty eligibility. Counts identify distinct platform program pages, not deduplicated organizations.', 'counts':counts,'possible_identity_review_groups':groups,'deduplication':'Exact normalized program URLs deduplicate observations; HackerOne type=team is display-only. Similar names are review leads, not evidence that distinct programs should merge.','batches':[{k:v for k,v in b.items() if k!='entries'} for b in batches],'listings':records}
    lines=['# Official program discovery queue','','[Library home](../README.md) · [Verified policies and asset scope](programs.md) · [Public bounty scopes](public-bounties.md)','',export['notice'],'',f'**{counts["unique_program_page_listings"]} distinct program-page listings**; {counts["already_has_verified_policy"]} link to an existing verified policy record, {counts["verified_with_asset_scope"]} of those have reviewed asset-scope snapshots, {counts["public_scope_tables_captured"]} additional listings have published scope tables captured, and {counts["awaiting_policy_review"]} await full policy review. These counts must not be added to verified-policy counts without removing overlap.','','## Coverage and continuation','']
    for batch in batches:
        c=batch['coverage'];lines += ['### '+text(batch['platform']), '',text(c['filters']), '',text(c['pagination_note']), '', '**Next review:** '+text(c['continuation_note']), '']
        lines += ['- '+text(x) for x in c['limitations']]
        lines += ['- '+link(s['page_label'],s['url'])+'; observed '+text(s['observed_at'])+'.' for s in batch['sources']]
        lines += ['']
    lines+=['## Observed listings','','Browse the separate platform pages. Type and status reflect only directory evidence; unknown stays explicit.','']
    platform_pages={}
    for platform in sorted({r['platform'] for r in records}):
        subset=[r for r in records if r['platform']==platform]
        path='docs/program-discovery/'+platform.lower()+'.md'
        lines+=['- '+link(platform+' — '+str(len(subset))+' program-page listings','program-discovery/'+platform.lower()+'.md')]
        page=['# '+platform+' directory observations','','[Discovery overview](../program-discovery.md) · [Public bounty scopes](../public-bounties.md)'+(' · [All Bugcrowd public scopes](../bugcrowd-programs.md)' if platform=='Bugcrowd' else '')+' · [Verified policies](../programs.md) · [Library home](../../README.md)','',export['notice'],'']
        for r in subset:
            policy=(' · '+link('Verified policy and scope','../programs.md#program-'+r['verified_policy_id'])+
                    ' · '+link('JSON','../../data/programs/'+r['verified_policy_id']+'.json')+
                    (f' ({r["verified_asset_scope"]["in_scope_entries"]} in / {r["verified_asset_scope"]["out_of_scope_entries"]} out)' if r['verified_asset_scope'] else '')) if r['verified_policy_id'] else ''
            capture=captures.get(r['id'])
            policy_type=policy_types.get(r['verified_policy_id'])
            bounty=(policy_type!='vulnerability_disclosure' and
                    not (capture and capture['status']=='not_paid_bounty') and
                    (policy_type=='paid_bounty' or r['program_type']=='paid_bounty' or
                     capture is not None and capture.get('offers_bounties') is True or
                     platform=='Bugcrowd' and capture is not None and r['program_type']=='unknown'))
            bounty_link=(' · '+link('Bounty scope','../public-bounties/'+platform.lower()+'/'+r['id']+'.md')) if bounty else ''
            vdp_link=(' · '+link('VDP scope','../bugcrowd-programs/vdp/'+r['id']+'.md')) if platform=='Bugcrowd' and r['program_type']=='vulnerability_disclosure' else ''
            page+=['- '+link(r['name'],r['program_url'])+' — '+text(r['program_type'].replace('_',' '))+'; '+text(r['submission_status'].replace('_',' '))+policy+bounty_link+vdp_link+' — '+text(r['evidence_note'])]
        page+=['','[Machine-readable export](../../exports/program-discovery.json) · [License and source rights](../../LICENSE.md)','']
        platform_pages[path]='\n'.join(page)
    lines += ['', '## Identity and provenance', '',export['deduplication'],'','[Machine-readable export](../exports/program-discovery.json) preserves batches, observations and candidate identity groups. Official source material and trademarks retain their own rights; original commentary and arrangement use [CC BY 4.0](../LICENSE.md).','']
    return {'exports/program-discovery.json':json.dumps(export,indent=2,ensure_ascii=False)+'\n','docs/program-discovery.md':'\n'.join(lines),**platform_pages}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    for name,content in build().items():
        path=ROOT/name
        if args.check:
            if not path.is_file() or path.read_text(encoding='utf-8')!=content:raise SystemExit('Missing or stale discovery output: '+name)
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8')
    print('Official program listings, provenance, deduplication and deterministic outputs validated (offline).')

if __name__=='__main__':main()
