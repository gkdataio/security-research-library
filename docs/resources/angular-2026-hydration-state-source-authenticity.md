# Angular hydration: verify the source of restored state

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/angular-2026-hydration-state-source-authenticity.json>) · [Official resource](<https://github.com/angular/angular/security/advisories/GHSA-rgjc-h3x7-9mwg>)

**Publisher:** Angular maintainers  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations  
**Defensive skills:** Review input trust boundaries; Review artifact isolation; Verify remediation evidence

## Original summary

CVE-2026-54267 concerns hydrated server state accepting an unintended document source\. Applicability requires SSR with hydration and untrusted influence over document identifiers\. Maintainers describe response-cache integrity loss; XSS depends on unsafe downstream rendering\. Editorial root cause: parseable data was treated as authoritative without sufficiently constraining its source\.

## Defensive use

Editorial lesson: source authenticity and data validity are separate requirements when restoring state across a server/browser boundary\. Cached content should retain its trust classification through later consumers\. The linked patch restricts restoration to the expected container type\. Review that source-selection invariant separately from safe rendering, and distinguish reading a patch from verifying its effectiveness in a deployment\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Server rendering, client hydration and response-cache concepts
- The distinction between data parsing, source trust and browser rendering

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory, patch discussion and advisory-database chronology\.

**Reviewed:** 2026-10-06T03:41:33Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Read the advisory, linked pull request and database chronology\. No reproduction, target testing or independent patch verification performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-10; precision: day; basis: explicit; source: [Angular Client Hydration DOM Clobbering &amp; Response-Cache Poisoning](<https://github.com/angular/angular/security/advisories/GHSA-rgjc-h3x7-9mwg>) (source ID: advisory). Original maintainer-advisory publication\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition date established\.
- **source displayed:** 2026-06-10; precision: day; basis: explicit; source: [Angular Client Hydration DOM Clobbering &amp; Response-Cache Poisoning](<https://github.com/angular/angular/security/advisories/GHSA-rgjc-h3x7-9mwg>) (source ID: advisory). Displayed primary publication date; database events remain separate\.

## Caveats

- For @angular/core, the advisory lists affected ranges &gt;= 22\.0\.0-next\.0 &lt; 22\.0\.1, &gt;= 21\.0\.0-next\.0 &lt; 21\.2\.17, &gt;= 20\.0\.0-next\.0 &lt; 20\.3\.25, and &lt;= 19\.2\.25\. Listed fixes are 22\.0\.1, 21\.2\.17 and 20\.3\.25; the older range has no listed patch\.
- Potential consequences are maintainer claims; reviewed evidence does not establish production compromise, account takeover or data theft\.
- SkyZeroZx is credited as Reporter; alan-agius4 published the advisory and is a Remediation reviewer, alongside AndrewKushnir and JeanMeche\. josephperrott is credited as Other\. No narrative byline or individual award is established\.
- The patch pull request opened June 1 and merged June 3, 2026\. These are development events, not software-release dates or the selected advisory's publication date\.
- The database records publication there on June 15 and an update on July 15, 2026\. Neither replaces the June 10 primary publication\. Software-release dates were not established in this review\.
- The source explicitly identifies XSS; stored, reflected and blind subtypes are not established\. This source-selection lesson is distinct from the library's output-serialization and host-binding context cases\. Learning prerequisites and generalized guidance are editorial\.

## Sources and attribution

- [Angular Client Hydration DOM Clobbering &amp; Response-Cache Poisoning](<https://github.com/angular/angular/security/advisories/GHSA-rgjc-h3x7-9mwg>) — Angular maintainers; source ID: advisory; provenance: official primary; retrieved 2026-10-06T03:40:00Z; supports: summary, dates.
- [Angular transfer-state restoration hardening, pull request 69064](<https://github.com/angular/angular/pull/69064>) — Angular maintainers; source ID: patch; provenance: official primary; retrieved 2026-10-06T03:40:46Z; supports: summary, dates.
- [GitHub Advisory Database chronology for GHSA-rgjc-h3x7-9mwg](<https://github.com/advisories/GHSA-rgjc-h3x7-9mwg>) — GitHub Advisory Database; source ID: advisory-database; provenance: official primary; retrieved 2026-10-06T03:41:02Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
