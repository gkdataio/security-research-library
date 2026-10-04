# Serialize JavaScript: every serialized field must retain data semantics

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/serialize-javascript-2026-output-code-boundary.json>) · [Official resource](<https://github.com/yahoo/serialize-javascript/security/advisories/GHSA-5c6j-r48x-rmvq>)

**Publisher:** Yahoo serialize-javascript  
**Authors:** redonkulus  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Verification; Interpreter Boundaries  
**Defensive skills:** Review parsing and serialization; Review input trust boundaries; Verify remediation evidence

## Original summary

The maintainer describes inconsistent escaping across structured-object serialization: some object-derived strings entered generated JavaScript without equivalent protection\. Code execution requires attacker-influenced objects and subsequent executable interpretation of the output\. The advisory demonstrates local execution; universal remote exploitability or production compromise is not established\.

## Defensive use

The maintainer advisory and official release identify 7\.0\.3 as the repair\. Editorial lesson: audit serialization contracts across every supported type and output consumer, including overridable object behavior\. Prefer data-only exchange where possible and avoid granting generated text execution authority merely because a serializer produced it\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- JavaScript object behavior and serialization contracts
- Data versus executable-output trust boundaries

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and release notes\.

**Reviewed:** 2026-10-03T08:19:27Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory and official release reviewed\. No reproduction or independent patch testing performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-02-27; precision: day; basis: explicit; source: [RCE via RegExp\.flags and Date\.prototype\.toISOString\(\)](<https://github.com/yahoo/serialize-javascript/security/advisories/GHSA-5c6j-r48x-rmvq>) (source ID: advisory). Maintainer advisory publication, not software-release chronology\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource-edition release established\.
- **source displayed:** 2026-02-27; precision: day; basis: explicit; source: [RCE via RegExp\.flags and Date\.prototype\.toISOString\(\)](<https://github.com/yahoo/serialize-javascript/security/advisories/GHSA-5c6j-r48x-rmvq>) (source ID: advisory). Advisory publication date\.

## Caveats

- The maintainer table says affected versions are below 7\.0\.2, but its prose includes 7\.0\.2\. The GitHub-reviewed entry includes 7\.0\.2; all reviewed sources identify 7\.0\.3 as patched\.
- The maintainer labels this an incomplete CVE-2020-7660 fix, while the GitHub-reviewed entry assigns no known CVE\. The stable identity here is GHSA-5c6j-r48x-rmvq; its 2026 publication does not make the earlier CVE a 2026 identifier\.
- The advisory credits uug4na as reporter; redonkulus is the publishing maintainer\. No bounty established\.
- The software-release page displays February 27 without a year in the retrieved rendering\. No exact software-release date is inferred; advisory publication is independently explicit\.
- Learning prerequisites and generalized design guidance are editorial\. Control of ordinary JSON alone does not establish the object-control and executable-consumer prerequisites\.

## Sources and attribution

- [RCE via RegExp\.flags and Date\.prototype\.toISOString\(\)](<https://github.com/yahoo/serialize-javascript/security/advisories/GHSA-5c6j-r48x-rmvq>) — Yahoo serialize-javascript; source ID: advisory; provenance: official primary; retrieved 2026-10-03T08:19:27Z; supports: summary, dates.
- [Serialize JavaScript v7\.0\.3 release](<https://github.com/yahoo/serialize-javascript/releases/tag/v7.0.3>) — Yahoo serialize-javascript; source ID: release; provenance: official primary; retrieved 2026-10-03T08:19:27Z; supports: summary.
- [Serialize JavaScript is Vulnerable to RCE via RegExp\.flags and Date\.prototype\.toISOString\(\)](<https://github.com/advisories/GHSA-5c6j-r48x-rmvq>) — GitHub Advisory Database; source ID: reviewed-entry; provenance: official primary; retrieved 2026-10-03T08:19:27Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
