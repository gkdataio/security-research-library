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
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from source_access import BUGCROWD_SCOPE_HOSTS, excluded_source_reason, require_source_access
from scope_integrity import redacted_scope_count

ROOT = Path(__file__).resolve().parents[1]
CAPTURES = ('data/public-bounty-scopes.json', 'data/bugcrowd-vdp-scopes.json')
AUDIT = 'data/scope-refresh-status.json'
MAX_BYTES = 8 * 1024 * 1024
# One already recorded public identity contains a literal ampersand. Keep this
# exception exact instead of permitting arbitrary URL punctuation or decoding.
INTIGRITI_AMPERSAND_PATH = '/programs/uz%20leuven/ehealthhub&meta-hubvznkul'
INTIGRITI_PROGRAM_PATH = r'/programs/(?:[a-zA-Z0-9_-]|%20)+/(?:[a-zA-Z0-9_-]|%20)+'


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


def exact_url_parts(url):
    # urlsplit silently strips some whitespace/control characters. Reject them
    # before parsing, along with backslashes and even empty query/fragment marks.
    if not isinstance(url, str) or re.search(r'[\s\x00-\x1f\x7f\\?#]', url):
        raise ValueError('Not an exact approved public platform scope URL')
    return urlsplit(url)


def intigriti_program_path(path):
    return path == INTIGRITI_AMPERSAND_PATH or bool(re.fullmatch(INTIGRITI_PROGRAM_PATH, path))


def official_url(url):
    require_source_access(url)
    parts = exact_url_parts(url)
    if (parts.scheme == 'https' and parts.netloc == 'app.intigriti.com' and not parts.query
            and not parts.fragment and parts.path.endswith('/detail')
            and intigriti_program_path(parts.path[:-len('/detail')])):
        return parts
    if (parts.scheme == 'https' and parts.netloc == 'hackerone.com' and not parts.query
            and not parts.fragment and re.fullmatch(r'/teams/[a-zA-Z0-9_-]+/assets/download_csv\.csv', parts.path)):
        return parts
    if (parts.scheme != 'https' or parts.netloc not in BUGCROWD_SCOPE_HOSTS
            or parts.query or parts.fragment or not re.fullmatch(
                r'/engagements/[a-zA-Z0-9_-]+(?:/changelog/[a-zA-Z0-9_-]+\.json)?', parts.path)):
        raise ValueError('Not an exact approved public platform scope URL')
    return parts


OBSERVATION_MESSAGES = {
    'http_response_incomplete': 'HTTP response is not a complete 200 response; last-good scope retained',
    'redirect_requires_review': 'Redirect requires manual review; no redirect was followed',
    'bugcrowd_scope_schema_invalid': 'Missing or malformed public scope structure; last-good scope retained',
    'bugcrowd_scope_empty': 'Validated public scope structure contains zero asset rows; last-good scope retained',
    'bugcrowd_scope_redacted': 'Public scope rows contain only redacted identifiers; no usable public asset identifiers verified; last-good scope retained',
    'hackerone_scope_empty': 'Validated CSV contains zero asset rows; last-good scope retained',
    'intigriti_no_visible_rows': 'No visible SSR asset rows were observed; table readiness and current scope remain unverified; last-good scope retained',
}
SAFE_VALUE_ERRORS = {
    'Not an exact approved public platform scope URL': 'source_url_invalid',
    'Not an exact HackerOne program identity': 'program_identity_invalid',
    'Not an exact Intigriti program identity': 'program_identity_invalid',
    'Response exceeds size limit': 'response_size_limit',
    'Incomplete HTTP response': 'response_incomplete',
    'Missing or ambiguous current public brief': 'current_brief_ambiguous',
    'Current brief does not belong to this exact program': 'current_brief_identity_mismatch',
    'Scope group schema changed': 'scope_group_schema_invalid',
    'Scope target schema changed': 'scope_target_schema_invalid',
    'Invalid publication timestamp': 'publication_timestamp_invalid',
    'CSV response lacks complete final line': 'csv_response_incomplete',
    'Public CSV schema changed or incomplete response': 'csv_schema_invalid',
    'Invalid or incomplete CSV asset row': 'csv_row_invalid',
    'Missing or ambiguous complete SSR asset table': 'ssr_table_ambiguous',
    'Possible asset table pagination requires review': 'ssr_pagination_unverified',
    'Unclosed or unparsed asset row': 'ssr_row_incomplete',
    'Incomplete SSR asset row': 'ssr_row_incomplete',
    'Empty asset value or unknown bounty tier': 'ssr_row_invalid',
    'More than half of prior asset identities disappeared; manual review required': 'scope_removal_guard',
    'Reviewed policy has no existing scope table; manual review required': 'policy_scope_missing',
    'Curated scope qualifications require manual review': 'curated_qualifications_require_review',
    'Automated source is shared by policy claims; manual review required': 'policy_source_shared',
}
REDIRECT_CATEGORIES = frozenset({
    'same_program_preview_route', 'same_program_terms_route', 'same_program_scope_route',
    'same_program_migration_route', 'same_origin_other_route', 'cross_origin', 'unsafe_or_unrecognized',
})


class ObservationError(ValueError):
    """Typed evidence, never a raw response, header, or exception message."""
    def __init__(self, reason_code, **details):
        super().__init__(OBSERVATION_MESSAGES[reason_code])
        self.reason_code = reason_code
        self.details = details


def safe_audit_source(url):
    """Return only a validated scope URL, without query, fragment or credentials.

    This is for reporting only. It never relaxes the request URL validator.
    Callers use the requested source, never an HTTP error's untrusted URL.
    """
    if not isinstance(url, str) or len(url) > 4096 or re.search(r'[\s\x00-\x1f\x7f\\]', url):
        return None
    try:
        parts = urlsplit(url)
        if parts.username or parts.password or parts.port:
            return None
        clean = parts._replace(query='', fragment='').geturl()
        official_url(clean)
        return clean
    except (ValueError, TypeError):
        return None


def redirect_category(source, destination):
    """Classify a no-follow Location without retaining any destination text.

    A preview/terms route is not a verified login gate. Hostnames and path/query
    text from unrecognized destinations are never written to the audit.
    """
    source = safe_audit_source(source)
    if (not source or not isinstance(destination, str) or not destination or len(destination) > 4096
            or re.search(r'[\s\x00-\x1f\x7f\\]', destination)):
        return 'unsafe_or_unrecognized'
    try:
        before, after = urlsplit(source), urlsplit(urljoin(source, destination))
        if after.scheme != 'https' or not after.hostname or after.username or after.password or after.port:
            return 'unsafe_or_unrecognized'
        if before.netloc != after.netloc:
            return 'cross_origin'
        if (before.netloc in BUGCROWD_SCOPE_HOSTS
                and re.fullmatch(r'/engagements/[a-zA-Z0-9_-]+', before.path)
                and after.path == before.path + '/migrated'):
            return 'same_program_migration_route'
        if before.netloc == 'app.intigriti.com' and before.path.endswith('/detail'):
            base = before.path[:-len('/detail')]
            routes = {base + '/preview/detail': 'same_program_preview_route',
                      base + '/tac/detail': 'same_program_terms_route',
                      base + '/detail': 'same_program_scope_route'}
            if after.path in routes:
                return routes[after.path]
        return 'same_origin_other_route'
    except (ValueError, TypeError):
        return 'unsafe_or_unrecognized'


def failure_fields(error, stage, source_url=None):
    """Allowlist audit fields. Never serialize str(error), headers, or bodies."""
    result = {'status': 'failed', 'verification_status': 'unknown',
              'failure_stage': stage if stage in ('identity_validation', 'source_request', 'response_parse', 'record_update') else 'unknown',
              'reason_code': 'unexpected_collector_error',
              'reason': 'Unexpected collector error; details omitted; last-good scope retained',
              'observation_status': 'unverified'}
    if isinstance(error, ObservationError) and error.reason_code in OBSERVATION_MESSAGES:
        result.update(reason_code=error.reason_code, reason=OBSERVATION_MESSAGES[error.reason_code])
        details = error.details
        if error.reason_code == 'redirect_requires_review':
            result['observation_status'] = 'redirect_not_followed'
            category = details.get('redirect_category')
            result['redirect_category'] = category if isinstance(category, str) and category in REDIRECT_CATEGORIES else 'unsafe_or_unrecognized'
        elif error.reason_code == 'bugcrowd_scope_redacted':
            result.update(observation_status='redacted_public_table', observed_non_redacted_asset_count=0)
            count = details.get('observed_redacted_asset_count')
            if type(count) is int and count > 0:
                result['observed_redacted_asset_count'] = count
        elif error.reason_code.endswith('_scope_empty'):
            result.update(observation_status='empty_public_table', observed_asset_count=0)
        elif error.reason_code == 'intigriti_no_visible_rows':
            # A zero-row SSR container can be a loading or login shell. Without
            # a validated empty-state marker it cannot prove an empty scope.
            result.update(observation_status='unverified_no_rows_observed', observed_asset_row_count=0)
        else:
            result['observation_status'] = 'invalid_source_response'
        digest = details.get('response_sha256')
        if isinstance(digest, str) and re.fullmatch(r'[0-9a-f]{64}', digest):
            result['response_sha256'] = digest
        code = details.get('http_status')
        if type(code) is int and ((300 <= code <= 399 and error.reason_code == 'redirect_requires_review')
                                 or (100 <= code <= 599 and error.reason_code == 'http_response_incomplete')):
            result['http_status'] = code
    elif isinstance(error, HTTPError):
        code = error.code
        if type(code) is int and 100 <= code <= 599:
            result.update(reason_code='http_error', http_status=code,
                          reason=f'HTTP {code}; last-good scope retained')
        else:
            result.update(reason_code='http_error', reason='HTTP request failed; last-good scope retained')
        result['observation_status'] = 'source_request_failed'
    elif isinstance(error, (TimeoutError, URLError)):
        result.update(reason_code='source_transport_error', observation_status='source_request_failed',
                      reason='Source request failed or timed out; details omitted; last-good scope retained')
    elif isinstance(error, (json.JSONDecodeError, csv.Error, UnicodeError)):
        result.update(reason_code='source_encoding_or_syntax_invalid', observation_status='invalid_source_response',
                      reason='Source response encoding or syntax is invalid; last-good scope retained')
    elif isinstance(error, ValueError) and str(error) in SAFE_VALUE_ERRORS:
        message = str(error)
        result.update(reason_code=SAFE_VALUE_ERRORS[message], reason=message,
                      observation_status='record_update_rejected' if stage == 'record_update' else 'invalid_source_response')
    clean = safe_audit_source(source_url)
    if clean and stage == 'source_request':
        result['failed_source_url'] = clean
    elif clean and stage == 'response_parse':
        result['observation_source_url'] = clean
    return result


class NoRedirect(HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        # Inspect only metadata and stop before urllib normalizes/rejects a
        # Location or tries another request. Never retain its untrusted text.
        if hasattr(headers, 'get_all'):
            locations = headers.get_all('Location', []) or headers.get_all('URI', [])
        else:
            locations = [value for key, value in headers.items() if key.lower() == 'location']
            if not locations:
                locations = [value for key, value in headers.items() if key.lower() == 'uri']
        destination = locations[0] if len(locations) == 1 else None
        try:
            return self.redirect_request(req, fp, code, msg, headers, destination)
        finally:
            if fp is not None:
                fp.close()

    http_error_301 = http_error_303 = http_error_307 = http_error_308 = http_error_302

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # A changed identity or access gate needs review, not automatic traversal.
        raise ObservationError('redirect_requires_review', http_status=code,
                               redirect_category=redirect_category(req.full_url, newurl))


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
            status = response.getcode()
            if status != 200 or response.headers.get('Content-Range') is not None:
                raise ObservationError('http_response_incomplete', http_status=status)
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
    source = program.scheme + '://' + program.netloc + path + '.json'
    official_url(source)
    raw = body_get(source)
    digest = hashlib.sha256(raw.encode()).hexdigest()
    try:
        document = json.loads(raw)
    except json.JSONDecodeError:
        raise ObservationError('bugcrowd_scope_schema_invalid', response_sha256=digest) from None
    if (not isinstance(document, dict) or not isinstance(document.get('data'), dict)
            or not isinstance(document['data'].get('scope'), list)):
        raise ObservationError('bugcrowd_scope_schema_invalid', response_sha256=digest)
    groups = document['data']['scope']
    published = document.get('publishedAt')
    if published is not None and not isinstance(published, str):
        raise ValueError('Invalid publication timestamp')
    assets, seen, duplicates = [], set(), 0
    for group in groups:
        if (not isinstance(group, dict) or type(group.get('inScope')) is not bool or not isinstance(group.get('name'), str)
                or not isinstance(group.get('targets'), list)):
            raise ValueError('Scope group schema changed')
        for target in group['targets']:
            if (not isinstance(target, dict) or not isinstance(target.get('name'), str) or not target['name'].strip()
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
        raise ObservationError('bugcrowd_scope_empty', response_sha256=digest)
    if redacted_scope_count(assets) == len(assets):
        raise ObservationError('bugcrowd_scope_redacted', response_sha256=digest,
                               observed_redacted_asset_count=len(assets))
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
        raise ObservationError('hackerone_scope_empty', response_sha256=hashlib.sha256(raw.encode()).hexdigest())
    return {'assets': assets, 'source_url': source, 'captured_at': now(),
            'source_method': 'public_hackerone_program_and_structured_scopes',
            'published_asset_count': total, 'duplicate_source_rows': total - len(assets),
            'evidence_sha256': hashlib.sha256(raw.encode()).hexdigest()}


def parse_intigriti(program_url, body_get):
    program = exact_url_parts(program_url)
    if (program.scheme != 'https' or program.netloc != 'app.intigriti.com' or program.query
            or program.fragment or not intigriti_program_path(program.path.removesuffix('/'))):
        raise ValueError('Not an exact Intigriti program identity')
    source = program_url.rstrip('/') + '/detail'
    official_url(source)
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
        raise ObservationError('intigriti_no_visible_rows', response_sha256=hashlib.sha256(raw.encode()).hexdigest())
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
        exclusion = excluded_source_reason(url)
        if exclusion:
            outcome.update(status='deferred', reason_code='source_excluded',
                           verification_status='unknown', reason=exclusion)
        elif platform not in audit['supported_platforms']:
            outcome.update(status='unsupported', reason='No validated unattended collector for this platform')
        elif platform == 'HackerOne' and all(row.get('status') == 'not_paid_bounty' for _, _, row in refs):
            outcome.update(status='unsupported', reason='Prior non-bounty classification requires a separate program review; scope CSV cannot reverify it')
        elif time.monotonic() >= deadline:
            outcome.update(status='deferred', reason='65-minute run budget exhausted; last-good data retained')
        elif platform in stopped:
            outcome.update(status='deferred', reason='Platform access/rate-limit stop; last-good data retained')
        else:
            outcome['attempted_at'] = now()
            failure_stage, last_source = 'identity_validation', None
            def observed_get(source):
                nonlocal failure_stage, last_source
                # Validate before recording or requesting. An invalid new source
                # must not inherit the preceding successful request's attribution.
                failure_stage, last_source = 'identity_validation', None
                official_url(source)
                failure_stage, last_source = 'source_request', source
                body = client.get(source)
                failure_stage = 'response_parse'
                return body
            try:
                fresh = (parse_brief(url, observed_get(url), observed_get) if platform == 'Bugcrowd'
                         else parse_hackerone(url, observed_get) if platform == 'HackerOne'
                         else parse_intigriti(url, observed_get))
                failure_stage = 'record_update'
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
                outcome.update(failure_fields(error, failure_stage, last_source))
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
