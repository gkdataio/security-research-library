# Stored XSS

[2025–2026 category index](../vulnerability-reports-2025-2026.md) · [Broad vulnerability families](../vulnerability-types.md) · [Library home](../../README.md)

**1 award-backed report · 2 educational case studies · 0 learning references**

Cross-site scripting where a source establishes that persisted content or state later reaches a browser execution context\. Persistence alone is insufficient evidence of XSS\.

Search aliases: sxss.

Parent: [Cross-site scripting \(XSS\)](<xss.md>). Parent membership never assigns a subtype.

Publication groups use original selected-source publication dates, retaining their recorded precision and uncertainty. Learning relevance is editorial, not evidence that a vulnerability remains present. Review dates, CVE years and later page updates are not publication dates. [Date and classification rules](../vulnerability-navigation.md).

On this page: [Award-backed reports](#award-reports) · [Educational case studies](#case-studies) · [Learning references](#learning)

<a id="award-reports"></a>
## Award-backed reports

### 2026 publications

No mapped records with an established publication date in this year.

### 2025 publications

No mapped records with an established publication date in this year.

### Unknown original publication date

- **[Meta Conversions API Gateway mixed configuration data with executable output](<../reports/meta-conversions-gateway-generated-script-boundary-2025.md>)**
  bug bounty; publication: Unknown original publication date; precision: unknown; basis: not reported.
  Date qualification: Current page header is January 13, 2026; a separately indexed 2025 URL also exists\. Original publication versus archive migration or republication is not established\.
  Classification: Stored XSS (source explicit). The source identifies stored XSS where persisted configuration becomes generated JavaScript consumed by browsers\.
  Evidence: [Multiple XSS in Meta Conversion API Gateway Leading to Zero-Click Account Takeover](<https://ysamm.com/uncategorized/2026/01/13/capig-xss.html>); location: Bug \#2 backend finding.
  2025–2026 learning relevance (editorial): Preserve context-safe serialization when configuration is later emitted as executable browser content; the archive header does not establish a 2026 publication\.

<a id="case-studies"></a>
## Related educational case studies

Maintainer advisories and researcher publications remain educational resources; they do not establish a qualifying individual award.

### 2026 publications

- **[Next\.js: response metadata must preserve representation boundaries](<../resources/nextjs-2026-response-metadata-representation-boundary.md>)**
  Research Paper; publication: 2026-06; precision: month; basis: explicit.
  Publication evidence: [Re:CACHE: Next\.js response-reflection research](<https://zhero-web-sec.github.io/research-and-things/re-cache-excessive-reflection-type-confusion-and-0-click-sxss-on-nextjs>).
  Date qualification: The article displays June 2026; no publication day is established\.
  Classification: Stored XSS (source explicit). The researcher identifies cache-mediated stored XSS and distinguishes it from classic reflected XSS\.
  Evidence: [Re:CACHE: Next\.js response-reflection research](<https://zhero-web-sec.github.io/research-and-things/re-cache-excessive-reflection-type-confusion-and-0-click-sxss-on-nextjs>); location: Override, mutation and \(S\)XSS section.
  2025–2026 learning relevance (editorial): Review response meaning and shared-cache persistence together while retaining the source's configuration-specific limits\.

- **[Parse Server: preserve safe file interpretation across storage and browsers](<../resources/parse-server-2026-upload-metadata-consumer-boundary.md>)**
  Maintainer Advisory; publication: 2026-06-25; precision: day; basis: explicit.
  Publication evidence: [Stored XSS via malformed Content-Type bypassing file upload extension blocklist](<https://github.com/parse-community/parse-server/security/advisories/GHSA-r899-h629-j84r>).
  Date qualification: Maintainer advisory publication\.
  Classification: Stored XSS (source explicit). The maintainer explicitly identifies stored XSS across uploaded-object metadata, storage and browser interpretation\.
  Evidence: [Stored XSS via malformed Content-Type bypassing file upload extension blocklist](<https://github.com/parse-community/parse-server/security/advisories/GHSA-r899-h629-j84r>); location: Advisory title and Impact.
  2025–2026 learning relevance (editorial): Keep upload acceptance and delivery interpretation in one security contract, with the affected storage configuration and user-interaction requirements preserved\.

### 2025 publications

No mapped records with an established publication date in this year.

<a id="learning"></a>
## Related learning references

General guidance is kept separate from individual disclosures and is not counted as a case study.

No related learning references currently mapped from reviewed evidence. This is a collection gap, not evidence that this vulnerability type does not occur.

---

Generated offline from [evidence-backed navigation metadata](<../../data/vulnerability-navigation.json>) and unchanged canonical records. [Schema](<../../schema/vulnerability-navigation.schema.json>) · [Maintenance and limitations](../vulnerability-navigation.md). No target requests, tests or exploit instructions.
