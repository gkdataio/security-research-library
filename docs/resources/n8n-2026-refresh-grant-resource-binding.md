# n8n: refreshed authority must remain bound to the consented resource

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/n8n-2026-refresh-grant-resource-binding.json>) · [Official resource](<https://github.com/n8n-io/n8n/security/advisories/GHSA-cw9w-vv67-hf73>)

**Publisher:** n8n  
**Authors:** Matsuuu  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Identity; Business Logic and State Integrity  
**Defensive skills:** Model access-control invariants; Review security-token design; Threat-model integrations

## Original summary

The maintainer reports that initial OAuth authorization preserved resource-specific consent, while refresh grants checked registration without preserving that binding\. A client could consequently receive authority over another workflow accessible to the consenting user\. This is a delegated-consent failure; the source does not establish access beyond that user’s underlying permissions or a production incident\.

## Defensive use

The stated repair retains the granted resource in refresh-token state and rejects conflicting resource choices\. The maintainer also calls for renewed authorization after upgrading because older refresh tokens lack this binding; temporary restrictions are incomplete mitigation\. Editorial lesson: review authorization invariants throughout a grant’s lifecycle, including migration of pre-fix state\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- OAuth grant, refresh, resource, and consent concepts
- Distinguishing a user’s permissions from the smaller authority delegated to a client

## Access and freshness

**Access cost at review:** free.

Public maintainer security advisory\.

**Reviewed:** 2026-10-03T11:10:39Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary maintainer evidence reviewed\. No exploit reproduction, live testing, or independent patch verification performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-09-03; precision: day; basis: explicit; source: [Per-Resource OAuth Consent Bypass via Unbound Refresh Token Resource Substitution](<https://github.com/n8n-io/n8n/security/advisories/GHSA-cw9w-vv67-hf73>) (source ID: advisory). Maintainer advisory publication, not software patch release\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition release established\.
- **source displayed:** 2026-09-03; precision: day; basis: explicit; source: [Per-Resource OAuth Consent Bypass via Unbound Refresh Token Resource Substitution](<https://github.com/n8n-io/n8n/security/advisories/GHSA-cw9w-vv67-hf73>) (source ID: advisory). Explicit advisory publication date\.

## Caveats

- CVE-2026-86073\. The advisory credits bariskececi as reporter; Matsuuu is its publishing maintainer\.
- Prerequisites include client registration, authenticated user consent for one protected workflow, and another identifiable workflow within that user’s execution permissions\.
- The patched-version table lists 2\.38\.2 and 2\.37\.7, while prose says 2\.38\.1 and 2\.37\.7\. No corrected affected interval is inferred\.
- Official release pages date both 2\.38\.2 and 2\.37\.7 to September 2, 2026, separately from September 3 advisory publication; 2\.38\.2 is labeled pre-release\. Release existence does not resolve the advisory inconsistency\.
- No bounty is established\. Learning prerequisites and general design guidance are editorial\.

## Sources and attribution

- [Per-Resource OAuth Consent Bypass via Unbound Refresh Token Resource Substitution](<https://github.com/n8n-io/n8n/security/advisories/GHSA-cw9w-vv67-hf73>) — n8n; source ID: advisory; provenance: official primary; retrieved 2026-10-03T11:10:39Z; supports: summary, dates.
- [n8n@2\.38\.2 release](<https://github.com/n8n-io/n8n/releases/tag/n8n@2.38.2>) — n8n; source ID: release-2382; provenance: official primary; retrieved 2026-10-03T11:10:39Z; supports: dates.
- [n8n@2\.37\.7 release](<https://github.com/n8n-io/n8n/releases/tag/n8n@2.37.7>) — n8n; source ID: release-2377; provenance: official primary; retrieved 2026-10-03T11:10:39Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
