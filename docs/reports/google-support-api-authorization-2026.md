# Google support API exposed customer and agent data

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Google Real-time Support API

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

Ordinary authenticated customers could read internal support activity; the researcher reports a USD 14,337 award\.

### Root cause

Customer authentication did not enforce the boundary around internal support-wide information\. The researcher contrasted denied resource-specific operations with an accessible aggregate operation\. This supports an authorization gap; middleware behavior and the intended management use remain hypotheses, not confirmed implementation details\.

### Bounded impact

Observed disclosures linked customer names or phone numbers with cases and agents, including agent activity\. Phishing and harassment were potential consequences\. Millions of affected records were estimated; conversation contents and call manipulation were not demonstrated\.

### Defensive lessons

- Editorial lesson: treat aggregate views as separately privileged resources; successful authentication is not evidence of permission to observe other users\.
- Editorial lesson: reducing identifiable details limits the harm when a support-data boundary fails\. The source does not document the deployed authorization repair\.

## Award and evidence

**USD 14,337** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported\_with\_vendor\_quote. Single report award includes a USD 1,000 report-quality bonus; no settlement date is given\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-support-api-authorization-2026.json>).

## Dates

- **published:** 2026-03-31; precision: day; basis: explicit
- **public disclosure:** 2026-03-31; precision: day; basis: explicit
- **reported:** 2025-06-01; precision: day; basis: explicit
- **awarded:** 2025-06-10; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported. The source records closure as fixed on November 12, 2025, not a deployment date\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T04:49:20Z. Fresh-read the primary disclosure and timeline; separated observed disclosure from hypothesized reach\. No target testing or reproduction\.

- Researcher-published evidence does not independently establish settlement, total affected population, backend implementation or deployed repair\.
- The prerequisite was an ordinary signed-in account; describing the exposure as unauthenticated would erase that requirement\.

## Sources and attribution

- [Hacking Google Support: Leaking millions of customer records \($14k bounty\)](<https://michaeldalton.au/posts/hacking-google-support>) — Michael Dalton; retrieved 2026-10-03T04:49:20Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
