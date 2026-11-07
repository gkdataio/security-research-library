#!/usr/bin/env python3
"""Refresh supported public scope tables, never targets or complete policy reviews.

Bugcrowd brief JSON, HackerOne public CSV and Intigriti visible SSR tables are supported. An error,
empty table or unusually large removal retains the last-good snapshot. All
programs receive an explicit audit outcome, including unsupported platforms.
"""
import argparse
import copy
import csv
import io
import datetime as dt
import hashlib
import html
import json
from pathlib import Path
import re
import time
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
CAPTURES = ('data/public-bounty-scopes.json', 'data/bugcrowd-vdp-scopes.json')
AUDIT = 'data/scope-refresh-status.json'
MAX_BYTES = 8 * 1024 * 1024


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


def official_url(url):
    parts = urlsplit(url)
    if (parts.scheme == 'https' and parts.netloc == 'app.intigriti.com' and not parts.query
            and not parts.fragment and re.fullmatch(r'/programs/(?:[a-zA-Z0-9_-]|%20)+/(?:[a-zA-Z0-9_-]|%20)+/detail', parts.path)):
        return parts
    if (parts.scheme == 'https' and parts.netloc == 'hackerone.com' and not parts.query
            and not parts.fragment and re.fullmatch(r'/teams/[a-zA-Z0-9_-]+/assets/download_csv\.csv', parts.path)):
        return parts
    if (parts.scheme != 'https' or parts.netloc not in ('bugcrowd.com', 'www.bugcrowd.com')
            or parts.query or parts.fragment or not re.fullmatch(
                r'/engagements/[a-zA-Z0-9_-]+(?:/changelog/[a-zA-Z0-9_-]+\.json)?', parts.path)):
        raise ValueError('Not an exact approved public platform scope URL')
    return parts


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # A changed identity or access gate needs review, not automatic traversal.
        raise ValueError('Redirect requires manual review')


class PublicClient:
    def __init__(self, delay=2):
        self.delay = max(1, delay)
        self.last = 0
        self.opener = build_opener(NoRedirect())

    def get(self, url):
        official_url(url)
        time.sleep(max(0, self.delay - (time.monotonic() - self.last)))
        self.last = time.monotonic()
        request = Request(url, headers={'User-Agent': 'PublicScopeCatalogReview/1.0',
                                       'Accept': 'text/html,application/json'})
        with self.opener.open(request, timeout=35) as response:
            raw = response.read(MAX_BYTES + 1)
            if len(raw) > MAX_BYTES:
                raise ValueError('Response exceeds size limit')
            length = response.headers.get('Content-Length')
            if length is not None and len(raw) != int(length):
                raise ValueError('Incomplete HTTP response')
            return raw.decode('utf-8')


def parse_brief(program_url, page, body_get):
    """Only follow the exact current brief link emitted by this program page."""
    program = official_url(program_url)
    links = set(re.findall(r'"getBriefVersionDocument"\s*:\s*"([^"]+)"', html.unescape(page)))
    if len(links) != 1:
        raise ValueError('Missing or ambiguous current public brief')
    path = links.pop()
    if not re.fullmatch(re.escape(program.path) + r'/changelog/[a-zA-Z0-9_-]+', path):
        raise ValueError('Current brief does not belong to this exact program')
    source = 'https://bugcrowd.com' + path + '.json'
    raw = body_get(source)
    document = json.loads(raw)
    groups = document['data']['scope']
    if not isinstance(groups, list) or not groups:
        raise ValueError('Missing or empty scope groups require review')
    assets, seen, duplicates = [], set(), 0
    for group in groups:
        if (type(group.get('inScope')) is not bool or not isinstance(group.get('name'), str)
                or not isinstance(group.get('targets'), list)):
            raise ValueError('Scope group schema changed')
        for target in group['targets']:
            if (not isinstance(target.get('name'), str) or not target['name'].strip()
                    or not isinstance(target.get('category'), str) or not target['category'].strip()
                    or (target.get('uri') is not None and not isinstance(target['uri'], str))):
                raise ValueError('Scope target schema changed')
            asset = {'name': ' '.join(target['name'].split()), 'asset_type': target['category'],
                     'location': target.get('uri') or None, 'group': group['name'],
                     'scope': 'in' if group['inScope'] else 'out'}
            key = json.dumps(asset, sort_keys=True)
            if key in seen:
                duplicates += 1
            else:
                seen.add(key)
                assets.append(asset)
    if not assets:
        raise ValueError('Empty public table requires review; last-good scope retained')
    published = document.get('publishedAt')
    if published is not None and not isinstance(published, str):
        raise ValueError('Invalid publication timestamp')
    return {'assets': assets, 'source_url': source, 'captured_at': now(),
            'published_at': published, 'scope_groups': len(groups),
            'duplicate_source_rows': duplicates, 'published_asset_count': len(assets) + duplicates,
            'source_method': 'public_bugcrowd_scope_groups',
            'evidence_sha256': hashlib.sha256(raw.encode()).hexdigest()}


def parse_hackerone(program_url, body_get):
    program = urlsplit(program_url)
    if (program.scheme != 'https' or program.netloc not in ('hackerone.com', 'www.hackerone.com')
            or program.query not in ('', 'type=team') or program.fragment
            or not re.fullmatch(r'/[a-zA-Z0-9_-]+/?', program.path)):
        raise ValueError('Not an exact HackerOne program identity')
    source = 'https://hackerone.com/teams/' + program.path.strip('/') + '/assets/download_csv.csv'
    raw = body_get(source)
    if not raw.endswith('\n'):
        raise ValueError('CSV response lacks complete final line')
    reader = csv.DictReader(io.StringIO(raw), strict=True)
    required = {'identifier', 'asset_type', 'instruction', 'eligible_for_submission', 'eligible_for_bounty',
                'availability_requirement', 'confidentiality_requirement', 'integrity_requirement',
                'max_severity', 'system_tags', 'created_at', 'updated_at'}
    if not reader.fieldnames or set(reader.fieldnames) != required or len(reader.fieldnames) != len(required):
        raise ValueError('Public CSV schema changed or incomplete response')
    assets, seen, total = [], set(), 0
    for row in reader:
        if (None in row or any(value is None for value in row.values())
                or not row['identifier'].strip() or not row['asset_type'].strip()
                or row['eligible_for_submission'] not in ('true', 'false')
                or row['eligible_for_bounty'] not in ('true', 'false')):
            raise ValueError('Invalid or incomplete CSV asset row')
        total += 1
        asset = {'name': row['identifier'], 'asset_type': row['asset_type'], 'location': None,
                 'group': None, 'scope': 'in' if row['eligible_for_submission'] == 'true' else 'out',
                 'bounty_eligible': row['eligible_for_bounty'] == 'true'}
        key = json.dumps(asset, sort_keys=True)
        if key not in seen:
            seen.add(key)
            assets.append(asset)
    if not assets:
        raise ValueError('Empty CSV requires review; last-good scope retained')
    return {'assets': assets, 'source_url': source, 'captured_at': now(),
            'source_method': 'public_hackerone_program_and_structured_scopes',
            'published_asset_count': total, 'duplicate_source_rows': total - len(assets),
            'evidence_sha256': hashlib.sha256(raw.encode()).hexdigest()}


def parse_intigriti(program_url, body_get):
    program = urlsplit(program_url)
    if (program.scheme != 'https' or program.netloc != 'app.intigriti.com' or program.query
            or program.fragment or not re.fullmatch(r'/programs/(?:[a-zA-Z0-9_-]|%20)+/(?:[a-zA-Z0-9_-]|%20)+/?', program.path)):
        raise ValueError('Not an exact Intigriti program identity')
    source = program_url.rstrip('/') + '/detail'
    raw = body_get(source)
    tables = re.findall(r'<lib-assets-detail(?:\s[^>]*)?>(.*?)</lib-assets-detail>', raw, re.S)
    if len(tables) != 1 or len(re.findall(r'<lib-assets-detail(?:\s|>)', raw)) != 1:
        raise ValueError('Missing or ambiguous complete SSR asset table')
    table = tables[0]
    if re.search(r'paginat|load[\s_-]*more|show[\s_-]*more|infinite[\s_-]*scroll', table, re.I):
        raise ValueError('Possible asset table pagination requires review')
    rows = re.findall(r'<lib-asset-detail(?:\s[^>]*)?>(.*?)</lib-asset-detail>', table, re.S)
    if len(rows) != len(re.findall(r'<lib-asset-detail(?:\s|>)', raw)):
        raise ValueError('Unclosed or unparsed asset row')
    def clean(value):
        return ' '.join(html.unescape(re.sub('<[^>]*>', ' ', value)).split())
    assets, seen = [], set()
    for row in rows:
        namepart = re.search(r'<div[^>]*class="asset-name[^\"]*"[^>]*>(.*?)</div>', row, re.S)
        kind = re.search(r'<lib-asset-type-label[^>]*>(.*?)</lib-asset-type-label>', row, re.S)
        tier = re.search(r'<lib-bounty-tier-label[^>]*>(.*?)</lib-bounty-tier-label>', row, re.S)
        if not all((namepart, kind, tier)):
            raise ValueError('Incomplete SSR asset row')
        name, kind, tier = clean(namepart[1]), clean(kind[1]), clean(tier[1])
        if not name or not kind or tier not in ('Tier 1', 'Tier 2', 'Tier 3', 'Tier 4', 'Tier 5', 'No bounty', 'Out of scope'):
            raise ValueError('Empty asset value or unknown bounty tier')
        link = re.search(r'href="([^"]*)"', namepart[1])
        asset = {'name': name, 'asset_type': kind, 'location': html.unescape(link[1]) if link else None,
                 'group': None if tier == 'Out of scope' else tier,
                 'scope': 'out' if tier == 'Out of scope' else 'in'}
        key = json.dumps(asset, sort_keys=True)
        if key not in seen:
            seen.add(key)
            assets.append(asset)
    if not assets:
        raise ValueError('Empty visible SSR table requires review; last-good scope retained')
    return {'assets': assets, 'source_url': source, 'captured_at': now(),
            'source_method': 'public_intigriti_asset_table', 'html_has_assets_heading': 'header="Assets"' in raw,
            'duplicate_source_rows': len(rows) - len(assets),
            'evidence_sha256': hashlib.sha256(raw.encode()).hexdigest()}


def queue_identity(row):
    # Only the established display-only HackerOne query is removed. Other
    # queries/fragments stay intact and are rejected by the collector.
    url = row['program_url']
    if row['platform'] == 'HackerOne' and url.endswith('?type=team'):
        return url[:-10].rstrip('/')
    return url


def protect_removals(old_assets, new_assets):
    # A fully replaced or substantially truncated table is never auto-published.
    def identities(rows):
        return {(r['name'], r.get('location'), r.get('scope')) for r in rows}
    before, after = identities(old_assets), identities(new_assets)
    if before and len(before - after) / len(before) > 0.5:
        raise ValueError('More than half of prior asset identities disappeared; manual review required')


def update_capture(record, fresh):
    result = copy.deepcopy(record)
    protect_removals(record.get('assets', []), fresh['assets'])
    for key in ('gap_review', 'error', 'published_asset_count', 'duplicate_source_rows'):
        result.pop(key, None)
    result.update({k: v for k, v in fresh.items() if k != 'evidence_sha256'})
    result['status'] = 'captured'
    result['source_method'] = fresh['source_method']
    if not result['duplicate_source_rows']:
        result.pop('duplicate_source_rows')
    return result


def referenced_ids(value):
    if isinstance(value, dict):
        result = set(value.get('source_ids', []))
        for key, item in value.items():
            if key != 'source_ids':
                result.update(referenced_ids(item))
        return result
    if isinstance(value, list):
        return set().union(*(referenced_ids(item) for item in value)) if value else set()
    return set()


def update_program(record, fresh):
    result = copy.deepcopy(record)
    old = result.get('asset_scope')
    if not old:
        raise ValueError('Reviewed policy has no existing scope table; manual review required')
    old_assets = [dict(row, scope=side) for side, key in (('in', 'in_scope'), ('out', 'out_of_scope'))
                  for row in old[key]]
    if any(set(row) - {'name', 'asset_type', 'location', 'group', 'source_ids', 'scope', 'bounty_eligible'} for row in old_assets):
        raise ValueError('Curated scope qualifications require manual review')
    protect_removals(old_assets, fresh['assets'])
    other = {k: v for k, v in result.items() if k not in ('asset_scope', 'sources')}
    used_elsewhere = referenced_ids(other)
    source_id = 'automated-public-asset-scope'
    if source_id in used_elsewhere:
        raise ValueError('Automated source is shared by policy claims; manual review required')
    obsolete = set(old['source_ids']) - used_elsewhere
    result['sources'] = [s for s in result['sources'] if s['id'] not in obsolete | {source_id}]
    result['sources'].append({'id': source_id, 'title': 'Current published public asset table',
                              'url': fresh['source_url'], 'publisher': record.get('platform', 'Bugcrowd'),
                              'retrieved_at': fresh['captured_at'],
                              'provenance': 'official_primary', 'access_method': 'text'})
    old.update({'capture_status': 'published_list', 'collection_method': 'official_platform_scope_table',
                'verified_at': fresh['captured_at'], 'source_ids': [source_id],
                'limitations': list(dict.fromkeys(old.get('limitations', []) + ['Only public asset identifiers and explicit scope/bounty flags were refreshed automatically. Per-asset instruction prose, severity, group descriptions and rules may further restrict permission and are not reproduced. Whole-policy review dates, eligibility and restrictions were not refreshed. Live program rules prevail; this snapshot is not testing authorization.']))})
    for side, key in (('in', 'in_scope'), ('out', 'out_of_scope')):
        old[key] = [dict({k: v for k, v in row.items() if k != 'scope'}, source_ids=[source_id])
                    for row in fresh['assets'] if row['scope'] == side]
    return result


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def refresh(root, client):
    documents = {name: json.loads((root / name).read_text()) for name in CAPTURES}
    programs = {str(path.relative_to(root)): json.loads(path.read_text())
                for path in sorted((root / 'data/programs').glob('*.json'))}
    queue = {}
    for name, doc in documents.items():
        for i, row in enumerate(doc['captures']):
            queue.setdefault(queue_identity(row), []).append((name, i, row))
    for name, row in programs.items():
        queue.setdefault(queue_identity(row), []).append((name, None, row))
    # Rotate deterministically every day so a platform stop never starves the tail.
    urls = sorted(queue)
    offset = dt.date.today().toordinal() % max(1, len(urls))
    urls = urls[offset:] + urls[:offset]
    audit = {'schema_version': '1.0.0', 'started_at': now(), 'completed_at': None,
             'supported_platforms': ['Bugcrowd', 'HackerOne', 'Intigriti'], 'directory_discovery_refreshed': False,
             'whole_policies_refreshed': False, 'results': []}
    stopped = set()
    deadline = time.monotonic() + 65 * 60
    for url in urls:
        refs = queue[url]
        platform = refs[0][2]['platform']
        outcome = {'program_url': url, 'platform': platform}
        if platform not in audit['supported_platforms']:
            outcome.update(status='unsupported', reason='No validated unattended collector for this platform')
        elif platform == 'HackerOne' and all(row.get('status') == 'not_paid_bounty' for _, _, row in refs):
            outcome.update(status='unsupported', reason='Prior non-bounty classification requires a separate program review; scope CSV cannot reverify it')
        elif time.monotonic() >= deadline:
            outcome.update(status='deferred', reason='65-minute run budget exhausted; last-good data retained')
        elif platform in stopped:
            outcome.update(status='deferred', reason='Platform access/rate-limit stop; last-good data retained')
        else:
            outcome['attempted_at'] = now()
            try:
                fresh = (parse_brief(url, client.get(url), client.get) if platform == 'Bugcrowd'
                         else parse_hackerone(url, client.get) if platform == 'HackerOne'
                         else parse_intigriti(url, client.get))
                # Prepare every reference before changing any: overlap stays consistent.
                changed = [(name, index, update_capture(row, fresh) if index is not None else update_program(row, fresh))
                           for name, index, row in refs]
                for name, index, value in changed:
                    if index is None:
                        programs[name] = value
                    else:
                        documents[name]['captures'][index] = value
                outcome.update(status='refreshed', captured_at=fresh['captured_at'],
                               source_url=fresh['source_url'], evidence_sha256=fresh['evidence_sha256'],
                               in_scope=sum(a['scope'] == 'in' for a in fresh['assets']),
                               out_of_scope=sum(a['scope'] == 'out' for a in fresh['assets']))
            except Exception as error:
                outcome.update(status='failed', reason=f'{type(error).__name__}: {error}')
                if isinstance(error, HTTPError) and error.code in (401, 403, 429):
                    stopped.add(platform)
        audit['results'].append(outcome)
    audit['completed_at'] = now()
    audit['counts'] = {status: sum(r['status'] == status for r in audit['results'])
                       for status in ('refreshed', 'failed', 'deferred', 'unsupported')}
    audit['counts']['total'] = len(queue)
    audit['counts']['attempted'] = sum('attempted_at' in r for r in audit['results'])
    for name, doc in {**documents, **programs}.items():
        if json.loads((root / name).read_text()) != doc:
            dump(root / name, doc)
    dump(root / AUDIT, audit)
    return audit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--delay', type=float, default=2)
    args = parser.parse_args()
    audit = refresh(args.root, PublicClient(args.delay))
    print(json.dumps(audit['counts'], sort_keys=True))


if __name__ == '__main__':
    main()
