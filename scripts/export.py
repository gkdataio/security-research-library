#!/usr/bin/env python3
"""Create a deterministic, offline JSON export for future downstream adapters."""
import argparse
import json
from pathlib import Path
from validate import ROOT, validate_library

def build_export(root=ROOT):
    records, taxonomy = validate_library(root)
    records.sort(key=lambda x: (x['dates']['published']['value'] or '', x['id']), reverse=True)
    return {
        'schema_version': '1.2.0',
        'dataset': 'security-research-library',
        'as_of': max(r['recency']['as_of'] for r in records),
        'latest_reviewed_at': max(r['verification']['reviewed_at'] for r in records),
        'purpose': 'Historical public-disclosure research and defensive skill development for authorized reviews',
        'inclusion_policy': {
            'minimum_individual_award': 10000,
            'currency': 'USD',
            'preferred_publication_window_months': 12,
            'counts_award_announcements': True,
            'independent_cash_settlement_audit': False,
            'program_maximums_and_aggregate_earnings_excluded': True,
            'competition_awards_explicitly_labeled': True,
            'payloads_and_reproduction_steps_excluded': True,
        },
        'counts': {
            'included': len(records),
            'within_preferred_window': sum(r['recency']['within_preferred_window'] is True for r in records),
            'older_or_uncertain': sum(r['recency']['within_preferred_window'] is not True for r in records),
            'bug_bounty': sum(r['reward']['type'] == 'bug_bounty' for r in records),
            'competition_award': sum(r['reward']['type'] == 'competition_award' for r in records),
        },
        'downstream_compatibility': 'Portable research export only. A vulns.co ingestion contract has not been supplied or validated; no ingestion or deployment is performed.',
        'taxonomy': taxonomy,
        'reports': records,
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--check', action='store_true', help='Check committed export without modifying it')
    args = parser.parse_args()
    data = json.dumps(build_export(args.root), ensure_ascii=False, indent=2) + '\n'
    output = args.root/'exports/vulns-co.json'
    if args.check:
        if not output.is_file() or output.read_text() != data:
            parser.exit(1, 'Export missing or stale. Run python3 scripts/export.py\n')
        print('Export is current and deterministic.')
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(data)
        print(output)

if __name__ == '__main__':
    main()
