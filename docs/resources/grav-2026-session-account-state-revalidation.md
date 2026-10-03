# Grav API: account-disable enforcement across session authenticators

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/grav-2026-session-account-state-revalidation.json>) · [Official resource](<https://github.com/getgrav/grav/security/advisories/GHSA-7qfj-82q8-frw6>)

**Publisher:** Grav  
**Authors:** rhukster  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; Business Logic and State Integrity  
**Defensive skills:** Review identity lifecycle; Model access-control invariants; Verify remediation evidence

## Original summary

GHSA-7qfj-82q8-frw6 describes inconsistent account-disable enforcement across authentication methods\. Existing browser or remembered sessions could retain API authority because refreshed permissions did not also establish current account validity\.

## Defensive use

Editorial lesson: authentication state is a revocable claim\. Every authentication method should enforce the same account-lifecycle invariants, and failed account refresh must remove authority rather than preserve cached permission\. The advisory proposes requiring a freshly loaded, enabled account and failing closed on refresh errors\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic understanding of authentication, account state and authorization

## Access and freshness

**Access cost at review:** free.

Public maintainer disclosure\.

**Reviewed:** 2026-10-03T13:09:31Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory reviewed; no deployment assessment or independent reproduction performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-09-23; precision: day; basis: explicit; source: [Disabled grav-plugin-api accounts retain access through existing sessions](<https://github.com/getgrav/grav/security/advisories/GHSA-7qfj-82q8-frw6>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition date established; software fix versions are discussed separately\.
- **source displayed:** 2026-09-23; precision: day; basis: explicit; source: [Disabled grav-plugin-api accounts retain access through existing sessions](<https://github.com/getgrav/grav/security/advisories/GHSA-7qfj-82q8-frw6>) (source ID: advisory).

## Caveats

- Requires an already authorized session belonging to the subsequently disabled account\. The maintainer describes static-review findings, not a demonstrated production compromise\. Retained access is bounded by prior permissions and session lifetime; no additional privilege is claimed\.
- Remediation evidence conflicts: advisory metadata names 1\.0\.36 as patched, while its body says a fix is not yet released\. It lists affected versions through 1\.0\.35\. Release availability and fix date are not independently established here\.
- rhukster published the advisory and credits AlpetGexha as reporter\. Original report date is unknown\. Learning prerequisites and the invariant formulation are editorial\.

## Sources and attribution

- [Disabled grav-plugin-api accounts retain access through existing sessions](<https://github.com/getgrav/grav/security/advisories/GHSA-7qfj-82q8-frw6>) — Grav; source ID: advisory; provenance: official primary; retrieved 2026-10-03T13:09:31Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
