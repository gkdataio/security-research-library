# Facebook error responses exposed unintended application data

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

[Read the original source](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook · [Canonical JSON](<../../data/reports/facebook-error-response-data-isolation-2019.json>)

<a id="what-the-evidence-establishes"></a>
## Main takeaway

Facebook error responses could include application data that the requester should not receive\. The initial finding led Facebook to review a broader error-handling problem\. Facebook confirms a USD 65,000 payment for the report\.

**Organization:** Meta \(Facebook\)  
**Product:** Facebook copyright-management endpoint and shared error handling

<a id="root-cause"></a>
## What went wrong

An error-handling configuration could include unintended application data in a response; subsequent review found a broader framework issue\.

<a id="bounded-impact"></a>
## What the evidence shows

A copyright-management request could return data fragments not intended for the requester\. The award reflected the vendor’s assessment of potential wider impact\.

## Defensive lessons

- Apply data-minimization rules to error responses as well as successful responses\.
- Review shared exception-handling behavior after an endpoint-level fix\.

## Award and evidence

**USD 65,000** — bug\_bounty; single\_report; status: paid.

Evidence level: vendor\_confirmed. Vendor explicitly identifies USD and says the report was paid\. Exact transfer date is unknown; this is not the event or program total\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/facebook-error-response-data-isolation-2019.json>).

## Dates

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

- **published:** 2020-02-07; precision: day; basis: explicit. Initial page date; a separate May 7, 2020 update is displayed\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported. The reviewed vendor retrospective was published February 7, 2020; earliest public disclosure is not established\.
- **reported:** 2019-09; precision: month; basis: inferred. September event in the vendor’s 2019 retrospective; the day is unspecified\.
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Vendor states an initial fix followed within hours of the report, then broader framework remediation; exact deployment dates are not supplied\.
- **paid:** Unknown; precision: unknown; basis: not\_reported. Vendor confirms payment but gives no transfer date\.
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T18:24:00Z. Read the official vendor retrospective and its explicit US-dollar per-report payment\. Summaries retain the vendor’s bounded impact statement\.

- Historical case; exact award, settlement and deployment dates are unknown\.
- The source gives a high-level finding, not a complete technical advisory\.

## Related conceptual diagrams

- [Failures need separate public and diagnostic contracts](<../diagram-gallery.md#error-diagnostic-disclosure-boundary>)

## Sources and attribution

- [2019 Bug Bounty highlights, official Spanish edition](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook; retrieved 2026-10-02T18:24:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
