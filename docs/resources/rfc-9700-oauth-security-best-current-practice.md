# RFC 9700: Best Current Practice for OAuth 2\.0 Security

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/rfc-9700-oauth-security-best-current-practice.json>) · [Official resource](<https://www.rfc-editor.org/rfc/rfc9700.html>)

**Publisher:** Internet Engineering Task Force / RFC Editor  
**Authors:** Not identified in the reviewed record  
**Resource type:** Technical Standard  
**Version:** RFC 9700 / BCP 240  
**Topics:** Identity  
**Defensive skills:** Review identity lifecycle; Model access-control invariants; Threat-model integrations

## Original summary

Consensus guidance updating OAuth's security model with deployment experience, stronger protocol requirements, and deprecated insecure patterns\. A primary reference for identity integration reviews\.

## Defensive use

Compare an owned integration's documented design against the standard and record deviations and compensating controls\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- OAuth roles and authorization flows
- HTTP redirects and TLS
- Basic token and session concepts

## Access and freshness

**Access cost at review:** free.

Verified as free at review time; optional accounts or provider features may have separate terms\.

**Reviewed:** 2026-10-02T14:50:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Review records accessible official guidance as of this date; living content and current versions may change\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-01; precision: month; basis: explicit; source: [RFC 9700: Best Current Practice for OAuth 2\.0 Security](<https://www.rfc-editor.org/rfc/rfc9700.html>) (source ID: primary).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

No additional caveats recorded; this is not a completeness or security guarantee.

## Related conceptual diagrams

- [Delegated authority stays within the approved grant](<../diagram-gallery.md#delegated-grant-authority-continuity>)
- [An identity claim must belong to the user](<../diagram-gallery.md#identity-claim-binding>)

## Sources and attribution

- [RFC 9700: Best Current Practice for OAuth 2\.0 Security](<https://www.rfc-editor.org/rfc/rfc9700.html>) — Internet Engineering Task Force / RFC Editor; source ID: primary; provenance: official primary; retrieved 2026-10-02T14:50:00Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
