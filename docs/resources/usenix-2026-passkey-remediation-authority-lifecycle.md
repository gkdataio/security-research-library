# Adversarial passkeys: account recovery must close every continuing source of authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/usenix-2026-passkey-remediation-authority-lifecycle.json>) · [Official resource](<https://www.usenix.org/conference/usenixsecurity26/presentation/daffalla>)

**Publisher:** USENIX Association  
**Authors:** Alaa Daffalla; Grace Myers; Rosanna Bellini; Thomas Ristenpart; Nicola Dell  
**Resource type:** Research Paper  
**Version:** USENIX Security 2026 proceedings  
**Topics:** Identity; Authorization; Web Foundations  
**Defensive skills:** Review identity lifecycle; Review approval-state integrity; Write bounded security evidence

## Original summary

A qualitative lab study of 31 participants across three services found that unclear passkey labels, notifications and recovery interfaces obstructed complete account remediation\. Conceptual boundary: proof that a recovery action completed does not establish that every independent credential or active session has lost authority\.

## Defensive use

Review an owned application’s recovery completion criteria across registered credentials, sessions and recovery channels\. Make security interfaces explain what each revocation changes and what remains authorized; use clear credential provenance and action-specific notifications\. Treat these as design-review questions, not evidence of a deployed fix\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Passkey registration and relying-party credential records
- Session invalidation and account-recovery concepts

## Access and freshness

**Access cost at review:** free.

Publisher page and full paper were publicly readable at review\.

**Reviewed:** 2026-10-03T06:50:31Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed publisher metadata and paper findings, discussion and limitations\. Proceedings edition identified; no separate revision date established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08; precision: month; basis: explicit; source: [“Maybe there’s only one passkey?”: Challenges Investigating and Remediating Adversarial Passkeys](<https://www.usenix.org/conference/usenixsecurity26/presentation/daffalla>) (source ID: primary). Publisher proceedings citation gives August 2026; first online publication day is not established\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- The simulated scenario presupposes earlier account access sufficient to register a credential; one service additionally required an email challenge\. This is not a cryptographic break of passkeys or evidence of unauthenticated access\.
- The paper reports that no participant completed all required remediation unaided\. This demonstrates usability failures in controlled test accounts, not population-wide compromise rates or current service exposure\.
- The small, single-city sample used researcher-provided devices and accounts; researcher assistance limits generalization of success rates\.
- The authors explicitly label proposed interface improvements speculative and needing validation\. Password reset, credential removal and session termination have distinct effects\.
- This is a conference proceedings research paper, not a vendor patch advisory; no fixed-version claim is made\.

## Sources and attribution

- [“Maybe there’s only one passkey?”: Challenges Investigating and Remediating Adversarial Passkeys](<https://www.usenix.org/conference/usenixsecurity26/presentation/daffalla>) — USENIX Association; source ID: primary; provenance: official primary; retrieved 2026-10-03T06:50:31Z; supports: summary, version, dates.
- [Publisher-hosted proceedings paper](<https://www.usenix.org/system/files/usenixsecurity26-daffalla.pdf>) — USENIX Association; source ID: paper; provenance: official primary; retrieved 2026-10-03T06:50:31Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
