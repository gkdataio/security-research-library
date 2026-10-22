# Astro: routing and authorization must agree on resource identity

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/withastro/astro/security/advisories/GHSA-376h-93r7-7g6f>) · [Canonical JSON](<../../data/resources/astro-2026-route-normalization-authorization-consistency.json>)

<a id="original-summary"></a>
## Main takeaway

Astro's routing and permission middleware could interpret the same path differently because base-path removal did not check for a complete path segment\. The maintainer limits the resulting authorization bypass to applications with a non-root base path and pathname-based middleware protection\. The finding does not apply to every Astro application\.

## Defensive use

The maintainer identifies 7\.2\.4 as patched, and its release notes confirm segment-aware base handling\. Editorial lesson: a permission decision must bind to the same canonical resource that execution resolves\. Review normalization contracts between middleware and routing, and preserve resource-level checks when public path representations change\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Astro  
**Authors:** matthewp  
**Resource type:** [Maintainer Advisory](<../resource-types.md#type-maintainer-advisory>)  
**Version:** Not established in the reviewed record  
**Topics:** [Web Foundations](<../resource-topics.md#topic-web-foundations>); [Authorization](<../resource-topics.md#topic-authorization>); [Server/Client Framework Security](<../resource-topics.md#topic-server-client-frameworks>)  
**Defensive skills:** [Model access-control invariants](<../skillsets.md#skill-authorization-modeling>); [Review parsing and serialization](<../skillsets.md#skill-secure-parser-review>); [Verify remediation evidence](<../skillsets.md#skill-patch-verification>)

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
