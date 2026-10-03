# Shopify Exchange screenshot service crossed internal boundaries

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Shopify  
**Product:** Shopify Exchange screenshot service

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

Shopify awarded USD 25,000 for a screenshot-service request-isolation flaw with impact bounded to one infrastructure subset\.

### Root cause

Server-side fetching crossed the boundary between externally influenced screenshot work and internal infrastructure\. The vendor’s remediation targeted metadata access and internal destinations; its retrospective omits authentication prerequisites and the researcher’s reasoning process\.

### Bounded impact

Shopify confirms reported root-access capability across containers in the affected subset, explicitly excluding Shopify core\. The retrospective does not establish compromise of every container or quantify exposed data\. The service was disabled within an hour; infrastructure review preceded metadata shielding and internal-address restrictions\.

### Defensive lessons

- Editorial lesson: separately enforce request-destination policy, workload privilege and infrastructure segmentation; each limits a different boundary\.
- Editorial lesson: treat metadata as privileged infrastructure data and deny unneeded service access\.
- Editorial lesson: preserve the distinction between a demonstrated access capability and a claim of widespread compromise\.

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

Reviewed: 2026-10-02T23:00:55Z. Reread the vendor retrospective, including its impact boundary and remediation account\. No target testing\.

- The publication date is retrospective, not the original discovery date\.
- Underlying report details were not independently reread; no additional exploit prerequisites or investigative chronology are asserted\.

## Related conceptual diagrams

- [Layer server-request destination controls](<../diagram-gallery.md#server-request-destination-policy>)

## Sources and attribution

- [One Million Dollars in Bug Bounties](<https://shopify.engineering/one-million-dollars-in-bug-bounties>) — Peter Yaworski / Shopify; retrieved 2026-10-02T23:00:55Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
