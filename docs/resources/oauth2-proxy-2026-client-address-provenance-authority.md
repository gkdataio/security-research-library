# OAuth2 Proxy: client-address provenance must precede authentication exemptions

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/oauth2-proxy-2026-client-address-provenance-authority.json>) · [Official resource](<https://github.com/oauth2-proxy/oauth2-proxy/security/advisories/GHSA-wr5q-7wxw-x568>)

**Publisher:** OAuth2 Proxy  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; Web Foundations  
**Defensive skills:** Model access-control invariants; Threat-model integrations; Review input trust boundaries; Verify remediation evidence

## Original summary

GHSA-wr5q-7wxw-x568 describes client-address metadata acquiring authority to waive authentication without verified transport-peer and intermediary provenance\. The maintainer reports unauthenticated access within the authority already granted by configured address exemptions\. This requires optional trusted-address exemptions, reverse-proxy mode and client-controlled address metadata reaching the decision\. The educational focus is the authority of an exception path\.

## Defensive use

The v7\.15\.5 release describes transport-peer verification, bounded intermediary trust and safe failure when trusted-intermediary address metadata is missing or malformed\. Upgrading alone is insufficient: compatibility defaults retain overly broad proxy trust\. Deployments retaining exemptions must narrowly scope trusted intermediaries and ensure ingress establishes trustworthy address metadata\. The advisory recommends removing the exemptions as a workaround\. Editorial lesson: treat an authentication exception as an authorization mechanism with its own evidence requirements\. Record who can assert each decision-relevant attribute, what authority it can unlock, and what happens when its provenance is unavailable\. Patch verification must cover effective configuration as well as installed version; a code change cannot establish a trust boundary that deployment policy leaves universal\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Reverse-proxy, transport-peer and forwarded-metadata concepts
- Authentication exemptions and attribute-based authorization concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and official release notes\.

**Reviewed:** 2026-10-04T16:42:14Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Advisory, release notes and release API metadata reviewed\. This records maintainer statements, not independent patch testing; the educational resource edition remains unknown\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-10-01; precision: day; basis: explicit; source: [OAuth2 Proxy client-address authentication-exemption advisory GHSA-wr5q-7wxw-x568](<https://github.com/oauth2-proxy/oauth2-proxy/security/advisories/GHSA-wr5q-7wxw-x568>) (source ID: maintainer). Advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-10-01; precision: day; basis: explicit; source: [OAuth2 Proxy client-address authentication-exemption advisory GHSA-wr5q-7wxw-x568](<https://github.com/oauth2-proxy/oauth2-proxy/security/advisories/GHSA-wr5q-7wxw-x568>) (source ID: maintainer). Advisory publication date\.

## Caveats

- Affected-version metadata lists 6\.1\.0 through 7\.15\.3, patched-version metadata says later than 7\.15\.4, and the advisory body names 7\.15\.5\. This gap does not establish 7\.15\.4 as unaffected\.
- The release API records v7\.15\.5 publication at 2026-10-01T09:05:48Z\. This is software-release chronology, not the educational resource's edition date or proof of deployment remediation\.
- The advisory credits gronke, SmylerMC, etsubu, SnailSploit and ihopenre-eng as reporters\. Publishing account tuunit is not an established byline; authors remain unassigned\.
- The sources establish neither universal deployment exposure, downstream account takeover, a production incident nor an award\. The advisory lists no known CVE; unrelated release CVEs are not assigned to this record\.

## Sources and attribution

- [OAuth2 Proxy client-address authentication-exemption advisory GHSA-wr5q-7wxw-x568](<https://github.com/oauth2-proxy/oauth2-proxy/security/advisories/GHSA-wr5q-7wxw-x568>) — OAuth2 Proxy; source ID: maintainer; provenance: official primary; retrieved 2026-10-04T16:41:23Z; supports: summary, dates.
- [OAuth2 Proxy v7\.15\.5 release notes](<https://github.com/oauth2-proxy/oauth2-proxy/releases/tag/v7.15.5>) — OAuth2 Proxy; source ID: release; provenance: official primary; retrieved 2026-10-04T16:40:59Z; supports: summary.
- [OAuth2 Proxy v7\.15\.5 official release metadata](<https://api.github.com/repos/oauth2-proxy/oauth2-proxy/releases/tags/v7.15.5>) — OAuth2 Proxy; source ID: release-metadata; provenance: official primary; retrieved 2026-10-04T16:41:23Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
