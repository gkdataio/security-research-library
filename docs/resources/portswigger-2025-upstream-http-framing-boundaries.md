# Upstream HTTP framing and parser-consistency boundaries

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/portswigger-2025-upstream-http-framing-boundaries.json>) · [Official resource](<https://portswigger.net/research/http1-must-die>)

**Publisher:** PortSwigger  
**Authors:** James Kettle  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Verification  
**Defensive skills:** Review parsing and serialization; Threat-model integrations; Review input trust boundaries; Verify remediation evidence

## Original summary

The researcher explains how inconsistent message-boundary interpretation across proxies and origins can break request isolation on shared upstream connections\. Client-facing HTTP/2 alone does not remove this risk when intermediaries translate requests into HTTP/1\.1\.

## Defensive use

Review framing contracts across every intermediary, including protocol translation and connection reuse\. Consider upstream HTTP/2, consistent validation and normalization, and isolation tradeoffs where legacy transport remains\. Assess remediation against the architecture rather than relying on a front-end protocol label or filtering claim\.

Educational reference only; linked material does not authorize testing unrelated systems.

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

Reviewed the primary article’s conceptual explanation and defensive sections\. Historical research remains relevant to 2026 architecture reviews; vendor capabilities require separate current verification\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-08-06; precision: day; basis: explicit; source: [HTTP/1\.1 must die: the desync endgame](<https://portswigger.net/research/http1-must-die>) (source ID: primary). Original article publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2025-10-17; precision: day; basis: explicit; source: [HTTP/1\.1 must die: the desync endgame](<https://portswigger.net/research/http1-must-die>) (source ID: primary). Displayed update date; not original publication\.

## Caveats

- Protocol migration is the researcher’s recommendation, not proof that every HTTP/2 implementation is secure\.
- Historical cases and vendor support observations do not establish current vulnerabilities or feature availability\.
- Linked operational material is omitted\. No individual award qualification or testing authorization is implied\.

## Sources and attribution

- [HTTP/1\.1 must die: the desync endgame](<https://portswigger.net/research/http1-must-die>) — PortSwigger; source ID: primary; provenance: official primary; retrieved 2026-10-03T04:59:12Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
