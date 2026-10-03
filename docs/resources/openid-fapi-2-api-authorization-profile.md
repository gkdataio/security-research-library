# FAPI 2\.0 Security Profile

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/openid-fapi-2-api-authorization-profile.json>) · [Official resource](<https://openid.net/specs/fapi-security-profile-2_0-final.html>)

**Publisher:** OpenID Foundation  
**Authors:** Daniel Fett; Dave Tonge; Joseph Heenan  
**Resource type:** Technical Standard  
**Version:** 2\.0 Final  
**Topics:** Identity; Authorization  
**Defensive skills:** Model access-control invariants; Review security-token design; Threat-model integrations

## Original summary

Defines a high-security OAuth profile with coordinated requirements for confidential clients, authorization servers, and resource servers\. Connects sender-constrained tokens and authorization-request integrity with the separate requirement to evaluate whether a token’s authority is sufficient for each protected resource\.

## Defensive use

Map the ownership of token validation, issuer trust, client authentication, and resource-access decisions across an owned API integration\. Keep protocol conformance distinct from application-specific authorization\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- OAuth roles and authorization-code flows
- Public-key client authentication and token validation

## Access and freshness

**Access cost at review:** free.

Official specification readable without an account at review time\.

**Reviewed:** 2026-10-03T04:40:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed this identified edition and its relevant design and security sections\. Retrieval date is separate from publication; later revisions or errata may exist\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-02-22; precision: day; basis: explicit; source: [FAPI 2\.0 Security Profile](<https://openid.net/specs/fapi-security-profile-2_0-final.html>) (source ID: primary). Publication date of this RFC or final specification\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Public clients are outside this profile’s scope\.
- Security claims depend on the stated model and complete implementation; this record is not certification\.

## Sources and attribution

- [FAPI 2\.0 Security Profile](<https://openid.net/specs/fapi-security-profile-2_0-final.html>) — OpenID Foundation; source ID: primary; provenance: official primary; retrieved 2026-10-03T04:40:00Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
