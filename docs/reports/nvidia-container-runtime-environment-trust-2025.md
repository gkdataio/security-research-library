# NVIDIA container initialization inherited untrusted execution context

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** NVIDIA  
**Product:** NVIDIA Container Toolkit

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

ZDI awarded Wiz researchers USD 30,000 for this single Pwn2Own Berlin 2025 entry\.

### Root cause

A privileged container-initialization component inherited container-controlled execution context without sufficient separation from host authority\.

### Bounded impact

An untrusted container image could lead to code execution with elevated host permissions\. Scope depends on runtime configuration; NVIDIA explicitly excludes systems using crun from this CVE\.

### Defensive lessons

- Keep privileged runtime initialization independent of workload-controlled configuration\.
- Use layered tenant isolation and verify vendor-specific runtime applicability before remediation\.

## Award and evidence

**USD 30,000** — competition\_award; single\_competition\_entry; status: awarded.

Evidence level: organizer\_confirmed. One competition-entry award, not the researchers’ event total\. Official rules specify US currency; recipient allocation and actual cash settlement are unverified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/nvidia-container-runtime-environment-trust-2025.json>).

## Dates

- **published:** 2025-07-17; precision: day; basis: explicit. Primary research article publication; earlier competition results are separately dated\.
- **public disclosure:** 2025-05-17; precision: day; basis: explicit. Public demonstration and result; vendor technical advisory followed later\.
- **reported:** 2025-05-17; precision: day; basis: explicit. The researchers explicitly date this CVE’s initial vendor report at Pwn2Own to May 17\. ZDI separately lists June 5 as its vendor-notification date; that later coordination event is not substituted for the initial report\.
- **awarded:** 2025-05-17; precision: day; basis: explicit. Award announced for the named individual entry\.
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Vendor bulletin initially released July 15, 2025 and later revised affected products and fixes; the exact release date for each patched component was not established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2025-05-17; precision: day; basis: explicit
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T17:39:00Z. Read the researcher’s explicit CVE-to-Pwn2Own submission timeline and matched its date, product and named researchers to the organizer’s individual-entry award; corroborated CVE and scope with vendor guidance\. Official rules establish USD denomination\.

- Historical technical publication, outside the preferred twelve-month window\.
- One awarded competition entry shared by two named researchers; recipient splits and cash-transfer date are unknown\.
- NVIDIA credits an additional finder, without assigning that person this competition award\.
- Vendor bulletin was updated after initial disclosure; affected configurations and product-specific fixed releases should be read there\.

## Sources and attribution

- [NVIDIAScape: NVIDIA Container Toolkit CVE-2025-23266](<https://www.wiz.io/blog/nvidia-ai-vulnerability-cve-2025-23266-nvidiascape>) — Nir Ohfeld and Shir Tamari / Wiz Research; retrieved 2026-10-02T17:39:00Z.
- [Pwn2Own Berlin 2025 daily results](<https://www.zerodayinitiative.com/blog/2025/5/17/pwn2own-berlin-2025-day-three-results>) — Dustin Childs / Zero Day Initiative; retrieved 2026-10-02T17:39:00Z.
- [Pwn2Own Berlin 2025 rules](<https://www.zerodayinitiative.com/Pwn2OwnBerlin2025Rules.html>) — Trend Micro Zero Day Initiative; retrieved 2026-10-02T17:39:00Z.
- [NVIDIA Container Toolkit security bulletin, July 2025](<https://nvidia.custhelp.com/app/answers/detail/a_id/5659>) — NVIDIA PSIRT; retrieved 2026-10-02T17:39:00Z.
- [ZDI-25-626 NVIDIA Container Toolkit advisory](<https://www.zerodayinitiative.com/advisories/ZDI-25-626/>) — Zero Day Initiative; retrieved 2026-10-02T17:39:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
