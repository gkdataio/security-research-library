# Authlib: error responses must preserve redirect-destination validation

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/authlib-2026-error-path-redirect-authority.json>) · [Official resource](<https://github.com/authlib/authlib/security/advisories/GHSA-r95x-qfjj-fjj2>)

**Publisher:** Authlib  
**Authors:** azmeuk  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization  
**Defensive skills:** Review identity lifecycle; Model access-control invariants; Verify remediation evidence

## Original summary

CVE-2026-44681 describes an OIDC error path selecting a response destination before client and destination validation\. The maintainer reports an unauthorized browser redirect, explicitly excluding direct disclosure of authorization codes or tokens\. The failed boundary was untrusted request data becoming trusted error-response routing\.

## Defensive use

Editorial reasoning: an exception can exercise authority even when the main operation fails\. Establish destination trust before producing redirect-capable errors, and review rejection paths across grant implementations\. The official v1\.6\.12 release notes corroborate the validation correction\.

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

- **published:** 2026-05-07; precision: day; basis: explicit; source: [Open Redirect in Authlib OIDC Implicit/Hybrid Authorization](<https://github.com/authlib/authlib/security/advisories/GHSA-r95x-qfjj-fjj2>) (source ID: advisory). Maintainer advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational edition date established\.
- **source displayed:** 2026-05-07; precision: day; basis: explicit; source: [Open Redirect in Authlib OIDC Implicit/Hybrid Authorization](<https://github.com/authlib/authlib/security/advisories/GHSA-r95x-qfjj-fjj2>) (source ID: advisory). Maintainer advisory publication date\.

## Caveats

- Exposure requires an affected server supporting implicit or hybrid OIDC grants; the advisory excludes code-only configurations from this variant\. Authentication is unnecessary, but browser redirection requires user interaction\. Phishing consequences are possible downstream harm, not demonstrated account compromise\.
- The advisory identifies 1\.6\.12 and 1\.7\.1 as patched\. Software versions are not resource editions; exact patch-release dates remain unrecorded\.
- azmeuk published the advisory; y011d4 is credited as reporter\. No bounty qualification or independent reproduction is established\.

## Sources and attribution

- [Open Redirect in Authlib OIDC Implicit/Hybrid Authorization](<https://github.com/authlib/authlib/security/advisories/GHSA-r95x-qfjj-fjj2>) — Authlib; source ID: advisory; provenance: official primary; retrieved 2026-10-03T15:39:39Z; supports: summary, dates, version.
- [Release v1\.6\.12](<https://github.com/authlib/authlib/releases/tag/v1.6.12>) — Authlib; source ID: release; provenance: official primary; retrieved 2026-10-03T15:39:39Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
