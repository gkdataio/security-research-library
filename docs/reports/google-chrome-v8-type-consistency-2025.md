# V8 optimized object handling retained invalid type assumptions

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

[Read the original source](<https://securitylab.github.com/advisories/GHSL-2025-114_Chromium/>) — Man Yue Mo / GitHub Security Lab · [Canonical JSON](<../../data/reports/google-chrome-v8-type-consistency-2025.json>)

<a id="what-the-evidence-establishes"></a>
## Main takeaway

V8's optimized property lookup could keep using outdated assumptions after an object's structure changed\. Memory reads and writes were possible; the researcher describes possible renderer code execution when combined with a separate V8 heap-sandbox escape\. Google awarded USD 50,000 for this one report\.

**Organization:** Google  
**Product:** Chrome / V8

<a id="root-cause"></a>
## What went wrong

V8 sped up property lookups by caching assumptions about the objects that supplied them\. For prototype chains involving WebAssembly objects, changes to an object's structure did not always invalidate those assumptions\. An optimized handler could then use the wrong type assumptions\.

<a id="bounded-impact"></a>
## What the evidence shows

Memory read/write was possible\. The researcher describes possible code execution within Chrome's renderer when combined with a separate V8 heap-sandbox escape\. This does not establish escape from the renderer's process sandbox or full-machine compromise\.

## Defensive lessons

- Optimized execution must invalidate cached assumptions when object state changes and handle all supported object families consistently\.
- Distinguish issue-status fixes from stable-release availability\.

## Award and evidence

**USD 50,000** — bug\_bounty; single\_vulnerability; status: awarded.

Evidence level: vendor\_confirmed. Case notices use $; USD is contextual from the official Chromium program source\. No currency conversion or cash-receipt claim\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-chrome-v8-type-consistency-2025.json>).

## Dates

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

- **published:** 2026-03-17; precision: day; basis: explicit; source: [GHSL-2025-114: Chromium V8 advisory](<https://securitylab.github.com/advisories/GHSL-2025-114_Chromium/>) (source ID: researcher-advisory). Detailed researcher advisory; public issue access opened January 13, 2026, after the October 2025 vendor notice\.
- **public disclosure:** 2025-10-28; precision: day; basis: explicit; source: [Chrome Stable Channel Update for Desktop, 2025-10-28](<https://chromereleases.googleblog.com/2025/10/stable-channel-update-for-desktop_28.html?hl=fr>) (source ID: release). Vendor release disclosure; full issue access was enabled later\.
- **reported:** 2025-09-26; precision: day; basis: explicit; source: [Chromium issue 447613211](<https://issues.chromium.org/issues/447613211>) (source ID: vendor-report).
- **awarded:** 2025-10-14; precision: day; basis: explicit; source: [Chromium issue 447613211](<https://issues.chromium.org/issues/447613211>) (source ID: vendor-report).
- **fixed:** 2025-10-28; precision: day; basis: explicit; source: [Chrome Stable Channel Update for Desktop, 2025-10-28](<https://chromereleases.googleblog.com/2025/10/stable-channel-update-for-desktop_28.html?hl=fr>) (source ID: release). Documented stable release; issue was marked Fixed 2025-10-06\. Backport availability may differ\.
- **paid:** Unknown; precision: unknown; basis: not\_reported; source: Not recorded.
- **award announced:** 2025-10-28; precision: day; basis: explicit; source: [Chrome Stable Channel Update for Desktop, 2025-10-28](<https://chromereleases.googleblog.com/2025/10/stable-channel-update-for-desktop_28.html?hl=fr>) (source ID: release). Per-issue reward listed in the public release notice\.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported; source: Not recorded.

## Verification limits

Reviewed: 2026-10-02T16:08:00Z. Public Chromium issue award/date metadata read in the cloud browser; official release corroborates exact per-issue total and CVE\. Researcher advisory independently reviewed\.

- Case notices use dollar notation; USD denomination relies on official Chromium program context\.
- Award decisions are established; payment completion is not\.
- Fixed status and publicly available stable release are separate dates\.
- Release list revised November 17, 2025; it identifies the newly added entries separately as CVE-2025-13226 through 13230\. This record retains the October 28 release disclosure\.

## Related conceptual diagrams

- [Parsing safety and action authority](<../diagram-gallery.md#parsing-safety-action-authority>)

## Sources and attribution

- [Chromium issue 447613211](<https://issues.chromium.org/issues/447613211>) — Google Chromium security team; source ID: vendor-report; retrieved 2026-10-02T16:08:00Z.
- [Chrome Stable Channel Update for Desktop, 2025-10-28](<https://chromereleases.googleblog.com/2025/10/stable-channel-update-for-desktop_28.html?hl=fr>) — Google Chrome team; source ID: release; retrieved 2026-10-02T16:08:00Z.
- [Security rewards at Google: Two MEEELLION Dollars Later](<https://blog.chromium.org/2013/08/security-rewards-at-google-two.html>) — Chromium team; source ID: currency-context; retrieved 2026-10-02T16:08:00Z.
- [GHSL-2025-114: Chromium V8 advisory](<https://securitylab.github.com/advisories/GHSL-2025-114_Chromium/>) — Man Yue Mo / GitHub Security Lab; source ID: researcher-advisory; retrieved 2026-10-02T16:08:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
