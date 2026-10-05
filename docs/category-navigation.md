# Category navigation maintenance

[Browse by vulnerability type](vulnerability-types.md) · [Library home](../README.md)

The main vulnerability-type hub is a static, offline view of existing records. It combines broad families, nested source-backed types and separately labeled security themes in one place. It changes no report IDs, source URLs, category memberships, review dates, resource topics or diagram evidence.

## Relationship rules

- Every category in `data/taxonomy.json` has exactly one entry in `data/category-navigation.json`, validated against `schema/category-navigation.schema.json`.
- `kind` separates vulnerability families from security themes and environments. Category names and descriptions come from the existing taxonomy; this browser adds no CWE or narrower vulnerability classification.
- Specific types are placed under a family using `family_id` in `data/vulnerability-navigation.json`; `parent_id` nests subtypes within it. XSS and SSTI appear under Injection, and SSRF under Server-side request trust. This is display placement only. The [specific-type rules](vulnerability-navigation.md) require independent evidence for record memberships; broad-family membership never assigns a subtype.
- A report belongs when its primary or secondary category ID matches. Its role is labeled. Resources never create report membership.
- A diagram belongs only when its existing `linked_report_ids` includes a report in the category. The browser does not traverse relationships recursively.
- Related learning is the union of resources whose topic matches the explicit crosswalk and resources explicitly linked by those diagrams. Each resource appears once per page, with all matching topic and diagram relationships shown.
- A related resource is educational context, not an awarded finding or proof that it addresses every report. Unmapped topics remain accessible through the full resource index and topic browser.
- Counts are distinct within each collection and page. Membership can overlap across pages, so category counts must not be summed. The hub's library totals count each canonical record once.

Groups and sibling entries sort by case-folded title, then stable ID; parents precede their nested subtypes. IDs determine filenames and links; display-title edits do not change routes. Empty groups and missing related material are explicit. Specific-type counts separate award reports, educational case studies and learning references across all publication years. Year groups and date uncertainty remain on the individual type pages.

## Regenerate and check

Run from the repository root with Python 3.10+:

```sh
python3 scripts/build_navigation.py
python3 scripts/build_navigation.py --check
python3 -m unittest discover -s tests -p 'test_category_navigation.py' -v
```

The existing builder produces the main hub, broad-family pages and individual type pages, and preserves the report/resource topic pages and their anchors. Its check rejects missing, stale and unexpected category pages without deleting files. Edit the crosswalk and generator rather than generated Markdown. When the report taxonomy grows, add an explicit navigation entry and review its kind and related-learning mappings.

Regeneration performs no network access, source re-review, target discovery or testing. Follow the [evidence and maintenance policy](../DATA_POLICY.md) for research changes.
