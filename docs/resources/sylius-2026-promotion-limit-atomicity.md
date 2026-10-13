# Sylius: promotion entitlement must be checked and consumed atomically

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/Sylius/Sylius/security/advisories/GHSA-7mp4-25j8-hp5q>) · [Canonical JSON](<../../data/resources/sylius-2026-promotion-limit-atomicity.json>)

<a id="original-summary"></a>
## Main takeaway

Sylius could exceed promotion limits because eligibility checks and recorded usage were not kept in sync during overlapping orders\. The maintainer describes stale counts and lost concurrent updates affecting promotion-wide, coupon and per-customer limits\. A limited promotion or coupon is required, but authentication is not; financial loss is a possible consequence rather than a measured production incident\.

## Defensive use

Editorial lesson: model the limit check and entitlement consumption as one serialized decision\. Accounting correctness alone does not prove eligibility correctness\. In owned local models, verify that committed usage never exceeds the authorized allowance, including cancellation semantics\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Sylius  
**Authors:** NoResponseMate  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Business Logic and State Integrity  
**Defensive skills:** Reason about concurrent state; Review approval-state integrity; Verify remediation evidence

## Prerequisites

**Basis:** editorial guidance.

- Basic authorization, application state machines and database transaction concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer evidence\.

**Reviewed:** 2026-10-03T15:59:29Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Public primary evidence reviewed; no live testing or independent deployment verification\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-03-09; precision: day; basis: explicit; source: [Promotion Usage Limit Bypass via Race Condition](<https://github.com/Sylius/Sylius/security/advisories/GHSA-7mp4-25j8-hp5q>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-03-09; precision: day; basis: explicit; source: [Promotion Usage Limit Bypass via Race Condition](<https://github.com/Sylius/Sylius/security/advisories/GHSA-7mp4-25j8-hp5q>) (source ID: advisory).

## Caveats

- The maintainer reports limit overruns without required authentication; a limited promotion or coupon and overlapping order processing are prerequisites\. Financial loss is a potential consequence, not a measured production incident\.
- The advisory lists fixes in 1\.9\.12, 1\.10\.16, 1\.11\.17, 1\.12\.23, 1\.13\.15, 1\.14\.18, 2\.0\.16, 2\.1\.12 and 2\.2\.3\. Consult its branch-specific affected ranges\. Patch dates are not asserted; resource edition remains null\.
- NoResponseMate published the advisory\. Reporters are Djibril Mounkoro \(whiteov3rflow\) and Bartłomiej Nowiński \(bnBart\); CVE-2026-31824\.

## Sources and attribution

- [Promotion Usage Limit Bypass via Race Condition](<https://github.com/Sylius/Sylius/security/advisories/GHSA-7mp4-25j8-hp5q>) — Sylius; source ID: advisory; provenance: official primary; retrieved 2026-10-03T15:59:29Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
