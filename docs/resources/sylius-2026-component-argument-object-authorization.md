# Sylius: component integrity does not authorize referenced objects

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://securitylab.github.com/advisories/GHSL-2026-055_Sylius/>) · [Canonical JSON](<../../data/resources/sylius-2026-component-argument-object-authorization.json>)

<a id="original-summary"></a>
## Main takeaway

Sylius checked component-state integrity without checking ownership of every object referenced by action arguments\. GitHub Security Lab demonstrates cross-customer address disclosure by an authenticated customer in version 2\.2\.3-dev; the maintainer also identifies exposure of cart and order financial summaries\. The evidence does not establish write access, payment execution or account takeover\.

## Defensive use

Editorial lesson: integrity protection on component state does not establish authority over every referenced object\. Bind each lookup to the current customer or authorized session context\. The maintainer lists fixes in 2\.0\.16, 2\.1\.12 and 2\.2\.3 and supplies a project-level authorization workaround; its correctness for customized deployments is not established here\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** GitHub Security Lab  
**Authors:** Man Yue Mo  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Web Foundations; API Security; Server/Client Framework Security  
**Defensive skills:** Model access-control invariants; Verify remediation evidence

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

- **published:** 2026-03-17; precision: day; basis: explicit; source: [GHSL-2026-055: Unauthorized access to PII in Sylius - CVE-2026-31820](<https://securitylab.github.com/advisories/GHSL-2026-055_Sylius/>) (source ID: research).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-03-17; precision: day; basis: explicit; source: [GHSL-2026-055: Unauthorized access to PII in Sylius - CVE-2026-31820](<https://securitylab.github.com/advisories/GHSL-2026-055_Sylius/>) (source ID: research).

## Caveats

- Requires an authenticated customer using affected shop components\. The demonstrated research case concerns another customer’s address; the maintainer’s broader scope also covers order summaries because active carts and completed orders share a data model\.
- The research describes controlled cross-customer disclosure, not an observed customer breach\. The reviewed evidence does not establish write access, payment execution or account takeover\.
- GHSL records reporting on February 19, 2026 and maintainer-advisory publication on March 9; detailed research was published March 17\. Exact product release dates are not established by these sources\. Resource edition release remains unknown\.
- The development snapshot tested by GHSL is distinct from the final 2\.2\.3 release named as patched by the maintainer\. No contradiction or remediation failure is inferred from the similar labels\.
- The byline is Man Yue Mo\. Discovery is credited to GitHub Security Lab Taskflow Agent, with manual verification by Peter Stöckli and Man Yue Mo; the maintainer credits both and the GHSL team\. Learning prerequisites are editorial\.

## Sources and attribution

- [GHSL-2026-055: Unauthorized access to PII in Sylius - CVE-2026-31820](<https://securitylab.github.com/advisories/GHSL-2026-055_Sylius/>) — GitHub Security Lab; source ID: research; provenance: official primary; retrieved 2026-10-03T11:30:37Z; supports: summary, dates.
- [IDOR in Cart and Checkout LiveComponents](<https://github.com/Sylius/Sylius/security/advisories/GHSA-2xc6-348p-c2x6>) — Sylius; source ID: maintainer-advisory; provenance: official primary; retrieved 2026-10-03T11:30:37Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
