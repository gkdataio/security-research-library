# Framework serialization change exposed private HackerOne user attributes

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** HackerOne  
**Product:** HackerOne report serialization

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

The cited vendor documents a USD 25,000 award for this finding\.

### Root cause

A framework upgrade changed JSON serialization behavior, exposing private user attributes in public report data\. Explicit response allowlists and privacy-focused contract tests help prevent this class of regression\.

### Bounded impact

Sensitive user-data exposure and cross-program linking risk\. HackerOne describes the report as Critical and confirms remediation and retesting\.

### Defensive lessons

- Serialize only explicitly allowed response fields\.
- Include privacy-contract regression checks in framework upgrades\.

## Award and evidence

**USD 25,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. Vendor confirms the individual report’s reward; exact award and payment dates are not supplied\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/hackerone-report-json-serialization-data-exposure-2025.json>).

## Dates

- **published:** 2025-06-24; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T14:43:00Z. Primary public sources read; individual reward, dates, and attribution reviewed\. No target testing performed\.

- June 24 is the vendor case-study date, not an asserted first disclosure or payment date
- Public report requires JavaScript; exact timeline and researcher identity were not recovered
- The security issue was serialization, not a vulnerability in Hai itself

## Sources and attribution

- [Framework serialization change exposed private HackerOne user attributes](<https://www.hackerone.com/blog/hai-insight-agent-case-study>) — Crystal Hazen / HackerOne; retrieved 2026-10-02T14:43:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
