# Astro: routing and authorization must agree on resource identity

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/astro-2026-route-normalization-authorization-consistency.json>) · [Official resource](<https://github.com/withastro/astro/security/advisories/GHSA-376h-93r7-7g6f>)

**Publisher:** Astro  
**Authors:** matthewp  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Authorization  
**Defensive skills:** Model access-control invariants; Review parsing and serialization; Verify remediation evidence

## Original summary

Astro's base-path removal accepted a textual prefix without establishing a complete path segment\. Routing and authorization middleware could consequently disagree about the requested resource\. The maintainer bounds the authorization bypass to applications with a non-root base and pathname-based middleware protection; it is not a claim that every Astro application lacks authorization\.

## Defensive use

The maintainer identifies 7\.2\.4 as patched, and its release notes confirm segment-aware base handling\. Editorial lesson: a permission decision must bind to the same canonical resource that execution resolves\. Review normalization contracts between middleware and routing, and preserve resource-level checks when public path representations change\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- URL path normalization and framework routing
- Middleware authorization and canonical resource identity

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and release notes\.

**Reviewed:** 2026-10-03T14:19:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory and release notes read\. No live testing or independent patch execution\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08-27; precision: day; basis: explicit; source: [Authorization bypass from missing path-segment boundary check when stripping the configured base](<https://github.com/withastro/astro/security/advisories/GHSA-376h-93r7-7g6f>) (source ID: advisory). Advisory publication\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition established\.
- **source displayed:** 2026-08-27; precision: day; basis: explicit; source: [Authorization bypass from missing path-segment boundary check when stripping the configured base](<https://github.com/withastro/astro/security/advisories/GHSA-376h-93r7-7g6f>) (source ID: advisory). Explicit advisory publication date\.

## Caveats

- CVE-2026-84376\. matthewp published the advisory; Ryoga-exe is credited as reporter\. The affected range is astro through 7\.2\.3\.
- The software release page displays August 19 without a year in retrieved text\. A full patch-release date is therefore not asserted; it is distinct from advisory publication and resource-edition chronology\.
- No production compromise or individual bounty is established\. Learning prerequisites and generalized review guidance are editorial\.

## Sources and attribution

- [Authorization bypass from missing path-segment boundary check when stripping the configured base](<https://github.com/withastro/astro/security/advisories/GHSA-376h-93r7-7g6f>) — Astro; source ID: advisory; provenance: official primary; retrieved 2026-10-03T14:18:30Z; supports: summary, dates.
- [astro@7\.2\.4 release](<https://github.com/withastro/astro/releases/tag/astro@7.2.4>) — Astro; source ID: release; provenance: official primary; retrieved 2026-10-03T14:18:52Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
