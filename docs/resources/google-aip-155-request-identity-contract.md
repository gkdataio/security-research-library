# Google API request identity: bind retry semantics to the logical operation

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://google.aip.dev/155>) · [Canonical JSON](<../../data/resources/google-aip-155-request-identity-contract.json>)

<a id="original-summary"></a>
## Main takeaway

Google's approved request-ID guidance defines how services recognize retries for a service-defined retention period: a duplicate should receive the earlier success response, with a documented exception allowing the current resource state\. AWS's supporting article adds guidance on scoping IDs to callers, keeping response meaning consistent, recording IDs and effects together, and rejecting reuse for a changed intent\. Those AWS recommendations are separate from Google's requirements\.

## Defensive use

Editorial synthesis: distinguish who may act, which logical operation is being repeated and what state was committed\. Document identity scope, retention assumptions and response meaning\. A request ID does not confer authority\. Preventing duplicate effects does not guarantee eventual success or establish end-to-end exactly-once delivery\. Keep each integration's completion and authorization responsibilities explicit\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Google  
**Authors:** Not identified in the reviewed record  
**Resource type:** [Implementation Guide](<../resource-types.md#type-implementation-guide>)  
**Version:** Not established in the reviewed record  
**Topics:** [Business Logic and State Integrity](<../resource-topics.md#topic-business-logic>); [Web Foundations](<../resource-topics.md#topic-web-foundations>); [API Security](<../resource-topics.md#topic-api-security>)  
**Defensive skills:** [Reason about concurrent state](<../skillsets.md#skill-concurrency-reasoning>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>)

## Prerequisites

**Basis:** editorial guidance.

- Basic familiarity with API requests, distributed failures and application state transitions

## Access and freshness

**Access cost at review:** free.

Public official API guidance and supporting architecture article\.

**Reviewed:** 2026-10-04T09:43:28Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed the Approved AIP, its first-party changelog commit and the official AWS supporting article\. Documentation review only; no implementation was assessed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. The page's Created field does not establish publication of its current text\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No dated educational-resource edition is established for this living guidance\.
- **source displayed:** 2024-01-08; precision: day; basis: explicit; source: [AIP-155: Request identification](<https://google.aip.dev/155>) (source ID: primary). Newest displayed AIP-155 Changelog entry; not publication, an edition release or the corresponding commit date\.

## Caveats

- AIP-155 permits APIs to add request IDs and says they should be optional\. The ID belongs to the request, not the resource\. Its guarantees apply to the service's documented contract, not every API\.
- The current-state response exception applies when reproducing the historical success response is infeasible\. Idempotent effects do not require byte-identical response data\.
- Caller scoping, changed-parameter rejection and coordinated identity/effect recording are AWS guidance, not explicit AIP-155 requirements\. AWS describes service-dependent retention; it does not prescribe a universal lifetime\.
- AIP-155's Created and Updated headers both display 2019-05-06\. The corresponding first-party commit is timestamped 2024-01-26T17:45:54Z but adds a 2024-01-08 changelog entry\. These are distinct maintenance signals, not new 2026 guidance\.
- Authorization separation and completion limits are editorial synthesis\. This resource establishes no incident, affected deployment, bounty, implementation correctness, current exposure or testing authorization\.

## Sources and attribution

- [AIP-155: Request identification](<https://google.aip.dev/155>) — Google; source ID: primary; provenance: official primary; retrieved 2026-10-04T09:41:55Z; supports: summary, dates.
- [Making retries safe with idempotent APIs](<https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/>) — Amazon Web Services; source ID: retry-contract-guidance; provenance: official primary; retrieved 2026-10-04T09:42:43Z; supports: summary.
- [AIP-155: correct the request message and add a changelog entry](<https://github.com/aip-dev/google.aip.dev/commit/71f6491a997370b572d003536a1f7ad0e8c1c511>) — Google AIP maintainers; source ID: changelog-change; provenance: official primary; retrieved 2026-10-04T09:42:06Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
