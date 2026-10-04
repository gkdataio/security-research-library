# DOMPurify: accepted DOM realms must retain complete sanitization

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/dompurify-2026-cross-realm-sanitization-consistency.json>) · [Official resource](<https://github.com/cure53/DOMPurify/security/advisories/GHSA-hpcv-96wg-7vj8>)

**Publisher:** DOMPurify / Cure53  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Interpreter Boundaries  
**Defensive skills:** Review input trust boundaries; Review parsing and serialization; Verify remediation evidence

## Original summary

CVE-2026-49458 describes a mismatch between accepting DOM objects from another realm and recognizing them during later sanitization\. Checks tied to local constructor identity could omit protective decisions and subtree traversal\. The general lesson is that admitting an input representation also commits the implementation to enforcing every required security check for that representation\.

## Defensive use

Compare the set of accepted representations with the set covered by every protective decision, including nested content\. Treat an unrecognized representation as an explicit policy decision rather than silently skipping validation\. Review remediation and regression coverage together\. These are conceptual review objectives, not a claim that any specific proposed implementation was shipped or independently tested\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- JavaScript realm and DOM object concepts
- Sanitization, nested content and browser activation boundaries

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and official release evidence\.

**Reviewed:** 2026-10-04T17:55:25Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory and official release sources read\. Review does not establish current exposure or independently reproduce the behavior\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-05-26; precision: day; basis: explicit; source: [Cross-realm IN\_PLACE sanitization leaves executable markup intact via realm-bound instanceof checks](<https://github.com/cure53/DOMPurify/security/advisories/GHSA-hpcv-96wg-7vj8>) (source ID: maintainer). Publication of the selected advisory\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition is established\.
- **source displayed:** 2026-05-26; precision: day; basis: explicit; source: [Cross-realm IN\_PLACE sanitization leaves executable markup intact via realm-bound instanceof checks](<https://github.com/cure53/DOMPurify/security/advisories/GHSA-hpcv-96wg-7vj8>) (source ID: maintainer).

## Caveats

- The advisory requires attacker-influenced DOM from another same-origin realm, in-place sanitization and subsequent consumer activation\. It excludes ordinary string input and same-realm in-place use from this issue\.
- It reports script execution with Chromium 148 and DOMPurify 3\.4\.5\. Production compromise, account takeover and independent reproduction are not established here\.
- The advisory lists versions through 3\.4\.5 as affected and 3\.4\.6 as patched\. This historical minimum is not a comprehensive current security guarantee\.
- The official 3\.4\.6 release describes stronger cross-realm and shadow-DOM checks plus expanded regression coverage\. Its metadata records May 26, 2026 at 13:04:11 UTC; that software-release time is separate from the unknown resource-edition date\. Advisory suggestions are not evidence of exact shipped implementation\.
- The advisory credits offset as Reporter\. cure53 is the publishing account, not an explicit article byline, so authors remains empty\. Release-wide thanks to offset and Bankde do not establish both as reporters of this particular advisory\.

## Sources and attribution

- [Cross-realm IN\_PLACE sanitization leaves executable markup intact via realm-bound instanceof checks](<https://github.com/cure53/DOMPurify/security/advisories/GHSA-hpcv-96wg-7vj8>) — DOMPurify / Cure53; source ID: maintainer; provenance: official primary; retrieved 2026-10-04T17:52:49Z; supports: summary, dates.
- [DOMPurify 3\.4\.6](<https://github.com/cure53/DOMPurify/releases/tag/3.4.6>) — DOMPurify / Cure53; source ID: release; provenance: official primary; retrieved 2026-10-04T17:52:49Z; supports: summary, dates.
- [Official DOMPurify 3\.4\.6 release metadata](<https://api.github.com/repos/cure53/DOMPurify/releases/tags/3.4.6>) — DOMPurify / Cure53 via GitHub; source ID: release-metadata; provenance: official primary; retrieved 2026-10-04T17:54:37Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
