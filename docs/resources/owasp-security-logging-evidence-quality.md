# OWASP Logging: trustworthy and minimal application evidence

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html>) · [Canonical JSON](<../../data/resources/owasp-security-logging-evidence-quality.json>)

<a id="original-summary"></a>
## Main takeaway

OWASP explains how consistent context, interaction identifiers, outcomes and confidence information make logs more useful for investigations\. It distinguishes when an event happened from when it was recorded and treats event data from other systems as untrusted\. Useful evidence also requires limited data collection, access restrictions, integrity protection and reliable logging\.

## Defensive use

Using synthetic events in an owned application, review whether records can explain a decision without exposing credentials or personal data\. Document correlation gaps, timestamp uncertainty and what the logs cannot prove\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** OWASP Cheat Sheet Series  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Verification; Reporting  
**Defensive skills:** Write bounded security evidence; Review secrets containment; Review input trust boundaries

## Prerequisites

**Basis:** editorial guidance.

- Basic familiarity with application events and structured logs
- Understanding of sensitive-data handling and access controls

## Access and freshness

**Access cost at review:** free.

Official public guidance; no account required to read\.

**Reviewed:** 2026-10-03T01:41:34Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed the current official guidance\. No publication, release or last-update date was established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Logging does not automatically provide independent proof or non-repudiation\.
- Collection and retention must match the authorized purpose; more recorded data is not necessarily better evidence\.

## Related conceptual diagrams

- [Failures need separate public and diagnostic contracts](<../diagram-gallery.md#error-diagnostic-disclosure-boundary>)

## Sources and attribution

- [OWASP Logging: trustworthy and minimal application evidence](<https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html>) — OWASP Cheat Sheet Series; source ID: primary; provenance: official primary; retrieved 2026-10-03T01:39:33Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
