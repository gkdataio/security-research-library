# V8 optimized object handling retained invalid type assumptions

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Chrome / V8

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

One V8 type-consistency report earned a USD 50,000 award\.

### Root cause

Optimized object handling could retain invalid type assumptions, producing a type-consistency failure\.

### Bounded impact

Memory read/write was possible; broader code execution required an additional boundary failure\.

### Defensive lessons

- Optimized execution must invalidate cached assumptions when object state changes and handle all supported object families consistently\.
- Distinguish issue-status fixes from stable-release availability\.

## Award and evidence

**USD 50,000** — bug\_bounty; single\_vulnerability; status: awarded.

Evidence level: vendor\_confirmed. Case notices use $; USD is contextual from the official Chromium program source\. No currency conversion or cash-receipt claim\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-chrome-v8-type-consistency-2025.json>).

## Dates

- **published:** 2026-03-17; precision: day; basis: explicit. Detailed researcher advisory; public issue access opened January 13, 2026, after the October 2025 vendor notice\.
- **public disclosure:** 2025-10-28; precision: day; basis: explicit. Vendor release disclosure; full issue access was enabled later\.
- **reported:** 2025-09-26; precision: day; basis: explicit
- **awarded:** 2025-10-14; precision: day; basis: explicit
- **fixed:** 2025-10-28; precision: day; basis: explicit. Documented stable release; issue was marked Fixed 2025-10-06\. Backport availability may differ\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2025-10-28; precision: day; basis: explicit. Per-issue reward listed in the public release notice\.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T16:08:00Z. Public Chromium issue award/date metadata read in the cloud browser; official release corroborates exact per-issue total and CVE\. Researcher advisory independently reviewed\.

- Case notices use dollar notation; USD denomination relies on official Chromium program context\.
- Award decisions are established; payment completion is not\.
- Fixed status and publicly available stable release are separate dates\.
- Release list revised November 17, 2025; it identifies the newly added entries separately as CVE-2025-13226 through 13230\. This record retains the October 28 release disclosure\.

## Related conceptual diagrams

- [Parsing safety and action authority](<../diagram-gallery.md#parsing-safety-action-authority>)

## Sources and attribution

- [Chromium issue 447613211](<https://issues.chromium.org/issues/447613211>) — Google Chromium security team; retrieved 2026-10-02T16:08:00Z.
- [Chrome Stable Channel Update for Desktop, 2025-10-28](<https://chromereleases.googleblog.com/2025/10/stable-channel-update-for-desktop_28.html?hl=fr>) — Google Chrome team; retrieved 2026-10-02T16:08:00Z.
- [Security rewards at Google: Two MEEELLION Dollars Later](<https://blog.chromium.org/2013/08/security-rewards-at-google-two.html>) — Chromium team; retrieved 2026-10-02T16:08:00Z.
- [GHSL-2025-114: Chromium V8 advisory](<https://securitylab.github.com/advisories/GHSL-2025-114_Chromium/>) — Man Yue Mo / GitHub Security Lab; retrieved 2026-10-02T16:08:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
