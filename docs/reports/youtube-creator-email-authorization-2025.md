# YouTube creator metadata exposed private email addresses

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** YouTube Studio and Content ID APIs

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

A monetized-channel account could access another monetized creator’s private email through inconsistent cross-API authorization\. The researcher reports a USD 20,000 award\.

### Root cause

Ordinary sensitive-field checks appeared effective, but an alternate metadata path exposed a cross-service association\. The researcher then questioned whether monetized creator accounts inherited rights intended for specialist rights-management accounts\.

### Bounded impact

The demonstrated disclosure concerned the email stored when the target channel became monetized, which may differ from its current email\. Broader phishing consequences were potential impact, not demonstrated account compromise\.

### Defensive lessons

- Editorial lesson: check privacy guarantees across alternate response paths and linked services\.
- Editorial lesson: separate caller eligibility for an API from authority over each returned object\.

## Award and evidence

**USD 20,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. USD 13,337 initial award plus USD 6,663 adjustment for this same report; awarded date records the final adjustment\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/youtube-creator-email-authorization-2025.json>).

## Dates

- **published:** 2025-03-13; precision: day; basis: explicit
- **public disclosure:** 2025-03-13; precision: day; basis: explicit
- **reported:** 2024-12-12; precision: day; basis: explicit
- **awarded:** 2025-01-23; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Vendor confirmed the issue fixed on February 21, 2025; actual deployment date is not established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T05:09:57Z. Fresh read of the primary researcher article through web text extraction; compared prerequisites, authorization boundary, demonstrated impact and remediation chronology with the existing record\. No target testing or exploit reproduction\.

- Award is reported by the cited source; cash settlement is not independently audited\.
- The article does not supply implementation-level patch details or establish actual deployment timing\.

## Sources and attribution

- [Disclosing YouTube Creator Emails for a $20k Bounty](<https://brutecat.com/articles/youtube-creator-emails/>) — Arvin Shivram \(Brutecat\); retrieved 2026-10-03T05:09:57Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
