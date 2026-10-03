# MariaDB JSON normalization exceeded allocated buffer capacity

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** MariaDB  
**Product:** MariaDB Server JSON schema validation

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

The organizer awarded Team Xint Code USD 30,000 for this individually identified ZeroDay\.cloud 2025 competition entry\.

### Root cause

JSON normalization copied variable-length text into an undersized allocation\. The fix uses storage management that grows the buffer to fit the value\.

### Bounded impact

An authenticated database user could crash the server\. The researcher demonstrated code execution at the event; the vendor-authored CVE record qualifies that outcome as dependent on unusually controlled memory conditions, generally associated with a lab\.

### Defensive lessons

- Make input length and allocated capacity explicit invariants in normalization code\.
- Prefer capacity-aware storage operations and safe local regression coverage\.
- Separate a controlled demonstration from deployment-wide impact claims\.

## Award and evidence

**USD 30,000** — competition\_award; single\_competition\_entry; status: awarded.

Evidence level: organizer\_confirmed. One entry award, excluding the team’s other database entries\. The results use $; USD denomination is contextualized by the organizer’s current rules, which concern 2026 rather than an archived 2025 rules snapshot\. No conversion or cash-settlement claim is made\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/mariadb-json-normalization-buffer-capacity-2026.json>).

## Dates

- **published:** 2026-05-04; precision: day; basis: inferred. Displayed May 4; year inferred from the completed 2026 remediation timeline\.
- **public disclosure:** 2025-12-11; precision: day; basis: explicit. Public competition demonstration\. Subsequent CVE/advisory publication and full technical article are separate events\.
- **reported:** 2025-12-11; precision: day; basis: explicit. Researcher timeline explicitly dates the report and vendor acknowledgement\.
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** 2026-02-04; precision: day; basis: explicit. Vendor patch release, not proof of deployment by every customer\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2025-12-16; precision: day; basis: explicit. Dated organizer recap announces the exact entry award; decision and transfer dates remain unknown\.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T18:12:00Z. Read the named researcher report, organizer CVE tracker and per-entry award result; cross-checked vendor advisories and CNA records\. Currency context is explicitly distinguished from award evidence\. No vulnerability testing performed\.

- Vendor CVE wording conditions code execution on tight memory control generally obtainable in a lab; do not infer reliable production-wide compromise\.
- Vendor advisory also lists patched 12\.2\.2, beyond the two release series emphasized in the research article\. The February 4 fix date refers to the reviewed 11\.4\.10 release\.
- The article shows May 4 without a year; 2026 is inferred from its explicitly dated remediation timeline\.
- Exact award decision and funds-transfer dates are not reported; December 16 is the dated organizer announcement\.
- Current rules establish program US-dollar notation but are not an archived snapshot of the 2025 rules\.

## Sources and attribution

- [CVE-2026-32710: MariaDB JSON\_SCHEMA\_VALID heap buffer overflow leading to RCE](<https://www.zeroday.cloud/blog/mariadb-cve-2026-32710-deep-dive>) — Team Xint Code / ZeroDay\.cloud; retrieved 2026-10-02T18:12:00Z.
- [ZeroDay\.cloud 2025 individual competition results](<https://www.wiz.io/blog/wiz-zeroday-cloud-hacking-competition-behind-the-scenes>) — Nir Ohfeld / Wiz Research; retrieved 2026-10-02T18:12:00Z.
- [ZeroDay\.cloud vulnerability tracker](<https://www.zeroday.cloud/vulnerability-tracker>) — Wiz / ZeroDay\.cloud; retrieved 2026-10-02T18:12:00Z.
- [ZeroDay\.cloud current rules: US-dollar denomination](<https://www.zeroday.cloud/rules>) — Wiz; retrieved 2026-10-02T18:12:00Z.
- [MariaDB heap-based buffer overflow in JSON\_SCHEMA\_VALID](<https://github.com/MariaDB/server/security/advisories/GHSA-4rj5-2227-9wgc>) — MariaDB; retrieved 2026-10-02T18:12:00Z.
- [CVE-2026-32710 CNA record](<https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/32xxx/CVE-2026-32710.json>) — GitHub CNA, MariaDB advisory / CVE Program; retrieved 2026-10-02T18:12:00Z.
- [MariaDB 11\.4\.10 release notes](<https://mariadb.com/docs/release-notes/community-server/11.4/11.4.10>) — MariaDB; retrieved 2026-10-02T18:12:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
