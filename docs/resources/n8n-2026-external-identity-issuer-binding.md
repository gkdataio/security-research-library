# n8n token exchange: preserve the issuer namespace

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/n8n-2026-external-identity-issuer-binding.json>) · [Official resource](<https://github.com/n8n-io/n8n/security/advisories/GHSA-mq3m-f8x3-579w>)

**Publisher:** n8n  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization  
**Defensive skills:** Review identity lifecycle; Review security-token design; Model access-control invariants

## Original summary

CVE-2026-59208 concerns token exchange resolving external identities by subject alone, dropping the issuer namespace\. With the feature enabled and multiple trusted issuers, a valid token whose subject matches an identity from another issuer can resolve to the wrong local account\. Maintainers report impersonation; the reviewed advisory does not provide a controlled demonstration or establish production compromise\.

## Defensive use

Editorial lesson: retain issuer and subject together throughout external-identity lookup and account binding; successful token validation alone does not establish which local account it represents\. OpenID Connect Core section 5\.7 supplies conceptual support for issuer-scoped identity\. Follow the maintainer's upgrade guidance; reducing trusted issuers or disabling unused exchange is explicitly incomplete temporary mitigation\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic federation, token claims and local-account binding concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and supporting references\.

**Reviewed:** 2026-10-05T22:31:42Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Advisory, release pages and conceptual standard reviewed\. No live testing, reproduction or independent patch audit performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-24; precision: day; basis: explicit; source: [Cross-Issuer Token Exchange Account Binding via Subject-Only Identity Resolution](<https://github.com/n8n-io/n8n/security/advisories/GHSA-mq3m-f8x3-579w>) (source ID: advisory). Advisory publication, not software release or original report date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition date established\.
- **source displayed:** 2026-06-24; precision: day; basis: explicit; source: [Cross-Issuer Token Exchange Account Binding via Subject-Only Identity Resolution](<https://github.com/n8n-io/n8n/security/advisories/GHSA-mq3m-f8x3-579w>) (source ID: advisory). Displayed advisory publication date\.

## Caveats

- Patched metadata lists &gt;= 2\.27\.4 and &gt;= 2\.28\.1, while remediation prose names 2\.28\.1\. The overlapping affected entries &lt; 2\.27\.4 and &lt; 2\.28\.1 are preserved as published; no normalized affected interval is inferred\.
- Release pages date both versions to June 24, 2026; 2\.28\.1 is labeled pre-release\. They do not identify this fix and support chronology only, not independent patch verification\.
- Jubke published the advisory; bearsyankees is credited as Reporter\. No narrative byline or individual award is established\.
- OpenID Connect Core's displayed December 15, 2023 edition is a conceptual reference, not this advisory's publication date or a claim that n8n violates an OIDC conformance requirement\.
- This issuer-namespace case differs from the library's LDAP attribute linking, refresh-grant resource binding, Dynamic Credentials ownership, Prowler tenant selection and multi-app OAuth binding examples\.

## Sources and attribution

- [Cross-Issuer Token Exchange Account Binding via Subject-Only Identity Resolution](<https://github.com/n8n-io/n8n/security/advisories/GHSA-mq3m-f8x3-579w>) — n8n; source ID: advisory; provenance: official primary; retrieved 2026-10-05T22:31:42Z; supports: summary, dates.
- [n8n@2\.27\.4 release](<https://github.com/n8n-io/n8n/releases/tag/n8n@2.27.4>) — n8n; source ID: release-2274; provenance: official primary; retrieved 2026-10-05T22:31:42Z; supports: dates.
- [n8n@2\.28\.1 release](<https://github.com/n8n-io/n8n/releases/tag/n8n@2.28.1>) — n8n; source ID: release-2281; provenance: official primary; retrieved 2026-10-05T22:31:42Z; supports: dates.
- [OpenID Connect Core 1\.0 incorporating errata set 2, section 5\.7](<https://openid.net/specs/openid-connect-core-1_0.html#ClaimStability>) — OpenID Foundation; source ID: oidc-claim-stability; provenance: official primary; retrieved 2026-10-05T22:31:42Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
