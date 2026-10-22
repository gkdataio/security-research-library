# Prowler SAML: retain validated tenant authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/prowler-cloud/prowler/security/advisories/GHSA-h8m9-jgf8-vwvp>) · [Canonical JSON](<../../data/resources/prowler-2026-saml-tenant-issuance-binding.json>)

<a id="original-summary"></a>
## Main takeaway

Prowler's maintainers report that token issuance chose a tenant from an asserted email domain rather than the validated SAML configuration \(CVE-2026-59151\)\. They describe possible cross-tenant account takeover\. Their adapter-level demonstration showed a linking-method call, not a persisted account link, completed token issuance or production compromise\.

## Defensive use

Keep federation configuration, accepted identity claims, membership changes and issued-token tenant consistent\. The advisory lists Prowler API through 5\.30\.2 as affected and 5\.30\.3 as patched; no patch-release date is established here\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Prowler  
**Authors:** Not identified in the reviewed record  
**Resource type:** [Maintainer Advisory](<../resource-types.md#type-maintainer-advisory>)  
**Version:** Not established in the reviewed record  
**Topics:** [Identity](<../resource-topics.md#topic-identity>); [Authorization](<../resource-topics.md#topic-authorization>)  
**Defensive skills:** [Review identity lifecycle](<../skillsets.md#skill-identity-lifecycle-review>); [Review security-token design](<../skillsets.md#skill-security-token-design>); [Model access-control invariants](<../skillsets.md#skill-authorization-modeling>)

## Prerequisites

**Basis:** editorial guidance.

- Basic federation and object-level authorization concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory\.

**Reviewed:** 2026-10-03T11:49:44Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory reviewed; no immutable educational edition established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-22; precision: day; basis: explicit; source: [SAML Domain Claiming Enables Cross-Tenant Account Takeover](<https://github.com/prowler-cloud/prowler/security/advisories/GHSA-h8m9-jgf8-vwvp>) (source ID: maintainer). Advisory publication, not software patch release\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-06-22; precision: day; basis: explicit; source: [SAML Domain Claiming Enables Cross-Tenant Account Takeover](<https://github.com/prowler-cloud/prowler/security/advisories/GHSA-h8m9-jgf8-vwvp>) (source ID: maintainer). Advisory publication, not software patch release\.

## Caveats

- Requires SAML, authenticated control of a tenant configuration and identity provider, and a target domain mapped to another SAML tenant; no victim interaction\.
- Configured domains remain globally unique\. The advisory narrative corrects conflicting older demonstration comments\.
- Credits: EQSTLab, reporter; AdriiiPRodri, remediation developer; jfagoagas, coordinator/publishing account; josema-xyz, analyst\. Article authorship is not established\.
- Broader access and persistence are potential consequences\. The fix was not independently audited\.
- The displayed test mocks the linking method and checks its invocation with an existing user; it is narrower evidence than completed persistent linking\.

## Sources and attribution

- [SAML Domain Claiming Enables Cross-Tenant Account Takeover](<https://github.com/prowler-cloud/prowler/security/advisories/GHSA-h8m9-jgf8-vwvp>) — Prowler; source ID: maintainer; provenance: official primary; retrieved 2026-10-03T11:49:44Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
