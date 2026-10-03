# Open WebUI: credentials must bind to their destination connection

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/open-webui-2026-connection-credential-capture.json>) · [Official resource](<https://github.com/open-webui/open-webui/security/advisories/GHSA-p78m-89r6-pgf7>)

**Publisher:** Open WebUI  
**Authors:** doge-woof  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; Ai Security  
**Defensive skills:** Threat-model integrations; Review secrets containment; Verify remediation evidence

## Original summary

CVE-2026-87015 concerns late-bound connection state: tool callables retained their own headers but read a shared cookie variable after connection processing finished\. A maintainer-described controlled observation confirmed unintended session-cookie forwarding\. Connection-specific authentication choice therefore failed to constrain the credentials crossing an integration boundary\.

## Defensive use

Editorial lesson: treat destination, headers and cookies as one immutable request-authority context\. Review capture semantics independently of configuration correctness\. The advisory identifies 0\.11\.1 as fixed by binding cookies per connection\. Credential isolation should survive changes in connection order\.

Educational reference only; linked material does not authorize testing unrelated systems.

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
