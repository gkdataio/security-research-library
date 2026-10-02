# iCloud sharing consent and Safari trust boundaries failed together

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Apple  
**Product:** iCloud Sharing and Safari

## What the evidence establishes

Publication window: uncertain original publication date; reviewed as of 2026-10-02.

The cited researcher documents a USD 100,500 award for this reported chain\.

### Root cause

Consent to open shared content remained effective after material content changes, and cross-application trust handling failed to preserve browser isolation\. Review whether persisted consent remains valid as shared resources evolve\.

### Bounded impact

The researcher reports access across website security contexts and media permissions; additional research covered local-file exposure\.

### Defensive lessons

- Use one coherent origin model for permission enforcement\.
- Invalidate persistent consent when the underlying resource or trust context materially changes\.

## Award and evidence

**USD 100,500** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. One award for the reported vulnerability chain, not this amount per CVE\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.json>).

## Dates

- **published:** Unknown; precision: unknown; basis: not\_reported. The primary researcher page does not supply a publication date; no exact date is inferred\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** 2021-07; precision: month; basis: explicit
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T14:43:00Z. Primary public sources read; individual reward, dates, and attribution reviewed\. No target testing performed\.

- One award for a reported chain; not a separate award per CVE
- Broader research included four bugs, only two used for the camera demonstration
- Complete remediation and payment dates are not stated; page says all issues patched by early 2022
- Publication date is unknown in the primary source, so recency is explicitly uncertain\.

## Sources and attribution

- [iCloud sharing consent and Safari trust boundaries failed together](<https://www.ryanpickren.com/safari-uxss>) — Ryan Pickren; retrieved 2026-10-02T14:43:00Z.
- [Apple security release advisory](<https://support.apple.com/en-us/103237>) — Apple; retrieved 2026-10-02T14:43:00Z.
- [Apple security release advisory](<https://support.apple.com/en-us/103236>) — Apple; retrieved 2026-10-02T14:43:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
