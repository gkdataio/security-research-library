# STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/usenix-2025-tls-resumption-identity-isolation.json>) · [Official resource](<https://www.usenix.org/conference/usenixsecurity25/presentation/hebrok>)

**Publisher:** USENIX Association  
**Authors:** Sven Hebrok; Tim Leonhard Storm; Felix Matthias Cramer; Maximilian Radoy; Juraj Somorovsky  
**Resource type:** Research Paper  
**Version:** USENIX Security 2025  
**Topics:** Identity; Authorization; Web Foundations  
**Defensive skills:** Review identity lifecycle; Threat-model integrations; Review security-token design

## Original summary

Studies a cross-layer authentication failure: shared TLS session-ticket infrastructure can preserve cryptographic session state without preserving the intended virtual-host identity and client-authentication policy\. The authors connect that mismatch to inconsistent isolation during session resumption\.

## Defensive use

Document which authenticated identities and policy decisions must survive connection resumption in an owned hosting design\. Review library contracts and remediation evidence for preserved identity context rather than assuming that an accepted session ticket establishes all application authority\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- TLS certificates and session resumption
- Virtual hosting and application routing

## Access and freshness

**Access cost at review:** free.

Official publication record and publisher-hosted paper were readable without an account at review time\.

**Reviewed:** 2026-10-03T04:41:45Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed the official publication record and publisher-hosted paper’s discussion, countermeasures, limitations, and conclusion\. No research tooling was retrieved or run\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-08; precision: month; basis: explicit; source: [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](<https://www.usenix.org/conference/usenixsecurity25/presentation/hebrok>) (source ID: primary). Month in the publisher’s proceedings citation; not an inferred first online date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Measurements and vendor observations are historical, not evidence of present exposure\.
- The study describes sampling and configuration limits; its findings are not exhaustive\.
- This record summarizes identity invariants and countermeasures, not the paper’s testing procedures\.

## Sources and attribution

- [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](<https://www.usenix.org/conference/usenixsecurity25/presentation/hebrok>) — USENIX Association; source ID: primary; provenance: official primary; retrieved 2026-10-03T04:41:45Z; supports: summary, version, dates.
- [Publisher-hosted proceedings paper](<https://www.usenix.org/system/files/usenixsecurity25-hebrok.pdf>) — USENIX Association; source ID: paper; provenance: official primary; retrieved 2026-10-03T04:41:45Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
