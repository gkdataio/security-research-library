# OWASP Server-Side Request Forgery Prevention

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/owasp-server-request-destination-boundaries.json>) · [Official resource](<https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html>)

**Publisher:** OWASP Cheat Sheet Series  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Cloud Security  
**Defensive skills:** Threat-model integrations; Review parsing and serialization; Review input trust boundaries; Review secrets containment

## Original summary

Explains destination validation and network isolation for server-initiated requests, distinguishing fixed trusted destinations from services that need broader external access\.

## Defensive use

Review owned-service destination policy, parser consistency, redirect behavior and independent egress restrictions\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic knowledge of web requests and application/network boundaries

## Access and freshness

**Access cost at review:** free.

Public official guidance\.

**Reviewed:** 2026-10-02T16:29:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Living guidance; publication and update dates were not established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- The destination-policy design depends on business requirements\. Metadata protections complement application validation and network isolation\.

## Related conceptual diagrams

- [Layer server-request destination controls](<../diagram-gallery.md#server-request-destination-policy>)

## Sources and attribution

- [Server-Side Request Forgery Prevention Cheat Sheet](<https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html>) — OWASP; source ID: primary; provenance: official primary; retrieved 2026-10-02T16:29:00Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
