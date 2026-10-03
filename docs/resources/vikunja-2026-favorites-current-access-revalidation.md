# Vikunja: saved favorites must recheck current project access

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/vikunja-2026-favorites-current-access-revalidation.json>) · [Official resource](<https://github.com/go-vikunja/vikunja/security/advisories/GHSA-jp29-jrxc-92vf>)

**Publisher:** Vikunja  
**Authors:** kolaente  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Business Logic and State Integrity  
**Defensive skills:** Model access-control invariants; Review identity lifecycle; Verify remediation evidence

## Original summary

GHSA-jp29-jrxc-92vf describes a task-search branch that trusted a saved favorite without checking current project access\. Favorite records survived share revocation, allowing previously authorized collaborators to keep reading selected tasks through search despite denial by direct task reads\.

## Defensive use

Editorial lesson: saved associations express preference, not continuing authority\. Every query branch returning an object should enforce its current authorization policy, including alternate views and aggregates\. The advisory lists 2\.6\.0 as patched; the August 31, 2026 maintainer release article separately confirms this revocation issue was fixed\.

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

- **published:** 2026-08-31; precision: day; basis: explicit; source: [Favorited tasks remain readable after project access is revoked](<https://github.com/go-vikunja/vikunja/security/advisories/GHSA-jp29-jrxc-92vf>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-08-31; precision: day; basis: explicit; source: [Favorited tasks remain readable after project access is revoked](<https://github.com/go-vikunja/vikunja/security/advisories/GHSA-jp29-jrxc-92vf>) (source ID: advisory).

## Caveats

- Requires prior write-level sharing and a favorite saved while authorized, followed by revocation\. The advisory lists versions through 2\.5\.0 as affected and reports runtime verification on 2\.5\.0\.
- Reported observation: titles and descriptions edited after revocation remained readable\. Impact is read-only and limited to previously favorited tasks; it does not establish access to all project tasks or a production incident\.
- Published August 31, 2026 by kolaente; JellowBeanz26 is credited as reporter\. Software release 2\.6\.0 was announced the same day in the separate maintainer article; this is not a resource-edition date\.
- The advisory proposes current-access filtering and/or favorite cleanup\. Neither reviewed source establishes the exact implemented combination, so these proposals are not represented as verified patch internals\.

## Sources and attribution

- [Favorited tasks remain readable after project access is revoked](<https://github.com/go-vikunja/vikunja/security/advisories/GHSA-jp29-jrxc-92vf>) — Vikunja; source ID: advisory; provenance: official primary; retrieved 2026-10-03T12:29:14Z; supports: summary, version, dates.
- [Vikunja 2\.6\.0: Eighteen security fixes, Planka import, and attachment previews](<https://vikunja.io/changelog/vikunja-2.6.0-was-released/>) — Vikunja; source ID: release; provenance: official primary; retrieved 2026-10-03T12:29:14Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
