# HackerOne exports omitted internal-attachment authorization

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** HackerOne  
**Product:** HackerOne report archive export

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

HackerOne awarded $12,500 for internal attachments exposed through report export in 2016\. Its enduring lesson for 2026 applications is that export and interactive views must enforce the same visibility policy\.

### Root cause

Export authorization diverged from report-view visibility\. A file moved into an internal comment remained exportable\. The researcher compared redacted display content with archive output; the vendor confirmed this was a distinct newly introduced issue\.

### Bounded impact

A user able to export a report could obtain team-only attachments\. Vendor review additionally identified potential inline-attachment exposure, but found no evidence of malicious exploitation\. This does not establish access to every private report\.

### Defensive lessons

- Derive export contents from the same object-level policy used for interactive views\.
- Treat referenced attachments as independently authorized objects, including after visibility changes\.

## Award and evidence

**USD 12,500** — bug\_bounty; single\_report; status: awarded.

Evidence level: platform\_confirmed. One report-level award includes the vendor’s expanded inline-attachment impact assessment\. USD uses later platform-wide payment guidance reviewed in 2026, about ten years after the award; it does not prove individual settlement\. The report explicitly distinguishes earlier report 182358\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/hackerone-export-attachment-authorization-2016.json>).

## Dates

- **published:** 2016-11-30; precision: day; basis: explicit. Detailed report became public at the recorded disclosure event; later 2017 retrospective is not original publication\.
- **public disclosure:** 2016-11-30; precision: day; basis: explicit
- **reported:** 2016-11-29; precision: day; basis: explicit
- **awarded:** 2016-11-30; precision: day; basis: explicit
- **fixed:** 2016-11-29; precision: day; basis: explicit. Vendor fix-release comment at 04:36 UTC; researcher confirmation at 05:02 UTC\. Summary says November 28 without a timezone; UTC timeline supplies the recorded date\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T14:00:08Z. Read the full public report in the cloud browser, including vendor summary, fix confirmation, award and disclosure timeline; corroborated award with the vendor retrospective\. Reviewed currency guidance separately\.

- No independent confirmation of cash settlement\.
- Currency uses later platform-wide guidance, not an explicit currency code in the historical award event\.
- Summary uses November 28 without timezone; the report and fix events display November 29 UTC\.
- No patch implementation is disclosed\.

## Sources and attribution

- [Internal attachments can be exported via "Export as \.zip" feature](<https://hackerone.com/reports/186230>) — HackerOne and japz; retrieved 2026-10-03T14:00:08Z.
- [Celebrating $20M in Bounties with a Recap of Our Top 20 Up Voted Reports on Hacktivity](<https://www.hackerone.com/blog/celebrating-20m-bounties-recap-our-top-20-voted-reports-hacktivity>) — johnk / HackerOne; retrieved 2026-10-03T14:00:08Z.
- [Vulnerability Disclosure Guidelines](<https://www.hackerone.com/terms/disclosure-guidelines>) — HackerOne; retrieved 2026-10-03T14:00:08Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
