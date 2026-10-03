# Nuxt: rendered-data caches must preserve request authorization

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/nuxt-2026-rendered-payload-cache-authorization.json>) · [Official resource](<https://github.com/nuxt/nuxt/security/advisories/GHSA-wm8w-6qjm-cv43>)

**Publisher:** Nuxt  
**Authors:** danielroe  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Verification; Authorization  
**Defensive skills:** Model access-control invariants; Review artifact isolation; Verify remediation evidence

## Original summary

CVE-2026-71316 documents an authorization mismatch between server-rendered HTML and extracted data\. A shared path-keyed payload cache omitted requester identity and returned data before current-request guards\. The maintainer confirms cross-user and unauthenticated disclosure while HTML remained protected\. Application-specific secrets are possible contents, not independently observed production losses\.

## Defensive use

The advisory identifies 4\.5\.1 as fixed by limiting shared payload caching to prerendering and restoring runtime authorization\. Official release notes corroborate the fix and recommend clearing upstream caches\. Editorial lesson: treat each rendered representation as a separate disclosure boundary; correct HTML protection does not prove data-response protection\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Server-side rendering and client data hydration
- Cache partitioning and request authorization

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and release notes\.

**Reviewed:** 2026-10-03T08:19:27Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory and official release reviewed\. No reproduction or independent patch testing performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-07-27; precision: day; basis: explicit; source: [Nuxt runtime payload cache discloses another user's SSR data across users and to unauthenticated clients](<https://github.com/nuxt/nuxt/security/advisories/GHSA-wm8w-6qjm-cv43>) (source ID: advisory). Maintainer advisory publication, not software-release chronology\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource-edition release established\.
- **source displayed:** 2026-07-27; precision: day; basis: explicit; source: [Nuxt runtime payload cache discloses another user's SSR data across users and to unauthenticated clients](<https://github.com/nuxt/nuxt/security/advisories/GHSA-wm8w-6qjm-cv43>) (source ID: advisory). Advisory publication date\.

## Caveats

- Exposure requires affected Nuxt 4\.4\.0–4\.5\.0, cached routes with runtime payload extraction, and user-specific server-rendered data\. Nuxt 3\.x is excluded by the advisory\.
- The advisory credits quantumshiro as finder; danielroe is the publishing maintainer\.
- No production incident or bounty amount established\. Learning prerequisites and generalized review guidance are editorial\.
- The software-release page displays July 27 without a year in the retrieved rendering\. No exact software-release date is inferred; advisory publication is independently explicit\.

## Sources and attribution

- [Nuxt runtime payload cache discloses another user's SSR data across users and to unauthenticated clients](<https://github.com/nuxt/nuxt/security/advisories/GHSA-wm8w-6qjm-cv43>) — Nuxt; source ID: advisory; provenance: official primary; retrieved 2026-10-03T08:19:27Z; supports: summary, dates.
- [Nuxt v4\.5\.1 release](<https://github.com/nuxt/nuxt/releases/tag/v4.5.1>) — Nuxt; source ID: release; provenance: official primary; retrieved 2026-10-03T08:19:27Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
