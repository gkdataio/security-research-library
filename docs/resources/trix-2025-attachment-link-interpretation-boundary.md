# Trix: validate stored attachment data before link interpretation

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/trix-2025-attachment-link-interpretation-boundary.json>) · [Official resource](<https://github.com/basecamp/trix/security/advisories/GHSA-g9jg-w8vm-g96v>)

**Publisher:** Trix maintainers  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Interpreter Boundaries  
**Defensive skills:** Review input trust boundaries; Review client isolation; Verify remediation evidence

## Original summary

The Trix maintainer advisory explicitly identifies stored XSS involving attachment metadata, later HTML rendering and a user click\. It describes JavaScript running in the user’s session, with possible unauthorized actions or information disclosure\. Conceptual root cause: stored attachment data was reused as link authority without validating its meaning in that browser context; storage does not confer trust\.

## Defensive use

Editorial lesson: validate the meaning of untrusted values whenever data becomes an active browser attribute, including after storage and transformation\. The maintainer patch and release notes add DOMPurify attribute validation before attachment links become anchors\. The patch includes regression assertions; reading them does not establish that tests ran or that every integration is protected\. Review the deployed rendering path and dependency state\. The historical patched version is not a current safety recommendation\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Browser attribute contexts and the distinction between stored data and active interpretation
- Rich-text attachment metadata and rendering lifecycles

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory, patch, release notes and supporting GitHub Advisory Database entry\.

**Reviewed:** 2026-10-05T18:32:37Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Read the maintainer advisory, patch, release notes and database entry\. No reproduction, target testing or independent patch verification performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-12-30; precision: day; basis: explicit; source: [Trix attachment-link security advisory GHSA-g9jg-w8vm-g96v](<https://github.com/basecamp/trix/security/advisories/GHSA-g9jg-w8vm-g96v>) (source ID: advisory). Original maintainer-advisory publication; later database events are separate\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No educational-resource edition date established; software releases are separate events\.
- **source displayed:** 2025-12-30; precision: day; basis: explicit; source: [Trix attachment-link security advisory GHSA-g9jg-w8vm-g96v](<https://github.com/basecamp/trix/security/advisories/GHSA-g9jg-w8vm-g96v>) (source ID: advisory). Publication date displayed by the selected primary advisory\.

## Caveats

- Applicability requires an affected editor integration, influence over attachment metadata, later rendering and a user click\. The low-privileges severity metric does not identify a specific application role or storage workflow\.
- The advisory lists npm trix and RubyGems action\_text-trix below 2\.1\.16 as affected and 2\.1\.16 as patched\. These are historical software-version statements, not an educational-resource edition\.
- The described impact is a maintainer claim; production exploitation, account takeover and independently reproduced execution are not established by this review\.
- flavorjones published the advisory; michaelcheers is credited as the reporting researcher\. No explicit author byline is established, so authors remains empty\.
- The database records publication there on December 31, 2025 and an update on January 8, 2026\. Neither replaces the December 30, 2025 primary publication\.
- The advisory lists no known CVE\. No qualifying individual award is established\. Learning prerequisites and generalized defensive guidance are editorial; this educational case grants no testing authorization\.

## Sources and attribution

- [Trix attachment-link security advisory GHSA-g9jg-w8vm-g96v](<https://github.com/basecamp/trix/security/advisories/GHSA-g9jg-w8vm-g96v>) — Trix maintainers; source ID: advisory; provenance: official primary; retrieved 2026-10-05T18:31:19Z; supports: summary, dates.
- [Trix attachment-link validation patch](<https://github.com/basecamp/trix/commit/73c20cf03ab2b56c0ef9c9b1aaf63f2de44f4010>) — Trix maintainers; source ID: patch; provenance: official primary; retrieved 2026-10-05T18:31:19Z; supports: summary.
- [Trix v2\.1\.16 release notes](<https://github.com/basecamp/trix/releases/tag/v2.1.16>) — Trix maintainers; source ID: release; provenance: official primary; retrieved 2026-10-05T18:31:19Z; supports: summary.
- [GitHub Advisory Database entry for GHSA-g9jg-w8vm-g96v](<https://github.com/advisories/GHSA-g9jg-w8vm-g96v>) — GitHub Advisory Database; source ID: advisory-database; provenance: official primary; retrieved 2026-10-05T18:32:37Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
