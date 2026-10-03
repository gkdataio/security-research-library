# Directus: denied mutations must leave dependent state unchanged

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/directus-2026-preauthorization-side-effect-integrity.json>) · [Official resource](<https://github.com/directus/directus/security/advisories/GHSA-p623-wgx3-wxp8>)

**Publisher:** Directus  
**Authors:** br41nslug  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Business Logic and State Integrity  
**Defensive skills:** Model access-control invariants; Review approval-state integrity; Verify remediation evidence

## Original summary

GHSA-p623-wgx3-wxp8 describes service overrides committing cleanup before their superclass checked permission\. Rejected mutations could therefore disconnect automation links, remove attribution metadata or invalidate permission caches\. A denial response did not mean that the operation left application state unchanged\.

## Defensive use

Editorial lesson: include cleanup, cache invalidation and relationship changes in the authorization boundary, and assess state preservation on rejected operations\. The maintainer says 12\.1\.0 moves access checks before side effects or defers effects until an authorized mutation succeeds\. PR 27800 independently corroborates the ordering correction\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic server-side authorization and persistent-state concepts

## Access and freshness

**Access cost at review:** free.

Public primary disclosure readable without an account\.

**Reviewed:** 2026-10-03T12:29:14Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory and maintainer remediation evidence reviewed; no target testing or deployment verification performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08-05; precision: day; basis: explicit; source: [Directus pre-authorization side effects advisory](<https://github.com/directus/directus/security/advisories/GHSA-p623-wgx3-wxp8>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-08-05; precision: day; basis: explicit; source: [Directus pre-authorization side effects advisory](<https://github.com/directus/directus/security/advisories/GHSA-p623-wgx3-wxp8>) (source ID: advisory).

## Caveats

- The maintainer lists versions before 12\.1\.0 as affected\. The automation impact requires knowledge of the affected flow identifier; the advisory describes anonymous as well as unauthorized callers\.
- The advisory reports state changes, not a production incident\. It explicitly excludes content disclosure and privilege elevation; impact is confined to availability, cached state and specified attribution fields\.
- Published August 5, 2026 by br41nslug; tr4ce-ju is credited as reporter\. PR 27800 merged July 1, 2026\. The release page displays July 1 and includes that fix; its rendered timestamp omits the year, so the review does not independently assert a full software release date\.
- The advisory identifies 12\.1\.0 as patched but does not establish restoration of previously lost state\. No in-application workaround is supplied\. The resource edition date remains unknown; software chronology is recorded separately\.

## Sources and attribution

- [Directus pre-authorization side effects advisory](<https://github.com/directus/directus/security/advisories/GHSA-p623-wgx3-wxp8>) — Directus; source ID: advisory; provenance: official primary; retrieved 2026-10-03T12:29:14Z; supports: summary, version, dates.
- [Fix side effects in service overrides](<https://github.com/directus/directus/pull/27800>) — Directus; source ID: patch; provenance: official primary; retrieved 2026-10-03T12:29:14Z; supports: summary, dates.
- [Directus v12\.1\.0 release](<https://github.com/directus/directus/releases/tag/v12.1.0>) — Directus; source ID: release; provenance: official primary; retrieved 2026-10-03T12:29:14Z; supports: version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
