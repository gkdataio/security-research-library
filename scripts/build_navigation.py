#!/usr/bin/env python3
"""Build deterministic GitHub-readable Markdown pages from canonical records. Offline."""
import argparse
import json
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



def report_topic_page(reports, taxonomy):
    """Index validated report category memberships without creating new records."""
    ordered = sorted(reports, key=lambda r: (r['title'].casefold(), r['id']))
    categories = sorted(taxonomy['categories'], key=lambda c: (c['title'].casefold(), c['id']))
    groups = [(category, [rec for rec in ordered
                          if category['id'] == rec['category_id']
                          or category['id'] in rec['secondary_category_ids']])
              for category in categories]
    lines = ['# Award-backed reports by topic', '',
             '[Report index](reports.md) · [Library home](../README.md)', '',
             'Generated offline from canonical primary and secondary category IDs and the report taxonomy. These historical disclosures are separate from educational resources and grant no testing authorization.', '',
             f'{len(ordered)} distinct award-backed reports across {len(categories)} taxonomy categories. A report can appear under several categories; overlapping memberships do not increase the distinct report count. Category counts must not be added to count reports.', '',
             'Each entry labels its primary or secondary category membership. Categories and reports are ordered alphabetically by title, with stable IDs breaking ties. Empty taxonomy categories are shown explicitly. Regeneration does not reverify sources or advance review timestamps.', '',
             '## Browse topics', '']
    for category, records in groups:
        anchor = 'category-'+quote(category['id'], safe='')
        lines.append('- '+link(category['title'], '#'+anchor)+f' — {len(records)} distinct '+('report.' if len(records) == 1 else 'reports.'))
    for category, records in groups:
        anchor = 'category-'+quote(category['id'], safe='')
        lines += ['', f'<a id="{anchor}"></a>', '## '+text(category['title']), '',
                  f'{len(records)} distinct '+('report.' if len(records) == 1 else 'reports.'), '']
        lines += ['- '+link(rec['title'], 'reports/'+rec['id']+'.md')+' — '+text(rec['organization'])+
                  '; '+('primary' if rec['category_id'] == category['id'] else 'secondary')+' category.'
                  for rec in records] or ['No reports currently assigned to this category.']
    return '\n'.join(lines)+'\n'


def resource_topic_page(resources, taxonomy):
    """Group canonical memberships, retaining one distinct record count."""
    ordered = sorted(resources, key=lambda r: (r['title'].casefold(), r['id']))
    topics = sorted(taxonomy['topics'], key=lambda t: (t['title'].casefold(), t['id']))
    groups = [(topic, [rec for rec in ordered if topic['id'] in rec['topic_ids']])
              for topic in topics]
    lines = ['# Learning resources by topic', '',
             '[Alphabetical resource index](resource-index.md) · [Curated resource guide](resources.md) · [Library home](../README.md)', '',
             'Generated offline from canonical resource topic IDs and the resource taxonomy. These educational references are separate from award-backed reports and grant no testing authorization.', '',
             f'{len(ordered)} distinct resources across {len(topics)} taxonomy topics. A resource can appear under several topics; overlapping memberships do not increase the distinct resource count. Topic counts must not be added to count resources.', '',
             'Topics and resources are ordered alphabetically by title, with stable IDs breaking ties. Empty taxonomy topics are shown explicitly. Regeneration does not reverify sources or advance review timestamps.', '',
             '## Browse topics', '']
    for topic, records in groups:
        anchor = 'topic-'+quote(topic['id'], safe='')
        lines.append('- '+link(topic['title'], '#'+anchor)+f' — {len(records)} resources.')
    for topic, records in groups:
        anchor = 'topic-'+quote(topic['id'], safe='')
        lines += ['', f'<a id="{anchor}"></a>', '## '+text(topic['title']), '',
                  f'{len(records)} resources.', '']
        lines += ['- '+link(rec['title'], 'resources/'+rec['id']+'.md')+' — '+text(rec['publisher'])+'.'
                  for rec in records] or ['No resources currently assigned to this topic.']
    return '\n'.join(lines)+'\n'


def resource_pages(resources, diagrams, taxonomy, skills):
    """Render editorial summaries without fetching or copying linked materials."""
    types = {item['id']: item['title'] for item in taxonomy['resource_types']}
    topics = {item['id']: item['title'] for item in taxonomy['topics']}
    skill_titles = {item['id']: item['title'] for item in skills['skillsets']}
    ordered = sorted(resources, key=lambda r: (r['title'].casefold(), r['id']))
    index = ['# Read the learning resources', '',
             '[Library home](../README.md) · [Browse by topic](resource-topics.md) · [Curated resource guide](resources.md) · [Report index](reports.md) · [Diagram gallery](diagram-gallery.md)', '',
             'Original defensive summaries of official educational references. These resources are separate from award-backed reports and grant no testing authorization. Generated from canonical JSON; edit the records, then regenerate.', '',
             f'{len(ordered)} resources. Review timestamps describe recorded source reviews, not a fresh check performed by this offline build.', '']
    pages = {}
    for rec in ordered:
        rid = rec['id']
        canonical = '../../data/resources/'+rid+'.json'
        index += ['- '+link(rec['title'], 'resources/'+rid+'.md')+' — '+text(rec['publisher'])+'; '+text(types[rec['resource_type_id']])+'.']
        lines = ['# '+text(rec['title']), '',
                 '[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)', '',
                 link('Canonical JSON', canonical)+' · '+link('Official resource', rec['primary_url']), '',
                 '**Publisher:** '+text(rec['publisher'])+'  ',
                 '**Authors:** '+text('; '.join(rec['authors']) or 'Not identified in the reviewed record')+'  ',
                 '**Resource type:** '+text(types[rec['resource_type_id']])+'  ',
                 '**Version:** '+text(rec['version'] or 'Not established in the reviewed record')+'  ',
                 '**Topics:** '+text('; '.join(topics[t] for t in rec['topic_ids']))+'  ',
                 '**Defensive skills:** '+text('; '.join(skill_titles[t] for t in rec['skillset_ids'])), '',
                 '## Original summary', '', text(rec['summary']), '',
                 '## Defensive use', '', text(rec['defensive_use']), '',
                 'Educational reference only; linked material does not authorize testing unrelated systems.', '',
                 '## Prerequisites', '',
                 '**Basis:** '+text(rec['prerequisites_basis'].replace('_', ' '))+'.', '']
        lines += ['- '+text(v) for v in rec['prerequisites']] or ['No prerequisites recorded; this does not establish that none are needed.']
        lines += ['', '## Access and freshness', '',
                  '**Access cost at review:** '+text(rec['access']['cost'])+'.']
        if rec['access']['note']:
            lines += ['', text(rec['access']['note'])]
        freshness = rec['freshness']
        lines += ['', '**Reviewed:** '+text(freshness['reviewed_at'])+'  ',
                  '**Review status:** '+text(freshness['status'].replace('_', ' '))+'  ',
                  '**Living resource:** '+('Yes' if freshness['living_resource'] else 'No')+'.', '',
                  text(freshness['note']), '',
                  'Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.', '',
                  '## Dates and provenance', '']
        sources = {source['id']: source for source in rec['sources']}
        for name in ('published', 'version_released', 'source_displayed'):
            date = rec['dates'][name]
            source = sources.get(date['source_id'])
            provenance = (link(source['title'], source['url'])+' (source ID: '+text(source['id'])+')') if source else 'Not recorded'
            lines += ['- **'+text(name.replace('_', ' '))+':** '+text(date['value'] or 'Unknown')+
                      '; precision: '+text(date['precision'] or 'unknown')+'; basis: '+text(date['basis'].replace('_', ' '))+
                      '; source: '+provenance+'.'+(' '+text(date['note']) if date['note'] else '')]
        lines += ['', '## Caveats', '']
        lines += ['- '+text(v) for v in rec['caveats']] or ['No additional caveats recorded; this is not a completeness or security guarantee.']
        related = sorted((d for d in diagrams if rid in d['linked_resource_ids']), key=lambda d: d['id'])
        if related:
            lines += ['', '## Related conceptual diagrams', '']
            lines += ['- '+link(d['title'], '../diagram-gallery.md#'+d['id']) for d in related]
        lines += ['', '## Sources and attribution', '']
        for source in rec['sources']:
            lines += ['- '+link(source['title'], source['url'])+' — '+text(source['publisher'])+
                      '; source ID: '+text(source['id'])+'; provenance: '+text(source['provenance'].replace('_', ' '))+
                      '; retrieved '+text(source['retrieved_at'])+'; supports: '+text(', '.join(source['supports']))+'.']
        lines += ['', 'Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).', '']
        pages['docs/resources/'+rid+'.md'] = '\n'.join(lines)
    pages['docs/resource-index.md'] = '\n'.join(index)+'\n'
    pages['docs/resource-topics.md'] = resource_topic_page(resources, taxonomy)
    return pages


def check_generated_page_sets(root, pages):
    """Reject obsolete generated pages without deleting potentially edited files."""
    for collection in ('reports', 'resources'):
        directory = 'docs/'+collection+'/'
        actual = {str(p.relative_to(root)) for p in (root/directory).glob('*.md')}
        expected = {name for name in pages if name.startswith(directory)}
        if actual != expected:
            raise SystemExit('Unexpected generated '+collection+' pages; review stale files manually')


def build(root=ROOT):
    resources, diagrams, taxonomy = validate_all(root)
    reports = [json.loads(p.read_text()) for p in sorted((root/'data/reports').glob('*.json'))]
    skills = json.loads((root/'data/taxonomy.json').read_text())
    pages = resource_pages(resources, diagrams, taxonomy, skills)
    index = ['# Read the reports', '', '[Library home](../README.md) · [Browse by topic](report-topics.md) · [Programs](programs.md) · [Diagram gallery](diagram-gallery.md)', '',
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
    pages['docs/report-topics.md'] = report_topic_page(reports, skills)
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
    check_generated_page_sets(ROOT, pages)
    print(f'{"Checked" if args.check else "Generated"} {len(pages)} static navigation pages (offline).')

if __name__ == '__main__': main()
