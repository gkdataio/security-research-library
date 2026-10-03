# GraphQL object authorization exposed private-program metadata

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** HackerOne  
**Product:** HackerOne GraphQL object access

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

HackerOne awarded USD 25,000 for one private-program object-authorization report\.

### Root cause

GraphQL object access did not consistently enforce private-program visibility rules\.

### Bounded impact

Private-program metadata and report titles could be disclosed without authorization\. HackerOne stated its investigation found no exploitation beyond the researcher’s demonstration\.

### Defensive lessons

- Apply authorization to every object and relationship boundary\.
- Treat metadata fields as part of the privacy contract\.

## Award and evidence

**USD 25,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. Dollar notation appears in the report UI; USD denomination is contextual from HackerOne’s disclosure policy\. Award events do not establish cash receipt\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/hackerone-private-program-graphql-object-authorization-2025.json>).

## Dates

- **published:** 2025-01-21; precision: day; basis: explicit
- **public disclosure:** 2025-01-21; precision: day; basis: explicit
- **reported:** 2022-06-28; precision: day; basis: explicit
- **awarded:** 2022-07-05; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Report status changed to Resolved on July 5, 2022; exact deployment time is not stated\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T15:45:00Z. Original public HackerOne report, vendor statements and expanded award timeline read in the cloud browser\. Currency policy read separately\.

- Award events establish an award, not independently audited settlement\.
- Exact fix-deployment date is unavailable; a Resolved status date is not treated as deployment\.
- Implementation-level patch details are not public\. Updated comment timestamps are distinct from original event dates\.

## Sources and attribution

- [GraphQL object authorization exposed private-program metadata \(report 1618347\)](<https://hackerone.com/reports/1618347>) — HackerOne and the credited researchers; retrieved 2026-10-02T15:45:00Z.
- [Vulnerability Disclosure Standards: Bug Bounty payment denomination](<https://www.hackerone.com/terms/disclosure-guidelines>) — HackerOne; retrieved 2026-10-02T15:43:47Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
