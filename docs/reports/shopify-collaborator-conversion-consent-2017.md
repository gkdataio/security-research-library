# Shopify automatic account conversion lost merchant-consent binding

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Shopify  
**Product:** Shopify partner collaborator accounts

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

Shopify confirms a $20,000 award for unauthorized collaborator access caused by automatic account conversion\.

### Root cause

Account-conversion logic did not preserve the distinction between identity linkage and authorization to collaborate on a merchant’s store\. The vendor attributes the issue to automatic conversion of ordinary accounts into collaborator accounts\.

### Bounded impact

The vendor confirms unintended store access without merchant interaction in a partner-account context, and says it fixed the issue within hours\. Its retrospective does not establish data extraction, the exact permissions obtained or the researcher’s discovery process\.

### Defensive lessons

- Editorial lesson: require an independently verified entitlement for each role transition; matching identity attributes do not prove resource access rights\.
- Editorial lesson: preserve merchant approval when accounts are linked, merged or automatically converted\.
- Editorial lesson: model authorization before and after lifecycle transitions, including repeated or conflicting identities, using approved test accounts\.

## Award and evidence

**USD 20,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. One report, separate from event totals\. USD is a contextual inference from HackerOne’s 2026 platform policy, nine years after the 2017 award; that policy does not prove settlement\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/shopify-collaborator-conversion-consent-2017.json>).

## Dates

- **published:** 2018-02-22; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** 2017; precision: year; basis: explicit. The vendor identifies the award as occurring during 2017; no precise day is supplied\.
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Vendor reports a fix within hours but supplies no calendar date in the reviewed retrospective\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T02:32:41Z. Read public primary-source text and checked award scope, provenance and dates\. No target testing\.

- The underlying linked HackerOne report was JavaScript-only in text retrieval and was not independently reviewed\.
- Currency context is platform-wide and later than the award; no independent payment audit is claimed\.
- No exact reporting, fix or payment date was established\.

## Sources and attribution

- [2017 Bug Bounty Year in Review](<https://shopify.engineering/bug-bounty-year-in-review>) — Peter Yaworski / Shopify; retrieved 2026-10-03T02:32:41Z.
- [Vulnerability Disclosure Standards](<https://www.hackerone.com/terms/disclosure-guidelines>) — HackerOne; retrieved 2026-10-03T02:32:41Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
