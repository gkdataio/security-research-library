# Astro: composable dispatch must preserve mandatory origin checks

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/astro-2026-composable-dispatch-origin-enforcement.json>) · [Official resource](<https://github.com/withastro/astro/security/advisories/GHSA-8mv7-9c27-98vc>)

**Publisher:** Astro  
**Authors:** matthewp  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Verification  
**Defensive skills:** Threat-model integrations; Model access-control invariants; Verify remediation evidence

## Original summary

The maintainer describes origin enforcement attached to optional middleware while independently composed dispatchers could invoke application handlers first\. The resulting cross-site request forgery can change state using browser credentials but cannot read cross-origin responses\. Conceptual failure: a security setting did not guarantee enforcement along every path to a protected operation\.

## Defensive use

The advisory identifies 7\.0\.5 as patched, moving equivalent checks to dispatch boundaries so composition order cannot remove them\. Editorial lesson: review mandatory controls as invariants of each protected operation, not assumptions about wrapper ordering\. Local regression coverage should establish that composition changes preserve rejection before side effects\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Server-rendered applications and framework composition
- Trust-boundary modeling and application authorization

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory\.

**Reviewed:** 2026-10-03T15:39:32Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory read\. No live testing or independent patch execution performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-07-17; precision: day; basis: explicit; source: [composable astro/hono pipeline bypasses security\.checkOrigin when middleware\(\) is absent or misordered](<https://github.com/withastro/astro/security/advisories/GHSA-8mv7-9c27-98vc>) (source ID: advisory). Explicit advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No educational-resource edition established; software patch chronology is separate\.
- **source displayed:** 2026-07-17; precision: day; basis: explicit; source: [composable astro/hono pipeline bypasses security\.checkOrigin when middleware\(\) is absent or misordered](<https://github.com/withastro/astro/security/advisories/GHSA-8mv7-9c27-98vc>) (source ID: advisory). Explicit advisory publication date\.

## Caveats

- CVE-2026-73423\. Applicability requires the composable astro/hono pipeline with omitted or late middleware; the default pipeline is excluded\.
- The affected-version field says at least 7\.0\.0 without an upper bound, while the patch field names 7\.0\.5\. Preserve that source inconsistency\. matthewp published the advisory; jlgore is credited as reporter\.
- Exact patch-release date was not established\. Actual business consequences depend on application handlers; production exploitation is not established\.
- No bounty or production compromise is established\. Learning prerequisites and generalized defensive reasoning are editorial\.

## Sources and attribution

- [composable astro/hono pipeline bypasses security\.checkOrigin when middleware\(\) is absent or misordered](<https://github.com/withastro/astro/security/advisories/GHSA-8mv7-9c27-98vc>) — Astro; source ID: advisory; provenance: official primary; retrieved 2026-10-03T15:39:32Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
