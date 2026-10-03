# OpenFGA: policy intersections must preserve explicit exclusions

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/openfga-2026-composed-policy-exclusion-integrity.json>) · [Official resource](<https://github.com/openfga/openfga/security/advisories/GHSA-g3pg-frfm-pr2m>)

**Publisher:** OpenFGA  
**Authors:** justincoh  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Business Logic and State Integrity  
**Defensive skills:** Model access-control invariants; Verify remediation evidence

## Original summary

CVE-2026-61709 describes incorrect authorization-policy evaluation in user enumeration\. Under a particular composition of wildcard membership, exclusion and intersection, a user denied by one policy component could reappear in the result through another component\. The failed boundary is preservation of explicit denial when combining permission sets\.

## Defensive use

Editorial lesson: reason about policy results as complete sets, including exclusions, rather than merging positive membership alone\. Design contained regression cases that compare composed policy outcomes with their intended semantics\. The maintainer recommends OpenFGA 1\.18\.1 or later and lists Helm chart 0\.3\.10 as patched\.

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

- **published:** 2026-07-16; precision: day; basis: explicit; source: [OpenFGA Improper Policy Enforcement](<https://github.com/openfga/openfga/security/advisories/GHSA-g3pg-frfm-pr2m>) (source ID: advisory). Publication date displayed by the primary maintainer advisory\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-07-16; precision: day; basis: explicit; source: [OpenFGA Improper Policy Enforcement](<https://github.com/openfga/openfga/security/advisories/GHSA-g3pg-frfm-pr2m>) (source ID: advisory). Publication date displayed by the primary maintainer advisory\.

## Caveats

- Applies when an application relies on ListUsers and its model combines a wildcard-based exclusion with an intersected relation that explicitly grants the excluded user\. This does not establish that all models or authorization APIs are affected\.
- The advisory establishes an incorrect result; downstream unauthorized disclosure depends on application use\. No production incident or independently verified impact is reported\.
- Published July 16, 2026 by justincoh; reporter 5ud0er is credited\. Affected OpenFGA versions are listed through 1\.18\.0, Helm charts through 0\.3\.9\. Patch release dates and resource-edition dates are not established\.

## Sources and attribution

- [OpenFGA Improper Policy Enforcement](<https://github.com/openfga/openfga/security/advisories/GHSA-g3pg-frfm-pr2m>) — OpenFGA; source ID: advisory; provenance: official primary; retrieved 2026-10-03T15:19:23Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
