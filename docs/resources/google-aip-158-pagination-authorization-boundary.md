# Google AIP-158: pagination continuation does not grant resource authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/google-aip-158-pagination-authorization-boundary.json>) · [Official resource](<https://google.aip.dev/158>)

**Publisher:** Google  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Web Foundations  
**Defensive skills:** Model access-control invariants; Threat-model integrations

## Original summary

Google's Approved pagination guidance separates a continuation position from permission to read the collection\. Page tokens must be opaque and convey no authorization; each request still requires authorization\. Subsequent requests retain the other query arguments, while page size may change\. Opacity protects interface abstraction rather than establishing access rights\.

## Defensive use

Editorial lesson: document continuation state and actor/resource policy as separate design contracts\. An integration following a stored cursor must still rely on the service's per-request authorization decision\. Treat query continuity as a request-consistency requirement, not evidence of entitlement\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic familiarity with paginated collection APIs and access-control modeling

## Access and freshness

**Access cost at review:** free.

Public official API implementation guidance\.

**Reviewed:** 2026-10-04T04:05:09Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed the official AIP page, shown as Approved, and the first-party commit corroborating its later changelog entry\. This is a documentation review, not an implementation assessment\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Original publication of the current text is not established by the page's Created field\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No dated educational-resource edition is established for this living guidance\.
- **source displayed:** 2025-07-08; precision: day; basis: explicit; source: [AIP-158: Pagination](<https://google.aip.dev/158>) (source ID: primary). Date of the newest displayed Changelog entry, concerning degraded-skip guidance; not original publication, an edition release, or the date of the authorization rule\.

## Caveats

- The page's Created and Updated fields both display 2019-02-18, although its changelog includes 2025-07-08\. The linked first-party commit corroborates that later edit; the header is not treated as the current text's last revision date\.
- Query-argument consistency excludes page size: the guidance requires honoring a changed page size and recommends rejecting changes to other arguments\. This contract does not establish snapshot isolation or a fixed collection across pages\.
- Opaque token format does not establish permission\. This guide supplies no incident, affected-product, bounty, or deployment-specific security claim\.

## Sources and attribution

- [AIP-158: Pagination](<https://google.aip.dev/158>) — Google; source ID: primary; provenance: official primary; retrieved 2026-10-04T04:02:03Z; supports: summary, dates.
- [fix\(AIP-158\): clarify degraded skip response guidance \(\#1510\)](<https://github.com/aip-dev/google.aip.dev/commit/1b7bc19ccd0fb19d8c24642eb2907d0246328c41>) — Google AIP maintainers; source ID: changelog-change; provenance: official primary; retrieved 2026-10-04T04:04:42Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
