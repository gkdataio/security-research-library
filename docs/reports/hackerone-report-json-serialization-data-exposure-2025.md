# Framework serialization change exposed private HackerOne user attributes

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** HackerOne  
**Product:** HackerOne report serialization

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

A framework upgrade exposed private contributor attributes in public report responses\. The vendor confirmed a USD 25,000 award; the public report supplies the underlying serialization and test-normalization explanation\.

### Root cause

The vendor explains that an internal user object and a sanitized public representation shared a field name under different Ruby key types\. Earlier serialization retained only the sanitized representation; the upgrade emitted both\. Snapshot tests reparsed the response and discarded the earlier duplicate field, concealing sensitive data present in the raw response\. The affected context was a disclosed report with a reporter or team-member summary\. This was an application output-boundary failure exposed by a framework behavior change, not an AI-agent defect\.

### Bounded impact

The vendor reproduced private-attribute exposure\. The public report describes personal and security-sensitive account attributes, but does not demonstrate account takeover or establish an affected-user count or wider exploitation\. The vendor announced a deployed fix on February 21, 2025; the researcher retested and observed only intended public attributes for team and reporter summaries\. The exact code change is not disclosed\.

### Defensive lessons

- Editorial lesson: construct public responses from explicit safe fields rather than relying on later serialization to overwrite an internal object\.
- Editorial lesson: test both raw serialized output and parsed structure; normalization can hide duplicate fields and sensitive data\.
- Editorial lesson: treat framework upgrades as changes to security-relevant output semantics, and exercise nested representations with private-field exclusion assertions\.

## Award and evidence

**USD 25,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. Vendor confirms the individual report’s reward; the public report records the award event on February 21, 2025, while settlement remains unreported\. The award article uses a dollar sign; current official HackerOne standards supply USD context only\. Exhibit C reproduces guideline version 1\.2 dated July 29, 2019 and specifies USD on printed page 12, supplying historical platform context rather than individual payment proof\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/hackerone-report-json-serialization-data-exposure-2025.json>).

## Dates

- **published:** 2025-04-01; precision: day; basis: explicit. Public technical report disclosure date; the later vendor case study was published June 24, 2025\.
- **public disclosure:** 2025-04-01; precision: day; basis: explicit
- **reported:** 2025-02-19; precision: day; basis: explicit
- **awarded:** 2025-02-21; precision: day; basis: explicit. Public timeline records the bounty event; the vendor case study establishes its USD 25,000 amount\. Separate retest compensation is not included\.
- **fixed:** 2025-02-21; precision: day; basis: explicit. Vendor deployment confirmation and successful researcher retest appear on this day; exact deployment time is not established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T08:59:00Z. Freshly read the vendor case study and the public technical report in the cloud browser, including vendor root-cause explanation and timeline\. No target testing\. Existing denomination sources retained without a fresh review\.

- Award evidence does not establish settlement; the USD 25,000 amount comes from the case study, while the report hides the bounty amount\.
- The technical report names the earlier Rails version as 6\.1\.7\.9; the later case study says 6\.1\.7\.10\. Both identify the upgrade to 7\.1\.5\.1; the discrepancy is unresolved\.
- The case study describes retest validation within an hour, but visible retest-request and completion timestamps are about 72 minutes apart\. Edited timeline timestamps and deployment timing limit precise duration comparisons\.
- The public sources do not establish exact authentication prerequisites, affected-user count, a code-level patch, or successful account compromise\.
- Currency context includes currently reviewed standards dated July 27, 2026 and historical platform guidelines; neither independently proves individual settlement\.

## Related conceptual diagrams

- [Server disclosure and browser interpretation](<../diagram-gallery.md#server-client-data-consumer-boundaries>)

## Sources and attribution

- [We’re Running Hai Insight Agent on Our Own Bug Bounty Program – See it in Action](<https://www.hackerone.com/blog/hai-insight-agent-case-study>) — Crystal Hazen / HackerOne; retrieved 2026-10-03T08:59:00Z.
- [Vulnerability Disclosure Standards](<https://www.hackerone.com/terms/disclosure-guidelines>) — HackerOne; retrieved 2026-10-02T23:03:50Z.
- [HackerOne terms and disclosure guidelines in official reseller GSA contract attachment, Exhibit C](<https://www.carahsoft.com/buy/gsa-schedule-contracts/approved-csas/docFileDownload/286450/24c3653f-9d13-4944-8f2e-5baa23efa63c>) — HackerOne / Carahsoft \(contract attachment\); retrieved 2026-10-02T23:05:44Z.
- [Public report 3000510: private user attributes exposed in report serialization](<https://hackerone.com/reports/3000510>) — HackerOne and avinash\_; retrieved 2026-10-03T08:59:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
