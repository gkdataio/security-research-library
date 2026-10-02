#!/usr/bin/env python3
"""Offline JSON/schema and editorial-integrity validation; never contacts targets."""
import argparse
import calendar
import datetime as dt
import json
import math
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]

class Invalid(ValueError):
    pass

def fail(path, message):
    raise Invalid(f'{path}: {message}')

def check_schema(value, spec, schema, path='$'):
    """Validate the documented JSON Schema subset used by report.schema.json."""
    if '$ref' in spec:
        ref = spec['$ref']
        if not ref.startswith('#/'):
            fail(path, 'external schema references are not allowed')
        spec = schema
        for key in ref[2:].split('/'):
            spec = spec[key]
    if 'const' in spec and value != spec['const']:
        fail(path, f'expected constant {spec["const"]!r}')
    if 'enum' in spec and value not in spec['enum']:
        fail(path, f'value not in enum {spec["enum"]!r}')
    types = spec.get('type', [])
    types = [types] if isinstance(types, str) else types
    istype = {
        'object': isinstance(value, dict), 'array': isinstance(value, list),
        'string': isinstance(value, str), 'null': value is None,
        'boolean': type(value) is bool,
        'number': type(value) in (int, float) and math.isfinite(value),
        'integer': type(value) is int,
    }
    if types and not any(istype.get(t, False) for t in types):
        fail(path, f'expected type {types!r}')
    if isinstance(value, dict):
        props = spec.get('properties', {})
        for key in spec.get('required', []):
            if key not in value:
                fail(path, f'missing {key}')
        if spec.get('additionalProperties') is False and set(value) - set(props):
            fail(path, f'unexpected keys: {sorted(set(value) - set(props))}')
        for key, item in value.items():
            if key in props:
                check_schema(item, props[key], schema, f'{path}.{key}')
    elif isinstance(value, list):
        if len(value) < spec.get('minItems', 0):
            fail(path, 'too few items')
        if spec.get('uniqueItems') and len({json.dumps(x, sort_keys=True) for x in value}) != len(value):
            fail(path, 'duplicate items')
        for index, item in enumerate(value):
            if 'items' in spec:
                check_schema(item, spec['items'], schema, f'{path}[{index}]')
    elif isinstance(value, str):
        if len(value) < spec.get('minLength', 0) or len(value) > spec.get('maxLength', math.inf):
            fail(path, 'invalid string length')
        if 'pattern' in spec and not re.search(spec['pattern'], value):
            fail(path, 'does not match required pattern')
        fmt = spec.get('format')
        try:
            if fmt == 'date':
                if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
                    raise ValueError('not ISO date')
                dt.date.fromisoformat(value)
            elif fmt == 'date-time':
                if 'T' not in value or not dt.datetime.fromisoformat(value.replace('Z', '+00:00')).tzinfo:
                    raise ValueError('timezone required')
            elif fmt == 'uri':
                u = urlsplit(value)
                if u.scheme != 'https' or not u.netloc or u.username or u.password:
                    raise ValueError('HTTPS source URL without credentials required')
        except ValueError as exc:
            fail(path, f'invalid {fmt}: {exc}')
    elif type(value) in (int, float):
        if value < spec.get('minimum', -math.inf):
            fail(path, 'below required minimum')

def date_bounds(item):
    value, precision = item['value'], item['precision']
    if value is None:
        if precision is not None or item['basis'] != 'not_reported' or item['source_id'] is not None:
            raise Invalid('unknown date must have null precision/source and not_reported basis')
        return None
    if item['basis'] == 'not_reported' or item['source_id'] is None:
        raise Invalid('known date requires evidence source and basis')
    parts = [int(p) for p in value.split('-')]
    expected = {'year': 1, 'month': 2, 'day': 3}
    if precision not in expected or len(parts) != expected[precision]:
        raise Invalid('date value and precision disagree')
    year = parts[0]
    if precision == 'year':
        return dt.date(year, 1, 1), dt.date(year, 12, 31)
    month = parts[1]
    if precision == 'month':
        return dt.date(year, month, 1), dt.date(year, month, calendar.monthrange(year, month)[1])
    day = dt.date(*parts)
    return day, day

def normalize_url(url):
    u = urlsplit(url)
    return urlunsplit((u.scheme.lower(), u.netloc.lower(), u.path.rstrip('/'), u.query, ''))

def validate_record(record, taxonomy, schema):
    check_schema(record, schema, schema)
    cats = {x['id'] for x in taxonomy['categories']}
    skills = {x['id'] for x in taxonomy['skillsets']}
    used_cats = [record['category_id'], *record['secondary_category_ids']]
    if len(set(used_cats)) != len(used_cats) or not set(used_cats) <= cats:
        fail(record['id'], 'duplicate or undefined category')
    if not set(record['skillset_ids']) <= skills:
        fail(record['id'], 'undefined skillset')
    sources = {s['id']: s for s in record['sources']}
    if len(sources) != len(record['sources']):
        fail(record['id'], 'duplicate source IDs')
    refs = [record['primary_source_id'], record['reward']['source_id']]
    refs += [c['source_id'] for c in record['cwe_mappings']]
    refs += [d['source_id'] for d in record['dates'].values() if d['source_id'] is not None]
    if not set(refs) <= set(sources):
        fail(record['id'], 'unknown source reference')
    reward = record['reward']
    src = sources[reward['source_id']]
    required_type = {'vendor_confirmed':'vendor', 'platform_confirmed':'platform', 'organizer_confirmed':'competition_organizer'}
    if reward['evidence_level'] in required_type and src['type'] != required_type[reward['evidence_level']]:
        fail(record['id'], 'reward attribution overstates source provenance')
    if 'reward' not in src['supports']:
        fail(record['id'], 'reward source does not support reward')
    if len(reward['evidence_quote'].split()) > 25:
        fail(record['id'], 'reward quotation exceeds 25 words')
    try:
        bounds = {key:date_bounds(item) for key,item in record['dates'].items()}
    except (ValueError, TypeError) as exc:
        fail(record['id'], f'invalid date: {exc}')
    asof = dt.date.fromisoformat(record['recency']['as_of'])
    start = dt.date.fromisoformat(record['recency']['window_start'])
    if start > asof:
        fail(record['id'], 'recency window is reversed')
    for key, interval in bounds.items():
        if interval and interval[0] > asof:
            fail(record['id'], f'{key} date is after as_of')
        if interval and record['dates'][key]['basis'] != 'explicit' and not record['dates'][key]['note']:
            fail(record['id'], f'{key} inferred date requires a note')
    if bounds['reported']:
        for key in ('awarded','paid','fixed','public_disclosure'):
            if bounds[key] and bounds['reported'][0] > bounds[key][1]:
                fail(record['id'], f'{key} predates original report')
    if reward['status'] == 'paid' and not (bounds['paid'] or 'paid' in reward['notes'].lower()):
        fail(record['id'], 'paid status requires a date or explicit qualification')
    pub = bounds['published']
    expected = None if not pub else (False if pub[1] < start else True if pub[0] >= start and pub[1] <= asof else None)
    if record['recency']['within_preferred_window'] is not expected:
        fail(record['id'], 'recency does not agree with publication date precision')
    if expected is not True and not record['recency']['note']:
        fail(record['id'], 'older or uncertain recency requires a note')
    return normalize_url(sources[record['primary_source_id']]['url'])

def validate_library(root=ROOT):
    schema = json.loads((root/'schema/report.schema.json').read_text())
    taxonomy = json.loads((root/'data/taxonomy.json').read_text())
    for field in ('categories','skillsets'):
        ids = [x['id'] for x in taxonomy[field]]
        if len(ids) != len(set(ids)):
            fail('taxonomy', f'duplicate {field} IDs')
    records, ids, urls = [], set(), set()
    for path in sorted((root/'data/reports').glob('*.json')):
        record = json.loads(path.read_text())
        url = validate_record(record, taxonomy, schema)
        if path.stem != record['id']:
            fail(str(path), 'filename and stable ID differ')
        if record['id'] in ids or url in urls:
            fail(str(path), 'duplicate stable ID or primary source URL')
        ids.add(record['id']); urls.add(url); records.append(record)
    if not records:
        fail(str(root), 'no records')
    return records, taxonomy

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        records, _ = validate_library(args.root)
    except (Invalid, OSError, json.JSONDecodeError, KeyError) as exc:
        parser.exit(1, f'Validation failed: {exc}\n')
    print(f'Validated {len(records)} disclosure records (offline).')

if __name__ == '__main__':
    main()
