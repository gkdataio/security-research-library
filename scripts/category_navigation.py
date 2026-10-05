"""Pure, offline category navigation. No new research classifications or records."""
import json
from validate import Invalid, check_schema
from vulnerability_navigation import family_navigation, load_config, publication_guidance


def validate_config(config, schema, taxonomy, resource_taxonomy):
    check_schema(config, schema, schema)
    ids = [c['id'] for c in config['categories']]
    if len(set(ids)) != len(ids):
        raise Invalid('duplicate navigation category')
    if set(ids) != {c['id'] for c in taxonomy['categories']}:
        raise Invalid('navigation must cover exactly the report taxonomy')
    topics = {t['id'] for t in resource_taxonomy['topics']}
    for category in config['categories']:
        if not set(category['resource_topic_ids']) <= topics:
            raise Invalid('unknown navigation resource topic')


def count_label(count, singular):
    return f'{count} {singular}' + ('s' if count != 1 else '')


def collection_counts(reports, learning, diagrams):
    return ' · '.join((count_label(len(reports), 'report'),
                        count_label(len(learning), 'related resource'),
                        count_label(len(diagrams), 'diagram')))


def ordered(records):
    return sorted(records, key=lambda r: (r['title'].casefold(), r['id']))


def memberships(category, reports, resources, diagrams):
    """One-hop relationships only; learning links never classify a report."""
    cid = category['id']
    matched = ordered(r for r in reports
                      if cid in [r['category_id'], *r['secondary_category_ids']])
    report_ids = {r['id'] for r in matched}
    related_diagrams = ordered(d for d in diagrams
                              if report_ids.intersection(d['linked_report_ids']))
    learning = []
    for resource in ordered(resources):
        topics = sorted(set(resource['topic_ids']) & set(category['resource_topic_ids']))
        diagram_ids = [d['id'] for d in related_diagrams
                       if resource['id'] in d['linked_resource_ids']]
        if topics or diagram_ids:
            learning.append((resource, topics, diagram_ids))
    return matched, learning, related_diagrams


def category_pages(root, reports, resources, diagrams, taxonomy, resource_taxonomy,
                   text, link):
    config = json.loads((root/'data/category-navigation.json').read_text())
    schema = json.loads((root/'schema/category-navigation.schema.json').read_text())
    validate_config(config, schema, taxonomy, resource_taxonomy)
    vulnerability_config = load_config(root, reports, resources)
    titles = {c['id']: c for c in taxonomy['categories']}
    topics = {t['id']: t['title'] for t in resource_taxonomy['topics']}
    diagram_titles = {d['id']: d['title'] for d in diagrams}
    categories = sorted(config['categories'], key=lambda c: (titles[c['id']]['title'].casefold(), c['id']))
    hub = ['# Browse by vulnerability type', '',
           '[Library home](../README.md) · [All reports](reports.md) · [All learning resources](resource-index.md) · [Diagram gallery](diagram-gallery.md)', '',
           'Choose a vulnerability family or a specific type below. XSS and its stored, reflected and blind subtypes, SSRF and SSTI are nested directly under their navigation families. Broader security themes are listed separately.', '',
           f'**{len(reports)} distinct reports · {len(resources)} learning resources · {len(diagrams)} conceptual diagrams** in the library.', '',
           'Family pages bring together reports, related learning and conceptual diagrams. Specific-type pages keep award-backed reports, educational case studies and learning references separate, with publication-year groups and explicit gaps.', '',
           'On this page: [Vulnerability families and specific types](#vulnerability-families) · [Security themes](#security-themes) · [Publication groups and coverage](#publication-and-coverage) · [General foundations](#general-foundations)', '']
    pages = {}
    for kind, heading in [('vulnerability_family', 'Vulnerability families'), ('security_theme', 'Security themes and environments')]:
        anchor = 'vulnerability-families' if kind == 'vulnerability_family' else 'security-themes'
        hub += ['', '<a id="'+anchor+'"></a>', '## '+heading, '']
        if kind == 'security_theme':
            hub += ['These describe environments or trust boundaries, rather than specific vulnerability types.', '']
        for category in (c for c in categories if c['kind'] == kind):
            cid = category['id']
            title = titles[cid]['title']
            matched, learning, related = memberships(category, reports, resources, diagrams)
            counts = collection_counts(matched, learning, related)
            hub += ['- **'+link(title, 'categories/'+cid+'.md')+'** — '+counts,
                    '  '+text(titles[cid]['description'])+'.']
            hub += family_navigation(vulnerability_config, cid, reports, resources, link, indent=2)
            lines = ['# '+text(title), '',
                     '[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)', '',
                     '**'+('Security theme / environment' if kind == 'security_theme' else 'Vulnerability family')+'** · '+counts, '',
                     text(titles[cid]['description'])+'.', '',
                     'Report membership uses the existing primary or secondary category '+text(cid)+'. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.', '']
            specific_types = family_navigation(vulnerability_config, cid, reports, resources, link,
                                               prefix='../vulnerabilities/')
            if specific_types:
                lines += ['## Specific vulnerability types', '',
                          'These narrower pages use separate source-backed memberships and publication-year groups. Their placement here is navigation, not an additional classification of every record in this family.', '',
                          *specific_types, '']
            lines += ['On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)', '',
                     '<a id="reports"></a>', '## Reports', '']
            for report in matched:
                role = 'primary' if report['category_id'] == cid else 'secondary'
                lines += ['- '+link(report['title'], '../reports/'+report['id']+'.md')+' — '+text(report['organization'])+'; '+role+' category.']
            if not matched:
                lines += ['No reports currently assigned to this category.']
            lines += ['', '<a id="related-learning"></a>', '## Related learning', '',
                      'Included by the topic crosswalk or an explicit resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.', '']
            for resource, topic_ids, diagram_ids in learning:
                basis = []
                if topic_ids:
                    basis += ['topic: '+', '.join(text(topics[t]) for t in topic_ids)]
                if diagram_ids:
                    basis += ['diagram: '+', '.join(link(diagram_titles[d], '../diagram-gallery.md#'+d) for d in diagram_ids)]
                lines += ['- '+link(resource['title'], '../resources/'+resource['id']+'.md')+' — '+'; '.join(basis)+'.']
            if not learning:
                lines += ['No related learning currently linked. [Browse all resources](../resource-index.md).']
            lines += ['', '<a id="conceptual-diagrams"></a>', '## Conceptual diagrams', '',
                      'Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.', '']
            for diagram in related:
                lines += ['- '+link(diagram['title'], '../diagram-gallery.md#'+diagram['id'])]
            if not related:
                lines += ['No conceptual diagrams currently linked.']
            lines += ['', '---', '',
                      'Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).', '']
            pages['docs/categories/'+cid+'.md'] = '\n'.join(lines)
    hub += ['', *publication_guidance(vulnerability_config)]
    hub += ['', '<a id="general-foundations"></a>', '## General foundations and research practice', '',
            'These learning topics span multiple vulnerability families:', '',
            '- [Web foundations](resource-topics.md#topic-web-foundations)',
            '- [Verification](resource-topics.md#topic-verification)',
            '- [Reporting](resource-topics.md#topic-reporting)', '',
            '[All resource topics](resource-topics.md) · [Original report topic index](report-topics.md)', '',
            'Generated offline; rebuilding does not reverify sources or change canonical records. [Family relationships](category-navigation.md) · [Specific-type evidence and dates](vulnerability-navigation.md).', '']
    pages['docs/vulnerability-types.md'] = '\n'.join(hub)
    return pages
