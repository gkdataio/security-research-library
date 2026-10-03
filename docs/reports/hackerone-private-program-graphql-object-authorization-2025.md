# GraphQL object authorization exposed private-program metadata

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** HackerOne  
**Product:** HackerOne GraphQL object access

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

HackerOne awarded USD 25,000 in 2022 for private-program GraphQL metadata exposure; the report became public in January 2025 \(primary\)\.

### Root cause

A GraphQL object lookup failed to preserve private-program visibility for associated metadata \(primary\)\. The researcher described an unauthenticated request and triage validated the report\. Exposure depended on resolving a valid program-associated object; the public record does not establish equal reachability across every private-program type\. Conceptually, resolving an object is distinct from authorizing its disclosure\. The exact omitted check and code-level repair are not public\.

### Bounded impact

The researcher demonstrated private-program metadata exposure\. HackerOne’s internal investigation additionally determined that report titles could be accessed and raised severity to critical; title access was a vendor-assessed consequence, not the researcher’s demonstrated result in the visible evidence\. HackerOne said it found no exploitation beyond the demonstration \(primary\)\. Full report-body access is not established\.

### Defensive lessons

- Editorial design lesson: independently enforce visibility on object lookup, returned fields and related objects, including unauthenticated access paths\.
- Editorial privacy lesson: program metadata and report titles can disclose confidential information even when report bodies remain protected\.
- HackerOne marked the report Resolved on July 5, 2022 \(primary\)\. Treat that as resolution evidence; the deployment date and implementation-level remediation remain unknown\.

## Award and evidence

**USD 25,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. One report award, not verified cash receipt\. USD is contextual from HackerOne’s platform-wide payment policy reviewed in October 2026, more than four years after the July 2022 award; it does not independently establish that payment’s denomination or settlement\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/hackerone-private-program-graphql-object-authorization-2025.json>).

## Dates

- **published:** 2025-01-21; precision: day; basis: explicit. Public disclosure event activity-32092519; the underlying report and award are from 2022\.
- **public disclosure:** 2025-01-21; precision: day; basis: explicit
- **reported:** 2022-06-28; precision: day; basis: explicit
- **awarded:** 2022-07-05; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Report status changed to Resolved on July 5, 2022; exact deployment time is not stated\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T05:30:46Z. Freshly read the rendered public report, researcher demonstration, vendor triage/investigation statements and award/disclosure events in the cloud browser; independently read platform currency policy\. Omitted payloads and private-program details\.

- Award events establish an award, not independently audited settlement; later platform-wide currency policy is contextual evidence\.
- Exact fix-deployment date is unavailable; Resolved status is not treated as deployment\.
- Code-level patch details are not public\. Vendor investigation supports possible report-title access; the visible researcher evidence demonstrates metadata exposure\.
- The researcher expressed uncertainty about coverage of fully private programs\. The record does not generalize exposure to every private-program category\.
- Updated comment timestamps differ from original event dates\.

## Sources and attribution

- [GraphQL object authorization exposed private-program metadata \(report 1618347\)](<https://hackerone.com/reports/1618347>) — HackerOne and the credited researchers; retrieved 2026-10-03T05:30:46Z.
- [Vulnerability Disclosure Standards: Bug Bounty payment denomination](<https://www.hackerone.com/terms/disclosure-guidelines>) — HackerOne; retrieved 2026-10-03T05:30:46Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
