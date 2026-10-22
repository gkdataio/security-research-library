# OWASP LLM05:2025: generated-output consumer trust

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/>) · [Canonical JSON](<../../data/resources/owasp-llm-output-consumer-trust.json>)

<a id="original-summary"></a>
## Main takeaway

OWASP explains why model-generated content must still be treated as untrusted input by browsers, databases and backend functions\. Text should not become executable code or gain extra permissions merely because an application generated it\. This guidance addresses unsafe downstream handling, which is separate from whether an answer is accurate\.

## Defensive use

Map each output consumer in an owned AI application to its validation and encoding contract\. Prefer parameterized database operations and context-aware encoding, with monitoring and browser policy controls as supplementary layers\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** OWASP Gen AI Security Project  
**Authors:** Not identified in the reviewed record  
**Resource type:** [Implementation Guide](<../resource-types.md#type-implementation-guide>)  
**Version:** LLM05:2025  
**Topics:** [Ai Security](<../resource-topics.md#topic-ai-security>); [Web Foundations](<../resource-topics.md#topic-web-foundations>); [Browser Security](<../resource-topics.md#topic-browser-security>)  
**Defensive skills:** [Review AI authority boundaries](<../skillsets.md#skill-ai-authority-boundaries>); [Review input trust boundaries](<../skillsets.md#skill-untrusted-input-handling>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>)

## Prerequisites

**Basis:** editorial guidance.

- Basic LLM application data flow
- Context-sensitive encoding and separation of data from executable interpretation

## Access and freshness

**Access cost at review:** free.

Official public guidance was readable without an account at review time\.

**Reviewed:** 2026-10-06T22:50:21Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Scoped review of edition-release and archive metadata; the original primary-page retrieval remains recorded separately\. The 2025 web entry may change\. This review does not establish its original publication or latest-update date, or substantively review the 2026 guidance\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** 2024-11-18; precision: day; basis: explicit; source: [OWASP Top 10 for LLM Applications 2025: official edition PDF](<https://genai.owasp.org/download/43299/?tmstv=1731900559>) (source ID: edition-2025-pdf). The official 2025 PDF gives November 18, 2024 on its cover and in its revision history\. This is the edition release, not the individual web entry publication or latest update\.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- The 2025 designation is an edition identifier\. The edition-2025-pdf source dates its release to November 18, 2024, while edition-2025-landing displays November 17, 2024 for that landing page\. Neither date establishes the individual web entry publication or latest update; those remain unknown\.
- As of October 6, 2026, release-index labels the 2025 edition archived and the 2026 edition current; edition-2026-status confirms the newer release is published\. This record preserves its 2025 URL, identifier and educational summary\. Technical equivalence with the 2026 edition has not been assessed\.
- The source contains attack scenarios; this record retains only trust-boundary and remediation concepts\.
- This category describes possible failure modes rather than current exposure of a particular product\.

## Related conceptual diagrams

- [Server disclosure and browser interpretation](<../diagram-gallery.md#server-client-data-consumer-boundaries>)

## Sources and attribution

- [LLM05:2025 Improper Output Handling](<https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/>) — OWASP Gen AI Security Project; source ID: primary; provenance: official primary; retrieved 2026-10-03T04:40:03Z; supports: summary, version.
- [OWASP Top 10 for LLM Applications 2025: official edition PDF](<https://genai.owasp.org/download/43299/?tmstv=1731900559>) — OWASP Gen AI Security Project; source ID: edition-2025-pdf; provenance: official primary; retrieved 2026-10-06T22:49:00Z; supports: version, dates.
- [OWASP Top 10 for LLM Applications 2025: resource landing page](<https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/>) — OWASP Gen AI Security Project; source ID: edition-2025-landing; provenance: official primary; retrieved 2026-10-06T22:49:06Z; supports: dates.
- [OWASP LLM Top 10 legacy repository: current and archived releases](<https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/README.md>) — OWASP; source ID: release-index; provenance: official primary; retrieved 2026-10-06T22:49:06Z; supports: version.
- [OWASP LLM Top 10 2026: published release overview](<https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/README.md>) — OWASP GenAI Security Project; source ID: edition-2026-status; provenance: official primary; retrieved 2026-10-06T22:49:40Z; supports: version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
