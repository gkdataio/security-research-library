# Chrome graphics input validation weakened an isolation boundary

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Chrome / ANGLE

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-02.

One Chrome graphics report earned USD 250,000 across two award decisions\.

### Root cause

The graphics translation layer insufficiently validated untrusted input\.

### Bounded impact

Insufficiently validated graphics input could cross a browser security boundary; the vendor classified the issue High\.

### Defensive lessons

- Validate untrusted graphics inputs at security boundaries and verify that mitigations cover all relevant input paths\.
- Distinguish issue-status fixes from stable-release availability\.

## Award and evidence

**USD 250,000** — bug\_bounty; single\_vulnerability; status: awarded.

Evidence level: vendor\_confirmed. USD 25,000 on June 4 plus USD 225,000 on June 29 for one report\. Case notices use $; USD is contextual from the official Chromium program source\. No currency conversion or cash-receipt claim\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-chrome-angle-input-validation-2026.json>).

## Dates

- **published:** 2026-09-03; precision: day; basis: explicit. Full report access restrictions removed; vendor release notice appeared earlier\.
- **public disclosure:** 2026-06-30; precision: day; basis: explicit. Vendor release disclosure; full issue access was enabled later\.
- **reported:** 2026-03-13; precision: day; basis: explicit
- **awarded:** 2026-06-29; precision: day; basis: explicit
- **fixed:** 2026-06-30; precision: day; basis: explicit. Documented stable release; issue was marked Fixed 2026-05-27\. Backport availability may differ\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2026-06-30; precision: day; basis: explicit. Per-issue reward listed in the public release notice\.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T16:08:00Z. Public Chromium issue award/date metadata read in the cloud browser; official release corroborates exact per-issue total and CVE\. No operational details retained\.

- Case notices use dollar notation; USD denomination relies on official Chromium program context\.
- Award decisions are established; payment completion is not\.
- Fixed status and publicly available stable release are separate dates\.
- Release credits an anonymous researcher\. No identity or per-person split is inferred\.

## Sources and attribution

- [Chromium issue 492218546](<https://issues.chromium.org/issues/492218546>) — Google Chromium security team; retrieved 2026-10-02T16:08:00Z.
- [Chrome Stable Channel Update for Desktop, 2026-06-30](<https://chromereleases.googleblog.com/2026/06/stable-channel-update-for-desktop_0175352312.html?m=1>) — Google Chrome team; retrieved 2026-10-02T16:08:00Z.
- [Security rewards at Google: Two MEEELLION Dollars Later](<https://blog.chromium.org/2013/08/security-rewards-at-google-two.html>) — Chromium team; retrieved 2026-10-02T16:08:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
