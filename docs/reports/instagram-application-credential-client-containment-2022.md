# Instagram client configuration exposed an application credential

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Meta  
**Product:** Instagram server-driven client interface

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

Meta confirmed a $30,000 base award for an Instagram application-token exposure; additional researcher-listed bonuses are excluded from the recorded amount\.

### Root cause

Server-delivered interface configuration exposed an application credential to a client\. The researcher distinguished application-level authority from ordinary client-token authority, identifying a mismatch between the data needed for rendering and the privilege carried by an embedded credential\.

### Bounded impact

The researcher reports retrieving application-role metadata\. Meta confirms credential exposure but says independent protections limited further impact and it found no evidence of abuse\. Unrestricted administration, account takeover and actual customer compromise were not established\.

### Defensive lessons

- Classify every credential by its authority and intended holder before deciding whether it belongs in client-visible data\.
- Keep privileged application credentials inside controlled server contexts; minimize the capabilities available to client integrations\.
- Preserve independent authorization checks after credential validation, and distinguish the demonstrated exposure from hypothetical downstream consequences\.
- Treat containment and least-privilege recommendations as design guidance; the sources do not document the complete vendor patch\.

## Award and evidence

**USD 30,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. Records the vendor-confirmed base once\. The researcher separately lists $6,000 league, $2,250 delay and $50 event bonuses; these are not added to this amount or counted as separate findings\. USD uses earlier official program denomination context; settlement is unknown\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/instagram-application-credential-client-containment-2022.json>).

## Dates

- **published:** 2022-07-20; precision: day; basis: explicit. Dated vendor publication is used\. The researcher page presents February 24, 2022 and August 27, 2024 without a clearly extracted original-versus-update label; its original public release remains uncertain\.
- **public disclosure:** 2022-07-20; precision: day; basis: explicit. Vendor discussion and direct researcher link establish public availability by this date, not the earliest possible disclosure\.
- **reported:** 2022-02-24; precision: day; basis: explicit
- **awarded:** 2022-05-19; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported. The researcher records fix confirmation on February 24, 2022 and removal within hours\. The exact deployment date is not independently established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2022-07-20; precision: day; basis: explicit. Public vendor confirmation; an earlier researcher announcement is possible\.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T20:20:00Z. Matched Meta’s named researcher and report-specific award to its directly linked technical article\. Separated credential exposure, observed metadata access and vendor-stated containment\.

- The vendor confirms the base; bonus breakdown and report/award timeline are researcher-reported\.
- Original researcher publication and exact fix deployment are uncertain; the vendor bulletin supplies the publication date used here\.
- The currency reference is older program context, not a report-specific settlement record\.
- No full patch implementation or unrestricted downstream compromise is established\.

## Sources and attribution

- [How Meta and the security industry collaborate to secure the internet](<https://engineering.fb.com/2022/07/20/security/how-meta-and-the-security-industry-collaborate-to-secure-the-internet/>) — Meta Engineering; retrieved 2026-10-02T20:20:00Z.
- [Instagram App Access Token](<https://philippeharewood.com/instagram-app-access-token/>) — Philippe Harewood; retrieved 2026-10-02T20:20:00Z.
- [Facebook Bug Bounty and BountyCon US-dollar reporting](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook; retrieved 2026-10-02T20:20:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
