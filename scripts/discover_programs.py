#!/usr/bin/env python3
"""Validate browser-observed directory pages and report newly seen program URLs.

This is an OFFLINE importer, not a live crawler. With no --observations, every
platform is needs_browser and discovery counts are null, never a false zero.
It never changes the canonical catalog or requests program/target URLs.

Input: {"platforms": [{"platform": "HackerOne", "filters": "Active; launch desc",
 "pages": [{"number": 1, "url": "https://hackerone.com/directory/programs",
 "observed_at": "2026-11-07T12:00:00Z", "advertised_total": 1,
 "pagination_exhausted": true, "entries": [{"name": "Example",
 "program_url": "https://hackerone.com/example", "program_type": "unknown"}]}]}]}

For infinite scroll, pages are logical observed batches; only mark the last as
exhausted after reaching the visible footer/end. advertised_total may be null
if the UI does not advertise one. Numbered directories must cover every page.
The caller must attest actual visible pagination, not infer exhaustion from an
empty response. A complete import means the supplied filter's visible listing,
not every program on a platform. Feed only public official-directory metadata.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

from export_program_discovery import identity_url

ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = {
    'Bugcrowd': ('https://bugcrowd.com/engagements', 'https://bugcrowd.com/engagement_listings'),
    'HackerOne': ('https://hackerone.com/directory/programs', 'https://hackerone.com/directory'),
    'Intigriti': ('https://www.intigriti.com/researchers/bug-bounty-programs',),
}
HOSTS = {'Bugcrowd': {'bugcrowd.com', 'eu.bugcrowd.net', 'gov.bugcrowd.net'},
         'HackerOne': {'hackerone.com'}, 'Intigriti': {'app.intigriti.com', 'www.intigriti.com'}}
TYPES = {'paid_bounty', 'vulnerability_disclosure', 'unknown'}


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError('missing observation timestamp')
    parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('observation timestamp must include timezone')
    return parsed


def official_url(url, platform, directory=False):
    if not isinstance(url, str):
        raise ValueError('missing URL')
    p = urlsplit(url)
    if p.scheme != 'https' or p.hostname not in HOSTS[platform] or p.username or p.password or p.port or p.fragment:
        raise ValueError('URL must be an official HTTPS platform URL')
    if directory:
        if f'https://{p.hostname}{p.path.rstrip("/")}' not in DIRECTORIES[platform]:
            raise ValueError('source is not an official program directory')
    elif platform == 'HackerOne' and not re.fullmatch(r'/[a-zA-Z0-9_-]+/?', p.path):
        raise ValueError('expected HackerOne program page')
    elif platform == 'Bugcrowd' and not re.fullmatch(r'/(?:engagements/)?[a-zA-Z0-9_-]+/?', p.path):
        raise ValueError('expected Bugcrowd engagement page')
    elif platform == 'Intigriti' and not p.path.startswith('/programs/'):
        raise ValueError('expected Intigriti program page')
    return identity_url(url)


def validate_observation(capture, now):
    platform = capture['platform']
    if not isinstance(capture.get('filters'), str) or not capture['filters'].strip():
        raise ValueError('directory filters and sort must be recorded')
    pages = capture.get('pages')
    if not isinstance(pages, list) or not pages:
        raise ValueError('no observed pages')
    entries, seen, sources, totals = [], set(), [], set()
    for number, page in enumerate(pages, 1):
        if type(page.get('number')) is not int or page['number'] != number:
            raise ValueError('pages must be contiguous from page 1')
        official_url(page['url'], platform, directory=True)
        age = now - timestamp(page['observed_at'])
        if age < dt.timedelta(0) or age > dt.timedelta(hours=36):
            raise ValueError('observations must be within the past 36 hours')
        exhausted = page.get('pagination_exhausted')
        if type(exhausted) is not bool or exhausted != (number == len(pages)):
            raise ValueError('explicit pagination exhaustion required only on final page')
        total = page.get('advertised_total')
        if total is not None and (type(total) is not int or total <= 0):
            raise ValueError('invalid advertised total')
        totals.add(total)
        rows = page.get('entries')
        if not isinstance(rows, list) or not rows:
            raise ValueError('empty pages are not proof of completed pagination')
        for row in rows:
            key = official_url(row['program_url'], platform)
            if key in seen:
                raise ValueError('duplicate program URL across pages; repeat a stable directory pass')
            seen.add(key)
            name = row.get('name')
            kind = row.get('program_type', 'unknown')
            if not isinstance(name, str) or not name.strip() or kind not in TYPES:
                raise ValueError('invalid program name or type')
            entries.append({'name': name.strip(), 'program_url': key, 'platform': platform,
                            'program_type': kind, 'submission_status': 'unknown',
                            'source_url': page['url'], 'observed_at': page['observed_at'],
                            'review_state': 'directory_listing_only'})
        sources.append({k: page[k] for k in ('number', 'url', 'observed_at', 'pagination_exhausted')})
    if len(totals) != 1:
        raise ValueError('advertised totals changed or are inconsistent across pages')
    total = next(iter(totals))
    if total is not None and len(entries) != total:
        raise ValueError('distinct listing count does not match advertised total')
    return entries, sources


def build_report(baseline, observations=None, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    known = {(r['platform'], identity_url(r['program_url'])) for r in baseline['listings']}
    supplied = {}
    for capture in (observations or {}).get('platforms', []):
        platform = capture.get('platform')
        if platform not in DIRECTORIES or platform in supplied:
            raise ValueError('unknown or duplicate platform capture')
        supplied[platform] = capture
    statuses = []
    for platform in DIRECTORIES:
        result = {'platform': platform, 'status': 'needs_browser', 'observed_count': None,
                  'new_count': None, 'candidates': [], 'sources': [],
                  'reason': 'No current browser-observed complete directory supplied. No live collector is implemented.'}
        if platform in supplied:
            capture = supplied[platform]
            result['filters'] = capture.get('filters')
            try:
                entries, sources = validate_observation(capture, now)
                candidates = [r for r in entries if (platform, r['program_url']) not in known]
                result.update(status='complete_visible_listing', observed_count=len(entries),
                              new_count=len(candidates), candidates=candidates, sources=sources,
                              reason='Complete only for recorded visible filters. Candidates require policy and scope review.')
            except (ValueError, KeyError, TypeError) as exc:
                result.update(status='invalid_observation', reason=str(exc))
        statuses.append(result)
    complete = all(r['status'] == 'complete_visible_listing' for r in statuses)
    return {'schema_version': '1.0.0', 'completed_at': now.isoformat().replace('+00:00', 'Z'),
            'status': 'complete_visible_listings' if complete else 'incomplete',
            'mode': 'offline_observation_import',
            'notice': 'New means absent from the historical URL baseline, not newly launched. Directory listings are not testing authorization. No removals inferred; canonical data is unchanged.',
            'counts': {'baseline_urls': len(known), 'platforms_completed': sum(r['status'] == 'complete_visible_listing' for r in statuses),
                       'new_programs': sum(r['new_count'] for r in statuses) if complete else None,
                       'validated_candidates': sum(r['new_count'] or 0 for r in statuses)},
            'platforms': statuses}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path, default=ROOT/'exports/program-discovery.json')
    parser.add_argument('--observations', type=Path, help='Current complete browser directory observations; no fetching is performed')
    parser.add_argument('--output', type=Path, default=ROOT/'data/program-discovery-status.json')
    args = parser.parse_args()
    raw = args.baseline.read_bytes()
    observations = json.loads(args.observations.read_text()) if args.observations else None
    report = build_report(json.loads(raw), observations)
    report['baseline_sha256'] = hashlib.sha256(raw).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(f"Discovery observation import: {report['status']}; {report['counts']['platforms_completed']}/3 platforms complete")


if __name__ == '__main__':
    main()
