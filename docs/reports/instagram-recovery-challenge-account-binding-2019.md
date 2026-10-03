# Instagram recovery challenges were insufficiently bound to accounts

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Facebook / Instagram  
**Product:** Instagram account recovery

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

The researcher reports a $10,000 award for this finding\. USD is a contextual currency inference from Facebook’s later official retrospective of its 2019 bounty program, not an explicit denomination in the individual award statement\.

### Root cause

Recovery challenge state did not maintain sufficiently strict binding among account, device context, and verification secret\. Review challenge ownership and uniqueness throughout the recovery lifecycle\.

### Bounded impact

Researcher reports a separate, lower-severity account-takeover finding, fixed before publication\.

### Defensive lessons

- Bind recovery attempts and verification state to the intended account\.
- Use atomic security counters and test concurrent state transitions locally\.

## Award and evidence

**USD 10,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. Individual finding, distinct from the researcher’s other Instagram recovery report; no additional bonus is counted\. The primary article states $10000 without naming the currency\. USD is a contextual inference from source-3, Facebook’s official 2019 program retrospective published February 7, 2020, roughly six months after the August 25, 2019 original article publication\. The retrospective reports program-wide amounts in USD; it does not independently establish the denomination or settlement of this individual award\. Exact award/payment dates remain unknown\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/instagram-recovery-challenge-account-binding-2019.json>).

## Dates

- **published:** 2019-08-25; precision: day; basis: explicit. Original publication date preserved by the author’s archive; current article header is a later update\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T23:53:25Z. Re-read the primary article award statement and Facebook’s official 2019 program retrospective for contextual currency evidence\. Existing publication chronology retained\. No target testing performed\.

- The current 2024 article header is not the original disclosure date
- Exact report, fix, and award dates are unavailable
- No independent vendor-hosted payout confirmation retrieved
- Current article update: 2024-12-06; original publication is stored separately\.
- USD is inferred from later program-wide context \(source-3\), not explicitly stated by the individual award source; neither individual denomination nor cash settlement is independently confirmed\.

## Related conceptual diagrams

- [Recovery must preserve account ownership](<../diagram-gallery.md#account-recovery-challenge-lifecycle>)

## Sources and attribution

- [Instagram recovery challenges were insufficiently bound to accounts](<https://thezerohack.com/hack-instagram-again>) — Laxman Muthiyah; retrieved 2026-10-03T23:51:11Z.
- [Original publication archive](<https://thezerohack.com/digital-marketing>) — Laxman Muthiyah; retrieved 2026-10-02T14:43:00Z.
- [Facebook 2019 Bug Bounty retrospective — contextual USD denomination only](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook; retrieved 2026-10-03T23:50:58Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
