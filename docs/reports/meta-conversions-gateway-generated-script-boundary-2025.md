# Meta Conversions API Gateway mixed configuration data with executable output

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Meta  
**Product:** Conversions API Gateway

## What the evidence establishes

Publication window: uncertain original publication date; reviewed as of 2026-10-03.

The researcher attributes a USD 250,000 award to the article’s separately identified backend finding, Bug \#2\.

### Root cause

Configuration values were concatenated into generated JavaScript without context-safe serialization\. Stored data thereby acquired the authority of executable output\.

### Bounded impact

The researcher reports stored script execution in consuming pages and potential account compromise\. The article does not fully establish configuration-write prerequisites or independently substantiate its broader deployment and employee-system impact claims\.

### Defensive lessons

- Keep configuration data separate from executable source; use context-appropriate serialization and structured interfaces\.
- Treat shared analytics code as part of the consuming application’s trusted computing base\.
- Document configuration-write permissions, downstream consumers and remediation coverage independently; do not infer universal compromise from shared distribution\.

## Award and evidence

**USD 250,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. Only Bug \#2 is represented\. The separately awarded Bug \#1 is excluded; no awards are summed\. The source uses $\. USD is inferred from official 2020 program reporting, five years before this award, rather than an individual payment receipt\. No bonus or settlement is established\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/meta-conversions-gateway-generated-script-boundary-2025.json>).

## Dates

- **published:** Unknown; precision: unknown; basis: not\_reported. Current page header is January 13, 2026; a separately indexed 2025 URL also exists\. Original publication versus archive migration or republication is not established\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported. Earliest public disclosure is not established\.
- **reported:** 2024-11-22; precision: day; basis: explicit. Timeline entry specifically identified as Bug \#2\.
- **awarded:** 2025-01-16; precision: day; basis: explicit. Timeline entry specifically identified as Bug \#2\.
- **fixed:** 2025-01-03; precision: day; basis: explicit. Timeline entry specifically identified as Bug \#2\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T09:50:24Z. Read the primary article and separately assigned reward timeline; reviewed official currency context and checked the existing report inventory for duplicate identity\.

- Researcher-reported award; neither vendor confirmation of this individual award nor payment settlement was established\.
- USD denomination uses official program context published five years before the award and is not an individual payment audit\.
- Original publication remains unknown; current archive dates must not inflate recency\.
- Only the backend configuration-to-script finding, labeled Bug \#2, is included\. The article also describes a different client-side finding with a separate award\.
- Configuration-write prerequisites, remediation implementation and broad deployment or employee-system consequences are not independently verified\.

## Sources and attribution

- [Multiple XSS in Meta Conversion API Gateway Leading to Zero-Click Account Takeover](<https://ysamm.com/uncategorized/2026/01/13/capig-xss.html>) — Youssef Sammouda; retrieved 2026-10-03T09:50:24Z.
- [Facebook Bug Bounty and BountyCon US-dollar reporting](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook; retrieved 2026-10-03T09:50:24Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
