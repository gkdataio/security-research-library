# OWASP Session Management: privilege-transition integrity

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/owasp-session-privilege-transition-integrity.json>) · [Official resource](<https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html>)

**Publisher:** OWASP Cheat Sheet Series  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; Web Foundations  
**Defensive skills:** Review identity lifecycle; Review security-token design; Model access-control invariants

## Original summary

Distinguishes application-issued session identifiers from client-selected values\. Explains renewing identifiers at login and other privilege changes, retiring previous identifiers, and separating anonymous tracking from authenticated session authority\. When several cookies represent one session, their relationship also requires validation\.

## Defensive use

Model login and privilege changes as explicit session-state transitions, with server-controlled identity and authority bindings\. Document which credentials represent anonymous and authenticated state and how superseded state loses authority\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic HTTP cookie and authentication concepts

## Access and freshness

**Access cost at review:** free.

Public official guidance\.

**Reviewed:** 2026-10-03T22:32:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Living guidance; publication and version dates were not established\. Review time does not imply a new edition or software release\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Renewing a session identifier does not establish authorization for every resource or action; access decisions remain a separate responsibility\.
- Official implementation guidance, not a product-specific finding, current-exposure claim or testing authorization\.

## Sources and attribution

- [Session Management Cheat Sheet](<https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html>) — OWASP Cheat Sheet Series; source ID: primary; provenance: official primary; retrieved 2026-10-03T22:32:00Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
