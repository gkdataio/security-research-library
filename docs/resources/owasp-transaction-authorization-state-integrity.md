# OWASP Transaction Authorization

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/owasp-transaction-authorization-state-integrity.json>) · [Official resource](<https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html>)

**Publisher:** OWASP Cheat Sheet Series  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Business Logic and State Integrity; Authorization  
**Defensive skills:** Review approval-state integrity; Reason about concurrent state; Model access-control invariants; Review security-token design

## Original summary

Explains operation-specific approval: show significant transaction details, preserve authorized data, enforce valid state transitions and recheck authorization at execution\.

## Defensive use

Model an owned workflow’s approval states, expiration and invalidation rules, and relate each transition to a server-side invariant\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Authentication versus operation authorization
- Basic application state-machine concepts

## Access and freshness

**Access cost at review:** free.

Public official guidance\.

**Reviewed:** 2026-10-02T16:39:51Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Living guidance; original publication and latest-update dates were not established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Approval controls must match the application’s risk and workflow\. This reference does not prescribe financial or legal policy\.

## Related conceptual diagrams

- [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>)

## Sources and attribution

- [Transaction Authorization Cheat Sheet](<https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html>) — OWASP Cheat Sheet Series; source ID: primary; provenance: official primary; retrieved 2026-10-02T16:39:51Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
