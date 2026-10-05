# Reflected XSS \(RXSS\)

[2025–2026 category index](../vulnerability-reports-2025-2026.md) · [Broad vulnerability families](../vulnerability-types.md) · [Library home](../../README.md)

**0 award-backed reports · 2 educational case studies · 0 learning references**

Cross-site scripting explicitly tied to untrusted request input in the resulting response\. The presence of a reflected value alone does not establish this subtype\.

Search aliases: rxss.

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

- **[Svelte hydration: serialization must preserve the enclosing output context](<../resources/svelte-2026-hydration-output-context-boundary.md>)**
  Research Paper; publication: 2026-03-17; precision: day; basis: explicit.
  Publication evidence: [CVE-2025-15265: Svelte Hydratable Key SSR XSS - Lydian](<https://caverav.cl/posts/svelte-hydratable-xss/svelte-hydratable-xss/>).
  Date qualification: Article displays this publication date; advisory disclosure is a separate event\.
  Classification: Reflected XSS \(RXSS\) (source explicit). The researcher advisory explicitly labels reflected XSS involving user-influenced hydration keys and HTML output context\.
  Evidence: [Svelte 5\.46\.0 - Hydratable Key Script-Breakout XSS \(SSR\)](<https://fluidattacks.com/advisories/lydian>); location: Summary: Vulnerability name and Vulnerability type.
  2025–2026 learning relevance (editorial): Use the article's March publication date separately from the January advisory event, and preserve a consistent encoding contract across keys and values\.

- **[TanStack Start: preserve server-owned response authority through errors](<../resources/tanstack-2026-server-function-response-authority.md>)**
  Maintainer Advisory; publication: 2026-09-30; precision: day; basis: explicit.
  Publication evidence: [Unauthenticated reflected XSS in TanStack Start server-function responses](<https://github.com/TanStack/router/security/advisories/GHSA-qx66-fv34-fjm8>).
  Date qualification: GitHub explicitly labels this as the advisory publication date\.
  Classification: Reflected XSS \(RXSS\) (source explicit). The maintainer explicitly describes reflected same-origin XSS when untrusted request data acquires response authority\.
  Evidence: [Unauthenticated reflected XSS in TanStack Start server-function responses](<https://github.com/TanStack/router/security/advisories/GHSA-qx66-fv34-fjm8>); location: Advisory title and Impact.
  2025–2026 learning relevance (editorial): Preserve server-owned response state through failure handling and verify deployment remediation separately from local dependency changes\.

### 2025 publications

No mapped records with an established publication date in this year.

<a id="learning"></a>
## Related learning references

General guidance is kept separate from individual disclosures and is not counted as a case study.

No related learning references currently mapped from reviewed evidence. This is a collection gap, not evidence that this vulnerability type does not occur.

---

Generated offline from [evidence-backed navigation metadata](<../../data/vulnerability-navigation.json>) and unchanged canonical records. [Schema](<../../schema/vulnerability-navigation.schema.json>) · [Maintenance and limitations](../vulnerability-navigation.md). No target requests, tests or exploit instructions.
