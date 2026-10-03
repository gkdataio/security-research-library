# Coder: privileged provisioning must preserve existing object ownership

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/coder-2026-provisioned-object-ownership-integrity.json>) · [Official resource](<https://github.com/coder/coder/security/advisories/GHSA-9rjw-3gwp-f59v>)

**Publisher:** Coder  
**Authors:** jdomeracki-coder  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Business Logic and State Integrity  
**Defensive skills:** Model access-control invariants; Verify remediation evidence

## Original summary

CVE-2026-55429 concerns a provisioning update-or-insert operation that could change an existing workspace application’s ownership relationship without checking the existing workspace\. The maintainer describes potential redirection of subsequent application traffic across workspace boundaries under elevated provisioning authority\.

## Defensive use

Editorial lesson: privileged service execution is not evidence that every referenced object belongs to the initiating workspace\. Enforce ownership invariants at the mutation boundary, including collision/update behavior\. The maintainer patch rejects cross-workspace reassignment while preserving legitimate same-workspace rebuilds and initial claims of unowned objects\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic understanding of server-side object authorization and resource ownership

## Access and freshness

**Access cost at review:** free.

Public sources readable without an account\.

**Reviewed:** 2026-10-03T13:10:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary disclosure and maintainer evidence reviewed; no deployment inspection or vulnerability testing performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-12; precision: day; basis: explicit; source: [Workspace app upsert allows cross-workspace agent rebinding via user-controlled app ID](<https://github.com/coder/coder/security/advisories/GHSA-9rjw-3gwp-f59v>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource edition is stated; software fix chronology is recorded in caveats\.
- **source displayed:** 2026-06-12; precision: day; basis: explicit; source: [Workspace app upsert allows cross-workspace agent rebinding via user-controlled app ID](<https://github.com/coder/coder/security/advisories/GHSA-9rjw-3gwp-f59v>) (source ID: advisory).

## Caveats

- The maintainer requires elevated access as a template author or external provisioner operator\. The stated consequence is application-traffic redirection, including IDE or terminal sessions; no customer incident, measured data loss, or independent reproduction is established here\.
- The advisory credits Anthropic’s Security Team for independent disclosure \(ANT-2026-22441\); the listed author is the advisory publisher account\.
- The advisory lists patched software versions 2\.34\.2, 2\.33\.8, 2\.32\.7, and 2\.29\.17 and no workaround\. Release v2\.34\.2 independently links this fix\. Pull request 26103 merged June 11, 2026; this merge date is not a resource edition date or a deployment date\.
- The maintainer pull request describes regression coverage for ownership transitions, including same-workspace rebuilds and unowned object claims\. This review did not execute those tests or establish that any installation is upgraded\. No award evidence is supplied\.

## Sources and attribution

- [Workspace app upsert allows cross-workspace agent rebinding via user-controlled app ID](<https://github.com/coder/coder/security/advisories/GHSA-9rjw-3gwp-f59v>) — Coder; source ID: advisory; provenance: official primary; retrieved 2026-10-03T13:10:00Z; supports: summary, dates.
- [Prevent cross-tenant workspace app rebinding](<https://github.com/coder/coder/pull/26103>) — Coder; source ID: maintainer-patch; provenance: official primary; retrieved 2026-10-03T13:10:00Z; supports: summary, dates.
- [v2\.34\.2 security release](<https://github.com/coder/coder/releases/tag/v2.34.2>) — Coder; source ID: release; provenance: official primary; retrieved 2026-10-03T13:10:00Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
