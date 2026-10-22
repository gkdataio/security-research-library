# LibreChat: delegated credentials must remain bound to the initiating session

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-vf7j-7mrx-hp7g>) · [Canonical JSON](<../../data/resources/librechat-2026-mcp-oauth-session-binding.json>)

<a id="original-summary"></a>
## Main takeaway

LibreChat could associate third-party credentials with the wrong local account during an MCP OAuth callback\. Its CVE-2026-31944 advisory explains that the callback trusted the cached initiator identity without authenticating the returning browser or checking that the identities matched\. The reported consequences stay within the integration's delegated permissions; they do not amount to takeover of the person's LibreChat account\. The scenario requires an authenticated initiator, enabled MCP OAuth and another person's interaction with the authorization flow\. Prior provider consent may skip the consent screen, but interaction is still required\.

## Defensive use

Editorial lesson: bind OAuth initiation, callback session, and credential-storage owner before accepting a grant\. Treat transaction state as correlation, not sufficient proof of browser identity\. The advisory names 0\.8\.3-rc1 as patched but does not explain its implementation\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** LibreChat  
**Authors:** danny-avila  
**Resource type:** [Maintainer Advisory](<../resource-types.md#type-maintainer-advisory>)  
**Version:** Not established in the reviewed record  
**Topics:** [Ai Security](<../resource-topics.md#topic-ai-security>); [Authorization](<../resource-topics.md#topic-authorization>); [Identity](<../resource-topics.md#topic-identity>)  
**Defensive skills:** [Model access-control invariants](<../skillsets.md#skill-authorization-modeling>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>); [Review AI authority boundaries](<../skillsets.md#skill-ai-authority-boundaries>); [Verify remediation evidence](<../skillsets.md#skill-patch-verification>)

## Prerequisites

**Basis:** editorial guidance.

- OAuth authorization-code callbacks and transaction state
- Local session identity versus external delegated authority

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory\.

**Reviewed:** 2026-10-03T13:39:19Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory reviewed; no vulnerability execution or deployment testing\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-03-13; precision: day; basis: explicit; source: [MCP OAuth callback does not validate browser session, allows token theft via redirect link](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-vf7j-7mrx-hp7g>) (source ID: advisory). Advisory publication; not software release\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separately versioned educational edition established\.
- **source displayed:** 2026-03-13; precision: day; basis: explicit; source: [MCP OAuth callback does not validate browser session, allows token theft via redirect link](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-vf7j-7mrx-hp7g>) (source ID: advisory). Advisory publication; not software release\.

## Caveats

- Prerequisites include an authenticated initiator, enabled MCP OAuth, and another person’s interaction with the authorization flow; existing provider consent can change the interaction required\.
- The source lists affected versions as &gt;= v0\.8\.2, &lt;= 0\.8\.2-rc3\. Preserve this unusual stable/prerelease range without silently normalizing it\.
- No independent production-compromise evidence, patch-release date, historical-token revocation behavior, or award amount is established\.
- Conceptual defensive summary; public disclosure grants no testing authorization\.

## Sources and attribution

- [MCP OAuth callback does not validate browser session, allows token theft via redirect link](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-vf7j-7mrx-hp7g>) — LibreChat; source ID: advisory; provenance: official primary; retrieved 2026-10-03T13:39:19Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
