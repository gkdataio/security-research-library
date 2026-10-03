# Chrome Local Network Access: separate browser reachability from site authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/chrome-local-network-permission-boundaries.json>) · [Official resource](<https://developer.chrome.com/blog/local-network-access>)

**Publisher:** Google Chrome for Developers  
**Authors:** Chris Thompson  
**Resource type:** Architecture Guide  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations  
**Defensive skills:** Review client isolation; Threat-model integrations; Model access-control invariants

## Original summary

Chrome's design addresses websites using the browser's network position to reach local devices without a separate user decision\. A secure-context permission gate reduces local-device CSRF and network fingerprinting\. The 2026 Chrome 145 release refines the boundary by separating local-network permission from loopback permission\.

## Defensive use

Editorial lesson: distinguish a website's origin, the browser's network reachability and the user's intended destination class\. Document which local integration actually needs permission and preserve a usable denial path\. Treat the grant as permission to connect, not proof of application-level authorization\. Review local-device authentication separately\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Browser origins, secure contexts and network address spaces

## Access and freshness

**Access cost at review:** free.

Public primary-source guidance\.

**Reviewed:** 2026-10-03T17:29:30Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Original guide and Chrome 142/145 documentation reviewed earlier; Chrome 147 coverage clarification added after fresh release-note review\. No live behavior was tested\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-06-09; precision: day; basis: explicit; source: [New permission prompt for Local Network Access](<https://developer.chrome.com/blog/local-network-access>) (source ID: guide). Historical guide with a separately dated September 2025 launch update\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Browser milestones are implementation chronology, not resource editions\.
- **source displayed:** 2025-09-29; precision: day; basis: explicit; source: [New permission prompt for Local Network Access](<https://developer.chrome.com/blog/local-network-access>) (source ID: guide). Explicit inline update; the footer still displays 2025-06-09\.

## Caveats

- The guide describes an evolving rollout and replaces the earlier Private Network Access preflight approach\. Its initial transport limitations are historical, not a verified inventory of current gaps\.
- Chrome 142 release notes identify an October 28, 2025 stable release and include local-to-loopback requests, beyond the original guide’s first-milestone scope\. Chrome 145 notes identify February 10, 2026 and separate local and loopback permissions while retaining the older permission name as an alias\.
- Chrome 147 release notes, last updated April 7, 2026, document permission gating for WebSockets and WebTransport and extend service-worker navigation coverage to subframes\. Those notes expressly exclude main-frame navigations; permission coverage must not be generalized to every browser request\.
- This is architectural guidance rather than a vulnerability or award report\. Browser-wide implementation parity and current enterprise-policy coverage were not established\.

## Sources and attribution

- [New permission prompt for Local Network Access](<https://developer.chrome.com/blog/local-network-access>) — Google Chrome for Developers; source ID: guide; provenance: official primary; retrieved 2026-10-03T15:20:45Z; supports: summary, dates.
- [Chrome 142](<https://developer.chrome.com/release-notes/142>) — Google Chrome for Developers; source ID: chrome-142; provenance: official primary; retrieved 2026-10-03T15:20:45Z; supports: summary.
- [Chrome 145](<https://developer.chrome.com/release-notes/145>) — Google Chrome for Developers; source ID: chrome-145; provenance: official primary; retrieved 2026-10-03T15:20:45Z; supports: summary.
- [Chrome 147: Local Network Access](<https://developer.chrome.com/release-notes/147>) — Google Chrome for Developers; source ID: chrome-147; provenance: official primary; retrieved 2026-10-03T17:29:30Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
