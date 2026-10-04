# Payload: request adapters must retain caller-level authorization

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/payload-2026-local-api-caller-authority.json>) · [Official resource](<https://github.com/jhb-software/payload-plugins/security/advisories/GHSA-4qpv-39hg-f7fx>)

**Publisher:** jhb-software / Payload plugins  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Authorization  
**Defensive skills:** Model access-control invariants; Threat-model integrations; Verify remediation evidence

## Original summary

CVE-2026-59965 describes authenticated plugin endpoints invoking a privileged server interface without preserving collection-level authorization\. Payload's Local API skips access checks by default, so a session check alone did not establish permission for selected upload documents\. The conceptual failure is a request adapter inheriting trusted-server authority instead of retaining the caller's permissions\.

## Defensive use

Treat every request-to-server-API adapter as an authority boundary\. Explicitly preserve the requesting actor and require the relevant collection policy for both reads and changes\. Separate permission to use a feature from permission to act on its underlying data, and distinguish the collections a plugin manages from those a particular caller may access\. These are editorial design-review objectives; the presence of a policy definition does not establish that an operation evaluates it\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Authentication versus operation-specific authorization
- Server-side API defaults, caller context and collection access policies

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory, official framework documentation and release evidence\.

**Reviewed:** 2026-10-04T18:24:39Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Advisory, framework documentation and official release metadata read\. This is source review, not independent reproduction or a current deployment assessment\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-21; precision: day; basis: explicit; source: [Alt Text Endpoint Authorization Bypass via Payload Local API overrideAccess Omission](<https://github.com/jhb-software/payload-plugins/security/advisories/GHSA-4qpv-39hg-f7fx>) (source ID: maintainer). Publication of the selected advisory\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition is established\.
- **source displayed:** 2026-06-21; precision: day; basis: explicit; source: [Alt Text Endpoint Authorization Bypass via Payload Local API overrideAccess Omission](<https://github.com/jhb-software/payload-plugins/security/advisories/GHSA-4qpv-39hg-f7fx>) (source ID: maintainer).

## Caveats

- The issue requires the affected alt-text plugin, an authenticated caller and collection policies that would otherwise deny the requested access\. It is not an unauthenticated access claim\.
- The advisory reports unauthorized upload-document reads and changes to alt text and keywords; this does not establish unrestricted field writes\. Its supplied demonstration uses the real plugin handler with a mocked Payload framework, not a complete deployed stack\. Production compromise, account takeover and independent reproduction are not established here\.
- The advisory lists plugin versions before 0\.8\.0 as affected and 0\.8\.0 as patched\. This historical minimum is not a comprehensive current security guarantee\.
- The official 0\.8\.0 release notes describe reads and writes under the requesting user's collection access rules, plus rejection of collections outside plugin management\. Release metadata records June 21, 2026 at 11:45:15 UTC; that software-release time is separate from the unknown resource-edition date\.
- The advisory credits EQSTLab as Reporter and 232-323 as Finder\. jhb-dev is the publishing account, not an explicit article byline, so authors remains empty\. No individual award is established by these sources\.

## Sources and attribution

- [Alt Text Endpoint Authorization Bypass via Payload Local API overrideAccess Omission](<https://github.com/jhb-software/payload-plugins/security/advisories/GHSA-4qpv-39hg-f7fx>) — jhb-software / Payload plugins; source ID: maintainer; provenance: official primary; retrieved 2026-10-04T18:22:57Z; supports: summary, dates.
- [Payload Local API documentation](<https://payloadcms.com/docs/local-api/overview>) — Payload; source ID: framework; provenance: official primary; retrieved 2026-10-04T18:23:39Z; supports: summary.
- [Official alt-text 0\.8\.0 release notes and metadata](<https://api.github.com/repos/jhb-software/payload-plugins/releases/tags/alt-text%400.8.0>) — jhb-software / Payload plugins via GitHub; source ID: release; provenance: official primary; retrieved 2026-10-04T18:23:10Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
