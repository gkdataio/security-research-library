# File Browser: existing shares must follow current owner permissions

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/filebrowser-2026-share-owner-permission-lifecycle.json>) · [Official resource](<https://github.com/filebrowser/filebrowser/security/advisories/GHSA-v9w4-gm2x-6rvf>)

**Publisher:** File Browser  
**Authors:** hacdias  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Business Logic and State Integrity  
**Defensive skills:** Model access-control invariants; Verify remediation evidence; Review identity lifecycle

## Original summary

GHSA-v9w4-gm2x-6rvf describes public file-sharing authority outliving its owner's permissions\. Creating a share required sharing and download rights, but subsequent public access did not revalidate those rights\. The maintainer-published report describes continued file retrieval after revocation in version 2\.62\.2\.

## Defensive use

Editorial lesson: permission changes must constrain previously issued capabilities, not only new capability creation\. The merged remediation checks the owner's current sharing and download permissions during public access\. Its pull-request description records separate regression cases for revoking either permission\. Model issuance and later use as distinct authorization decisions\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic server-side authorization concepts

## Access and freshness

**Access cost at review:** free.

Public primary sources readable without an account\.

**Reviewed:** 2026-10-03T10:50:10Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory and linked remediation evidence reviewed; deployment status was not assessed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-04-04; precision: day; basis: explicit; source: [Share links remain accessible after Share/Download permissions are revoked](<https://github.com/filebrowser/filebrowser/security/advisories/GHSA-v9w4-gm2x-6rvf>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-04-04; precision: day; basis: explicit; source: [Share links remain accessible after Share/Download permissions are revoked](<https://github.com/filebrowser/filebrowser/security/advisories/GHSA-v9w4-gm2x-6rvf>) (source ID: advisory).

## Caveats

- Requires an existing share and access to its link, followed by revocation of the owner's relevant permissions\. This is a source-reported demonstration, not independently reproduced here; no production exposure is established\.
- CVE-2026-35604\. The advisory lists versions through 2\.62\.2 as affected and 2\.63\.1 as patched; it does not resolve the intervening-version gap\. Pull request 5888 was merged April 4, 2026; that merge date is not a verified package-release date\.
- Published by hacdias; Koda Reef \(kodareef5\) is credited as reporter and authored the remediation pull request\. Resource edition is unspecified\. The repository displayed an August 31, 2026 archive notice at review\.

## Sources and attribution

- [Share links remain accessible after Share/Download permissions are revoked](<https://github.com/filebrowser/filebrowser/security/advisories/GHSA-v9w4-gm2x-6rvf>) — File Browser; source ID: advisory; provenance: official primary; retrieved 2026-10-03T10:50:10Z; supports: summary, version, dates.
- [Pull request 5888: share-owner permission revalidation](<https://github.com/filebrowser/filebrowser/pull/5888>) — File Browser; source ID: fix; provenance: official primary; retrieved 2026-10-03T10:50:10Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
