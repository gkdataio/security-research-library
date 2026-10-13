# Instagram mobile account recovery had inconsistent verification limits

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

[Read the original source](<https://thezerohack.com/hack-any-instagram>) — Laxman Muthiyah · [Canonical JSON](<../../data/reports/instagram-mobile-recovery-attempt-limits-2019.json>)

<a id="what-the-evidence-establishes"></a>
## Main takeaway

Instagram's mobile recovery checks did not consistently enforce account-level verification limits during concurrent activity\. The researcher demonstrated an unauthorized password reset and reports a USD 30,000 award\. He says the issue was fixed before publication\.

**Organization:** Facebook / Instagram  
**Product:** Instagram account recovery

<a id="root-cause"></a>
## What went wrong

Account recovery relied on verification limits that did not provide a consistent account-level security boundary under concurrent activity\. Centralized, atomic attempt accounting is the defensive concern\.

<a id="bounded-impact"></a>
## What the evidence shows

The researcher demonstrated unauthorized password reset and reports remediation before publication\.

## Defensive lessons

- Bind recovery attempts and verification state to the intended account\.
- Use atomic security counters and test concurrent state transitions locally\.

## Award and evidence

**USD 30,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. Individual finding, distinct from the researcher’s other Instagram recovery report; exact award/payment dates are unknown\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/instagram-mobile-recovery-attempt-limits-2019.json>).

## Dates

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

- **published:** 2019-07-14; precision: day; basis: explicit. Original publication date preserved by the author’s archive; current article header is a later update\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T14:43:00Z. Primary public sources read; individual reward, dates, and attribution reviewed\. No target testing performed\.

- The current 2024 article header is not the original disclosure date
- Exact report, fix, and award dates are unavailable
- Distinct from the August 2019 device-binding report
- Current article update: 2024-10-19; original publication is stored separately\.

## Sources and attribution

- [Instagram mobile account recovery had inconsistent verification limits](<https://thezerohack.com/hack-any-instagram>) — Laxman Muthiyah; retrieved 2026-10-02T14:43:00Z.
- [Original publication archive](<https://thezerohack.com/digital-marketing>) — Laxman Muthiyah; retrieved 2026-10-02T14:43:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
