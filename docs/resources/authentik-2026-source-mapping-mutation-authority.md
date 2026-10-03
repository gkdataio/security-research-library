# authentik: source-mapping edits carry identity-rebinding authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/authentik-2026-source-mapping-mutation-authority.json>) · [Official resource](<https://github.com/goauthentik/authentik/security/advisories/GHSA-wr38-7xg8-fqxr>)

**Publisher:** authentik  
**Authors:** rissson  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization  
**Defensive skills:** Review identity lifecycle; Model access-control invariants; Verify remediation evidence

## Original summary

CVE-2026-49443 concerns writable identity-mapping fields in API serializers\. Delegated connection-management authority could alter which local user or group a source identity represented\. The maintainer reports victim-account authentication; its example addresses user mappings, while the impact statement also covers groups\.

## Defensive use

Editorial reasoning: permission to maintain an integration object does not establish permission to reassign the identity it authenticates\. Treat identity bindings as security-sensitive relationships, restrict writable fields, and separately authorize any supported reassignment\. The advisory lists patched versions 2025\.12\.6, 2026\.2\.4 and 2026\.5\.1\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Identity-provider integration and authorization concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer disclosure\.

**Reviewed:** 2026-10-03T15:39:39Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary source reviewed; no independent reproduction or deployment assessment\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-05-28; precision: day; basis: explicit; source: [UserSourceConnection\.user and GroupSourceConnection\.group are changeable through the API](<https://github.com/goauthentik/authentik/security/advisories/GHSA-wr38-7xg8-fqxr>) (source ID: advisory). Maintainer advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational edition date established\.
- **source displayed:** 2026-05-28; precision: day; basis: explicit; source: [UserSourceConnection\.user and GroupSourceConnection\.group are changeable through the API](<https://github.com/goauthentik/authentik/security/advisories/GHSA-wr38-7xg8-fqxr>) (source ID: advisory). Maintainer advisory publication date\.

## Caveats

- The described user case requires both an account at a configured identity source and delegated permission to add or change source connections\. Ordinary authentication alone is insufficient\.
- rissson published the maintainer advisory; no separate reporter is identified\. Group consequences are described more broadly than the user-focused example; no independent reproduction is claimed\.
- Patch release dates are not established by the advisory\. Publication and educational edition metadata must not substitute for software chronology\. No individual award is established\.

## Sources and attribution

- [UserSourceConnection\.user and GroupSourceConnection\.group are changeable through the API](<https://github.com/goauthentik/authentik/security/advisories/GHSA-wr38-7xg8-fqxr>) — authentik; source ID: advisory; provenance: official primary; retrieved 2026-10-03T15:39:39Z; supports: summary, dates, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
