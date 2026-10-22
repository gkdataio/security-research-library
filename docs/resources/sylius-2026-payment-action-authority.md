# Sylius: order ownership does not confer payment-operation authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/Sylius/Sylius/security/advisories/GHSA-2rv4-pjmm-7fxf>) · [Canonical JSON](<../../data/resources/sylius-2026-payment-action-authority.json>)

<a id="original-summary"></a>
## Main takeaway

Sylius checked that customers owned an order but did not adequately limit which payment actions they could request\. The maintainer describes a risk of provider-side financial changes while the local order still appeared paid\. This requires an enabled production API and a gateway supporting the relevant operations; a plain default installation without that gateway is excluded, and actual merchant losses are not documented\.

## Defensive use

Editorial lesson: define operation permissions independently from object ownership, and reconcile provider outcomes with local fulfillment state\. The advisory recommends rejecting disallowed customer-context operations before effects\. Maintainer release notes corroborate remediation in 2\.1\.16 and 2\.2\.9\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Sylius  
**Authors:** TheMilek  
**Resource type:** [Maintainer Advisory](<../resource-types.md#type-maintainer-advisory>)  
**Version:** Not established in the reviewed record  
**Topics:** [Business Logic and State Integrity](<../resource-topics.md#topic-business-logic>); [Authorization](<../resource-topics.md#topic-authorization>)  
**Defensive skills:** [Model access-control invariants](<../skillsets.md#skill-authorization-modeling>); [Review approval-state integrity](<../skillsets.md#skill-approval-state-integrity>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>)

## Prerequisites

**Basis:** editorial guidance.

- Basic application state machines, authorization and database transaction concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and release notes\.

**Reviewed:** 2026-10-06T21:13:14Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Release chronology refreshed from official GitHub metadata; earlier advisory and release-page reviews are retained\. No live testing or independent incident verification\.

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
- Official GitHub release metadata \(release-21-metadata and release-22-metadata\) records v2\.1\.16 published September 2, 2026 at 14:03:30 UTC and v2\.2\.9 at 14:03:48 UTC; both release bodies link GHSA-2rv4-pjmm-7fxf\. These are software patch-release dates, not an educational-resource edition date; dates\.version\_released remains null\.

## Sources and attribution

- [Shop API accepts arbitrary PaymentRequest actions, allowing a customer-triggered refund](<https://github.com/Sylius/Sylius/security/advisories/GHSA-2rv4-pjmm-7fxf>) — Sylius; source ID: advisory; provenance: official primary; retrieved 2026-10-03T13:59:30Z; supports: summary, version, dates.
- [Sylius v2\.1\.16 security release](<https://github.com/Sylius/Sylius/releases/tag/v2.1.16>) — Sylius; source ID: release-21; provenance: official primary; retrieved 2026-10-03T13:59:30Z; supports: version, dates.
- [Sylius v2\.2\.9 security release](<https://github.com/Sylius/Sylius/releases/tag/v2.2.9>) — Sylius; source ID: release-22; provenance: official primary; retrieved 2026-10-03T13:59:30Z; supports: version, dates.
- [Sylius v2\.1\.16 official GitHub release metadata](<https://api.github.com/repos/Sylius/Sylius/releases/tags/v2.1.16>) — Sylius; source ID: release-21-metadata; provenance: official primary; retrieved 2026-10-06T21:10:33Z; supports: dates.
- [Sylius v2\.2\.9 official GitHub release metadata](<https://api.github.com/repos/Sylius/Sylius/releases/tags/v2.2.9>) — Sylius; source ID: release-22-metadata; provenance: official primary; retrieved 2026-10-06T21:10:33Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
