# Bugsink: time-unit consistency in account-access token expiry

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/bugsink-2026-token-expiry-unit-integrity.json>) · [Official resource](<https://github.com/bugsink/bugsink/security/advisories/GHSA-4f45-qmjf-82cv>)

**Publisher:** Bugsink  
**Authors:** vanschelven  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; Business Logic and State Integrity  
**Defensive skills:** Review identity lifecycle; Review security-token design; Verify remediation evidence

## Original summary

GHSA-4f45-qmjf-82cv describes account-access links whose configured seconds were interpreted as days\. The maintainer reports unused email-verification, password-reset and new-user setup tokens surviving their intended lifetime\.

## Defensive use

Editorial lesson: represent security durations with explicit units and verify expiration independently of single-use behavior\. The maintainer lists versions before 2\.5\.1 as affected and identifies 2\.5\.1 as correcting the unit conversion and removing over-age tokens before acceptance\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic server-side identity and authorization concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer disclosure\.

**Reviewed:** 2026-10-03T10:29:18Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory and release notes reviewed\. Deployment state and source immutability are not established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08-31; precision: day; basis: explicit; source: [Email verification, password-reset, and new-user setup links remain valid beyond their configured lifetime](<https://github.com/bugsink/bugsink/security/advisories/GHSA-4f45-qmjf-82cv>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource-edition release established\. Software patch-release date 2026-08-31 is distinct from resource publication\.
- **source displayed:** 2026-08-31; precision: day; basis: explicit; source: [Email verification, password-reset, and new-user setup links remain valid beyond their configured lifetime](<https://github.com/bugsink/bugsink/security/advisories/GHSA-4f45-qmjf-82cv>) (source ID: advisory).

## Caveats

- Requires possession of an unused token; the advisory says random tokens are not practically guessable\. Access remains within the associated account’s permissions, without adding team or project memberships\. Successful use deletes the token\.
- The source describes possible unauthorized login after expiry, not a documented production compromise or observed theft\. The fix is maintainer-reported; this review did not independently assess deployments or session cleanup\.
- vanschelven published the advisory; no separate reporter is named\. The original report date is unknown\. Learning prerequisites are editorial\.

## Sources and attribution

- [Email verification, password-reset, and new-user setup links remain valid beyond their configured lifetime](<https://github.com/bugsink/bugsink/security/advisories/GHSA-4f45-qmjf-82cv>) — Bugsink; source ID: advisory; provenance: official primary; retrieved 2026-10-03T10:29:18Z; supports: summary, version, dates.
- [Bugsink changelog: 2\.5\.1](<https://github.com/bugsink/bugsink/blob/main/CHANGELOG.md>) — Bugsink; source ID: release-notes; provenance: official primary; retrieved 2026-10-03T10:29:18Z; supports: version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
