"""Deterministic, offline browsing of existing publication and learning metadata."""
from urllib.parse import quote


def anchor(prefix, value):
    return prefix+'-'+quote(str(value), safe='')


def ordered(records):
    return sorted(records, key=lambda record: (record['title'].casefold(), record['id']))


def resource_type_page(resources, taxonomy, text, link):
    types = sorted(taxonomy['resource_types'], key=lambda item: (item['title'].casefold(), item['id']))
    lines = ['# Learning resources by type', '',
             '[Resource index](resource-index.md) · [Topics](resource-topics.md) · [Defensive skills](skillsets.md) · [Publication years](publication-years.md) · [Library home](../README.md)', '',
             f'{len(resources)} distinct educational resources across {len(types)} publication types. Each resource has exactly one canonical type; empty types remain visible.', '',
             'Types describe the primary publication, not its supporting sources, quality, current applicability or award eligibility. Maintainer advisories remain separate from researcher articles; controlled training remains a learning format. Regeneration does not reverify sources.', '',
             '## Browse types', '']
    for item in types:
        group = [record for record in ordered(resources) if record['resource_type_id'] == item['id']]
        lines.append('- '+link(item['title'], '#'+anchor('type', item['id']))+f' — {len(group)} resources.')
    for item in types:
        group = [record for record in ordered(resources) if record['resource_type_id'] == item['id']]
        lines += ['', '<a id="'+anchor('type', item['id'])+'"></a>', '## '+text(item['title']), '', f'{len(group)} resources.', '']
        lines += ['- '+link(record['title'], 'resources/'+record['id']+'.md')+' — '+text(record['publisher'])+'.'
                  for record in group] or ['No resources currently assigned to this type.']
    return '\n'.join(lines)+'\n'


def skillset_page(reports, resources, taxonomy, text, link):
    skills = sorted(taxonomy['skillsets'], key=lambda item: (item['title'].casefold(), item['id']))
    lines = ['# Browse by defensive skill', '',
             '[Reports](reports.md) · [Learning resources](resource-index.md) · [Resource types](resource-types.md) · [Publication years](publication-years.md) · [Library home](../README.md)', '',
             f'{len(reports)} distinct award-backed reports and {len(resources)} distinct educational resources across {len(skills)} defensive skills. A record can appear under several skills; overlapping memberships must not be added to count records.', '',
             'Skills are editorial learning objectives from the existing taxonomy, not certifications, new vulnerability classifications or permission to test. Reports and learning references remain separate. Empty skill groups remain visible; regeneration preserves review timestamps.', '',
             '## Browse skills', '']
    for skill in skills:
        rg = [r for r in reports if skill['id'] in r['skillset_ids']]
        eg = [r for r in resources if skill['id'] in r['skillset_ids']]
        lines.append('- '+link(skill['title'], '#'+anchor('skill', skill['id']))+f' — {len(rg)} reports; {len(eg)} resources.')
    for skill in skills:
        lines += ['', '<a id="'+anchor('skill', skill['id'])+'"></a>', '## '+text(skill['title']), '', text(skill['defensive_objective'])+'.']
        for label, collection, records in [('Award-backed reports', 'reports', reports), ('Educational resources', 'resources', resources)]:
            group = [r for r in ordered(records) if skill['id'] in r['skillset_ids']]
            lines += ['', '### '+label, '', f'{len(group)} records.', '']
            lines += ['- '+link(record['title'], collection+'/'+record['id']+'.md') for record in group] or ['No records currently assigned.']
    return '\n'.join(lines)+'\n'


def publication_year(record):
    """Use only the original publication field; never invent a fallback date."""
    value = record['dates']['published']['value']
    return value[:4] if value else None


def publication_year_page(reports, resources, text, link):
    years = sorted({publication_year(record) for record in [*reports, *resources]} - {None}, reverse=True)
    groups = [*years, None]
    lines = ['# Reports and resources by publication year', '',
             '[Reports](reports.md) · [Learning resources](resource-index.md) · [Resource types](resource-types.md) · [Defensive skills](skillsets.md) · [Library home](../README.md)', '',
             f'{len(reports)} award-backed reports and {len(resources)} educational resources, each listed once in its own collection. This general index covers every recorded publication year, with unknown original publication dates retained explicitly.', '',
             'Grouping uses only dates.published. A year or month precision remains partial; a source-displayed revision, software release, award date or review timestamp never fills a missing publication date. Living resources can therefore appear under Unknown even when a revision date is known. The date basis stays visible, and the linked record retains source evidence and qualifications.', '',
             'Years run newest first; records within each collection are alphabetical by title, with stable IDs breaking ties. Regeneration does not establish source currency or change the separate preferred-window assessment on award reports.', '',
             '## Browse years', '']
    for year in groups:
        rg = [r for r in reports if publication_year(r) == year]
        eg = [r for r in resources if publication_year(r) == year]
        lines.append('- '+link(year or 'Unknown original publication date', '#year-'+(year or 'unknown'))+f' — {len(rg)} reports; {len(eg)} resources.')
    for year in groups:
        lines += ['', '<a id="year-'+(year or 'unknown')+'"></a>', '## '+(year or 'Unknown original publication date')]
        for label, collection, records in [('Award-backed reports', 'reports', reports), ('Educational resources', 'resources', resources)]:
            group = [r for r in ordered(records) if publication_year(r) == year]
            lines += ['', '### '+label, '', f'{len(group)} records.', '']
            for record in group:
                date = record['dates']['published']
                lines.append('- '+link(record['title'], collection+'/'+record['id']+'.md')+' — publication: '+text(date['value'] or 'Unknown')+
                             '; precision: '+text(date['precision'] or 'unknown')+'; basis: '+text(date['basis'].replace('_', ' '))+'.')
            if not group:
                lines.append('No records with this original publication year.')
    return '\n'.join(lines)+'\n'


def learning_pages(reports, resources, taxonomy, resource_taxonomy, text, link):
    return {
        'docs/resource-types.md': resource_type_page(resources, resource_taxonomy, text, link),
        'docs/skillsets.md': skillset_page(reports, resources, taxonomy, text, link),
        'docs/publication-years.md': publication_year_page(reports, resources, text, link),
    }
