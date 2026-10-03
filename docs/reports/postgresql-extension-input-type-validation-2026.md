# PostgreSQL extension estimator trusted an unchecked input type

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** PostgreSQL  
**Product:** PostgreSQL intarray extension

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

Wiz confirms a USD 30,000 competition award for Daniel Firer’s PostgreSQL entry, uniquely mapped by the organizer to CVE-2026-2004\.

### Root cause

The extension’s selectivity estimator accepted input without checking that its type matched the routine’s expectations\. This broke the contract between database objects an authorized user could create and native extension code running with database-process authority\.

### Bounded impact

The vendor confirms possible code execution as the database operating-system account\. A user needed permission to install the vulnerable extension, or an existing installation plus object-creation permission\. The public sources do not establish a universal unauthenticated or cross-tenant compromise\.

### Defensive lessons

- Validate input types at extension boundaries before applying native-code assumptions\.
- Review extension installation and object-creation privileges together; either permission in isolation can hide the relevant trust boundary\.
- Verify the vendor’s fixed releases and keep the database process identity limited to necessary resources\.

## Award and evidence

**USD 30,000** — competition\_award; single\_competition\_entry; status: awarded.

Evidence level: organizer\_confirmed. One individually identified competition entry\. The organizer uses $; its current rules establish US-dollar notation but concern 2026, not an archived 2025 rules snapshot\. Exact award decision and cash settlement are unknown\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/postgresql-extension-input-type-validation-2026.json>).

## Dates

- **published:** 2026-02-12; precision: day; basis: explicit. Publication of the vendor CNA record; no separate detailed researcher article was established\.
- **public disclosure:** 2025-12-10; precision: day; basis: explicit. Public competition demonstration; separate from later vendor advisory and technical publication\.
- **reported:** Unknown; precision: unknown; basis: not\_reported. Exact initial report to the vendor is not stated; the tracker dates the competition entry, not vendor receipt\.
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** 2026-02-12; precision: day; basis: explicit. Vendor release date for PostgreSQL 18\.2, 17\.8, 16\.12, 15\.16 and 14\.21; individual deployment dates remain unknown\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2025-12-16; precision: day; basis: explicit. Organizer recap confirms the per-entry award; decision and payment dates remain unknown\.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T19:21:00Z. Matched the organizer’s named PostgreSQL award to the tracker’s exact CVE, then checked the vendor advisory and CNA prerequisites\. Summary remains within the published technical evidence\.

- The technical basis is the vendor advisory, not a detailed researcher walkthrough; discovery reasoning beyond that evidence is unknown\.
- The December competition demonstration, February advisory publication, award announcement and unknown payment date are distinct events\.
- Current rules provide explicit USD context but are not the archived 2025 rules\.

## Sources and attribution

- [ZeroDay\.cloud 2025 individual competition results](<https://www.wiz.io/blog/wiz-zeroday-cloud-hacking-competition-behind-the-scenes>) — Nir Ohfeld / Wiz Research; retrieved 2026-10-02T19:21:00Z.
- [ZeroDay\.cloud vulnerability tracker](<https://www.zeroday.cloud/vulnerability-tracker>) — Wiz / ZeroDay\.cloud; retrieved 2026-10-02T19:21:00Z.
- [ZeroDay\.cloud current rules: US-dollar denomination](<https://www.zeroday.cloud/rules>) — Wiz; retrieved 2026-10-02T19:21:00Z.
- [PostgreSQL CVE-2026-2004 security advisory](<https://www.postgresql.org/support/security/CVE-2026-2004/>) — PostgreSQL; retrieved 2026-10-02T19:21:00Z.
- [CVE-2026-2004 PostgreSQL CNA record](<https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/2xxx/CVE-2026-2004.json>) — PostgreSQL CNA / CVE Program; retrieved 2026-10-02T19:21:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
