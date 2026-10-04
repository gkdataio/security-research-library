# Google API field masks: preserve server-owned and immutable state

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/google-aip-161-update-field-authority.json>) · [Official resource](<https://google.aip.dev/161>)

**Publisher:** Google  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Business Logic and State Integrity; Web Foundations  
**Defensive skills:** Model access-control invariants; Review input trust boundaries

## Original summary

Google's Approved field-mask guidance defines which resource fields participate in an update\. Services must ignore output-only input whether selected directly or through a containing field\. Supporting field-behavior guidance says unchanged immutable values should be ignored, while requested changes should return INVALID\_ARGUMENT\. Its annotations describe behavior but add no validation themselves\.

## Defensive use

Editorial synthesis: document caller authorization, the selected change set and server-enforced field mutability as separate contracts\. Valid field selection does not establish permission to change it\. Preserve each nested field's behavior independently of its parent, and keep business-state transitions outside generic updates when the API contract requires dedicated operations\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic familiarity with resource-oriented APIs, partial updates and access-control modeling

## Access and freshness

**Access cost at review:** free.

Public official Google API design and implementation guidance\.

**Reviewed:** 2026-10-04T08:05:38Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed AIP-161 and supporting AIP-203/AIP-134, each shown as Approved, plus first-party commits distinguishing displayed changelog dates from later source maintenance\. Documentation review only; no implementation was assessed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. The pages' Created fields do not establish original publication of their current text\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No dated educational-resource edition is established for this living guidance\.
- **source displayed:** 2023-10-18; precision: day; basis: explicit; source: [AIP-161: Field masks](<https://google.aip.dev/161>) (source ID: primary). Newest displayed AIP-161 Changelog entry, concerning output-only fields in update masks\. It is not original publication, an edition release or the current text's last revision date\.

## Caveats

- AIP-161's Created and Updated headers both show 2021-03-01\. Its displayed output-only changelog date is 2023-10-18, while the corresponding first-party commit is timestamped 2023-10-19T15:57:39Z\. A later 2025-03-28 commit added an AIP-157 link; neither header nor newest displayed changelog establishes the last source revision\.
- AIP-203's headers show 2018-07-17 and its newest displayed changelog entry is 2023-09-14, although a reviewed 2026-06-25 commit adds an optional-field clarification\. AIP-134's headers show 2019-01-24 while its newest displayed changelog entry is 2025-10-03\. These dates are not interchangeable publication or edition dates\.
- AIP-203 forbids an error merely because output-only input is present and requires it to be cleared or ignored\. This differs from immutable input, for which unchanged values should be ignored and changes should cause a validation error\. Nested field behavior is independent of its parent's annotation\.
- AIP-134 says generic updates should avoid side effects and state fields must not be directly writable through them\. The separation of field selection from caller authorization is editorial synthesis; these AIPs' explicit rules concern field behavior and update semantics\.
- These are Google API design requirements, not universal protocol guarantees or proof that a particular service enforces them\. This resource establishes no incident, affected deployment, bounty, exploitability or testing authorization\.

## Sources and attribution

- [AIP-161: Field masks](<https://google.aip.dev/161>) — Google; source ID: primary; provenance: official primary; retrieved 2026-10-04T08:02:47Z; supports: summary, dates.
- [AIP-203: Field behavior documentation](<https://google.aip.dev/203>) — Google; source ID: field-behavior; provenance: official primary; retrieved 2026-10-04T08:02:58Z; supports: summary, dates.
- [AIP-134: Standard methods: Update](<https://google.aip.dev/134>) — Google; source ID: standard-update; provenance: official primary; retrieved 2026-10-04T08:02:58Z; supports: summary, dates.
- [AIP-161/AIP-203: converge output-only update-mask guidance](<https://github.com/aip-dev/google.aip.dev/commit/9d73091cb8519085c695a0d1388f7e35ea9e0686>) — Google AIP maintainers; source ID: output-only-change; provenance: official primary; retrieved 2026-10-04T08:04:34Z; supports: summary, dates.
- [AIP-161: link to AIP-157](<https://github.com/aip-dev/google.aip.dev/commit/ea79190087e673482c2579e6f38c9dbe5a287db2>) — Google AIP maintainers; source ID: field-mask-link-maintenance; provenance: official primary; retrieved 2026-10-04T08:04:34Z; supports: dates.
- [AIP-203: clarify optional field presence and field behavior](<https://github.com/aip-dev/google.aip.dev/commit/1f058efe4558aabe605daaff13b0d18d4563707d>) — Google AIP maintainers; source ID: field-behavior-maintenance; provenance: official primary; retrieved 2026-10-04T08:05:28Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
