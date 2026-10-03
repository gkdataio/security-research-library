# Spree: cart association must retain guest-possession checks

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/spree-2026-guest-cart-association-authority.json>) · [Official resource](<https://github.com/spree/spree/security/advisories/GHSA-4825-p4xm-pcf2>)

**Publisher:** Spree  
**Authors:** damianlegawiec  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Business Logic and State Integrity  
**Defensive skills:** Model access-control invariants; Verify remediation evidence

## Original summary

CVE-2026-94462 concerns a guest-cart ownership transition that required a signed-in customer but omitted the cart-possession check enforced by sibling operations\. Account authentication and object lookup were treated as sufficient authority to claim an unowned cart, exposing existing checkout addresses and changing ownership\.

## Defensive use

Editorial lesson: joining guest state to an account is a privileged ownership transition\. Verify existing possession before mutation and response serialization; client-supplied proof helps only when the server checks it\. The maintainer recommends backend releases 5\.4\.4 or 5\.5\.4 and says its storefront already supplied the required cart token\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic object-level authorization and policy-composition concepts

## Access and freshness

**Access cost at review:** free.

Public primary advisory readable without an account\.

**Reviewed:** 2026-10-03T15:19:23Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary maintainer advisory reviewed\. No live testing, independent reproduction or deployment verification performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-07-20; precision: day; basis: explicit; source: [Spree guest-cart association access-control advisory \(GHSA-4825-p4xm-pcf2\)](<https://github.com/spree/spree/security/advisories/GHSA-4825-p4xm-pcf2>) (source ID: advisory). Publication date displayed by the primary maintainer advisory\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-07-20; precision: day; basis: explicit; source: [Spree guest-cart association access-control advisory \(GHSA-4825-p4xm-pcf2\)](<https://github.com/spree/spree/security/advisories/GHSA-4825-p4xm-pcf2>) (source ID: advisory). Publication date displayed by the primary maintainer advisory\.

## Caveats

- Requires an authenticated store account, guest checkout enabled and an unassociated cart; address disclosure additionally requires stored checkout addresses\. The advisory reports limited, recoverable cart reassignment and email changes, not anonymous access or account takeover\.
- The primary advisory supplies technical impact analysis; no production incident or independently reproduced outcome is established\.
- Published July 20, 2026 by damianlegawiec; reporter laijunyue is credited\. The affected-version shorthand starts at 5\.4\.0 without an upper bound; use the stated patched branches rather than extrapolating\. Software patch dates are unestablished and are not resource-edition dates\.

## Sources and attribution

- [Spree guest-cart association access-control advisory \(GHSA-4825-p4xm-pcf2\)](<https://github.com/spree/spree/security/advisories/GHSA-4825-p4xm-pcf2>) — Spree; source ID: advisory; provenance: official primary; retrieved 2026-10-03T15:19:23Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
