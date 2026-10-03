# YouTube and Pixel Recorder exposed cross-product identity links

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** YouTube and Pixel Recorder

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

One cross-product privacy report received USD 3,133 and a USD 7,500 adjustment, totaling USD 10,633\.

### Root cause

Cross-product identifier exposure and insufficient field-level privacy controls weakened account pseudonymity\.

### Bounded impact

Researchers reported that private email addresses associated with YouTube users could be revealed\. No mass breach is established\.

### Defensive lessons

- Treat cross-product identifiers as sensitive correlation data\.
- Require entitlement before returning identity attributes\.
- Verify remediation across every affected component\.

## Award and evidence

**USD 10,633** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. One report: December 3 entry explicitly says it returned for additional reward consideration\. Headline rounds to $10,000\. Exact arithmetic is $10,633\. USD uses Google web VRP denomination documented by google-usd-context\. Awarded, not confirmed paid\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/youtube-pixel-recorder-identity-privacy-2025.json>).

## Dates

- **published:** 2025-02-12; precision: day; basis: explicit
- **public disclosure:** 2025-02-12; precision: day; basis: explicit
- **reported:** 2024-09-15; precision: day; basis: explicit
- **awarded:** 2024-12-12; precision: day; basis: explicit. Final additional award; initial award was November 5, 2024\.
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Researcher confirmed both components fixed on February 9, 2025; actual deployment date is not supplied\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T15:14:47Z. Primary source reviewed; individual award and attribution checked\. Historical defensive summary only\. Official 2024 program announcement was read in the cloud browser for USD denomination only; its advertised maximum is not award evidence\.

- Award evidence is not an independently audited cash receipt\.
- The source uses dollar notation, with USD established from Google program context\.
- No public report ID, recipient split, or exact fix-deployment date is provided\.
- Separate from the March 2025 creator-metadata report and its USD 20,000 award\.

## Sources and attribution

- [Leaking the email of any YouTube user for $10,000](<https://brutecat.com/articles/leaking-youtube-emails/>) — Arvin Shivram and Nathan; retrieved 2026-10-02T15:12:00Z.
- [Google and Alphabet VRP reward-denomination announcement, July 11, 2024](<https://bughunters.google.com/blog/increasing-google-alphabet-vrp-rewards-up-to-151515>) — Sam Erb and Krzysztof Kotowicz / Google; retrieved 2026-10-02T15:14:47Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
