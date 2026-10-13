# iCloud sharing consent and Safari trust boundaries failed together

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

[Read the original source](<https://www.ryanpickren.com/safari-uxss>) — Ryan Pickren · [Canonical JSON](<../../data/reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.json>)

<a id="what-the-evidence-establishes"></a>
## Main takeaway

Permission to open shared iCloud content could remain valid after that content changed, and Safari did not consistently keep website permissions separate\. Ryan Pickren reports a USD 100,500 award for the combined findings, rather than a separate award for each bug\.

**Organization:** Apple  
**Product:** iCloud Sharing and Safari

<a id="root-cause"></a>
## What went wrong

Consent to open shared content remained effective after material content changes, and cross-application trust handling failed to preserve browser isolation\. Review whether persisted consent remains valid as shared resources evolve\.

<a id="bounded-impact"></a>
## What the evidence shows

The researcher reports access across website security contexts and media permissions; additional research covered local-file exposure\.

## Defensive lessons

- Use one coherent origin model for permission enforcement\.
- Invalidate persistent consent when the underlying resource or trust context materially changes\.

## Award and evidence

**USD 100,500** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. One award for the reported vulnerability chain, not this amount per CVE\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.json>).

## Dates

Publication window: uncertain original publication date; reviewed as of 2026-10-03.

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
