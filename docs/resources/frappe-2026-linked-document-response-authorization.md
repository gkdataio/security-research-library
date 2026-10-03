# Frappe: linked data must preserve document and field permissions

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/frappe-2026-linked-document-response-authorization.json>) · [Official resource](<https://securitylab.github.com/advisories/GHSL-2026-012_Frappe/>)

**Publisher:** GitHub Security Lab  
**Authors:** Man Yue Mo  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Web Foundations  
**Defensive skills:** Model access-control invariants; Review parsing and serialization; Verify remediation evidence

## Original summary

CVE-2026-39351 concerns related-document expansion in a REST response\. Frappe loaded linked records without checking the caller’s permission and serialized them without field filtering\. The research identifies disclosure of otherwise inaccessible documents in tested version 15\.96\.0\.

## Defensive use

Editorial lesson: authorization on a parent object cannot authorize every object reachable from it\. Define response contracts that preserve both per-document access and field visibility during expansion\. The maintainer advisory identifies patched releases 15\.104\.0 and 16\.14\.0; it does not describe the patch implementation\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic API access-control concepts
- Familiarity with server-side data processing

## Access and freshness

**Access cost at review:** free.

Public sources readable without an account\.

**Reviewed:** 2026-10-03T07:10:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary research and maintainer evidence reviewed\. Article immutability and deployment remediation were not established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-04-24; precision: day; basis: explicit; source: [GHSL-2026-012: Unauthorized Data Exposure via REST API Link Expansion in Frappe - CVE-2026-39351](<https://securitylab.github.com/advisories/GHSL-2026-012_Frappe/>) (source ID: research).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-04-24; precision: day; basis: explicit; source: [GHSL-2026-012: Unauthorized Data Exposure via REST API Link Expansion in Frappe - CVE-2026-39351](<https://securitylab.github.com/advisories/GHSL-2026-012_Frappe/>) (source ID: research).

## Caveats

- Requires a readable parent document whose expanded links reach records the caller cannot otherwise access; it does not establish unrestricted access to every document\.
- The publication explains the code-level disclosure mechanism but supplies no customer incident or measured data-loss evidence\. Do not infer write access or account takeover\.
- Reported January 19, 2026; maintainer advisory published April 7; detailed research published April 24\. Fix-release dates were not established by the reviewed sources\.
- The byline is Man Yue Mo\. Discovery is credited to GitHub Security Lab Taskflow Agent, with human review by Peter Stöckli and Man Yue Mo\. Learning prerequisites are editorial\.

## Sources and attribution

- [GHSL-2026-012: Unauthorized Data Exposure via REST API Link Expansion in Frappe - CVE-2026-39351](<https://securitylab.github.com/advisories/GHSL-2026-012_Frappe/>) — GitHub Security Lab; source ID: research; provenance: official primary; retrieved 2026-10-03T07:10:00Z; supports: summary, dates.
- [Unrestricted Doctype access via API exploit](<https://github.com/frappe/frappe/security/advisories/GHSA-8ggw-hfr6-rw3x>) — Frappe; source ID: maintainer-advisory; provenance: official primary; retrieved 2026-10-03T07:10:00Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
