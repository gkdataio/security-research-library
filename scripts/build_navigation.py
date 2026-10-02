#!/usr/bin/env python3
"""Build deterministic GitHub-readable Markdown pages from canonical records. Offline."""
import argparse
import re
from pathlib import Path
from urllib.parse import quote
from validate import ROOT
from validate_extra import validate_all


def text(value):
    """Escape Markdown and HTML metacharacters in record text."""
    value = str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return re.sub(r'([\\`*_{}\[\]()#+.!|])', r'\\\1', value).replace('\n', ' ')


def link(label, url):
    safe_url = quote(str(url), safe="/:#?&=@[]!$'()*+,;%-._~")
    return f'[{text(label)}](<{safe_url}>)'


def build(root=ROOT):
    import json
    resources, diagrams, _ = validate_all(root)
    reports = [json.loads(p.read_text()) for p in sorted((root/'data/reports').glob('*.json'))]
    pages = {}
    index = ['# Read the reports', '', '[Library home](../README.md) · [Programs](programs.md) · [Diagram gallery](diagram-gallery.md)', '',
             'Original defensive summaries with award provenance, distinct event dates and verification limits. These historical disclosures do not authorize testing. Generated from canonical records; edit the JSON, then regenerate.', '']
    for rec in sorted(reports, key=lambda r: (r['organization'], r['title'])):
        rid = rec['id']; reward = rec['reward']
        index.append(f'- {link(rec["title"], "reports/"+rid+".md")} — {text(reward["currency"])} {reward["amount"]:,}; {text(reward["type"])}')
        lines = [f'# {text(rec["title"])}', '', '[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)', '',
                 f'**Organization:** {text(rec["organization"])}  ', f'**Product:** {text(rec["product"])}', '',
                 '## What the evidence establishes', '', 'Publication window: '+('within the preferred 12-month window' if rec['recency']['within_preferred_window'] is True else 'historical / outside the preferred window' if rec['recency']['within_preferred_window'] is False else 'uncertain original publication date')+'; reviewed as of '+text(rec['recency']['as_of'])+'.', '', text(rec['summary']), '', '### Root cause', '', text(rec['root_cause']), '',
                 '### Bounded impact', '', text(rec['impact']), '', '### Defensive lessons', '']
        lines += ['- '+text(t) for t in rec['defensive_takeaways']]
        lines += ['', '## Award and evidence', '', f'**{text(reward["currency"])} {reward["amount"]:,}** — {text(reward["type"])}; {text(reward["scope"])}; status: {text(reward["status"])}.', '',
                  f'Evidence level: {text(reward["evidence_level"])}. {text(reward["notes"] or "")}', '',
                  'Exact source quotation and location remain in the '+link('canonical record', '../../data/reports/'+rid+'.json')+'.', '', '## Dates', '']
        for name, date in rec['dates'].items():
            lines.append(f'- **{text(name.replace("_", " "))}:** {text(date["value"] or "Unknown")}; precision: {text(date["precision"] or "unknown")}; basis: {text(date["basis"])}'+ ('. '+text(date['note']) if date['note'] else ''))
        lines += ['', '## Verification limits', '', f'Reviewed: {text(rec["verification"]["reviewed_at"])}. {text(rec["verification"]["method"])}', '']
        lines += ['- '+text(v) for v in rec['verification']['limitations']]
        related = [d for d in diagrams if rid in d['linked_report_ids']]
        if related:
            lines += ['', '## Related conceptual diagrams', '']
            lines += ['- '+link(d['title'], '../diagram-gallery.md#'+d['id']) for d in related]
        lines += ['', '## Sources and attribution', '']
        lines += ['- '+link(s['title'], s['url'])+f' — {text(s["author"])}; retrieved {text(s["retrieved_at"])}.' for s in rec['sources']]
        lines += ['', 'Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).', '']
        pages['docs/reports/'+rid+'.md'] = '\n'.join(lines)
    pages['docs/reports.md'] = '\n'.join(index)+ '\n'
    gallery = ['# Diagram gallery', '', '[Library home](../README.md) · [Report index](reports.md) · [Visual learning guide](visual-theory.md)', '',
               'Original conceptual defensive models. Images are local, inert SVGs; no script, embeds, external dependencies or interactive links. These are not vendor architecture diagrams or operational sequences.', '']
    for d in diagrams:
        gallery += [f'<a id="{d["id"]}"></a>', f'## {text(d["title"])}', '', f'![{text(d["alt_text"])}](../{d["files"]["svg"]})', '', text(d['interpretation']), '', '**Related reports**', '']
        gallery += ['- '+link(next(r['title'] for r in reports if r['id']==rid), 'reports/'+rid+'.md') for rid in d['linked_report_ids']]
        gallery += ['', link('Canonical graph and provenance', '../data/diagrams/'+d['id']+'.json')+' · '+link('Mermaid source', '../'+d['files']['mermaid'])+' · '+link('DOT source', '../'+d['files']['graphviz']), '']
    gallery += ['Original diagrams: Security Research Library contributors, CC BY 4.0. [License scope](../LICENSE.md).', '']
    pages['docs/diagram-gallery.md'] = '\n'.join(gallery)
    return pages


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--check', action='store_true'); args = parser.parse_args()
    pages = build()
    for name, content in pages.items():
        path = ROOT/name
        if args.check:
            if not path.is_file() or path.read_text() != content: raise SystemExit('Missing or stale navigation: '+name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True); path.write_text(content)
    actual = {str(p.relative_to(ROOT)) for p in (ROOT/'docs/reports').glob('*.md')}
    expected = {name for name in pages if name.startswith('docs/reports/')}
    if actual != expected: raise SystemExit('Unexpected generated report pages; review stale files manually')
    print(f'{"Checked" if args.check else "Generated"} {len(pages)} static navigation pages (offline).')

if __name__ == '__main__': main()
