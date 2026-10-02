# Shopify Exchange screenshot service crossed internal boundaries

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Shopify  
**Product:** Shopify Exchange screenshot service

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

Shopify confirms a USD 25,000 award for a screenshot-service isolation flaw\.

### Root cause

Server-initiated requests could reach internal infrastructure and metadata that should have been isolated\.

### Bounded impact

Root access was possible within one infrastructure subset\. Shopify explicitly says its core platform was outside that subset\.

### Defensive lessons

- Restrict service egress and protect infrastructure metadata\.
- Preserve strong isolation between infrastructure groups\.

## Award and evidence

**USD 25,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. Vendor retrospective explicitly ties this amount to one report\. Original report, award, and fix dates are not supplied\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/shopify-exchange-request-isolation-2019.json>).

## Dates

- **published:** 2019-04-03; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T14:39:00Z. Primary public source read; individual award and source provenance verified\. No target testing or exploit reproduction performed\.

- The 2019 date is the vendor retrospective publication, not the original discovery date\.
- The cited HackerOne report link did not expose readable report metadata during this review\.

## Related conceptual diagrams

- [Layer server-request destination controls](<../diagram-gallery.md#server-request-destination-policy>)

## Sources and attribution

- [One Million Dollars in Bug Bounties](<https://shopify.engineering/one-million-dollars-in-bug-bounties>) — Peter Yaworski / Shopify; retrieved 2026-10-02T14:39:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
