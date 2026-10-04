# Angular host bindings: bind sanitization to the concrete output element

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/angular-2026-host-binding-context-authority.json>) · [Official resource](<https://github.com/angular/angular/security/advisories/GHSA-hh8m-fm6v-7cvg>)

**Publisher:** Angular  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations  
**Defensive skills:** Review text-encoding invariants; Review input trust boundaries; Verify remediation evidence

## Original summary

CVE-2026-88057 concerns sanitization chosen from a directive's compile-time selector rather than the concrete element receiving its host binding\. Composition and reuse could therefore apply an absent or weaker policy to a more sensitive browser sink\. The maintainer confirms browser script-execution risk when an attacker controls the affected bound value; reviewed sources do not establish production compromise\.

## Defensive use

Treat element identity and output context as part of a binding's security contract\. Re-evaluate that contract when composition, inheritance or dynamic construction changes the receiving element\. The maintainer lists 22\.1\.0, 21\.2\.20 and 20\.3\.28 as patched; older end-of-support branches receive no patch\. The researcher issue distinguishes ordinary URL, resource-loading and HTML contexts, so a generic URL filter is not evidence that all contexts are secured\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Framework component composition and template binding concepts
- Basic browser output-context and sanitization concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and linked primary discussion\.

**Reviewed:** 2026-10-03T11:31:08Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary pages read; publication dates are distinct from software release dates\. No immutable resource edition established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08-18; precision: day; basis: explicit; source: [Sanitization bypass via directive host bindings on concrete host elements in @angular/core and @angular/compiler](<https://github.com/angular/angular/security/advisories/GHSA-hh8m-fm6v-7cvg>) (source ID: maintainer). Publication of the selected maintainer advisory; earlier public discussion is separately noted\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-08-18; precision: day; basis: explicit; source: [Sanitization bypass via directive host bindings on concrete host elements in @angular/core and @angular/compiler](<https://github.com/angular/angular/security/advisories/GHSA-hh8m-fm6v-7cvg>) (source ID: maintainer).

## Caveats

- Exposure depends on attacker-influenced values reaching affected security-sensitive host bindings and a mismatch between compile-time and concrete-element context\. Composition alone does not prove exploitability\.
- SkyZeroZx published the linked issue on June 27, 2026; the advisory credits SkyZeroZx as Remediation developer, and alan-agius4, josephperrott and JeanMeche as Remediation reviewers\. GitHub identifies alan-agius4 as the publishing account\. The reviewed advisory has no explicit narrative byline, so authors is empty; publication and remediation credits do not by themselves establish who wrote the narrative\. The August 18 date describes the selected maintainer publication, not the earliest public discussion or a product release\.
- The maintainer suggests explicit sanitization or safe-scheme restriction as workarounds\. Their applicability depends on the actual sink; the reviewed issue identifies stricter resource-loading and HTML contexts\. This caveat is editorial defensive guidance, not a claim that the maintainer workaround was independently tested\.
- The issue explains a minimal case but links its runnable reproduction elsewhere\. No reproduction was run, and observed exploit outcomes are not independently established\.

## Sources and attribution

- [Sanitization bypass via directive host bindings on concrete host elements in @angular/core and @angular/compiler](<https://github.com/angular/angular/security/advisories/GHSA-hh8m-fm6v-7cvg>) — Angular; source ID: maintainer; provenance: official primary; retrieved 2026-10-03T11:31:08Z; supports: summary, dates.
- [ResourceURL sanitizer bypass through host-binding selector mismatch](<https://github.com/angular/angular/issues/69550>) — SkyZeroZx; source ID: research; provenance: official primary; retrieved 2026-10-03T11:31:08Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
