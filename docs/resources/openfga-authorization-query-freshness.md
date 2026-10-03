# OpenFGA query consistency: authorization decisions need sufficiently fresh state

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/openfga-authorization-query-freshness.json>) · [Official resource](<https://openfga.dev/docs/interacting/consistency>)

**Publisher:** OpenFGA  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Business Logic and State Integrity  
**Defensive skills:** Model access-control invariants; Reason about concurrent state

## Original summary

Authorization correctness includes the age of relationship state used for a decision\. OpenFGA documents a latency-oriented mode that can reuse cached results and a higher-consistency mode that bypasses the cache\. With caching enabled, an immediate permission check may miss a relationship update\.

## Defensive use

Editorial lesson: specify when permission changes must become observable and align decision freshness with that requirement\. Review cache invalidation and performance assumptions together; a newly issued request does not necessarily use newly changed authorization state\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Relationship-based authorization and cache consistency concepts

## Access and freshness

**Access cost at review:** free.

Public official implementation guidance\.

**Reviewed:** 2026-10-03T17:59:50Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Official documentation reviewed; no deployment or performance testing\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Original publication and edition release are not established\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Original publication and edition release are not established\.
- **source displayed:** 2026-09-28; precision: day; basis: explicit; source: [Query Consistency Modes](<https://openfga.dev/docs/interacting/consistency>) (source ID: primary). Displayed last-modified date, not original publication\.

## Caveats

- The documentation says caching is disabled by default\. Do not assume every deployment returns cached authorization decisions\.
- Its illustrative timestamp branch appears inconsistent with the prose; this record does not reproduce or endorse that example\.
- Consistency tokens are described as future work\. This guidance establishes neither a deployment-specific freshness guarantee nor evidence of an incident\.

## Sources and attribution

- [Query Consistency Modes](<https://openfga.dev/docs/interacting/consistency>) — OpenFGA; source ID: primary; provenance: official primary; retrieved 2026-10-03T17:59:50Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
