# Better Auth SCIM: absent ownership must not grant shared authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/better-auth-2026-scim-ownerless-provider-authority.json>) · [Official resource](<https://github.com/better-auth/better-auth/security/advisories/GHSA-j8v8-g9cx-5qf4>)

**Publisher:** Better Auth  
**Authors:** gustavovalverde  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization  
**Defensive skills:** Review identity lifecycle; Model access-control invariants; Verify remediation evidence

## Original summary

Personal SCIM providers could lack an owner, while management checks rejected mismatched ownership only when an owner existed\. Missing identity binding therefore admitted unrelated authenticated users\. The maintainer reports provider disclosure, deletion and token replacement, with provisioning authority limited to enabled SCIM features\.

## Defensive use

Editorial reasoning: an unknown owner is a separate authorization state, not an implicit shared resource\. Review creation, migration and subsequent management together\. The fix mandates owner binding and makes legacy ownerless records fail closed; administrators must resolve those records rather than assuming a package upgrade assigns legitimate ownership\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- SCIM provisioning, bearer-token authority and object ownership concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer disclosure\.

**Reviewed:** 2026-10-03T16:19:37Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary source reviewed; no independent reproduction or deployment assessment\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-05-31; precision: day; basis: explicit; source: [SCIM personal-provider ownership advisory](<https://github.com/better-auth/better-auth/security/advisories/GHSA-j8v8-g9cx-5qf4>) (source ID: advisory). Maintainer advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition established\.
- **source displayed:** 2026-05-31; precision: day; basis: explicit; source: [SCIM personal-provider ownership advisory](<https://github.com/better-auth/better-auth/security/advisories/GHSA-j8v8-g9cx-5qf4>) (source ID: advisory). Maintainer advisory publication date\.

## Caveats

- Exposure requires multiple signed-in users, personal providers and disabled ownership enforcement; organization-bound providers use separate checks\. Affected versions are 1\.5\.0 through 1\.7\.0-beta\.3\.
- The advisory identifies fixes in 1\.7\.0-beta\.4 and 1\.7\.0; the 1\.6\.x line requires mitigation\. The June 2, 2026 vendor bulletin independently identifies the SCIM-specific beta fix, rather than treating its general stable-release guidance as sufficient\.
- gustavovalverde published the notice; Jvr2022 is credited as reporter\. Impact is maintainer-reported; compromise of a deployed instance is not established\. Patch-release dates remain unverified and are not resource-edition dates\.

## Sources and attribution

- [SCIM personal-provider ownership advisory](<https://github.com/better-auth/better-auth/security/advisories/GHSA-j8v8-g9cx-5qf4>) — Better Auth; source ID: advisory; provenance: official primary; retrieved 2026-10-03T16:19:37Z; supports: summary, dates, version.
- [Security update: June 2026](<https://better-auth.com/blog/security-update-june-2026>) — Better Auth; source ID: bulletin; provenance: official primary; retrieved 2026-10-03T16:19:37Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
