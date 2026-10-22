# Langflow: project transport authorization must reach each resource read

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/langflow-ai/langflow/security/advisories/GHSA-4hmc-cfm3-w43c>) · [Canonical JSON](<../../data/resources/langflow-2026-mcp-resource-project-authorization.json>)

<a id="original-summary"></a>
## Main takeaway

Langflow's maintainer reports that file-reading handlers did not carry forward the user and project restrictions established by MCP authentication\. A local two-user demonstration disclosed another user's file, while the ordinary download interface denied access\. Authenticating a project connection therefore did not ensure permission for each later file read\.

## Defensive use

The documented fix carries authenticated context into object resolution, constrains project membership, and scopes discovery results\. Editorial lesson: connection admission and storage containment cannot replace per-resource authorization; compare policy across every interface to the same object\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Langflow  
**Authors:** Not identified in the reviewed record  
**Resource type:** [Maintainer Advisory](<../resource-types.md#type-maintainer-advisory>)  
**Version:** Not established in the reviewed record  
**Topics:** [Ai Security](<../resource-topics.md#topic-ai-security>); [Authorization](<../resource-topics.md#topic-authorization>); [Identity](<../resource-topics.md#topic-identity>); [API Security](<../resource-topics.md#topic-api-security>)  
**Defensive skills:** [Model access-control invariants](<../skillsets.md#skill-authorization-modeling>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>); [Review AI authority boundaries](<../skillsets.md#skill-ai-authority-boundaries>); [Verify remediation evidence](<../skillsets.md#skill-patch-verification>)

## Prerequisites

**Basis:** editorial guidance.

- Object ownership and project membership models
- MCP resource handling and application storage separation

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory\.

**Reviewed:** 2026-10-03T13:39:19Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory reviewed; no vulnerability execution or deployment testing\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-09-22; precision: day; basis: explicit; source: [Authenticated Cross-Project File Disclosure via Unscoped MCP Resource Handlers](<https://github.com/langflow-ai/langflow/security/advisories/GHSA-4hmc-cfm3-w43c>) (source ID: advisory). Advisory publication; not software release\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separately versioned educational edition established\.
- **source displayed:** 2026-09-22; precision: day; basis: explicit; source: [Authenticated Cross-Project File Disclosure via Unscoped MCP Resource Handlers](<https://github.com/langflow-ai/langflow/security/advisories/GHSA-4hmc-cfm3-w43c>) (source ID: advisory). Advisory publication; not software release\.

## Caveats

- Source prerequisites include authentication-enabled deployments, an accessible owned project, and another user’s uploaded flow-backed file\.
- The maintainer corrects affected versions to 1\.6\.8–1\.9\.0 and identifies 1\.9\.1, released April 24, 2026, as fixed\. September publication is not patch timing\.
- The September 22 triage update reports regression coverage; this review did not independently run it\. No observed production compromise or award is established\.
- Conceptual defensive summary; public disclosure grants no testing authorization\.
- The advisory credits R1ZZG0D as Reporter, andifilhohub as Analyst, and erichare as Remediation developer\. Its header identifies andifilhohub as the publishing account\. No explicit author byline is shown, so named authors remain unestablished rather than inferred from those roles\.

## Sources and attribution

- [Authenticated Cross-Project File Disclosure via Unscoped MCP Resource Handlers](<https://github.com/langflow-ai/langflow/security/advisories/GHSA-4hmc-cfm3-w43c>) — Langflow; source ID: advisory; provenance: official primary; retrieved 2026-10-03T13:39:19Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
