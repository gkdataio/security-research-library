# Paymenter: refund entitlement and ledger changes need one atomic transition

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/paymenter-2026-refund-transition-atomicity.json>) · [Official resource](<https://github.com/Paymenter/Paymenter/security/advisories/GHSA-5gmm-hjfj-8ff7>)

**Publisher:** Paymenter  
**Authors:** CorwinDev  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Business Logic and State Integrity; Authorization  
**Defensive skills:** Reason about concurrent state; Review approval-state integrity; Verify remediation evidence

## Original summary

The maintainer traces duplicate downgrade credits to an eligibility check separated from the later balance change, without transactional isolation\. A pending-operation guard did not protect the whole transition\. The failed invariant was one legitimate refund per service downgrade\.

## Defensive use

Editorial lesson: model refund eligibility, transition identity and ledger mutation as one atomic decision\. Local regression checks should establish that repeated or overlapping processing cannot mint additional entitlement\. The advisory identifies 1\.5\.7 as patched; its release notes explicitly link the fix\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic application state machines, authorization and database transaction concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and release notes\.

**Reviewed:** 2026-10-03T13:59:30Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory and release evidence reviewed; no live testing or independent incident verification\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08-13; precision: day; basis: explicit; source: [Credit-refund double-spend race condition in service downgrade \(doUpgrade\)](<https://github.com/Paymenter/Paymenter/security/advisories/GHSA-5gmm-hjfj-8ff7>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-08-13; precision: day; basis: explicit; source: [Credit-refund double-spend race condition in service downgrade \(doUpgrade\)](<https://github.com/Paymenter/Paymenter/security/advisories/GHSA-5gmm-hjfj-8ff7>) (source ID: advisory).

## Caveats

- Affected versions are listed as 1\.5\.6 and earlier\. The reported scenario requires an authenticated customer and an active service eligible for downgrade\.
- The maintainer reports excess spendable credit and potential operator loss, but supplies no production incident or independently measured loss\. This review does not establish deployment exposure\.
- CorwinDev published the advisory and is credited for remediation; Pig-Tail is credited as reporter\. The advisory assigns CVE-2026-71537\.
- The release page displays July 25 without a year in the reviewed rendering\. No full patch-release date is asserted\. Resource edition and version-release date remain null\.

## Sources and attribution

- [Credit-refund double-spend race condition in service downgrade \(doUpgrade\)](<https://github.com/Paymenter/Paymenter/security/advisories/GHSA-5gmm-hjfj-8ff7>) — Paymenter; source ID: advisory; provenance: official primary; retrieved 2026-10-03T13:59:30Z; supports: summary, version, dates.
- [Paymenter v1\.5\.7 release](<https://github.com/Paymenter/Paymenter/releases/tag/v1.5.7>) — Paymenter; source ID: release; provenance: official primary; retrieved 2026-10-03T13:59:30Z; supports: version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
