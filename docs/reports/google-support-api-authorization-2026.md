# Google support API exposed customer and agent data

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Google Real-time Support API

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-02.

A support-system authorization flaw received a documented USD 14,337 award\.

### Root cause

An internal support-data operation lacked the necessary restriction on ordinary authenticated accounts\.

### Bounded impact

Customer contact details and agent activity information were exposed\. The total affected record count was not confirmed by Google\.

### Defensive lessons

- Apply authorization consistently to every internal-data operation\.
- Minimize sensitive information returned by support integrations\.

## Award and evidence

**USD 14,337** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported\_with\_vendor\_quote. Single report award includes a USD 1,000 report-quality bonus; no settlement date is given\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-support-api-authorization-2026.json>).

## Dates

- **published:** 2026-03-31; precision: day; basis: explicit
- **public disclosure:** 2026-03-31; precision: day; basis: explicit
- **reported:** 2025-06-01; precision: day; basis: explicit
- **awarded:** 2025-06-10; precision: day; basis: explicit
- **fixed:** 2025-11-12; precision: day; basis: explicit
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T14:39:00Z. Primary public source read; individual award and source provenance verified\. No target testing or exploit reproduction performed\.

- Award is reported by the cited source; cash settlement is not independently audited\.

## Sources and attribution

- [Hacking Google Support: Leaking millions of customer records \($14k bounty\)](<https://michaeldalton.au/posts/hacking-google-support>) — Michael Dalton; retrieved 2026-10-02T14:39:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
