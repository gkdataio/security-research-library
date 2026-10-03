# Sylius: order ownership does not confer payment-operation authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/sylius-2026-payment-action-authority.json>) · [Official resource](<https://github.com/Sylius/Sylius/security/advisories/GHSA-2rv4-pjmm-7fxf>)

**Publisher:** Sylius  
**Authors:** TheMilek  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Business Logic and State Integrity; Authorization  
**Defensive skills:** Model access-control invariants; Review approval-state integrity; Threat-model integrations

## Original summary

The advisory distinguishes ownership of an order from authority over its payment operations\. Customer-context requests were constrained by ownership but not by operation\. A connected payment provider could therefore change financial state while local order status still indicated payment completion\.

## Defensive use

Editorial lesson: define operation permissions independently from object ownership, and reconcile provider outcomes with local fulfillment state\. The advisory recommends rejecting disallowed customer-context operations before effects\. Maintainer release notes corroborate remediation in 2\.1\.16 and 2\.2\.9\.

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

- **published:** 2026-09-02; precision: day; basis: explicit; source: [Shop API accepts arbitrary PaymentRequest actions, allowing a customer-triggered refund](<https://github.com/Sylius/Sylius/security/advisories/GHSA-2rv4-pjmm-7fxf>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-09-02; precision: day; basis: explicit; source: [Shop API accepts arbitrary PaymentRequest actions, allowing a customer-triggered refund](<https://github.com/Sylius/Sylius/security/advisories/GHSA-2rv4-pjmm-7fxf>) (source ID: advisory).

## Caveats

- Affected ranges are listed as 2\.0\.0 through versions before 2\.1\.16, and 2\.2\.0 through versions before 2\.2\.9\.
- Impact is conditional on an enabled production API and a gateway exposing the relevant financial operations\. The advisory explicitly excludes a plain default installation lacking that gateway\.
- The maintainer describes financial-state inconsistency and consequent merchant-loss risk, not a documented production loss\. This review does not independently verify those outcomes\.
- TheMilek published the advisory; acirtautas is credited as finder\. The reviewed advisory displays no known CVE; no identifier is inferred from secondary indexing\.
- Both release pages display September 2 without a year in the reviewed rendering\. Full patch dates are not asserted; the educational resource edition remains unknown\.

## Sources and attribution

- [Shop API accepts arbitrary PaymentRequest actions, allowing a customer-triggered refund](<https://github.com/Sylius/Sylius/security/advisories/GHSA-2rv4-pjmm-7fxf>) — Sylius; source ID: advisory; provenance: official primary; retrieved 2026-10-03T13:59:30Z; supports: summary, version, dates.
- [Sylius v2\.1\.16 security release](<https://github.com/Sylius/Sylius/releases/tag/v2.1.16>) — Sylius; source ID: release-21; provenance: official primary; retrieved 2026-10-03T13:59:30Z; supports: version, dates.
- [Sylius v2\.2\.9 security release](<https://github.com/Sylius/Sylius/releases/tag/v2.2.9>) — Sylius; source ID: release-22; provenance: official primary; retrieved 2026-10-03T13:59:30Z; supports: version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
