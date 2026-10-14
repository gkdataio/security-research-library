# GitHub comparison output lacked source-repository authorization

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

[Read the original source](<https://hackerone.com/reports/3124517>) — GitHub security team and furbreeze · [Canonical JSON](<../../data/reports/github-cross-repository-comparison-authorization-2025.json>)

<a id="what-the-evidence-establishes"></a>
## Main takeaway

GitHub Enterprise Server's comparison feature could reveal limited code from a repository the user was not allowed to read\. The user needed existing repository access and prior knowledge of private-repository references; the report does not establish unrestricted repository access\. GitHub awarded USD 10,000 for the finding\.

**Organization:** GitHub  
**Product:** GitHub Enterprise Server

<a id="root-cause"></a>
## What went wrong

GitHub identifies an access-control failure in cross-repository comparison \(vendor-report; vendor-release\)\. Permission to read one repository did not grant permission to see code from another repository in the comparison\. The user needed existing repository access and prior knowledge of private-repository references; this was not unrestricted anonymous browsing\. The general lesson is to check access to every source used in a combined view\. The vendor does not disclose how the access checks were implemented\.

<a id="bounded-impact"></a>
## What the evidence shows

The vendor confirms limited code disclosure from an otherwise unauthorized repository \(vendor-report; vendor-release\)\. The public summary does not establish complete repository extraction, write access, account takeover, or exploitation in the wild; those outcomes must not be inferred from the broader report title\.

## Defensive lessons

- Editorial design lesson: authorize every contributing source under the requesting actor before returning a combined or derived view\.
- Editorial review objective: ensure that permission to access one repository never substitutes for permission to read another repository’s content\.
- GitHub lists historical fixes in GHES 3\.14\.17, 3\.15\.12, 3\.16\.8 and 3\.17\.5 \(vendor-report\)\. These are historical remediation evidence, not current upgrade recommendations; the 3\.17 documentation now marks that release series unsupported \(vendor-release\)\.

## Award and evidence

**USD 10,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. One report award; cash receipt is unverified\. USD is inferred from HackerOne’s platform-wide payment policy reviewed in October 2026, later than the August 2025 award; that context does not independently establish settlement\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/github-cross-repository-comparison-authorization-2025.json>).

## Dates

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

- **published:** 2025-09-23; precision: day; basis: explicit. Detailed report disclosure event, activity-37054322\.
- **public disclosure:** 2025-08-25; precision: day; basis: explicit. Vendor advisory in Enterprise Server 3\.17\.5 release notes preceded the detailed report\.
- **reported:** 2025-05-03; precision: day; basis: explicit
- **awarded:** 2025-08-26; precision: day; basis: explicit
- **fixed:** 2025-08-25; precision: day; basis: explicit. Public GHES 3\.17\.5 release\. Report Resolved status is August 26; GitHub\.com deployment timing is not established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T05:30:46Z. Freshly read public GitHub summary and award/disclosure events in the cloud browser, plus GitHub release notes and HackerOne currency policy through web retrieval\. Added bounded conceptual analysis without reproduction or testing\.

- Public report content supplies a vendor summary, not implementation-level patch details or a complete demonstration transcript\.
- GitHub\.com deployment timing and exploitation-in-the-wild status are not established by the reviewed sources\.
- Release availability, report resolution and detailed publication have different dates\.
- Cash receipt is unverified; later platform-wide USD policy is contextual denomination evidence\.

## Related conceptual diagrams

- [Combined views preserve every source's access boundary](<../diagram-gallery.md#combined-view-source-authorization>)

## Sources and attribution

- [GitHub HackerOne report 3124517](<https://hackerone.com/reports/3124517>) — GitHub security team and furbreeze; retrieved 2026-10-03T05:30:46Z.
- [GitHub Enterprise Server 3\.17\.5 release notes](<https://docs.github.com/en/enterprise-server@3.17/admin/release-notes#3.17.5>) — GitHub; retrieved 2026-10-03T05:30:46Z.
- [Vulnerability Disclosure Standards: Bug Bounty payment denomination](<https://www.hackerone.com/terms/disclosure-guidelines>) — HackerOne; retrieved 2026-10-03T05:30:46Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
