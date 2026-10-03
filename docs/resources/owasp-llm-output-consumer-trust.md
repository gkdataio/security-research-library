# OWASP LLM05:2025: generated-output consumer trust

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/owasp-llm-output-consumer-trust.json>) · [Official resource](<https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/>)

**Publisher:** OWASP Gen AI Security Project  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** LLM05:2025  
**Topics:** Ai Security; Web Foundations  
**Defensive skills:** Review AI authority boundaries; Review input trust boundaries; Threat-model integrations

## Original summary

Explains why model-generated content remains untrusted when passed to browsers, databases or backend functions\. The relevant boundary is the consuming component: plausible model text must not acquire executable meaning or greater authority merely because an application generated it\. Distinguishes unsafe downstream handling from general reliance on answer accuracy\.

## Defensive use

Map each output consumer in an owned AI application to its validation and encoding contract\. Prefer parameterized database operations and context-aware encoding, with monitoring and browser policy controls as supplementary layers\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic LLM application data flow
- Context-sensitive encoding and separation of data from executable interpretation

## Access and freshness

**Access cost at review:** free.

Official public guidance was readable without an account at review time\.

**Reviewed:** 2026-10-03T04:41:24Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed the official page content\. The review date does not establish publication or an immutable revision\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- The 2025 designation is an edition identifier, not a verified publication date\.
- The source contains attack scenarios; this record retains only trust-boundary and remediation concepts\.
- This category describes possible failure modes rather than current exposure of a particular product\.

## Related conceptual diagrams

- [Server disclosure and browser interpretation](<../diagram-gallery.md#server-client-data-consumer-boundaries>)

## Sources and attribution

- [LLM05:2025 Improper Output Handling](<https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/>) — OWASP Gen AI Security Project; source ID: primary; provenance: official primary; retrieved 2026-10-03T04:40:03Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
