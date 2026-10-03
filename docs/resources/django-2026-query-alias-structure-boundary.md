# Django: ORM alias metadata must not acquire query authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/django-2026-query-alias-structure-boundary.json>) · [Official resource](<https://www.djangoproject.com/weblog/2026/feb/03/security-releases/>)

**Publisher:** Django Software Foundation  
**Authors:** Jacob Walls  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Verification  
**Defensive skills:** Review input trust boundaries; Review parsing and serialization; Verify remediation evidence

## Original summary

Django confirms CVE-2026-1312: application-controlled column aliases could cross from metadata into SQL structure when used across relation filtering and ordering\. Exploitability requires an application to admit untrusted alias definitions into that ORM workflow; using Django alone does not establish exposure\. The advisory establishes potential SQL injection, not observed production compromise\.

## Defensive use

The official announcement identifies repaired releases 6\.0\.2, 5\.2\.11 and 4\.2\.28, issued February 3, 2026; release notes independently corroborate the 6\.0\.2 fix\. Editorial lesson: distinguish query values from identifiers and structural metadata, constrain each according to its role, and preserve that contract when composing ORM features\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- ORM query composition and the distinction between bound values and SQL identifiers
- Tracing application-controlled metadata across library interfaces

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and official release documentation\.

**Reviewed:** 2026-10-03T09:09:13Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory and release documentation reviewed\. No reproduction, live-target access, or independent patch testing\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-02-03; precision: day; basis: explicit; source: [Django security releases issued: 6\.0\.2, 5\.2\.11, and 4\.2\.28](<https://www.djangoproject.com/weblog/2026/feb/03/security-releases/>) (source ID: advisory). Advisory publication, separate from software remediation chronology\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource-edition release established; software patch releases are described in defensive\_use\.
- **source displayed:** 2026-02-03; precision: day; basis: explicit; source: [Django security releases issued: 6\.0\.2, 5\.2\.11, and 4\.2\.28](<https://www.djangoproject.com/weblog/2026/feb/03/security-releases/>) (source ID: advisory). Explicit primary advisory publication date\.

## Caveats

- Solomon Kebede is the credited reporter; Jacob Walls authored the announcement\. No bounty amount is established\.
- This resource covers CVE-2026-1312 only\. Other issues in the same multi-issue announcement are not merged into its impact\.
- The reviewed announcement lists supported branches; it does not establish the status of every unsupported release\.
- No specific application data loss or universal remote exposure is demonstrated by the reviewed sources\. Learning prerequisites and generalized design guidance are editorial\.

## Sources and attribution

- [Django security releases issued: 6\.0\.2, 5\.2\.11, and 4\.2\.28](<https://www.djangoproject.com/weblog/2026/feb/03/security-releases/>) — Django Software Foundation; source ID: advisory; provenance: official primary; retrieved 2026-10-03T09:09:13Z; supports: summary, dates.
- [Django 6\.0\.2 release notes](<https://docs.djangoproject.com/en/dev/releases/6.0.2/>) — Django Software Foundation; source ID: release; provenance: official primary; retrieved 2026-10-03T09:09:13Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
