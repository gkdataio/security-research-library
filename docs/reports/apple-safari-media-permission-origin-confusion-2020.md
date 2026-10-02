# Safari origin confusion undermined stored media permissions

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Apple  
**Product:** Safari media permissions

## What the evidence establishes

Publication window: uncertain original publication date; reviewed as of 2026-10-02.

The cited researcher documents a USD 75,000 award for this reported chain\.

### Root cause

URL parsing, origin identity, and secure-context decisions were inconsistent with the identity used for stored permissions\. Defensive design should use one coherent origin model across permission enforcement\.

### Bounded impact

Unauthorized camera and microphone access under previously granted website permissions\.

### Defensive lessons

- Use one coherent origin model for permission enforcement\.
- Invalidate persistent consent when the underlying resource or trust context materially changes\.

## Award and evidence

**USD 75,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. One award for the reported vulnerability chain, not this amount per CVE\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/apple-safari-media-permission-origin-confusion-2020.json>).

## Dates

- **published:** Unknown; precision: unknown; basis: not\_reported. The primary researcher page does not supply a publication date; no exact date is inferred\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** 2020-01-28; precision: day; basis: explicit. Safari 13\.0\.5 vendor release date; the advisory entry was added February 6\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T14:43:00Z. Primary public sources read; individual reward, dates, and attribution reviewed\. No target testing performed\.

- One reported chain, not a $75,000 award for each CVE
- Broader project found seven bugs; source attributes this award to the camera exploit
- The researcher's page has no explicit publication date
- Publication date is unknown in the primary source, so recency is explicitly uncertain\.

## Sources and attribution

- [Safari origin confusion undermined stored media permissions](<https://www.ryanpickren.com/webcam-hacking-overview>) — Ryan Pickren; retrieved 2026-10-02T14:43:00Z.
- [Apple security release advisory](<https://support.apple.com/en-sa/103780>) — Apple; retrieved 2026-10-02T14:43:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
