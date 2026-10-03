# Vendure: payment child objects must inherit order channel authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/vendure-2026-payment-child-object-channel-authority.json>) · [Official resource](<https://github.com/vendurehq/vendure/security/advisories/GHSA-7qvr-c5vf-xxfh>)

**Publisher:** Vendure  
**Authors:** michaelbromley  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Business Logic and State Integrity  
**Defensive skills:** Model access-control invariants; Threat-model integrations; Verify remediation evidence

## Original summary

Order-level scoping did not carry into globally loaded payment, refund and fulfillment objects\. A channel-limited administrator could affect another channel through child-object operations\. The advisory contrasts scoped order reads with successful unauthorized refund processing, locating the failure at object-resolution and side-effect boundaries\.

## Defensive use

Editorial lesson: derive child-object authority from the parent order and current channel before any external effect\. A later database rejection cannot reliably undo an earlier gateway action\. Review alternate entry points against the same invariant, rather than assuming protected parent reads cover mutations\.

Educational reference only; linked material does not authorize testing unrelated systems.

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

- **published:** 2026-09-02; precision: day; basis: explicit; source: [Cross-channel payment/refund IDOR — money movement across tenants \(payment-side sibling of GHSA-frwg\)](<https://github.com/vendurehq/vendure/security/advisories/GHSA-7qvr-c5vf-xxfh>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-09-02; precision: day; basis: explicit; source: [Cross-channel payment/refund IDOR — money movement across tenants \(payment-side sibling of GHSA-frwg\)](<https://github.com/vendurehq/vendure/security/advisories/GHSA-7qvr-c5vf-xxfh>) (source ID: advisory).

## Caveats

- The reported setting is multi-channel commerce with channel-scoped order-update permission and suitable payment configuration\. The advisory reports controlled refund evidence and potential financial disruption; production losses are not established\.
- The advisory lists versions below 3\.7\.3 as affected and 3\.7\.3 as patched\. Release notes confirm channel enforcement and advise upgrading related packages together\.
- michaelbromley published the advisory; squinard1478 and raysabee are credited reporters\. No CVE is assigned on the reviewed page\.
- The release rendering displays September 2 without a year; no complete patch-release date is asserted\. Resource edition and its release date remain null\.

## Sources and attribution

- [Cross-channel payment/refund IDOR — money movement across tenants \(payment-side sibling of GHSA-frwg\)](<https://github.com/vendurehq/vendure/security/advisories/GHSA-7qvr-c5vf-xxfh>) — Vendure; source ID: advisory; provenance: official primary; retrieved 2026-10-03T15:59:29Z; supports: summary, version, dates.
- [Vendure v3\.7\.3 release](<https://github.com/vendurehq/vendure/releases/tag/v3.7.3>) — Vendure; source ID: release; provenance: official primary; retrieved 2026-10-03T15:59:29Z; supports: version, dates, summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
