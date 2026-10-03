# Category navigation maintenance

[Browse by vulnerability type](vulnerability-types.md) · [Library home](../README.md)

The category browser is a static, offline view of existing records. It changes no report IDs, source URLs, category memberships, review dates, resource topics or diagram evidence.

## Relationship rules

- Every category in `data/taxonomy.json` has exactly one entry in `data/category-navigation.json`, validated against `schema/category-navigation.schema.json`.
- `kind` separates vulnerability families from security themes and environments. Category names and descriptions come from the existing taxonomy; this browser adds no CWE or narrower vulnerability classification.
- A report belongs when its primary or secondary category ID matches. Its role is labeled. Resources never create report membership.
- A diagram belongs only when its existing `linked_report_ids` includes a report in the category. The browser does not traverse relationships recursively.
- Related learning is the union of resources whose topic matches the explicit crosswalk and resources explicitly linked by those diagrams. Each resource appears once per page, with all matching topic and diagram relationships shown.
- A related resource is educational context, not an awarded finding or proof that it addresses every report. Unmapped topics remain accessible through the full resource index and topic browser.
- Counts are distinct within each collection and page. Membership can overlap across pages, so category counts must not be summed. The hub's library totals count each canonical record once.

Groups and entries sort by case-folded title, then stable ID. IDs determine filenames and links; display-title edits do not change routes. Empty groups and missing related material are explicit.

## Regenerate and check

Run from the repository root with Python 3.10+:

```sh
python3 scripts/build_navigation.py
python3 scripts/build_navigation.py --check
python3 -m unittest discover -s tests -p 'test_category_navigation.py' -v
```

The existing builder also preserves the report/resource topic pages and their anchors. Its check rejects missing, stale and unexpected category pages without deleting files. Edit the crosswalk rather than generated Markdown. When the report taxonomy grows, add an explicit navigation entry and review its kind and related-learning mappings.

Regeneration performs no network access, source re-review, target discovery or testing. Follow the [evidence and maintenance policy](../DATA_POLICY.md) for research changes.
