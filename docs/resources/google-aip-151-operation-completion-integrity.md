# Google long-running operations: cancellation requests and completion evidence

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/google-aip-151-operation-completion-integrity.json>) · [Official resource](<https://google.aip.dev/151>)

**Publisher:** Google  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Business Logic and State Integrity; Web Foundations  
**Defensive skills:** Reason about concurrent state; Threat-model integrations; Review secure error behavior

## Original summary

Google's approved long-running-operation guidance separates failures before work starts from failures during execution\. Its linked Operation contract distinguishes best-effort cancellation, terminal outcomes and deletion of the tracking resource\. Work may finish despite a cancellation request; a returned wait response can still describe pending work\.

## Defensive use

Editorial synthesis: keep client intent, control acknowledgements, terminal operation evidence and business effects separate\. An application should not mark an action reversed or release a reserved entitlement merely because cancellation was requested\. Define the service-specific evidence needed to reconcile the outcome and any already-committed effects\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic asynchronous API and application state-machine concepts

## Access and freshness

**Access cost at review:** free.

The official AIP and linked first-party operation contract were readable without sign-in\.

**Reviewed:** 2026-10-04T12:14:17Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Official AIP, pinned operation contract and first-party error-guidance change reviewed\. Maintained guidance without a numbered edition; the review date does not make it newly published guidance\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Original publication was not established\. The Created header does not establish publication of the current text\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separately dated educational edition was established\.
- **source displayed:** 2025-02-04; precision: day; basis: explicit; source: [AIP-151: Long-running operations](<https://google.aip.dev/151>) (source ID: primary). Newest displayed changelog entry, not publication or latest repository modification\. The page's Created and Updated headers both show 2019-07-25\.

## Caveats

- The linked contract says successful cancellation retains the operation with a CANCELLED error\. Deleting the operation expresses disinterest in its result and does not cancel execution\.
- The done field marks completion, not success; the outcome can be failure or cancellation\. Some services may omit result data, so missing results must not be treated as proof of success\.
- Neither reviewed source guarantees rollback of prior effects or specifies a universal authorization policy for reading, cancelling or deleting operations\. Authorization is therefore not assigned as a topic\.
- The 2025-02-04 changelog entry was committed on 2025-02-07\. These maintenance signals and the 2019-07-25 page headers are distinct from publication or edition-release dates\.
- These are Google API contracts and design guidance, not universal asynchronous-API guarantees, an implementation audit, vulnerability claim, bounty evidence or testing authorization\.

## Sources and attribution

- [AIP-151: Long-running operations](<https://google.aip.dev/151>) — Google; source ID: primary; provenance: official primary; retrieved 2026-10-04T12:11:47Z; supports: summary, dates.
- [Google long-running operation contract at reviewed revision](<https://github.com/googleapis/googleapis/blob/1b141494162fee2993345d056cf709ebf1d0402c/google/longrunning/operations.proto>) — Google; source ID: operation-contract; provenance: official primary; retrieved 2026-10-04T12:12:35Z; supports: summary.
- [AIP-151 error-propagation clarification commit](<https://github.com/aip-dev/google.aip.dev/commit/5209e64b26c564e020690273a1b9fd09e6598e9d>) — Google AIP project; source ID: error-guidance-change; provenance: official primary; retrieved 2026-10-04T12:14:09Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
