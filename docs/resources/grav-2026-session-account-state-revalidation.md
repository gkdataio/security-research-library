# Grav API: account-disable enforcement across session authenticators

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/grav-2026-session-account-state-revalidation.json>) · [Official resource](<https://github.com/getgrav/grav/security/advisories/GHSA-7qfj-82q8-frw6>)

**Publisher:** Grav  
**Authors:** rhukster  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; Business Logic and State Integrity  
**Defensive skills:** Review identity lifecycle; Model access-control invariants; Verify remediation evidence

## Original summary

GHSA-7qfj-82q8-frw6 describes inconsistent account-disable enforcement across authentication methods\. Existing browser or remembered sessions could retain API authority because refreshed permissions did not also establish current account validity\.

## Defensive use

Editorial lesson: authentication state is a revocable claim\. Every authentication method should enforce the same account-lifecycle invariants, and failed account refresh must remove authority rather than preserve cached permission\. The advisory describes requiring a freshly loaded, enabled account and failing closed on refresh errors\. The official 1\.0\.36 release notes state that disabling or deleting an account immediately terminates its API sessions; this is maintainer-stated remediation, not an independently tested result\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic understanding of authentication, account state and authorization

## Access and freshness

**Access cost at review:** free.

Public maintainer disclosure\.

**Reviewed:** 2026-10-04T03:23:22Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory, official 1\.0\.36 release notes and GitHub release metadata reviewed; release availability and maintainer-stated remediation are established, but no deployment assessment or independent patch test was performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-09-23; precision: day; basis: explicit; source: [Disabled grav-plugin-api accounts retain access through existing sessions](<https://github.com/getgrav/grav/security/advisories/GHSA-7qfj-82q8-frw6>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition date established; software fix versions are discussed separately\.
- **source displayed:** 2026-09-23; precision: day; basis: explicit; source: [Disabled grav-plugin-api accounts retain access through existing sessions](<https://github.com/getgrav/grav/security/advisories/GHSA-7qfj-82q8-frw6>) (source ID: advisory).

## Caveats

- Requires an already authorized session belonging to the subsequently disabled account\. The maintainer describes static-review findings, not a demonstrated production compromise\. Retained access is bounded by prior permissions and session lifetime; no additional privilege is claimed\.
- The advisory lists affected versions through 1\.0\.35 and names 1\.0\.36 as patched, but its body still says no patch is available\. That stale internal discrepancy remains in the advisory\. The separately reviewed official 1\.0\.36 release and notes establish release availability and maintainer-stated session-revocation remediation, not independent verification of patch effectiveness\.
- Official GitHub release metadata records 1\.0\.36 as published on 2026-09-19 at 00:06:19 UTC, before the advisory's 2026-09-23 publication\. This is the software release chronology, not the educational resource's edition date, the original report date or a verified deployment-fix date; dates\.version\_released remains null\.
- rhukster published the advisory and credits AlpetGexha as reporter; the 1\.0\.36 release notes also credit AlpetGexha for the account-session remediation\. Original report date is unknown\. Learning prerequisites and the invariant formulation are editorial\.

## Sources and attribution

- [Disabled grav-plugin-api accounts retain access through existing sessions](<https://github.com/getgrav/grav/security/advisories/GHSA-7qfj-82q8-frw6>) — Grav; source ID: advisory; provenance: official primary; retrieved 2026-10-04T03:21:15Z; supports: summary, version, dates.
- [Grav API 1\.0\.36 release notes](<https://github.com/getgrav/grav-plugin-api/releases/tag/1.0.36>) — Grav; source ID: release-1-0-36; provenance: official primary; retrieved 2026-10-04T03:23:08Z; supports: summary, version.
- [Official GitHub release metadata for Grav API 1\.0\.36](<https://api.github.com/repos/getgrav/grav-plugin-api/releases/tags/1.0.36>) — Grav / GitHub; source ID: release-1-0-36-metadata; provenance: official primary; retrieved 2026-10-04T03:21:15Z; supports: version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
