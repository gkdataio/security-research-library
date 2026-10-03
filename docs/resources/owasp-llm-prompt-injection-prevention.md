# LLM Prompt Injection Prevention Cheat Sheet

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/owasp-llm-prompt-injection-prevention.json>) · [Official resource](<https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html>)

**Publisher:** OWASP Cheat Sheet Series  
**Authors:** Not identified in the reviewed record  
**Resource type:** Architecture Guide  
**Version:** Not established in the reviewed record  
**Topics:** Ai Security  
**Defensive skills:** Review AI authority boundaries; Threat-model integrations; Review input trust boundaries

## Original summary

Defense-in-depth guidance for LLM applications that consume untrusted content or invoke tools\. Covers data provenance, least privilege, action authorization, monitoring, and the limitations of guardrails\.

## Defensive use

Review permissions and action boundaries around an owned AI integration; treat filters and model-based checks as partial defenses rather than guarantees\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- LLM application and tool-call basics
- Trust boundaries
- An understanding of the application's data and permissions

## Access and freshness

**Access cost at review:** free.

Verified as free at review time; optional accounts or provider features may have separate terms\.

**Reviewed:** 2026-10-02T14:50:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Review records accessible official guidance as of this date; living content and current versions may change\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Includes attack examples; this collection uses it as a defensive-design reference
- Guidance evolves and individual examples require contextual evaluation

## Related conceptual diagrams

- [Retrieved content is data, not authority](<../diagram-gallery.md#ai-content-authority-separation>)

## Sources and attribution

- [LLM Prompt Injection Prevention Cheat Sheet](<https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html>) — OWASP Cheat Sheet Series; source ID: primary; provenance: official primary; retrieved 2026-10-02T14:50:00Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
