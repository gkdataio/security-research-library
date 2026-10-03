# Nuxt: island data must not acquire component-selection authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/nuxt-2026-island-component-selection-authority.json>) · [Official resource](<https://github.com/nuxt/nuxt/security/advisories/GHSA-48hr-524c-v5w3>)

**Publisher:** Nuxt  
**Authors:** danielroe  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Verification  
**Defensive skills:** Threat-model integrations; Review input trust boundaries; Model access-control invariants

## Original summary

The maintainer describes request-controlled island data reaching dynamic component selection through attribute inheritance\. This permits unintended registered-component or native-element rendering\. The boundary fails when input intended to configure an approved component instead chooses what component runs\. The advisory expressly excludes arbitrary JavaScript execution through this vector\.

## Defensive use

Nuxt identifies 4\.5\.1 and 3\.21\.10 as patched for the common implicit-inheritance path\. Explicit untrusted component selection remains application responsibility\. Editorial lesson: define both accepted data and allowed interpretation at component boundaries; map external choices to a closed set of trusted components rather than treating strings as authority\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Server-rendered applications and framework composition
- Trust-boundary modeling and application authorization

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory\.

**Reviewed:** 2026-10-03T15:39:32Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory read\. No live testing or independent patch execution performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-07-27; precision: day; basis: explicit; source: [Unauthorized Component Instantiation via Server Island Props in Nuxt](<https://github.com/nuxt/nuxt/security/advisories/GHSA-48hr-524c-v5w3>) (source ID: advisory). Explicit advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No educational-resource edition established; software patch chronology is separate\.
- **source displayed:** 2026-07-27; precision: day; basis: explicit; source: [Unauthorized Component Instantiation via Server Island Props in Nuxt](<https://github.com/nuxt/nuxt/security/advisories/GHSA-48hr-524c-v5w3>) (source ID: advisory). Explicit advisory publication date\.

## Caveats

- CVE-2026-71318\. Requires active server islands and a dynamic-component consumer; installing a UI library alone is insufficient\. Runtime template compilation is not required\.
- Affected ranges: 3\.1\.0 through below 3\.21\.10, and 4\.0\.0 through below 4\.5\.1\. Nuxt 2 is excluded\. danielroe published the advisory\.
- Patch-release dates were not established\. Data exposure beyond unintended rendering depends on reachable components and is not demonstrated here\.
- No bounty or production compromise is established\. Learning prerequisites and generalized defensive reasoning are editorial\.

## Sources and attribution

- [Unauthorized Component Instantiation via Server Island Props in Nuxt](<https://github.com/nuxt/nuxt/security/advisories/GHSA-48hr-524c-v5w3>) — Nuxt; source ID: advisory; provenance: official primary; retrieved 2026-10-03T15:39:32Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
