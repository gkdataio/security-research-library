# Framework serialization change exposed private HackerOne user attributes

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** HackerOne  
**Product:** HackerOne report serialization

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

A Rails upgrade changed how public report responses serialized private user attributes\. HackerOne confirmed the disclosure and a USD 25,000 award\.

### Root cause

The public-output boundary failed when serialization behavior changed\. The affected context was a disclosed report containing a reporter or team-member summary; public report visibility did not imply permission to expose its contributor’s private attributes\.

### Bounded impact

The vendor confirms sensitive-attribute exposure and describes cross-program linking risk, but gives no affected-user count or evidence of wider exploitation\. It reports a deployed fix and successful researcher retest; implementation details are absent\.

### Defensive lessons

- Editorial lesson: define an explicit public-response field allowlist independently of framework defaults\.
- Editorial lesson: make dependency-upgrade tests assert that private attributes remain absent across nested serializers\.
- Editorial lesson: distinguish confirmation of one corrected response from proof that every historical response path is safe\.

## Award and evidence

**USD 25,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. Vendor confirms the individual report’s reward; exact award and payment dates are not supplied\. The award article uses a dollar sign; current official HackerOne standards supply USD context only\. Exhibit C reproduces guideline version 1\.2 dated July 29, 2019 and specifies USD on printed page 12, supplying historical platform context rather than individual payment proof\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/hackerone-report-json-serialization-data-exposure-2025.json>).

## Dates

- **published:** 2025-06-24; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T23:05:44Z. Reread the vendor case study; checked award, exposure context and remediation statements\. No target testing\.

- Publication does not establish discovery, award or settlement dates\.
- The article does not describe the researcher’s investigative reasoning or exact access prerequisites beyond the affected report context\.
- The linked technical report was not independently reread; researcher identity remains unverified\.
- Hai assisted triage; the reported defect was serialization\.
- Currency context comes from the currently reviewed platform standards, updated July 27, 2026, not a preserved 2025 version\.

## Sources and attribution

- [We’re Running Hai Insight Agent on Our Own Bug Bounty Program – See it in Action](<https://www.hackerone.com/blog/hai-insight-agent-case-study>) — Crystal Hazen / HackerOne; retrieved 2026-10-02T23:00:55Z.
- [Vulnerability Disclosure Standards](<https://www.hackerone.com/terms/disclosure-guidelines>) — HackerOne; retrieved 2026-10-02T23:03:50Z.
- [HackerOne terms and disclosure guidelines in official reseller GSA contract attachment, Exhibit C](<https://www.carahsoft.com/buy/gsa-schedule-contracts/approved-csas/docFileDownload/286450/24c3653f-9d13-4944-8f2e-5baa23efa63c>) — HackerOne / Carahsoft \(contract attachment\); retrieved 2026-10-02T23:05:44Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
