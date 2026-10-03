# Rocket\.Chat: authentication must await a completed verification decision

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/rocketchat-2026-asynchronous-identity-verification.json>) · [Official resource](<https://securitylab.github.com/advisories/GHSL-2026-004_GHSL-2026-005_Rocket_Chat/>)

**Publisher:** GitHub Security Lab  
**Authors:** Peter Stöckli  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Web Foundations  
**Defensive skills:** Review identity lifecycle; Reason about concurrent state; Verify remediation evidence

## Original summary

CVE-2026-28514 concerned asynchronous password verification in the enterprise account service\. The authentication decision treated an unfinished validation object as success instead of using its eventual result\. The researcher tested Rocket\.Chat 7\.13\.2; the maintainer corroborates unauthorized access to available service methods, with possible account takeover depending on subsequent application behavior\.

## Defensive use

Editorial lesson: model authentication as a completed, explicit decision; pending, rejected, and failed validation must not imply success\. Maintain regression coverage for asynchronous rejection and service-specific authentication equivalence\. The maintainer remediation requires waiting for verification and recommends tooling to detect unhandled asynchronous results\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic server-side authentication and authorization concepts

## Access and freshness

**Access cost at review:** free.

Public sources readable without an account\.

**Reviewed:** 2026-10-03T09:29:37Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Research and maintainer evidence reviewed; no live deployment or remediation testing performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-03-12; precision: day; basis: explicit; source: [GHSL-2026-004\_GHSL-2026-005: Authentication bypass in Rocket\.Chat](<https://securitylab.github.com/advisories/GHSL-2026-004_GHSL-2026-005_Rocket_Chat/>) (source ID: research).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Resource has no stated release version; software fixes are described separately\.
- **source displayed:** 2026-03-12; precision: day; basis: explicit; source: [GHSL-2026-004\_GHSL-2026-005: Authentication bypass in Rocket\.Chat](<https://securitylab.github.com/advisories/GHSL-2026-004_GHSL-2026-005_Rocket_Chat/>) (source ID: research).

## Caveats

- Requires the affected enterprise streaming/account-service deployment and an account with password authentication configured; the reported identity must be known or guessable\. Do not generalize this to every Rocket\.Chat installation or authentication mode\.
- The researcher describes broad takeover potential\. The maintainer impact statement is narrower: access to available service methods, with takeover dependent on the application path\. Neither source supplies a customer incident count\.
- Reported January 9, 2026; the researcher dates the initial 8\.0\.0 fix to January 12 and supported-version fixes to March 5\. The maintainer advisory was published March 5; detailed research March 12\. These are not resource version-release dates\.
- Maintainer-listed patched releases: 8\.0\.0, 7\.13\.3, 7\.12\.4, 7\.11\.4, 7\.10\.7, 7\.9\.8 and 7\.8\.6\. No deployment remediation was verified\.
- The research page also covers CVE-2026-30833; this resource is confined to asynchronous authentication verification and does not summarize a combined attack\.
- Byline: Peter Stöckli\. Discovery used GitHub Security Lab Taskflow Agent, manually verified by Peter Stöckli and Man Yue Mo\. Learning prerequisites are editorial\.

## Sources and attribution

- [GHSL-2026-004\_GHSL-2026-005: Authentication bypass in Rocket\.Chat](<https://securitylab.github.com/advisories/GHSL-2026-004_GHSL-2026-005_Rocket_Chat/>) — GitHub Security Lab; source ID: research; provenance: official primary; retrieved 2026-10-03T09:29:37Z; supports: summary, dates.
- [Users can login with any password via the EE ddp-streamer-service](<https://github.com/RocketChat/Rocket.Chat/security/advisories/GHSA-w6vw-mrgv-69vf>) — Rocket\.Chat; source ID: maintainer-advisory; provenance: official primary; retrieved 2026-10-03T09:29:37Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
