# Parse Server: preserve safe file interpretation across storage and browsers

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/parse-server-2026-upload-metadata-consumer-boundary.json>) · [Official resource](<https://github.com/parse-community/parse-server/security/advisories/GHSA-r899-h629-j84r>)

**Publisher:** Parse Community  
**Authors:** mtrezza  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Verification  
**Defensive skills:** Review input trust boundaries; Review parsing and serialization; Verify remediation evidence

## Original summary

GHSA-r899-h629-j84r describes inconsistent interpretation of uploaded-file metadata across admission, storage and browser consumption\. The maintainer reports stored cross-site scripting when unsupported filename types retained invalid media-type metadata\. The affected storage configurations preserved that metadata; default GridFS is explicitly unaffected\.

## Defensive use

The maintainer recommends corrected versions, application-specific file allowlists, origin separation for uploads and storage-layer anti-sniffing policy\. Editorial lesson: admission checks and delivery behavior form one security contract\. A successful upload validation result alone does not establish that later consumers will treat the object as inert data\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic web upload handling and server-side validation
- Content-type interpretation and processing lifecycle concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and remediation references\.

**Reviewed:** 2026-10-03T12:19:32Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed maintainer sources and the merged version-9 patch to qualify configuration-dependent validation\. The version-8 diff was not independently inspected\. No reproduction or patch testing\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-25; precision: day; basis: explicit; source: [Stored XSS via malformed Content-Type bypassing file upload extension blocklist](<https://github.com/parse-community/parse-server/security/advisories/GHSA-r899-h629-j84r>) (source ID: advisory). Maintainer advisory publication\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition established\. Software fix chronology appears in caveats\.
- **source displayed:** 2026-06-25; precision: day; basis: explicit; source: [Stored XSS via malformed Content-Type bypassing file upload extension blocklist](<https://github.com/parse-community/parse-server/security/advisories/GHSA-r899-h629-j84r>) (source ID: advisory). Publication date displayed on the advisory\.

## Caveats

- Requires upload permission, a storage/delivery configuration retaining supplied metadata, and another user opening the uploaded object\. Browser-side script execution is maintainer-reported; production exploitation, account takeover and server compromise are not established\.
- The advisory lists affected ranges as &lt;= 8\.6\.83 and &gt;= 9\.0\.0, &lt; 9\.10\.0-alpha\.2\. It identifies 8\.6\.84 and 9\.10\.0-alpha\.2 as patched\.
- The version-8 and version-9 remediation records show June 25, 2026 merges and releases; the version-9 stable release 9\.10\.0 is dated July 13, 2026\. These are software events, not educational-resource editions\.
- CyberKareem is credited as finder and mtrezza as coordinator/advisory publisher\. No CVE is listed on the reviewed advisory\.
- The version-9 correction validates supplied media types for unrecognized filename extensions when extension filtering is enabled; disabling that filtering also disables this validation\. Well-formed custom types remain subject to configured restrictions\. This does not establish that all accepted content is harmless\.
- Learning prerequisites and the generalized consumer-contract lesson are editorial\. No award claim is made\.

## Sources and attribution

- [Stored XSS via malformed Content-Type bypassing file upload extension blocklist](<https://github.com/parse-community/parse-server/security/advisories/GHSA-r899-h629-j84r>) — Parse Community; source ID: advisory; provenance: official primary; retrieved 2026-10-03T12:09:10Z; supports: summary, dates.
- [Parse Server 9 remediation, pull request 10521](<https://github.com/parse-community/parse-server/pull/10521>) — Parse Community; source ID: remediation-v9; provenance: official primary; retrieved 2026-10-03T12:09:10Z; supports: summary, version, dates.
- [Parse Server 8 remediation, pull request 10523](<https://github.com/parse-community/parse-server/pull/10523>) — Parse Community; source ID: remediation-v8; provenance: official primary; retrieved 2026-10-03T12:09:10Z; supports: version, dates.
- [Parse Server 9\.10\.0 release](<https://github.com/parse-community/parse-server/releases/tag/9.10.0>) — Parse Community; source ID: release-v9; provenance: official primary; retrieved 2026-10-03T12:10:36Z; supports: version, dates.
- [Version-9 merged metadata-validation patch and configuration scope](<https://github.com/parse-community/parse-server/commit/cce91e554818492d1b153c46dc3b91fa6e0309bc>) — Parse Community; source ID: v9-merged-patch; provenance: official primary; retrieved 2026-10-03T12:19:32Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
