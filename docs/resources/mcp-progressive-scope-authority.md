# MCP scope selection: progressive consent and accumulated authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/mcp-progressive-scope-authority.json>) · [Official resource](<https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices>)

**Publisher:** Model Context Protocol  
**Authors:** Not identified in the reviewed record  
**Resource type:** Architecture Guide  
**Version:** 2026-07-28 documentation URL  
**Topics:** Ai Security; Authorization; Identity  
**Defensive skills:** Model access-control invariants; Threat-model integrations; Review AI authority boundaries

## Original summary

Server permission challenges shape what a general-purpose MCP client requests\. Broad discovery metadata and accumulated scopes can enlarge delegated authority\. Token scopes still require application-side authorization\.

## Defensive use

Map operations to permissions, issue focused challenges, support reduced grants and record elevations\. Review initial discovery and subsequent consent together; do not assume every authorization request represents only the current operation\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- OAuth scope and consent concepts; client/server authorization responsibilities

## Access and freshness

**Access cost at review:** free.

Public official documentation\.

**Reviewed:** 2026-10-03T16:49:11Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed scope-minimization guidance; no deployment assessment\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. The versioned URL does not establish a publication or release date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. The versioned URL does not establish a publication or release date\.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded. The versioned URL does not establish a publication or release date\.

## Caveats

- The guide permits several challenge-breadth strategies\. When an initial challenge omits scope, it documents requesting all advertised scopes; it does not universally require the narrowest request\.
- Maintained guidance, not evidence of a specific deployment’s exposure or a verified patch\. Publication and edition dates remain unknown; the URL version is preserved separately\.

## Sources and attribution

- [Security Best Practices: Scope Minimization](<https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices>) — Model Context Protocol; source ID: primary; provenance: official primary; retrieved 2026-10-03T16:49:11Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
