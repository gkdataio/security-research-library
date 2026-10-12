# Learning navigation maintenance

[Resource topics](resource-topics.md) · [Resource types](resource-types.md) · [Defensive skills](skillsets.md) · [Publication years](publication-years.md) · [Library home](../README.md)

The offline navigation builder derives these views from canonical metadata. Pages are alternate entry points, not additional research records. Regeneration does not fetch sources, execute training software, advance review times or establish current applicability.

## Learning-topic boundaries

- `ctf-and-practice` identifies provider-designated training and controlled exercises. `training-lab` remains the publication type. This lane is separate from report vulnerability categories and monetary competition disclosures.
- `api-security` covers request, operation, resource and field authority; interface composition; and transport or lifecycle continuity. It is not applied automatically to every authorization or OAuth resource.
- `browser-security` requires a browser, document, origin, permission, session or browser-consumer boundary. A web product name alone is insufficient.
- `server-client-frameworks` covers framework routing, server rendering and hydration, server functions/actions, component state and server/browser contracts. General backend libraries and every server-side advisory do not automatically belong.

Tags are editorial discovery aids supported by each record's reviewed subject matter. Add tags precisely and preserve existing IDs, primary URLs, publication types, source attribution, dates and review timestamps unless those facts are substantively re-reviewed. Existing broad topics remain available.

## Generated browse views

- Resource types use exactly one `resource_type_id` per educational record. All defined types, including empty types, are visible.
- Defensive skills use canonical `skillset_ids`, with reports and resources shown separately. Membership can overlap; never sum skill counts to obtain collection totals.
- Publication years use only `dates.published.value`. Partial year/month precision and date basis remain visible. Unknown original dates stay unknown even when a living resource has a source-displayed revision or a known review date. Do not substitute award, software-release or retrieval dates.
- Titles sort case-insensitively, with stable IDs resolving ties. Publication years sort newest first, followed by Unknown. Generated links use stable ID anchors.

The general publication index includes every report and resource. It does not replace the award collection's separately maintained preferred-window assessment or the narrower vulnerability-type views.

## Regenerate and verify

Edit canonical records and taxonomy rather than generated pages. Run the repository's complete offline checks from the README; the focused navigation checks are:

```sh
python3 scripts/build_navigation.py
python3 scripts/build_navigation.py --check
python3 -m unittest discover -s tests -p 'test_learning_navigation.py' -v
python3 -m unittest discover -s tests -p 'test_category_navigation.py' -v
```

Tests check exact memberships, complete coverage, no duplicate records within a group, partial/unknown dates, deterministic output, unchanged input records, and Markdown/HTML escaping. [Family crosswalk rules](category-navigation.md) govern explicit related-learning selections; those selections do not reclassify reports or resources.
