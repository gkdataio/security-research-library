# MCP elicitation: consent, credential custody and completion

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation>) · [Canonical JSON](<../../data/resources/mcp-elicitation-consent-credential-custody.json>)

<a id="original-summary"></a>
## Main takeaway

The MCP specification keeps secrets out of form elicitation and places sensitive URL interactions outside the client and model context, with the requesting server and destination visible to the user\. Agreeing to open an interaction does not prove it finished; the server checks completion separately\. For third-party OAuth, the MCP server holds the resulting credentials, and that grant is separate from the client's permission to access the server\.

## Defensive use

Editorial guidance: map the data recipient, credential holder and authoritative completion evidence for each interaction\. Preserve decline and cancellation, bind completion to the initiating identity, and review navigation consent and automatic URL handling independently\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Model Context Protocol  
**Authors:** Not identified in the reviewed record  
**Resource type:** [Technical Standard](<../resource-types.md#type-technical-standard>)  
**Version:** 2026-07-28 specification URL  
**Topics:** [Ai Security](<../resource-topics.md#topic-ai-security>); [Authorization](<../resource-topics.md#topic-authorization>); [Identity](<../resource-topics.md#topic-identity>)  
**Defensive skills:** [Review AI authority boundaries](<../skillsets.md#skill-ai-authority-boundaries>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>); [Review secrets containment](<../skillsets.md#skill-secrets-containment>)

## Prerequisites

**Basis:** editorial guidance.

- MCP client/server roles, OAuth delegation and credential storage

## Access and freshness

**Access cost at review:** free.

Public official specification\.

**Reviewed:** 2026-10-04T15:34:19Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed elicitation and the specification overview\. No implementation-conformance assessment\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Original publication date not established\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. A versioned URL alone does not establish an edition release date\.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate page date established\.

## Caveats

- The form prohibition concerns access or transaction secrets; ordinary contact data is not categorically excluded\.
- Elicitation prohibits automatic URL or metadata prefetching and navigation without explicit consent\. It requires the full URL to be shown and credentials to stay out of URLs\.
- The overview states that protocol rules alone cannot enforce its security principles; implementation controls remain necessary\.
- No deployed vulnerability, remediation or award is established\. The URL version is preserved separately from unknown publication and release dates\.

## Sources and attribution

- [Elicitation](<https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation>) — Model Context Protocol; source ID: elicitation; provenance: official primary; retrieved 2026-10-04T15:33:23Z; supports: summary, version.
- [Specification: Security and Trust &amp; Safety](<https://modelcontextprotocol.io/specification/2026-07-28>) — Model Context Protocol; source ID: overview; provenance: official primary; retrieved 2026-10-04T15:33:23Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
