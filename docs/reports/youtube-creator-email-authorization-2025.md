# YouTube creator metadata exposed private email addresses

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** YouTube Studio and Content ID APIs

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

A cross-API privacy finding received a USD 20,000 award after a documented adjustment\.

### Root cause

Inconsistent field-level access controls exposed private creator metadata across related APIs\.

### Bounded impact

Private email addresses associated with monetized channels could be disclosed\.

### Defensive lessons

- Apply field-level authorization consistently across APIs\.
- Treat cross-service identifiers as data, never as proof of entitlement\.

## Award and evidence

**USD 20,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. USD 13,337 initial award plus USD 6,663 adjustment for this same report; awarded date records the final adjustment\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/youtube-creator-email-authorization-2025.json>).

## Dates

- **published:** 2025-03-13; precision: day; basis: explicit
- **public disclosure:** 2025-03-13; precision: day; basis: explicit
- **reported:** 2024-12-12; precision: day; basis: explicit
- **awarded:** 2025-01-23; precision: day; basis: explicit
- **fixed:** 2025-02-21; precision: day; basis: explicit
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T14:39:00Z. Primary public source read; individual award and source provenance verified\. No target testing or exploit reproduction performed\.

- Award is reported by the cited source; cash settlement is not independently audited\.

## Sources and attribution

- [Disclosing YouTube Creator Emails for a $20k Bounty](<https://brutecat.com/articles/youtube-creator-emails/>) — Arvin Shivram \(Brutecat\); retrieved 2026-10-02T14:39:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
