# GitHub comparison output lacked source-repository authorization

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** GitHub  
**Product:** GitHub Enterprise Server

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

A cross-repository access-control report received a vendor-confirmed USD 10,000 award\.

### Root cause

A comparison feature did not consistently authorize access to both source repositories\.

### Bounded impact

Limited private code content could cross repository permission boundaries\.

### Defensive lessons

- Authorize every source object before producing a combined or derived view\.
- Keep comparison output subject to the access rules of all contributing repositories\.

## Award and evidence

**USD 10,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. One report award; HackerOne policy supplies USD context\. Payment receipt is unverified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/github-cross-repository-comparison-authorization-2025.json>).

## Dates

- **published:** 2025-09-23; precision: day; basis: explicit. Detailed report disclosure event, activity-37054322\.
- **public disclosure:** 2025-08-25; precision: day; basis: explicit. Vendor advisory in Enterprise Server 3\.17\.5 release notes preceded the detailed report\.
- **reported:** 2025-05-03; precision: day; basis: explicit
- **awarded:** 2025-08-26; precision: day; basis: explicit
- **fixed:** 2025-08-25; precision: day; basis: explicit. Public GHES 3\.17\.5 release\. Report Resolved status is August 26; GitHub\.com deployment timing is not established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T16:32:49Z. Read rendered public HackerOne vendor summary and award/disclosure events; independently read vendor release notes\.

- The public vendor summary does not supply implementation-level patch detail\.
- Cash receipt is unverified\. USD notation uses platform policy context\.
- Release availability, report resolution and detailed publication have different dates\.

## Sources and attribution

- [GitHub HackerOne report 3124517](<https://hackerone.com/reports/3124517>) — GitHub security team and furbreeze; retrieved 2026-10-02T16:31:00Z.
- [GitHub Enterprise Server 3\.17\.5 release notes](<https://docs.github.com/en/enterprise-server@3.17/admin/release-notes#3.17.5>) — GitHub; retrieved 2026-10-02T16:32:49Z.
- [Vulnerability Disclosure Standards: Bug Bounty payment denomination](<https://www.hackerone.com/terms/disclosure-guidelines>) — HackerOne; retrieved 2026-10-02T15:43:47Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
