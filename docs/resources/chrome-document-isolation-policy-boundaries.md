# Document Isolation Policy: process separation and residual authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/chrome-document-isolation-policy-boundaries.json>) · [Official resource](<https://developer.chrome.com/blog/document-isolation-policy>)

**Publisher:** Google Chrome for Developers  
**Authors:** Camille Lamy  
**Resource type:** Architecture Guide  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Memory Safety and Process Isolation  
**Defensive skills:** Review client isolation; Threat-model integrations; Review secrets containment

## Original summary

Explains per-document cross-origin isolation as a response to process-level information exposure that logical origin checks alone cannot prevent\. Document Isolation Policy allows independently isolated frames while preserving popup communication\. Subresource policy either requires explicit sharing permission or removes credentials from relevant cross-origin requests\.

## Defensive use

Editorial lesson: separate process confidentiality, resource delivery and application authority in architecture reviews\. Isolation does not remove same-origin storage access or asynchronous messaging, so these channels retain their own authorization requirements\. Evaluate isolation choices against required embedded-resource and sign-in behavior\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Browser origins, frames, HTTP resource policies and process isolation

## Access and freshness

**Access cost at review:** free.

Public first-party guidance\.

**Reviewed:** 2026-10-03T13:38:43Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Dated first-party guide reviewed; current browser coverage was not independently established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-05-01; precision: day; basis: explicit; source: [Document Isolation Policy: Enable powerful web features with ease](<https://developer.chrome.com/blog/document-isolation-policy>) (source ID: guide). Historical publication relevant to 2026 architecture review\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Chrome 137 is a software version, not an educational edition\.
- **source displayed:** 2025-05-01; precision: day; basis: explicit; source: [Document Isolation Policy: Enable powerful web features with ease](<https://developer.chrome.com/blog/document-isolation-policy>) (source ID: guide). Displayed last-updated date\.

## Caveats

- Architectural guidance, not an individual vulnerability disclosure or evidence of deployed compromise\. Security benefits are the publisher's design claims\.
- The article establishes desktop availability from Chrome 137; its Android rollout intention is not confirmation of present support\. Verify relevant browser support separately\.
- Isolated and non-isolated same-origin frames lose synchronous DOM access but retain asynchronous communication and storage sharing\. This is not general tenant isolation\.

## Sources and attribution

- [Document Isolation Policy: Enable powerful web features with ease](<https://developer.chrome.com/blog/document-isolation-policy>) — Google Chrome for Developers; source ID: guide; provenance: official primary; retrieved 2026-10-03T13:38:43Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
