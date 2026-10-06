# Vite: local reachability does not establish browser-origin authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/vite-2025-development-server-origin-authority.json>) · [Official resource](<https://github.com/vitejs/vite/security/advisories/GHSA-vg6x-rcgg-rjx6>)

**Publisher:** Vite  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Authorization  
**Defensive skills:** Review client isolation; Threat-model integrations; Verify remediation evidence

## Original summary

CVE-2025-24010 describes three development-server trust gaps: permissive HTTP response sharing, missing WebSocket origin validation and missing HTTP hostname validation\. Editorial boundary: local reachability does not establish the connecting website's authority\.

## Defensive use

Current Vite guidance recommends explicit trusted-origin and controlled-host lists, and warns against all-origin CORS and all-host acceptance\. Editorial lesson: document three separate decisions: who may read HTTP responses, who may join a realtime channel and which hostname a service answers to\. HTTP configuration does not substitute for WebSocket admission protection\. Keep those policies narrow while reviewing reverse proxies and framework/plugin integrations\. Select a currently supported patched release; inspect the actual deployment rather than treating a historical fix number as present-day upgrade advice\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Browser origins, HTTP response-sharing policy and WebSocket admission
- Development-server configuration and integration trust boundaries

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and current official configuration documentation\.

**Reviewed:** 2026-10-06T15:23:17Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Read the maintainer advisory and current server-option documentation\. No software execution, target testing or independent reproduction performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-01-20; precision: day; basis: explicit; source: [Vite development-server security advisory GHSA-vg6x-rcgg-rjx6](<https://github.com/vitejs/vite/security/advisories/GHSA-vg6x-rcgg-rjx6>) (source ID: advisory). Original maintainer-advisory publication\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No educational-resource edition date established; software fix versions remain separate\.
- **source displayed:** 2025-01-20; precision: day; basis: explicit; source: [Vite development-server security advisory GHSA-vg6x-rcgg-rjx6](<https://github.com/vitejs/vite/security/advisories/GHSA-vg6x-rcgg-rjx6>) (source ID: advisory). Publication date shown beside the publishing account\.

## Caveats

- Affected versions listed by the advisory are &lt;=4\.5\.5, 5\.0\.0–5\.4\.11 and 6\.0\.0–6\.0\.8; initial fixes are 4\.5\.6, 5\.4\.12 and 6\.0\.9\.
- Applicability requires a running affected development server and user interaction with an untrusted page, even with loopback-only listening\. Browser-specific qualifications describe 2025, not verified 2026 behavior\.
- The source describes a demonstration of HMR-message and source-snippet disclosure\. Broader source exposure is advisory-described; additional plugin/proxy consequences are conditional\. The advisory says Vite core has no request-triggered functionality that changes other state\.
- sapphi-red published the advisory; ivantsepp is credited as Reporter\. Neither role establishes an article byline, so authors remains empty\.
- Historical publication outside the preferred trailing-year window\. Included for its server-side origin/hostname checks, complementing Chrome Local Network Access's browser connection-permission model and Open WebUI's session-revocation consistency case\.
- Current server-option documentation is living guidance, not proof of January 2025 defaults or present browser-wide protection\. No production compromise, individual award or independent reproduction is established\. This educational case grants no testing authorization\.

## Sources and attribution

- [Vite development-server security advisory GHSA-vg6x-rcgg-rjx6](<https://github.com/vitejs/vite/security/advisories/GHSA-vg6x-rcgg-rjx6>) — Vite; source ID: advisory; provenance: official primary; retrieved 2026-10-06T15:21:12Z; supports: summary, dates.
- [Vite Server Options](<https://vite.dev/config/server-options>) — Vite; source ID: server-options; provenance: official primary; retrieved 2026-10-06T15:21:12Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
