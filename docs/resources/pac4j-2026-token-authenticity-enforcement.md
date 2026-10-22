# pac4j JWT validation: confidentiality does not establish authenticity

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://codeant.ai/security-research/pac4j-jwt-authentication-bypass-public-key>) · [Canonical JSON](<../../data/resources/pac4j-2026-token-authenticity-enforcement.json>)

<a id="original-summary"></a>
## Main takeaway

A researcher reports that pac4j could accept decrypted token claims as an authenticated profile without requiring signature validation \(CVE-2026-29000\)\. A library-level demonstration on 6\.0\.3 accepted arbitrary identities and roles\. The research does not establish production compromise\.

## Defensive use

Treat authenticity checks as mandatory, fail-closed prerequisites for profile creation\. Review all accepted token representations\. The maintainer confirms remediation and directs upgrades to 4\.5\.9, 5\.7\.9 or 6\.3\.3 and newer within those release lines\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** CodeAnt AI  
**Authors:** Amartya Jha  
**Resource type:** [Research Paper](<../resource-types.md#type-research-paper>)  
**Version:** Not established in the reviewed record  
**Topics:** [Identity](<../resource-topics.md#topic-identity>); [Authorization](<../resource-topics.md#topic-authorization>)  
**Defensive skills:** [Review security-token design](<../skillsets.md#skill-security-token-design>); [Review identity lifecycle](<../skillsets.md#skill-identity-lifecycle-review>); [Verify remediation evidence](<../skillsets.md#skill-patch-verification>)

## Prerequisites

**Basis:** editorial guidance.

- Basic authentication and access-control concepts
- Familiarity with application trust boundaries

## Access and freshness

**Access cost at review:** free.

Public sources readable without an account\.

**Reviewed:** 2026-10-03T06:19:33Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary sources reviewed; no immutable article revision established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-03-03; precision: day; basis: explicit; source: [CVE-2026-29000: pac4j-jwt Auth Bypass PoC With a Public Key](<https://codeant.ai/security-research/pac4j-jwt-authentication-bypass-public-key>) (source ID: research).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-03-03; precision: day; basis: explicit; source: [CVE-2026-29000: pac4j-jwt Auth Bypass PoC With a Public Key](<https://codeant.ai/security-research/pac4j-jwt-authentication-bypass-public-key>) (source ID: research).

## Caveats

- The demonstrated configuration uses RSA-encrypted JWTs with signature and encryption configuration; exposure cannot be inferred from any pac4j dependency alone\.
- Application-specific consequences depend on how authenticated claims map to authorization\.
- The maintainer confirms the issue and research credit but withholds technical details; the detailed mechanism remains researcher evidence\.
- Article publication is separate from reporting and patch events\. The article describes February 28 private disclosure and patches by March 2, 2026; exact version-release dates are not recorded here\.

## Sources and attribution

- [CVE-2026-29000: pac4j-jwt Auth Bypass PoC With a Public Key](<https://codeant.ai/security-research/pac4j-jwt-authentication-bypass-public-key>) — CodeAnt AI; source ID: research; provenance: official primary; retrieved 2026-10-03T06:19:33Z; supports: summary, dates.
- [Security advisory for pac4j-jwt \(JwtAuthenticator\)](<https://www.pac4j.org/blog/security-advisory-pac4j-jwt-jwtauthenticator.html>) — pac4j; source ID: maintainer; provenance: official primary; retrieved 2026-10-03T06:19:33Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
