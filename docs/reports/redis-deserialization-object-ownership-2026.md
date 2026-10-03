# Redis deserialization cleanup violated object-ownership invariants

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Redis  
**Product:** Redis serialized-object loading

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

Wiz confirms USD 30,000 for Emil Lerner’s Redis competition entry\. Two related disclosed defects remain one awarded entry\.

### Root cause

The researcher traced object ownership through deserialization and failure cleanup\. Validation and conversion interpreted legacy data differently, while another cleanup path released an object still owned elsewhere\. Both defects violated the invariant that each allocation is released exactly once; accepting a data-import request did not make its contents trustworthy\.

### Bounded impact

The researcher demonstrated code execution in the competition\. The vendor confirms possible execution under Redis-process authority for an authenticated user with import permission\. Host or tenant reach depends on deployment privileges and isolation; it is not established for every Redis installation\.

### Defensive lessons

- Make ownership transfer and cleanup responsibility explicit on success and failure paths\.
- Require validators and converters to interpret the same serialized representation consistently\.
- Follow vendor patch guidance; restrict unnecessary import permissions using access controls while remediation is assessed\.

## Award and evidence

**USD 30,000** — competition\_award; single\_competition\_entry; status: awarded.

Evidence level: organizer\_confirmed. One individually identified competition entry\. The organizer uses $; its current rules establish US-dollar notation but concern 2026, not an archived 2025 rules snapshot\. Exact award decision and cash settlement are unknown\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/redis-deserialization-object-ownership-2026.json>).

## Dates

- **published:** 2026-06-02; precision: day; basis: inferred. The article displays June 2; 2026 is inferred from its completed May 5, 2026 remediation timeline\.
- **public disclosure:** 2025-12-10; precision: day; basis: explicit. Public competition demonstration; separate from later vendor advisory and technical publication\.
- **reported:** Unknown; precision: unknown; basis: not\_reported. Exact initial report to the vendor is not stated; the tracker dates the competition entry, not vendor receipt\.
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** 2026-05-05; precision: day; basis: explicit. Official Redis 8\.6\.3 release names the CVE\. Researcher also identifies fixed versions in four other maintained series\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2025-12-16; precision: day; basis: explicit. Organizer recap confirms the per-entry award; decision and payment dates remain unknown\.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T19:21:00Z. Matched the individual award, exact CVE tracker row, named researcher explanation and vendor advisory\. Checked release metadata for the fix date and kept two defects inside the single awarded entry\.

- The vendor advisory also credits Joseph Surin; the reviewed award names Emil Lerner only, so no reward allocation to the additional credited researcher is inferred\.
- The advisory’s patched-version field still says TBD, while the official 8\.6\.3 release explicitly lists the CVE as fixed; the CNA affected range also excludes 8\.6\.3\.
- The researcher explains double-free mechanisms, while the CNA supplies CWE-122; neither classification is silently substituted for the other\.
- Original vendor-report, award decision and settlement dates remain unknown; June 2 publication year is inferred\.
- Current rules provide explicit USD context but are not the archived 2025 rules\.

## Sources and attribution

- [ZeroDay\.cloud 2025 individual competition results](<https://www.wiz.io/blog/wiz-zeroday-cloud-hacking-competition-behind-the-scenes>) — Nir Ohfeld / Wiz Research; retrieved 2026-10-02T19:21:00Z.
- [ZeroDay\.cloud vulnerability tracker](<https://www.zeroday.cloud/vulnerability-tracker>) — Wiz / ZeroDay\.cloud; retrieved 2026-10-02T19:21:00Z.
- [ZeroDay\.cloud current rules: US-dollar denomination](<https://www.zeroday.cloud/rules>) — Wiz; retrieved 2026-10-02T19:21:00Z.
- [CVE-2026-25243: Two Redis RESTORE Bugs Leading to RCE](<https://www.zeroday.cloud/blog/redis-cve-2026-25243-deep-dive>) — Emil Lerner / ZeroDay\.cloud; retrieved 2026-10-02T19:21:00Z.
- [Redis serialized-value validation advisory GHSA-c8h9-259x-jff4](<https://github.com/redis/redis/security/advisories/GHSA-c8h9-259x-jff4>) — Redis; retrieved 2026-10-02T19:21:00Z.
- [CVE-2026-25243 CNA record](<https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/25xxx/CVE-2026-25243.json>) — Redis / GitHub CNA; retrieved 2026-10-02T19:21:00Z.
- [Redis 8\.6\.3 security release](<https://github.com/redis/redis/releases/tag/8.6.3>) — Redis; retrieved 2026-10-02T19:21:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
