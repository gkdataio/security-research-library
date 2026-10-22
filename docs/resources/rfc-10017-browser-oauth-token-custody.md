# RFC 10017: OAuth 2\.0 for Browser-Based Applications

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://www.rfc-editor.org/rfc/rfc10017.html>) · [Canonical JSON](<../../data/resources/rfc-10017-browser-oauth-token-custody.json>)

<a id="original-summary"></a>
## Main takeaway

RFC 10017 compares browser-only OAuth clients, token-mediating backends and backend-for-frontend designs by where they keep tokens and manage sessions\. It distinguishes protecting token material from limiting what compromised application code on the same origin can still do\.

## Defensive use

Document which component holds each credential, binds the user session, and enforces request destinations\. Compare those responsibilities and residual risks against an owned application’s architecture\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Internet Engineering Task Force / RFC Editor  
**Authors:** Aaron Parecki; Philippe De Ryck; David Waite  
**Resource type:** [Technical Standard](<../resource-types.md#type-technical-standard>)  
**Version:** RFC 10017 / BCP 212  
**Topics:** [Identity](<../resource-topics.md#topic-identity>); [Authorization](<../resource-topics.md#topic-authorization>); [Web Foundations](<../resource-topics.md#topic-web-foundations>); [Browser Security](<../resource-topics.md#topic-browser-security>)  
**Defensive skills:** [Review identity lifecycle](<../skillsets.md#skill-identity-lifecycle-review>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>); [Review client isolation](<../skillsets.md#skill-browser-isolation-review>)

## Prerequisites

**Basis:** editorial guidance.

- OAuth client and resource-server roles
- Browser origins, cookies, and HTTP redirects

## Access and freshness

**Access cost at review:** free.

Official specification readable without an account at review time\.

**Reviewed:** 2026-10-03T04:40:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed this identified edition and its relevant design and security sections\. Retrieval date is separate from publication; later revisions or errata may exist\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08; precision: month; basis: explicit; source: [RFC 10017: OAuth 2\.0 for Browser-Based Applications](<https://www.rfc-editor.org/rfc/rfc10017.html>) (source ID: primary). Publication date of this RFC or final specification\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Backend token custody does not make compromised application code harmless\.
- Browser-specific guidance complements RFC 9700; it does not establish security of a particular deployment\.

## Sources and attribution

- [RFC 10017: OAuth 2\.0 for Browser-Based Applications](<https://www.rfc-editor.org/rfc/rfc10017.html>) — Internet Engineering Task Force / RFC Editor; source ID: primary; provenance: official primary; retrieved 2026-10-03T04:40:00Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
