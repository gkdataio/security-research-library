# Web cache key precision and capacity isolation

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://arxiv.org/abs/2608.04744>) · [Canonical JSON](<../../data/resources/arxiv-2026-cache-key-precision-and-capacity.json>)

<a id="original-summary"></a>
## Main takeaway

Unnecessary differences in cache keys can store multiple copies of the same content, make caching less effective and increase work for the origin server\. This author-submitted study explains why cache-key design affects availability as well as performance\.

## Defensive use

Document which request properties genuinely distinguish representations, and review key definitions against that application contract\. Compare precise keying with deduplication overhead and the legitimate-traffic costs of rate limiting or anomaly detection; preserve meaningful response distinctions when simplifying keys\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** arXiv  
**Authors:** Matteo Golinelli; Kaan Onarlioglu; Bruno Crispo  
**Resource type:** [Research Paper](<../resource-types.md#type-research-paper>)  
**Version:** arXiv:2608\.04744v1  
**Topics:** [Web Foundations](<../resource-topics.md#topic-web-foundations>); [Verification](<../resource-topics.md#topic-verification>)  
**Defensive skills:** [Review artifact isolation](<../skillsets.md#skill-cache-artifact-isolation>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>); [Write bounded security evidence](<../skillsets.md#skill-defensive-evidence-writing>)

## Prerequisites

**Basis:** editorial guidance.

- HTTP request and response semantics
- Reverse-proxy and origin-server architecture

## Access and freshness

**Access cost at review:** free.

Primary article readable without login\.

**Reviewed:** 2026-10-03T04:59:12Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed the abstract, version history and full-text limitations, mitigations and CDN discussion\. No accompanying tools were retrieved or run\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08-05; precision: day; basis: explicit; source: [Web Cache Overflow: Exploiting Imprecise Keys for Cache Degradation and Beyond](<https://arxiv.org/abs/2608.04744>) (source ID: primary). First arXiv submission, not a confirmed peer-reviewed publication date\.
- **version released:** 2026-08-05; precision: day; basis: explicit; source: [Web Cache Overflow: Exploiting Imprecise Keys for Cache Degradation and Beyond](<https://arxiv.org/abs/2608.04744>) (source ID: primary). Version 1 submission history\.
- **source displayed:** 2026-08-05; precision: day; basis: explicit; source: [Web Cache Overflow: Exploiting Imprecise Keys for Cache Degradation and Beyond](<https://arxiv.org/abs/2608.04744>) (source ID: primary). Submission date displayed on the abstract page\.

## Caveats

- Preprint; the reviewed pages do not establish peer review\.
- Experiments concern stand-alone caching proxies\. CDN applicability was not experimentally demonstrated and is explicitly limited by the authors\.
- Results depend on capacity, object sizes and workload; they do not establish present exposure of any deployment\.
- This record omits operational methods and grants no testing authorization\.

## Sources and attribution

- [Web Cache Overflow: Exploiting Imprecise Keys for Cache Degradation and Beyond](<https://arxiv.org/abs/2608.04744>) — arXiv; source ID: primary; provenance: official primary; retrieved 2026-10-03T04:59:12Z; supports: summary, version, dates.
- [Author-submitted version 1 full text](<https://arxiv.org/html/2608.04744v1>) — arXiv; source ID: paper; provenance: official primary; retrieved 2026-10-03T04:59:12Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
