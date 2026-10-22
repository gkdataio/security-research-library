# Open WebUI: credentials must bind to their destination connection

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/open-webui/open-webui/security/advisories/GHSA-p78m-89r6-pgf7>) · [Canonical JSON](<../../data/resources/open-webui-2026-connection-credential-capture.json>)

<a id="original-summary"></a>
## Main takeaway

Open WebUI's maintainer reports unintended session-cookie forwarding in a controlled observation \(CVE-2026-87015\)\. Tool functions kept their own headers but read cookies from shared state after connection processing finished\. As a result, a connection's authentication setting did not reliably limit which credentials it sent\.

## Defensive use

Editorial lesson: treat destination, headers and cookies as one immutable request-authority context\. Review capture semantics independently of configuration correctness\. The advisory identifies 0\.11\.1 as fixed by binding cookies per connection\. Credential isolation should survive changes in connection order\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Open WebUI  
**Authors:** doge-woof  
**Resource type:** [Maintainer Advisory](<../resource-types.md#type-maintainer-advisory>)  
**Version:** Not established in the reviewed record  
**Topics:** [Identity](<../resource-topics.md#topic-identity>); [Authorization](<../resource-topics.md#topic-authorization>); [Ai Security](<../resource-topics.md#topic-ai-security>)  
**Defensive skills:** [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>); [Review secrets containment](<../skillsets.md#skill-secrets-containment>); [Verify remediation evidence](<../skillsets.md#skill-patch-verification>)

## Prerequisites

**Basis:** editorial guidance.

- HTTP credentials, integration boundaries and secure data handling

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory\.

**Reviewed:** 2026-10-03T14:19:06Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory reviewed; no software executed or deployment tested\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-09-04; precision: day; basis: explicit; source: [A user's session cookies are sent to tool servers configured for bearer authentication](<https://github.com/open-webui/open-webui/security/advisories/GHSA-p78m-89r6-pgf7>) (source ID: advisory). Maintainer publication date; distinct from database ingestion or patch release\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational edition established\.
- **source displayed:** 2026-09-04; precision: day; basis: explicit; source: [A user's session cookies are sent to tool servers configured for bearer authentication](<https://github.com/open-webui/open-webui/security/advisories/GHSA-p78m-89r6-pgf7>) (source ID: advisory). Maintainer publication date; distinct from database ingestion or patch release\.

## Caveats

- Affected versions are &gt;=0\.6\.27 and &lt;0\.11\.1\. Requires multiple attached tool servers, including a session/system-OAuth connection; exposure depends on shared-state capture during connection processing\. Tool servers are not configured by default\.
- The recipient is an administrator-registered, partially trusted server\. Impersonation, including administrator access, is a stated consequence of session-token disclosure; production compromise is not established\.
- Classic298 is credited as reporter\. Patch-release date is not established here\.

## Sources and attribution

- [A user's session cookies are sent to tool servers configured for bearer authentication](<https://github.com/open-webui/open-webui/security/advisories/GHSA-p78m-89r6-pgf7>) — Open WebUI; source ID: advisory; provenance: official primary; retrieved 2026-10-03T14:19:06Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
