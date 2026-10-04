# Formie: integration settings need operation and attribute authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/formie-2026-integration-settings-credential-authority.json>) · [Official resource](<https://github.com/verbb/formie/security/advisories/GHSA-v3f3-cmj4-cvj9>)

**Publisher:** Verbb / Formie  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Web Foundations  
**Defensive skills:** Model access-control invariants; Threat-model integrations; Review secrets containment; Verify remediation evidence

## Original summary

Formie's advisory describes two coupled authority failures: an integration-settings operation lacked sufficient permission checks, and broad settings mutation could change the destination used with stored credentials\. The maintainer reports credential disclosure and server-side requests whose responses were returned to the caller\. The distinct lesson is to constrain both who may invoke an operation and which security-sensitive attributes it may change\.

## Defensive use

The two branch-specific patches require control-panel request context, a valid form and integration permission, then limit mutable settings while excluding destination and credential properties\. Editorial lesson: operation authorization and attribute authority are complementary controls; possessing an authenticated session does not establish either\. Review alternate entry points after a shared permission repair\. The official releases identify 2\.2\.23 for Craft 4 and 3\.1\.31 for Craft 5 as patched\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Distinguishing authentication from operation-specific authorization
- Understanding settings mutation and credential-bearing integration requests

## Access and freshness

**Access cost at review:** free.

The advisory, patches and release evidence are publicly readable\.

**Reviewed:** 2026-10-04T22:13:40Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory, both patches, database chronology and official release metadata reviewed\. This was source review, not reproduction or a deployment assessment\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-07-09; precision: day; basis: explicit; source: [Formie integration-settings security advisory](<https://github.com/verbb/formie/security/advisories/GHSA-v3f3-cmj4-cvj9>) (source ID: advisory). Maintainer publication; separate from the later database entry\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition date established\.
- **source displayed:** 2026-07-09; precision: day; basis: explicit; source: [Formie integration-settings security advisory](<https://github.com/verbb/formie/security/advisories/GHSA-v3f3-cmj4-cvj9>) (source ID: advisory). Publication date displayed by the maintainer advisory\.

## Caveats

- The described case requires an affected installation and an authenticated caller, including a front-end member; credential impact additionally depends on a configured integration holding credentials\.
- The advisory identifies incomplete earlier authorization remediation\. Temporary restrictions on registration and control-panel access are not a complete configuration-only fix\.
- The reviewed sources provide no controlled test transcript, production incident, victim count or independent reproduction\. Downstream account takeover or cloud compromise is not established\. No individual award is established\.
- The advisory body credits Jorge González as reporter; its formal credit lists Pig-Tail as Finder\. Their identity relationship is not established here\. engram-design is the publishing account, not an explicit narrative byline, so authors remains empty\.
- The GitHub database records its own publication and review on September 23, 2026\. The official release APIs give July 9, 2026 at 12:21:35 UTC for 2\.2\.23 and 12:26:02 UTC for 3\.1\.31\. Software release, advisory publication, database entry, educational edition and installation-specific deployment are separate events; deployment dates remain unknown\.

## Sources and attribution

- [Formie integration-settings security advisory](<https://github.com/verbb/formie/security/advisories/GHSA-v3f3-cmj4-cvj9>) — Verbb / Formie; source ID: advisory; provenance: official primary; retrieved 2026-10-04T22:12:53Z; supports: summary, version, dates.
- [GitHub Advisory Database entry for CVE-2026-76086](<https://github.com/advisories/GHSA-v3f3-cmj4-cvj9>) — GitHub; source ID: advisory-database; provenance: official primary; retrieved 2026-10-04T22:12:14Z; supports: dates, version.
- [Formie Craft 4 integration authorization and settings restriction patch](<https://github.com/verbb/formie/commit/6735fe4ae8f6a2a76930716ad7876b236f7c530d>) — Verbb / Formie; source ID: craft4-patch; provenance: official primary; retrieved 2026-10-04T22:12:43Z; supports: summary.
- [Formie Craft 5 integration authorization and settings restriction patch](<https://github.com/verbb/formie/commit/dde7799dfa7e4d0a11e28754ad8544dba62d5def>) — Verbb / Formie; source ID: craft5-patch; provenance: official primary; retrieved 2026-10-04T22:12:43Z; supports: summary.
- [Official Formie 2\.2\.23 release metadata](<https://api.github.com/repos/verbb/formie/releases/tags/2.2.23>) — Verbb / Formie; source ID: craft4-release; provenance: official primary; retrieved 2026-10-04T22:12:43Z; supports: version, dates.
- [Official Formie 3\.1\.31 release metadata](<https://api.github.com/repos/verbb/formie/releases/tags/3.1.31>) — Verbb / Formie; source ID: craft5-release; provenance: official primary; retrieved 2026-10-04T22:12:43Z; supports: version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
