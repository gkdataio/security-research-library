# Vikunja: saved favorites must recheck current project access

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/go-vikunja/vikunja/security/advisories/GHSA-jp29-jrxc-92vf>) · [Canonical JSON](<../../data/resources/vikunja-2026-favorites-current-access-revalidation.json>)

<a id="original-summary"></a>
## Main takeaway

Vikunja could keep showing favorited tasks after project access was revoked because search did not recheck current permissions\. The maintainer reports that updated titles and descriptions remained readable, despite direct task reads being denied\. This requires prior write-level sharing and favorites saved while authorized; the read-only exposure is limited to those tasks\.

## Defensive use

Editorial lesson: saved associations express preference, not continuing authority\. Every query branch returning an object should enforce its current authorization policy, including alternate views and aggregates\. The advisory lists 2\.6\.0 as patched; the August 31, 2026 maintainer release article separately confirms this revocation issue was fixed\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Vikunja  
**Authors:** kolaente  
**Resource type:** [Maintainer Advisory](<../resource-types.md#type-maintainer-advisory>)  
**Version:** Not established in the reviewed record  
**Topics:** [Authorization](<../resource-topics.md#topic-authorization>); [Business Logic and State Integrity](<../resource-topics.md#topic-business-logic>)  
**Defensive skills:** [Model access-control invariants](<../skillsets.md#skill-authorization-modeling>); [Review identity lifecycle](<../skillsets.md#skill-identity-lifecycle-review>); [Verify remediation evidence](<../skillsets.md#skill-patch-verification>)

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
