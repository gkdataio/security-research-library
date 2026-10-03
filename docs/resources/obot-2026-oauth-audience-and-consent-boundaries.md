# Obot: preserve delegated token audience and consent boundaries

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/obot-2026-oauth-audience-and-consent-boundaries.json>) · [Official resource](<https://github.com/obot-platform/obot/security/advisories/GHSA-xwmw-prc4-v3cr>)

**Publisher:** Obot  
**Authors:** thedadams  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization  
**Defensive skills:** Model access-control invariants; Threat-model integrations; Review identity lifecycle; Verify remediation evidence

## Original summary

GHSA-xwmw-prc4-v3cr describes MCP-delegated tokens accepted by broader application APIs because issuer validation did not establish audience authority\. Client authorization also lacked explicit consent\. The maintainer describes possible access to resources already available to the victim; this is bounded worst-case impact, not evidence of observed production compromise\.

## Defensive use

The maintainer identifies v0\.23\.0 as patched\. Its release notes corroborate consent, narrower token routing and audience checks\. Editorial lesson: verify issuer, intended recipient and permitted actions independently; consent alone cannot repair overbroad token acceptance\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- OAuth client registration, consent and token audience concepts
- Delegated authorization across application and MCP boundaries

## Access and freshness

**Access cost at review:** free.

Public maintainer sources readable without an account\.

**Reviewed:** 2026-10-03T08:39:25Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed maintainer advisory and corroborating project sources\. No software executed or deployment tested\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-22; precision: day; basis: explicit; source: [OAuth Dynamic Client Registration Enables API Token Theft via Audience Confusion](<https://github.com/obot-platform/obot/security/advisories/GHSA-xwmw-prc4-v3cr>) (source ID: advisory). Maintainer advisory publication; not software release date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separately versioned resource edition established; product fix versions are recorded below\.
- **source displayed:** 2026-06-22; precision: day; basis: explicit; source: [OAuth Dynamic Client Registration Enables API Token Theft via Audience Confusion](<https://github.com/obot-platform/obot/security/advisories/GHSA-xwmw-prc4-v3cr>) (source ID: advisory). Publication date beside the advisory publisher\.

## Caveats

- Publisher prerequisites: affected versions through v0\.22\.1, application authentication enabled, and interaction by an already signed-in victim\. No preexisting attacker account is required\.
- The maintainer credits EQSTLab as reporter\. No award claim is made\.
- GitHub records September 18, 2026 database publication and review separately from June 22 maintainer publication\. The release page displays June 17 without a year in the retrieved text; no full software-release date is inferred\.
- The reviewed sources do not establish automatic revocation of previously issued tokens after upgrade; historical exposure and remediation validation remain deployment-specific\.
- Conceptual defensive summary only; public disclosure grants no testing authorization\.

## Sources and attribution

- [OAuth Dynamic Client Registration Enables API Token Theft via Audience Confusion](<https://github.com/obot-platform/obot/security/advisories/GHSA-xwmw-prc4-v3cr>) — Obot; source ID: advisory; provenance: official primary; retrieved 2026-10-03T08:39:25Z; supports: summary, dates.
- [Obot v0\.23\.0 release notes](<https://github.com/obot-platform/obot/releases/tag/v0.23.0>) — Obot; source ID: release; provenance: official primary; retrieved 2026-10-03T08:39:25Z; supports: summary.
- [GHSA-xwmw-prc4-v3cr publication history](<https://github.com/advisories/GHSA-xwmw-prc4-v3cr>) — GitHub; source ID: database-history; provenance: official primary; retrieved 2026-10-03T08:39:25Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
