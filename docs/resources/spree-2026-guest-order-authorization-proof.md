# Spree: guest ownership still requires an authorization proof

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/spree-2026-guest-order-authorization-proof.json>) · [Official resource](<https://securitylab.github.com/advisories/GHSL-2026-029_Spree/>)

**Publisher:** GitHub Security Lab  
**Authors:** Peter Stöckli  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Web Foundations  
**Defensive skills:** Model access-control invariants; Verify remediation evidence

## Original summary

CVE-2026-25757 concerns completed guest orders\. The access decision treated absence of an account owner as sufficient permission, while lookup did not require the separate order token\. GHSL identifies the flaw in tested version 5\.2\.6; the maintainer corroborates guest-order disclosure\.

## Defensive use

Editorial lesson: a guest object needs an explicit authorization model even when no account owns it\. Keep object identification separate from evidence of permission\. The maintainer lists patched releases 5\.0\.8, 5\.1\.10, 5\.2\.7 and 5\.3\.2; this record does not independently verify their implementation\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic object-level access-control concepts
- Familiarity with web request and response processing

## Access and freshness

**Access cost at review:** free.

Public primary sources readable without an account\.

**Reviewed:** 2026-10-03T11:30:37Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Research and maintainer advisory reviewed; no deployment or independent reproduction was assessed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-03-12; precision: day; basis: explicit; source: [GHSL-2026-029: Insecure Direct Object Reference \(IDOR\) in Spree - CVE-2026-25757](<https://securitylab.github.com/advisories/GHSL-2026-029_Spree/>) (source ID: research).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-03-12; precision: day; basis: explicit; source: [GHSL-2026-029: Insecure Direct Object Reference \(IDOR\) in Spree - CVE-2026-25757](<https://securitylab.github.com/advisories/GHSL-2026-029_Spree/>) (source ID: research).

## Caveats

- Exposure requires an affected storefront and a completed guest order identifier\. Neither a signed-in account nor victim interaction is required; account-owned orders are not established as affected\.
- The maintainer describes a controlled demonstration exposing guest-order details\. GHSL identifies potential disclosure of names, addresses and phone numbers\. No customer incident, measured data loss, write access or account takeover is established\.
- GHSL records reporting on January 26, 2026 and publication of fixes and the maintainer advisory on February 5\. The detailed research was published March 12\. Resource edition release remains unknown and is separate from product patch chronology\.
- The maintainer affected-version shorthand is ambiguous; do not interpret it as normalized branch ranges\. Patched versions are reproduced as listed\.
- The research byline is Peter Stöckli\. Discovery is credited to GitHub Security Lab Taskflow Agent, with manual verification by Peter Stöckli and Man Yue Mo\. Learning prerequisites are editorial\.

## Sources and attribution

- [GHSL-2026-029: Insecure Direct Object Reference \(IDOR\) in Spree - CVE-2026-25757](<https://securitylab.github.com/advisories/GHSL-2026-029_Spree/>) — GitHub Security Lab; source ID: research; provenance: official primary; retrieved 2026-10-03T11:30:37Z; supports: summary, dates.
- [Unauthenticated users can view completed guest orders by Order ID](<https://github.com/spree/spree/security/advisories/GHSA-p6pv-q7rc-g4h9>) — Spree; source ID: maintainer-advisory; provenance: official primary; retrieved 2026-10-03T11:30:37Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
