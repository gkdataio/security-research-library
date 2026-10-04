# Storage Access API: permission, document activation and cookie eligibility

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/privacycg-storage-access-permission-activation-boundary.json>) · [Official resource](<https://privacycg.github.io/storage-access/>)

**Publisher:** Privacy Community Group  
**Authors:** Benjamin VanderSloot; Johann Hofmann; Anne van Kesteren  
**Resource type:** Technical Standard  
**Version:** Draft Community Group Report, 22 May 2026  
**Topics:** Web Foundations; Authorization  
**Defensive skills:** Review client isolation; Threat-model integrations

## Original summary

The API draft distinguishes permission for the top-level and embedded site pair from activated access in a document and cookie eligibility on each request\. Secure context, origin, embedding-policy and sandbox conditions still apply\. Navigation and redirects constrain continuity; a document's access does not authorize arbitrary cross-origin cookie attachment\. The companion Headers draft adds resource-controlled activation of an existing permission, independently of permission to read cross-origin responses\.

## Defensive use

Editorial guidance: model permission, document access and request eligibility separately\. Review denial, revocation and navigation paths, minimize resource opt-in, and retain independent server authorization and CSRF defenses\. Cookie availability does not establish authority for a business action\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Same-site versus same-origin relationships, embedded documents and HTTP cookies

## Access and freshness

**Access cost at review:** free.

Publicly readable drafts\.

**Reviewed:** 2026-10-04T15:06:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed both evolving drafts and their relevant permission, request and security sections\. No browser behavior testing\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Original publication date not established\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separately released edition established\.
- **source displayed:** 2026-05-22; precision: day; basis: explicit; source: [The Storage Access API](<https://privacycg.github.io/storage-access/>) (source ID: api-draft). Displayed API draft date, not original publication or final-standard release\.

## Caveats

- Both publications are Draft Community Group Reports\. The API draft is outside W3C's standards track and is not a WHATWG Living Standard\. The technical-standard taxonomy includes drafts; listed authors are the API's current editors\.
- The companion Headers draft displays 17 December 2025\. Its opt-in uses an existing grant; it does not create initial permission\. Cookie attachment and CORS response readability remain separate decisions\.
- Document activation here means enabled storage access, distinct from a user gesture\. A stored permission alone does not establish current document access; the API considers revocation and masks denied permission-query state\.
- This record focuses on HTTP cookies\. Non-cookie extensions, browser parity and deployed conformance are not established by this review\.

## Sources and attribution

- [The Storage Access API](<https://privacycg.github.io/storage-access/>) — Privacy Community Group; source ID: api-draft; provenance: official primary; retrieved 2026-10-04T15:04:39Z; supports: summary, version, dates.
- [Storage Access Headers](<https://privacycg.github.io/storage-access-headers/>) — Privacy Community Group; source ID: headers-draft; provenance: official primary; retrieved 2026-10-04T15:04:34Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
