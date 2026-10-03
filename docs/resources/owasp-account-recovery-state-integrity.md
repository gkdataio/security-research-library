# OWASP Forgot Password

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/owasp-account-recovery-state-integrity.json>) · [Official resource](<https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html>)

**Publisher:** OWASP Cheat Sheet Series  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Business Logic and State Integrity  
**Defensive skills:** Review identity lifecycle; Review security-token design; Reason about concurrent state

## Original summary

Explains account-bound recovery challenges, limited lifetime and reuse, consistent responses, attempt controls, notifications and post-reset session handling\.

## Defensive use

Document recovery-state invariants and ensure recovery cannot silently weaken the account’s normal authentication requirements\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic authentication and session concepts

## Access and freshness

**Access cost at review:** free.

Public official guidance\.

**Reviewed:** 2026-10-02T16:59:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Living guidance; original publication and latest-update dates were not established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Password reset and multifactor recovery are distinct security decisions\.

## Related conceptual diagrams

- [Recovery must preserve account ownership](<../diagram-gallery.md#account-recovery-challenge-lifecycle>)

## Sources and attribution

- [Forgot Password Cheat Sheet](<https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html>) — OWASP Cheat Sheet Series; source ID: primary; provenance: official primary; retrieved 2026-10-02T16:59:00Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
