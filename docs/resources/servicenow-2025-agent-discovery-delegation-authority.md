# ServiceNow: agent discovery expands the delegated authority boundary

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/servicenow-2025-agent-discovery-delegation-authority.json>) · [Official resource](<https://appomni.com/ao-labs/ai-agent-to-agent-discovery-prompt-injection/>)

**Publisher:** AppOmni AO Labs  
**Authors:** Aaron Costello  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Ai Security; Authorization  
**Defensive skills:** Review AI authority boundaries; Threat-model integrations; Model access-control invariants

## Original summary

AppOmni's configuration research illustrates why an agent's effective authority includes capabilities reachable through collaborating agents\. Restricting its own tools may leave a wider delegation boundary when lower-trust content is treated as task authority\. Aaron Costello reports controlled record-access, record-change and external-disclosure effects in Now Assist despite prompt-level protections\.

## Defensive use

Review permitted collaborators, execution identities and sensitive-action approvals together\. Restrict team composition and delegated capabilities to the task, apply least privilege, and require approval for sensitive actions\. ServiceNow's current documentation distinguishes discovery/invocation access from the agent's data-access identity and describes supervised execution\. Editorial lesson: evaluate reachable authority across the collaboration, rather than only the first agent's tool list\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- AI content-versus-instruction trust boundaries
- Role-based access, execution identities and delegated permissions

## Access and freshness

**Access cost at review:** free.

Public researcher article and supporting ServiceNow documentation\.

**Reviewed:** 2026-10-06T02:22:08Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Researcher article and two supporting vendor documentation pages read\. No behavior was independently reproduced; later vendor guidance is not historical demonstration verification\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-11-19; precision: day; basis: explicit; source: [When AI Turns on Its Team: Exploiting Agent-to-Agent Discovery via Prompt Injection](<https://appomni.com/ao-labs/ai-agent-to-agent-discovery-prompt-injection/>) (source ID: researcher). Article publication date displayed with the author byline\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separately versioned educational-resource edition is established\.
- **source displayed:** 2025-11-19; precision: day; basis: explicit; source: [When AI Turns on Its Team: Exploiting Agent-to-Agent Discovery via Prompt Injection](<https://appomni.com/ao-labs/ai-agent-to-agent-discovery-prompt-injection/>) (source ID: researcher). The primary article displays November 19, 2025\.

## Caveats

- The reported setup processed lower-trust record content under a privileged agent context with discoverable collaborators and relevant autonomous capabilities; this is configuration-dependent\.
- AppOmni says ServiceNow treated the behavior as intended and clarified on-platform documentation\. The reviewed evidence establishes no vulnerability patch, CVE or individual award for this case\.
- Reported effects are researcher demonstrations, not evidence of production exploitation or a prevalence estimate\.
- The supporting ServiceNow pages display Brazil release and September 10, 2026 updates\. They document the current configuration model, not the November 2025 demonstration, its defaults or a historical fix\.
- The research-paper taxonomy includes first-party research articles and does not imply academic peer review\. This educational record grants no testing authorization\.

## Sources and attribution

- [When AI Turns on Its Team: Exploiting Agent-to-Agent Discovery via Prompt Injection](<https://appomni.com/ao-labs/ai-agent-to-agent-discovery-prompt-injection/>) — AppOmni AO Labs; source ID: researcher; provenance: official primary; retrieved 2026-10-06T02:20:53Z; supports: summary, dates.
- [Define security controls for an AI agent](<https://www.servicenow.com/docs/r/intelligent-experiences/define-sec-controls-aia.html>) — ServiceNow; source ID: vendor-security-controls; provenance: official primary; retrieved 2026-10-06T02:20:53Z; supports: summary.
- [Use an AI agent action](<https://www.servicenow.com/docs/r/build-workflows/workflow-studio/use-an-ai-agent-action.html>) — ServiceNow; source ID: vendor-execution-controls; provenance: official primary; retrieved 2026-10-06T02:20:53Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
