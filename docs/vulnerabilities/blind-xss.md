# Blind XSS

[2025–2026 category index](../vulnerability-reports-2025-2026.md) · [Broad vulnerability families](../vulnerability-types.md) · [Library home](../../README.md)

**0 award-backed reports · 1 educational case study · 0 learning references**

Cross-site scripting whose execution occurs in a separate or not directly observable application context, established by source evidence\. Blind describes observation context and is not a synonym for stored; both labels may apply only with independent support\.

Search aliases: bxss.

Parent: [Cross-site scripting \(XSS\)](<xss.md>). Parent membership never assigns a subtype.

Publication groups use original selected-source publication dates, retaining their recorded precision and uncertainty. Learning relevance is editorial, not evidence that a vulnerability remains present. Review dates, CVE years and later page updates are not publication dates. [Date and classification rules](../vulnerability-navigation.md).

On this page: [Award-backed reports](#award-reports) · [Educational case studies](#case-studies) · [Learning references](#learning)

<a id="award-reports"></a>
## Award-backed reports

No award-backed reports currently mapped from reviewed evidence. This is a collection gap, not evidence that this vulnerability type does not occur.

<a id="case-studies"></a>
## Related educational case studies

Maintainer advisories and researcher publications remain educational resources; they do not establish a qualifying individual award.

### 2026 publications

- **[CI4MS: keep stored diagnostic content inert in administrative log views](<../resources/ci4ms-2026-log-viewer-stored-blind-xss-boundary.md>)**
  Maintainer Advisory; publication: 2026-03-31; precision: day; basis: explicit.
  Publication evidence: [CI4MS log-viewer security advisory GHSA-r4v5-rwr2-q7r4](<https://github.com/ci4-cms-erp/ci4ms/security/advisories/GHSA-r4v5-rwr2-q7r4>).
  Date qualification: Original maintainer-advisory publication; later database events are separate\.
  Classification: Blind XSS (source explicit). Both sources explicitly identify blind XSS; the database describes execution in a later administrative view rather than immediate observation by the contributor of logged data\.
  Evidence: [CI4MS log-viewer security advisory GHSA-r4v5-rwr2-q7r4](<https://github.com/ci4-cms-erp/ci4ms/security/advisories/GHSA-r4v5-rwr2-q7r4>), [GitHub Advisory Database entry for CVE-2026-34560](<https://github.com/advisories/GHSA-r4v5-rwr2-q7r4>); location: Maintainer Description; Advisory Database Summary and Description.
  2025–2026 learning relevance (editorial): Treat diagnostic displays as browser trust boundaries, even when input and execution occur in separate contexts\. Preserve the required administrator view and the conflicting interaction metric\.

### 2025 publications

No mapped records with an established publication date in this year.

<a id="learning"></a>
## Related learning references

General guidance is kept separate from individual disclosures and is not counted as a case study.

No related learning references currently mapped from reviewed evidence. This is a collection gap, not evidence that this vulnerability type does not occur.

---

Generated offline from [evidence-backed navigation metadata](<../../data/vulnerability-navigation.json>) and unchanged canonical records. [Schema](<../../schema/vulnerability-navigation.schema.json>) · [Maintenance and limitations](../vulnerability-navigation.md). No target requests, tests or exploit instructions.
