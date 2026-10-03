# PostgreSQL cryptographic parsing omitted a buffer-capacity check

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** PostgreSQL  
**Product:** PostgreSQL pgcrypto extension

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

The organizer awarded Team Xint Code USD 30,000 for this individually identified ZeroDay\.cloud 2025 competition entry\.

### Root cause

Cryptographic message parsing copied a derived key length into a fixed-capacity destination without verifying that the destination was large enough\.

### Bounded impact

The PostgreSQL advisory confirms possible code execution under the database operating-system account\. The vendor CVE record limits the prerequisite to permission to install the extension or supply ciphertext to an existing installation\.

### Defensive lessons

- Validate derived lengths against destination capacity before copying data\.
- Review extension permissions and least-privilege database process identities\.
- Use vendor release evidence to verify remediation rather than replaying an exploit\.

## Award and evidence

**USD 30,000** — competition\_award; single\_competition\_entry; status: awarded.

Evidence level: organizer\_confirmed. One entry award, excluding the team’s other database entries\. The results use $; USD denomination is contextualized by the organizer’s current rules, which concern 2026 rather than an archived 2025 rules snapshot\. No conversion or cash-settlement claim is made\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/postgresql-pgcrypto-buffer-capacity-validation-2026.json>).

## Dates

- **published:** 2026-05-04; precision: day; basis: inferred. Displayed May 4; year inferred from the completed 2026 remediation timeline\.
- **public disclosure:** 2025-12-10; precision: day; basis: explicit. Public competition demonstration\. Subsequent CVE/advisory publication and full technical article are separate events\.
- **reported:** Unknown; precision: unknown; basis: not\_reported. The researcher identifies the December 10–11 event; no exact initial vendor-report date is stated\. The tracker dates the public entry December 10\.
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** 2026-02-12; precision: day; basis: explicit. Vendor patch release, not proof of deployment by every customer\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2025-12-16; precision: day; basis: explicit. Dated organizer recap announces the exact entry award; decision and transfer dates remain unknown\.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T18:12:00Z. Read the named researcher report, organizer CVE tracker and per-entry award result; cross-checked vendor advisories and CNA records\. Currency context is explicitly distinguished from award evidence\. No vulnerability testing performed\.

- The event demonstration is distinct from the February 12, 2026 vendor advisory and May research article\.
- The source identifies Team Xint Code; no allocation to named individual recipients is established\.
- The article shows May 4 without a year; 2026 is inferred from its explicitly dated remediation timeline\.
- Exact award decision and funds-transfer dates are not reported; December 16 is the dated organizer announcement\.
- Current rules establish program US-dollar notation but are not an archived snapshot of the 2025 rules\.

## Sources and attribution

- [CVE-2026-2005: PostgreSQL pgcrypto heap buffer overflow leading to RCE](<https://www.zeroday.cloud/blog/postgres-xint>) — Team Xint Code / ZeroDay\.cloud; retrieved 2026-10-02T18:12:00Z.
- [ZeroDay\.cloud 2025 individual competition results](<https://www.wiz.io/blog/wiz-zeroday-cloud-hacking-competition-behind-the-scenes>) — Nir Ohfeld / Wiz Research; retrieved 2026-10-02T18:12:00Z.
- [ZeroDay\.cloud vulnerability tracker](<https://www.zeroday.cloud/vulnerability-tracker>) — Wiz / ZeroDay\.cloud; retrieved 2026-10-02T18:12:00Z.
- [ZeroDay\.cloud current rules: US-dollar denomination](<https://www.zeroday.cloud/rules>) — Wiz; retrieved 2026-10-02T18:12:00Z.
- [PostgreSQL CVE-2026-2005 security advisory](<https://www.postgresql.org/support/security/CVE-2026-2005/>) — PostgreSQL; retrieved 2026-10-02T18:12:00Z.
- [CVE-2026-2005 CNA record](<https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/2xxx/CVE-2026-2005.json>) — PostgreSQL CNA / CVE Program; retrieved 2026-10-02T18:12:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
