# Pixel lock-screen completion lost security-state binding

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Google Pixel / Android lock-screen state management

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

A researcher-published vendor decision documents a USD 70,000 award for CVE-2022-20465\.

### Root cause

The researcher’s patch analysis attributes the issue to completion events dismissing a different active security challenge after concurrent state changes\.

### Bounded impact

Physical access could bypass the lock screen on tested Pixel 5 and 6 devices\. Broader Android coverage was not established by the researcher\.

### Defensive lessons

- Bind authentication completion to the exact challenge and security context it satisfies\.
- Model concurrent authentication-state transitions and reject stale completion events\.
- Distinguish a security patch-level label from the date an update reached devices\.

## Award and evidence

**USD 70,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported\_with\_vendor\_quote. Explicit USD decision for this report\. It was initially marked duplicate; the reproduced response explains an exception because the report enabled remediation\. Cash receipt is not separately documented\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-pixel-lock-screen-state-binding-2022.json>).

## Dates

- **published:** 2022-11-10; precision: day; basis: explicit
- **public disclosure:** 2022-11-08; precision: day; basis: explicit. CVE record publication\. The Android bulletin is dated November 7; its original snapshot was not retrieved, so first appearance of this entry is not asserted\.
- **reported:** 2022-06-13; precision: day; basis: explicit
- **awarded:** 2022-10-12; precision: day; basis: explicit
- **fixed:** 2022-11; precision: month; basis: explicit. Reported fixed in the November update\. The 2022-11-05 patch-level label is not used as an exact rollout date\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T17:14:30Z. Read the researcher article, full reproduced report discussion and vendor bulletins; checked the explicit award decision and unique CVE\. Cross-checked the Google-authored CNA record publication date\.

- The award decision is reproduced by the researcher, not independently published by the vendor\.
- Payment completion is unverified\.
- Vendor patch-level labels and bulletin publication dates do not establish each device’s update deployment date\.

## Sources and attribution

- [Accidental $70k Google Pixel Lock Screen Bypass](<https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/>) — David Schütz; retrieved 2026-10-02T17:12:00Z.
- [Report 0016: Complete Lock Screen Bypass on Google Pixel devices](<https://feed.bugs.xdavidhu.me/bugs/0016>) — David Schütz; retrieved 2026-10-02T17:12:00Z.
- [Android Security Bulletin, November 2022](<https://source.android.com/docs/security/bulletin/2022-11-01>) — Android Open Source Project / Google; retrieved 2026-10-02T17:12:00Z.
- [Pixel Update Bulletin, November 2022](<https://source.android.com/docs/security/bulletin/pixel/2022-11-01>) — Google; retrieved 2026-10-02T17:12:00Z.
- [Google Android CNA record for CVE-2022-20465](<https://github.com/CVEProject/cvelistV5/blob/main/cves/2022/20xxx/CVE-2022-20465.json>) — Google Android CNA, distributed through the CVE Program; retrieved 2026-10-02T17:14:30Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
