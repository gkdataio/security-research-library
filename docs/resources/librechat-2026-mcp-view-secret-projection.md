# LibreChat: viewing an integration must not reveal its service secrets

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/librechat-2026-mcp-view-secret-projection.json>) · [Official resource](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-6vqg-rgpm-qvf9>)

**Publisher:** LibreChat  
**Authors:** LoGGGG2402  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Ai Security; Authorization  
**Defensive skills:** Model access-control invariants; Review secrets containment; Review AI authority boundaries; Review parsing and serialization

## Original summary

The MCP registry prepared decrypted configuration for internal use, and response handlers returned that representation to viewers without removing secrets\. Object visibility consequently became credential disclosure authority\. The advisory documents a local demonstration exposing administrator-managed provider credentials to a view-only account\.

## Defensive use

The source recommends secret-free responses and presence indicators\. Editorial review principle: define separate execution and presentation representations, then verify that list and detail responses preserve the same field-level disclosure policy\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Integration credentials, response serialization, and object versus field authorization

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory\.

**Reviewed:** 2026-10-03T16:19:05Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory reviewed; no vulnerability execution or deployment testing\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-02; precision: day; basis: explicit; source: [Shared MCP Server View Leaks Decrypted Admin Secrets](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-6vqg-rgpm-qvf9>) (source ID: advisory). Maintainer advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separately versioned educational edition established\.
- **source displayed:** 2026-06-02; precision: day; basis: explicit; source: [Shared MCP Server View Leaks Decrypted Admin Secrets](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-6vqg-rgpm-qvf9>) (source ID: advisory). Maintainer advisory publication date\.

## Caveats

- Requires MCP enabled, stored administrator-managed secrets, and viewer access to the shared integration\.
- CVE-2026-44653: affected v0\.8\.3 and patched v0\.8\.4 are listed; patch release date is not established by the advisory\. March 13 is the reported test date, not publication\.
- Credential reuse and indirect exposure through shared agents are possible extensions discussed by the source, not demonstrated outcomes\. No production compromise or award is established\.

## Sources and attribution

- [Shared MCP Server View Leaks Decrypted Admin Secrets](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-6vqg-rgpm-qvf9>) — LibreChat; source ID: advisory; provenance: official primary; retrieved 2026-10-03T16:19:05Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
