# Uptime Kuma: separate notification-template authority from server files

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/uptime-kuma-2025-notification-template-file-boundary.json>) · [Official resource](<https://github.com/louislam/uptime-kuma/security/advisories/GHSA-vffh-c9pq-4crh>)

**Publisher:** Uptime Kuma maintainers  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Interpreter Boundaries; Web Foundations  
**Defensive skills:** Review input trust boundaries; Review secrets containment; Verify remediation evidence

## Original summary

The October 2025 advisory identifies post-authentication SSTI \(CWE-1336\): editable notification templates were evaluated by Liquid with insufficiently restricted file capabilities\. Template-editing authority thereby reached server-side filesystem access\. The reported outcome is server file disclosure\. A 2026 follow-up says the initial restrictions left a file-resolution fallback outside the intended boundary\.

## Defensive use

Editorial lesson: define a minimal capability set for user-editable templates and keep notification formatting separate from host-file authority\. Apply containment consistently across every resolution path, including fallbacks; process-level least privilege limits exposure but does not repair template isolation\. Review later maintainer advisories before treating an earlier patch as complete\. The 2\.2\.1 release credits upstream LiquidJS remediation\. Capability removal is suggested in the follow-up advisory, but this review does not establish that suggestion as the shipped implementation\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Server-side template evaluation and capability boundaries
- Application-process file permissions and remediation evidence

## Access and freshness

**Access cost at review:** free.

Public maintainer advisories and release history\.

**Reviewed:** 2026-10-05T02:15:14Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Original advisory, incomplete-fix follow-up and both release notices reviewed\. No target testing, vulnerability reproduction or independent patch execution performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-10-20; precision: day; basis: explicit; source: [Server-side Template Injection \(SSTI\) in Notification Templates Allows Arbitrary File Read](<https://github.com/louislam/uptime-kuma/security/advisories/GHSA-vffh-c9pq-4crh>) (source ID: advisory). Explicit original advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No educational-resource edition date established; software release and follow-up disclosure dates remain separate\.
- **source displayed:** 2025-10-20; precision: day; basis: explicit; source: [Server-side Template Injection \(SSTI\) in Notification Templates Allows Arbitrary File Read](<https://github.com/louislam/uptime-kuma/security/advisories/GHSA-vffh-c9pq-4crh>) (source ID: advisory). The original advisory header displays its publication date\.

## Caveats

- Applicability requires an authenticated user able to edit notification templates in an affected configuration\. File disclosure is bounded by application-process read permissions; operating-system execution and production compromise are not established by these sources\.
- The original advisory lists &gt;=1\.23\.0 through 1\.23\.16 and &lt;=2\.0\.0-beta\.4 as affected, with 1\.23\.17 and 2\.0\.0 initially marked patched\. The October 20, 2025 release of 2\.0\.0 references that advisory; these historical patch claims are qualified by the later incomplete-fix evidence\.
- GHSA-v832-4r73-wx5j, published March 16, 2026, reports continued file disclosure on 2\.1\.3 and lists 2\.2\.1 as patched\. Its affected field says &gt;=1\.23\.0 without an upper bound\. The March 10, 2026 release of 2\.2\.1 attributes the correction to upstream LiquidJS\. These are software and follow-up disclosure events, not this resource's original publication or edition date\.
- louislam published the original advisory; TriangleSnake is credited as Reporter\. No separate author byline was established, so authors remains empty\. The follow-up separately credits peaktwilight as Reporter\.
- The original advisory states no known CVE\. CVE-2026-33130 belongs to the follow-up advisory and is not assigned to the 2025 finding here\. The follow-up supplies remediation context for this single educational record, not a second 2026 case\.
- Historical fixed-version labels are source claims, not a current safety recommendation or independent proof of patch effectiveness\. No qualifying individual award is established\. Learning prerequisites and generalized defensive guidance are editorial\.

## Sources and attribution

- [Server-side Template Injection \(SSTI\) in Notification Templates Allows Arbitrary File Read](<https://github.com/louislam/uptime-kuma/security/advisories/GHSA-vffh-c9pq-4crh>) — Uptime Kuma maintainers; source ID: advisory; provenance: official primary; retrieved 2026-10-05T02:13:50Z; supports: summary, dates.
- [Uptime Kuma 2\.0\.0 release](<https://github.com/louislam/uptime-kuma/releases/tag/2.0.0>) — Uptime Kuma maintainers; source ID: original-release; provenance: official primary; retrieved 2026-10-05T02:14:15Z; supports: summary, dates.
- [Another Server-side Template Injection \(SSTI\) in Notification Templates Allows Arbitrary File Read](<https://github.com/louislam/uptime-kuma/security/advisories/GHSA-v832-4r73-wx5j>) — Uptime Kuma maintainers; source ID: follow-up-advisory; provenance: official primary; retrieved 2026-10-05T02:12:18Z; supports: summary, dates.
- [Uptime Kuma 2\.2\.1 release](<https://github.com/louislam/uptime-kuma/releases/tag/2.2.1>) — Uptime Kuma maintainers; source ID: follow-up-release; provenance: official primary; retrieved 2026-10-05T02:14:15Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
