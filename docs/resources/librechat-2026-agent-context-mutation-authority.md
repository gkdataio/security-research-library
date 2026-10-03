# LibreChat: agent edit authority must cover attached context

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/librechat-2026-agent-context-mutation-authority.json>) · [Official resource](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-xcmf-rpmh-hg59>)

**Publisher:** LibreChat  
**Authors:** Lisa Gnedt; Michael Koppmann  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Ai Security; Authorization  
**Defensive skills:** Model access-control invariants; Review AI authority boundaries; Verify remediation evidence

## Original summary

The advisory contrasts denied access to a private agent with accepted changes to its attached files\. Upload handling omitted the agent permissions enforced elsewhere, allowing unauthorized context and search-file additions\. The documented demonstration changed the owner-visible agent response\. This is an application authorization failure before model interpretation\.

## Defensive use

The source recommends checking agent-edit permission for uploads\. Editorial review principle: enumerate every mutation of an agent’s effective context, including attachments and retrieval indexes; hiding its configuration does not protect those mutations\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Object-level authorization and agent context composition

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory\.

**Reviewed:** 2026-10-03T16:19:05Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory reviewed; no vulnerability execution or deployment testing\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-01-07; precision: day; basis: explicit; source: [LibreChat Insufficient Access Control on Agent Files](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-xcmf-rpmh-hg59>) (source ID: advisory). Maintainer advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separately versioned educational edition established\.
- **source displayed:** 2026-01-07; precision: day; basis: explicit; source: [LibreChat Insufficient Access Control on Agent Files](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-xcmf-rpmh-hg59>) (source ID: advisory). Maintainer advisory publication date\.

## Caveats

- Requires an authenticated account and knowledge of another agent’s identifier; private agents were not ordinarily visible\.
- CVE-2025-69220: the advisory identifies 0\.8\.1-rc2 as affected and records the 0\.8\.2-rc2 fix release on January 7, 2026\.
- No production compromise, data theft, or award is established\. Broader model behavior depends on application context; this review did not run the demonstration\.

## Sources and attribution

- [LibreChat Insufficient Access Control on Agent Files](<https://github.com/LibreChat-AI/LibreChat/security/advisories/GHSA-xcmf-rpmh-hg59>) — LibreChat; source ID: advisory; provenance: official primary; retrieved 2026-10-03T16:19:05Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
