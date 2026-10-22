# Better Auth: incoming identity proof does not validate existing credentials

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/better-auth/better-auth/security/advisories/GHSA-g38m-r43w-p2q7>) · [Canonical JSON](<../../data/resources/better-auth-2026-local-account-linking-verification.json>)

<a id="original-summary"></a>
## Main takeaway

Better Auth could keep an unauthorized local password when linking a verified provider identity to an unverified local account\. Its CVE-2026-53516 advisory explains that provider-side email verification was treated as proof that the earlier local credentials were legitimate\. The merged account could therefore retain that password login even when ordinary email verification was required\.

## Defensive use

Editorial reasoning: linking combines authorities, so prove ownership on both sides before merging credentials\. Requiring verification only after the merge cannot establish who created the earlier password\. Release 1\.6\.11 corroborates a verified-local-email gate; the advisory also identifies 1\.7\.0-beta\.4 as patched\. Disabling implicit linking is a documented interim control\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Better Auth  
**Authors:** gustavovalverde  
**Resource type:** [Maintainer Advisory](<../resource-types.md#type-maintainer-advisory>)  
**Version:** Not established in the reviewed record  
**Topics:** [Identity](<../resource-topics.md#topic-identity>); [Authorization](<../resource-topics.md#topic-authorization>)  
**Defensive skills:** [Review identity lifecycle](<../skillsets.md#skill-identity-lifecycle-review>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>); [Verify remediation evidence](<../skillsets.md#skill-patch-verification>)

## Prerequisites

**Basis:** editorial guidance.

- OAuth identity-provider claims and local account-linking concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer disclosure and release notes\.

**Reviewed:** 2026-10-03T14:39:59\.794959Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory and release notes reviewed; no independent reproduction or deployment assessment\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-05-31; precision: day; basis: explicit; source: [better-auth: OAuth sign-in can link to an account an attacker registered in advance](<https://github.com/better-auth/better-auth/security/advisories/GHSA-g38m-r43w-p2q7>) (source ID: advisory). Maintainer advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource edition date established; software remediation is recorded separately\.
- **source displayed:** 2026-05-31; precision: day; basis: explicit; source: [better-auth: OAuth sign-in can link to an account an attacker registered in advance](<https://github.com/better-auth/better-auth/security/advisories/GHSA-g38m-r43w-p2q7>) (source ID: advisory). Maintainer advisory publication date\.

## Caveats

- Exposure requires email/password sign-in, OAuth or SSO, implicit linking, and an existing unverified local account before the legitimate federated sign-in\. Impact is account access, not compromise of the identity provider\.
- The advisory lists stable versions below 1\.6\.11 and 1\.7\.0-beta\.0 through beta\.3\. Its deprecated compatibility opt-out restores weaker linking behavior\.
- gustavovalverde published the advisory; avrmeduard is credited as reporter\. Release notes show May 12 without an explicit year in retrieved text; exact patch date is left unestablished\.
- Maintainer disclosure, not a peer-reviewed paper, award-backed report, or evidence of production exploitation\.

## Sources and attribution

- [better-auth: OAuth sign-in can link to an account an attacker registered in advance](<https://github.com/better-auth/better-auth/security/advisories/GHSA-g38m-r43w-p2q7>) — Better Auth; source ID: advisory; provenance: official primary; retrieved 2026-10-03T14:39:59\.794959Z; supports: summary, dates, version.
- [Release v1\.6\.11](<https://github.com/better-auth/better-auth/releases/tag/v1.6.11>) — Better Auth; source ID: release; provenance: official primary; retrieved 2026-10-03T14:39:59\.794959Z; supports: summary, dates, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
