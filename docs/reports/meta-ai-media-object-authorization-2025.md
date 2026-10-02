# Meta AI media access lacked object-ownership authorization

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Meta  
**Product:** Meta AI media editing

## What the evidence establishes

Publication window: uncertain original publication date; reviewed as of 2026-10-02.

A missing media-ownership check earned a USD 10,000 award, according to the researcher\.

### Root cause

A media-editing API did not bind the requested object to the authenticated owner\.

### Bounded impact

Another user’s private prompts and generated media could be disclosed\. The reproduced vendor response says no abuse was found\.

### Defensive lessons

- Apply object-ownership checks consistently across media access and editing operations\.
- Track temporary mitigation separately from confirmation of a complete fix\.

## Award and evidence

**USD 10,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported\_with\_vendor\_quote. The researcher explicitly states USD and reproduces the vendor award decision\. Settlement is unverified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/meta-ai-media-object-authorization-2025.json>).

## Dates

- **published:** Unknown; precision: unknown; basis: not\_reported. Page is labeled Updated July 16, 2025; original publication is unknown\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported. First public disclosure is not established; article update date is July 16, 2025\.
- **reported:** 2024-12-26; precision: day; basis: explicit
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Full fix confirmed April 24, 2025; deployment date is not separately established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** 2025-01-24; precision: day; basis: explicit. Timeline labels this a temporary fix\.

## Verification limits

Reviewed: 2026-10-02T16:30:37Z. Read the researcher article, explicit USD timeline and reproduced vendor response\.

- Vendor wording is researcher-published, not independent vendor confirmation\.
- An updated date does not establish original publication\. Full-fix confirmation does not establish deployment timing\.
- Cash receipt is not established\.

## Sources and attribution

- [Meta AI prompts and generated content: technical analysis](<https://www.appsecure.security/blog/meta-ai-prompt-and-genertaed-content-leakage-technical-analysis>) — Sandeep / AppSecure; retrieved 2026-10-02T16:30:37Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
