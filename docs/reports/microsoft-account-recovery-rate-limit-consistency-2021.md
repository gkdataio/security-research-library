# Microsoft account recovery lacked consistent attempt-limit enforcement

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Microsoft  
**Product:** Microsoft account recovery

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

The cited researcher documents a USD 50,000 award for this finding\.

### Root cause

Recovery controls did not enforce attempt limits consistently across simultaneous verification operations\. Defensive reviews should verify atomic, account-bound limits and consistent treatment of recovery and multifactor checks\.

### Bounded impact

Potential account takeover; the researcher says Microsoft classified severity as Important because practical exploitation required substantial resources\.

### Defensive lessons

- Bind recovery attempts and verification state to the intended account\.
- Use atomic security counters and test concurrent state transitions locally\.

## Award and evidence

**USD 50,000** — bug\_bounty; single\_report; status: paid.

Evidence level: researcher\_reported. Researcher says the bounty was received on February 9, 2021; that is the payment date, not a separately confirmed award-decision date\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/microsoft-account-recovery-rate-limit-consistency-2021.json>).

## Dates

- **published:** 2021-03-02; precision: day; basis: explicit. Original publication date preserved by the author’s archive; current article header is a later update\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** 2020-11; precision: month; basis: explicit
- **paid:** 2021-02-09; precision: day; basis: explicit
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T14:43:00Z. Primary public sources read; individual reward, dates, and attribution reviewed\. No target testing performed\.

- The article header now shows a 2024 update; its archive preserves March 2, 2021 publication
- No independent vendor-hosted payout confirmation retrieved
- Current article update: 2024-12-06; original publication is stored separately\.

## Related conceptual diagrams

- [Recovery must preserve account ownership](<../diagram-gallery.md#account-recovery-challenge-lifecycle>)

## Sources and attribution

- [Microsoft account recovery lacked consistent attempt-limit enforcement](<https://thezerohack.com/how-i-might-have-hacked-any-microsoft-account>) — Laxman Muthiyah; retrieved 2026-10-02T14:43:00Z.
- [Original publication archive](<https://thezerohack.com/digital-marketing>) — Laxman Muthiyah; retrieved 2026-10-02T14:43:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
