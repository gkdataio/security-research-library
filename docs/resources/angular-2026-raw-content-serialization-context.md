# Angular SSR: preserve output context through serialization and post-processing

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/angular-2026-raw-content-serialization-context.json>) · [Official resource](<https://github.com/angular/angular/security/advisories/GHSA-vpx6-8pjr-4g3v>)

**Publisher:** Angular  
**Authors:** alan-agius4  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations  
**Defensive skills:** Review text-encoding invariants; Review parsing and serialization; Verify remediation evidence

## Original summary

Angular's advisory for CVE-2026-69149 describes unsafe serialization of untrusted text in fallback raw-content containers\. A server-generated DOM can lose its intended inert meaning when later serialization and parsing interpret that text as structure\. The maintainer confirms same-origin script-execution risk; session theft is a possible application-dependent consequence, not a documented production compromise\.

## Defensive use

Model every serialization and reparse boundary, including HTML post-processing\. The linked remediation discussion shows that preserving comment semantics matters alongside escaping\. The original advisory lists 22\.0\.7, 21\.2\.19 and 20\.3\.27 as fixes\. Later advisories identify additional node and fragment cases, so these historical minimums do not establish comprehensive current remediation\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Server-side rendering and browser output-context concepts
- Basic trust-boundary and secure-input review

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and linked primary discussion\.

**Reviewed:** 2026-10-03T11:31:08Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary pages read; publication dates are distinct from software release dates\. No immutable resource edition established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-07-29; precision: day; basis: explicit; source: [Missing Fallback Raw-Content Serialization Escaping leads to Cross-Site Scripting \(XSS\) in Angular SSR](<https://github.com/angular/angular/security/advisories/GHSA-vpx6-8pjr-4g3v>) (source ID: maintainer). Publication of the selected maintainer advisory; earlier public discussion is separately noted\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-07-29; precision: day; basis: explicit; source: [Missing Fallback Raw-Content Serialization Escaping leads to Cross-Site Scripting \(XSS\) in Angular SSR](<https://github.com/angular/angular/security/advisories/GHSA-vpx6-8pjr-4g3v>) (source ID: maintainer).

## Caveats

- Exposure requires SSR and untrusted content in the affected rendering context\. Ordinary Angular use alone does not establish exposure\. Avoiding those bindings or the implicated post-processing path are scoped workarounds, not universal guarantees\.
- SkyZeroZx authored the linked remediation proposal on June 22, 2026; maintainer alan-agius4 merged it July 7\. These are public-discussion and merge dates, not resource-edition or product-release dates\.
- The August 27 follow-ups describe separate processing-instruction and document-fragment reachability limits; they list 22\.1\.4, 21\.2\.22 and 20\.3\.30 as patched and older unsupported branches as unpatched\. These follow-ups limit the original patch claim without asserting that every initial deployment reached every later case\.
- The processing-instruction advisory requires programmatic construction, unlike ordinary template syntax; the fragment advisory includes ordinary text-node cases\. Both provide minimal demonstrations, but no production victim evidence\.

## Sources and attribution

- [Missing Fallback Raw-Content Serialization Escaping leads to Cross-Site Scripting \(XSS\) in Angular SSR](<https://github.com/angular/angular/security/advisories/GHSA-vpx6-8pjr-4g3v>) — Angular; source ID: maintainer; provenance: official primary; retrieved 2026-10-03T11:31:08Z; supports: summary, dates.
- [fix: escape fallback raw-content text nodes](<https://github.com/angular/domino/pull/32>) — SkyZeroZx / Angular; source ID: remediation; provenance: official primary; retrieved 2026-10-03T11:31:08Z; supports: summary, dates.
- [SSR XSS via Unescaped template Content Across DocumentFragment Boundaries in Fallback Raw-Content Elements](<https://github.com/angular/angular/security/advisories/GHSA-v3p8-whq6-r5jg>) — Angular; source ID: fragment-followup; provenance: official primary; retrieved 2026-10-03T11:31:08Z; supports: summary, dates.
- [SSR XSS via Unescaped Processing Instruction Nodes in Fallback Raw-Content Elements](<https://github.com/angular/angular/security/advisories/GHSA-j3r3-mxqp-r2p4>) — Angular; source ID: node-followup; provenance: official primary; retrieved 2026-10-03T11:31:08Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
