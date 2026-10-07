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

**Reviewed:** 2026-10-07T01:00:44Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Scoped completeness review of the Account Recovery After Suspected Compromise section in the current official page and OWASP Markdown, recorded as source compromise-recovery-guidance\. The added caveats complement the existing summary; this review does not establish publication, version-release or latest-update dates for the living resource\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Password reset and multifactor recovery are distinct security decisions\.
- During recovery after suspected compromise, changing the password may leave unauthorized access through existing sessions or altered recovery and MFA settings\.
- Recovery assurance must rely on independent evidence established previously, rather than recent recovery-setting changes alone\. With the verified owner, review recovery contacts and MFA methods and remove unauthorized changes\.
- Promptly suspend or invalidate authenticators known to be compromised\. Successful recovery must also invalidate existing sessions and unused password-reset or recovery links and codes\.
- Do not automatically reinstate replaced recovery contacts; loss or compromise may have prompted their removal\.

## Related conceptual diagrams

- [Recovery must preserve account ownership](<../diagram-gallery.md#account-recovery-challenge-lifecycle>)

## Sources and attribution

- [Forgot Password Cheat Sheet](<https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html>) — OWASP Cheat Sheet Series; source ID: primary; provenance: official primary; retrieved 2026-10-02T16:59:00Z; supports: summary.
- [Forgot Password Cheat Sheet: Account Recovery After Suspected Compromise](<https://github.com/OWASP/CheatSheetSeries/blob/29994dd8a2e6f50fa3d5607b046b54d7c6945afd/cheatsheets/Forgot_Password_Cheat_Sheet.md#account-recovery-after-suspected-compromise>) — OWASP Cheat Sheet Series; source ID: compromise-recovery-guidance; provenance: official primary; retrieved 2026-10-07T01:00:23Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
