# Redis Lua object lifetime failure crossed the scripting boundary

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Redis  
**Product:** Redis with Lua scripting

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

ZDI awarded Wiz researchers USD 40,000 for this single Pwn2Own Berlin 2025 entry\.

### Root cause

Lua garbage collection could leave an object referenced after its memory was freed, undermining the interpreter’s memory-safety assumptions\.

### Bounded impact

The vendor confirms possible native code execution by an authenticated user able to run Lua scripts\. This crosses the scripting boundary; host impact remains dependent on process privileges and deployment isolation\.

### Defensive lessons

- Review object-lifetime invariants across embedded interpreters and native components\.
- Grant scripting access only where needed and retain least-privilege service execution\.
- Check corrected vendor release guidance instead of relying on an early fixed-version summary\.

## Award and evidence

**USD 40,000** — competition\_award; single\_competition\_entry; status: awarded.

Evidence level: organizer\_confirmed. One competition-entry award, not the researchers’ event total\. Official rules specify US currency; recipient allocation and actual cash settlement are unverified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/redis-lua-object-lifetime-isolation-2025.json>).

## Dates

- **published:** 2025-10-06; precision: day; basis: explicit. Primary research article publication; earlier competition results are separately dated\.
- **public disclosure:** 2025-05-16; precision: day; basis: explicit. Public demonstration and result; vendor technical advisory followed later\.
- **reported:** 2025-05-16; precision: day; basis: explicit. Researcher timeline explicitly ties this CVE to its May 16 Pwn2Own report\.
- **awarded:** 2025-05-16; precision: day; basis: explicit. Award announced for the named individual entry\.
- **fixed:** 2025-10-03; precision: day; basis: explicit. Researcher article states that Redis released its advisory and patched version on this date\. This is not a universal customer-deployment date; later vendor corrections affected some Redis Software fixed-version labels\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2025-05-16; precision: day; basis: explicit
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T17:39:00Z. Read the researcher’s explicit CVE-to-Pwn2Own submission timeline and matched its date, product and named researchers to the organizer’s individual-entry award; corroborated CVE and scope with vendor guidance\. Official rules establish USD denomination\.

- Single competition-entry award; individual recipient splits and cash-transfer date are unknown\.
- The October 6 article is the primary research publication; May demonstration and October 3 vendor advisory are distinct events\.
- Vendor Redis Software release labels were corrected on October 27 and October 30, 2025; this record does not assume every product variant was fixed in its originally listed version\.

## Related conceptual diagrams

- [Parsing safety and action authority](<../diagram-gallery.md#parsing-safety-action-authority>)

## Sources and attribution

- [RediShell: Redis CVE-2025-49844](<https://www.wiz.io/blog/wiz-research-redis-rce-cve-2025-49844>) — Benny Isaacs and Nir Brakha / Wiz Research; retrieved 2026-10-02T17:39:00Z.
- [Pwn2Own Berlin 2025 daily results](<https://www.zerodayinitiative.com/blog/2025/5/16/pwn2own-berlin-2025-day-two-results>) — Dustin Childs / Zero Day Initiative; retrieved 2026-10-02T17:39:00Z.
- [Pwn2Own Berlin 2025 rules](<https://www.zerodayinitiative.com/Pwn2OwnBerlin2025Rules.html>) — Trend Micro Zero Day Initiative; retrieved 2026-10-02T17:39:00Z.
- [Redis Lua Use-After-Free security advisory](<https://github.com/redis/redis/security/advisories/GHSA-4789-qfc9-5f9q>) — Redis maintainers; retrieved 2026-10-02T17:39:00Z.
- [Redis CVE-2025-49844 remediation guidance and corrections](<https://redis.io/blog/security-advisory-cve-2025-49844/>) — Riaz Lakhani / Redis; retrieved 2026-10-02T17:39:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
