"""Render current collection limits separately from historical scope evidence."""
import datetime as dt
import json
from urllib.parse import urlsplit

from build_navigation import link, text
from scope_integrity import redaction_warning
from validate import Invalid


def identity(url):
    # Match only the established HackerOne display alias, not arbitrary queries.
    parts = urlsplit(url)
    if parts.netloc in ('hackerone.com', 'www.hackerone.com') and parts.query == 'type=team':
        return parts._replace(query='').geturl().rstrip('/')
    return url


def load_visibility(root):
    outcomes, reviews = {}, {}
    audit_path = root / 'data/scope-refresh-status.json'
    if audit_path.is_file():
        audit = json.loads(audit_path.read_text(encoding='utf-8'))
        for row in audit['results']:
            key = identity(row['program_url'])
            if key in outcomes:
                raise Invalid('duplicate scope-refresh program identity')
            outcomes[key] = dict(row, audit_completed_at=audit.get('completed_at'))
    path = root / 'data/scope-source-reviews.json'
    if path.is_file():
        data = json.loads(path.read_text(encoding='utf-8'))
        if set(data) != {'schema_version', 'reviews'} or data['schema_version'] != '1.0.0':
            raise Invalid('invalid scope-source review envelope')
        for row in data['reviews']:
            if set(row) != {'program_url', 'reviewed_at', 'kind', 'note', 'official_source_urls'}:
                raise Invalid('invalid scope-source review fields')
            if row['kind'] not in ('migrated_login_required', 'new_submissions_moved'):
                raise Invalid('unknown scope-source review kind')
            try:
                timestamp = dt.datetime.fromisoformat(row['reviewed_at'].replace('Z', '+00:00'))
                if timestamp.tzinfo is None:
                    raise ValueError('timezone missing')
            except (TypeError, ValueError):
                raise Invalid('invalid scope-source review timestamp') from None
            if not isinstance(row['note'], str) or not row['note'].strip() or not row['official_source_urls']:
                raise Invalid('scope-source review needs note and sources')
            for url in [row['program_url']] + row['official_source_urls']:
                parts = urlsplit(url)
                if (parts.scheme != 'https' or not parts.netloc or parts.username or parts.password
                        or parts.query or parts.fragment or parts.port):
                    raise Invalid('scope-source review URL must be a plain public HTTPS source')
            key = identity(row['program_url'])
            if key in reviews:
                raise Invalid('duplicate scope-source review program')
            reviews[key] = row
    return outcomes, reviews


def visibility_lines(item, visibility, audit_href):
    outcomes, reviews = visibility
    key = identity(item['program_url'])
    rows = item['in_scope'] + item['out_of_scope']
    lines = []
    warning = redaction_warning(rows)
    if warning:
        lines += ['**Redacted scope:** ' + text(warning), '']
    outcome = outcomes.get(key)
    attempted = (outcome.get('attempted_at') or outcome.get('audit_completed_at')) if outcome else None
    captured = item.get('scope_captured_at')
    superseded = bool(attempted and captured and
                      dt.datetime.fromisoformat(captured.replace('Z', '+00:00')) >
                      dt.datetime.fromisoformat(attempted.replace('Z', '+00:00')))
    if outcome and outcome['status'] in ('failed', 'deferred') and not superseded:
        attempted = attempted or 'Date unavailable'
        label = 'Latest refresh failed' if outcome['status'] == 'failed' else 'Latest refresh deferred'
        reason = outcome.get('reason') or 'No successful current scope capture was recorded.'
        lines += ['**' + label + ' (' + text(attempted) + '):** ' + text(reason.rstrip('.')) + '. ' +
                  'The capture status, rows and date on this page are retained evidence, not a current scope verification. ' +
                  link('Refresh audit', audit_href) + '.', '']
    review = reviews.get(key)
    if review:
        lines += ['**Official source review (' + text(review['reviewed_at'][:10]) + '):** ' + text(review['note']), '',
                  '**Review sources:** ' + ', '.join(link('Official source ' + str(i), url)
                                                     for i, url in enumerate(review['official_source_urls'], 1)), '']
    return lines
