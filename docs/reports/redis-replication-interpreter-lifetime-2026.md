# Redis replication state changes invalidated an active interpreter

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Redis  
**Product:** Redis replication and Lua function execution

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-02.

Wiz confirms a USD 30,000 individual competition award for Yoni Sherez’s Redis entry, identified as CVE-2026-23631\.

### Root cause

The researcher compared ordinary command handling with replication-related state changes during ongoing function execution\. The latter did not preserve equivalent lifetime checks, so interpreter state could be released while still in use\. The failed invariant was that background synchronization must not invalidate objects needed by active work\.

### Bounded impact

Code execution was demonstrated in the competition\. The vendor limits exposure to authenticated access and replicas configured, or configurable, for writes\. It reported Redis Cloud patched by its May 2026 announcement\. These conditions do not establish equivalent exposure across all deployments\.

### Defensive lessons

- Apply lifetime invariants to background synchronization and administrative state transitions as well as normal request paths\.
- Treat reentrant event handling as a concurrency boundary even in a nominally single-threaded service\.
- Review replica configuration and scripting privileges, and verify fixed versions against the vendor’s product-specific guidance\.

## Award and evidence

**USD 30,000** — competition\_award; single\_competition\_entry; status: awarded.

Evidence level: organizer\_confirmed. One individually identified competition entry\. The organizer uses $; its current rules establish US-dollar notation but concern 2026, not an archived 2025 rules snapshot\. Exact award decision and cash settlement are unknown\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/redis-replication-interpreter-lifetime-2026.json>).

## Dates

- **published:** 2026-06-02; precision: day; basis: inferred. Article displays June 2; 2026 is inferred from its completed May 5, 2026 remediation timeline\.
- **public disclosure:** 2025-12-10; precision: day; basis: explicit. Public competition demonstration; separate from later vendor advisory and technical publication\.
- **reported:** Unknown; precision: unknown; basis: not\_reported. Exact initial report to the vendor is not stated; the tracker dates the competition entry, not vendor receipt\.
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** 2026-05-05; precision: day; basis: explicit. Official Redis 8\.6\.3 release names the CVE\. Other supported release lines are listed separately by the vendor; this date is not a customer deployment date\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2025-12-16; precision: day; basis: explicit. Organizer recap confirms the per-entry award; decision and payment dates remain unknown\.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T20:00:00Z. Matched the individual award to the exact tracker CVE, researcher article and vendor credit\. Cross-checked configuration prerequisites, CNA classification and the official release date\.

- The tracker spells the researcher’s surname Sharez; the matching CVE, vendor credit and researcher article identify Yoni Sherez\.
- The advisory’s structured affected field starts at 7\.0\.0 and says patched versions TBD, while its prose is broader; vendor guidance and the official release identify corrected versions\. No universal version range is inferred\.
- Competition code execution and vendor-qualified deployment exposure are distinct claims; the vendor says it had no evidence of customer exploitation at publication\.
- Exact initial vendor-report, award-decision and cash-settlement dates are unknown\. The June publication year is inferred\.
- USD context comes from current organizer rules, explicitly distinct from an archived 2025 rules snapshot\.

## Sources and attribution

- [ZeroDay\.cloud 2025 individual competition results](<https://www.wiz.io/blog/wiz-zeroday-cloud-hacking-competition-behind-the-scenes>) — Nir Ohfeld / Wiz Research; retrieved 2026-10-02T20:00:00Z.
- [ZeroDay\.cloud vulnerability tracker](<https://www.zeroday.cloud/vulnerability-tracker>) — Wiz / ZeroDay\.cloud; retrieved 2026-10-02T20:00:00Z.
- [ZeroDay\.cloud current rules: US-dollar denomination](<https://www.zeroday.cloud/rules>) — Wiz; retrieved 2026-10-02T19:21:00Z.
- [DarkReplica \(CVE-2026-23631\): Redis Use-After-Free Leads to Post-Auth RCE](<https://www.zeroday.cloud/blog/redis-cve-2026-23631-dark-replica>) — Yoni Sherez / ZeroDay\.cloud; retrieved 2026-10-02T20:00:00Z.
- [Redis Lua lifetime advisory GHSA-8ghh-qpmp-7826](<https://github.com/redis/redis/security/advisories/GHSA-8ghh-qpmp-7826>) — Redis; retrieved 2026-10-02T20:00:00Z.
- [CVE-2026-23631 CNA record](<https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/23xxx/CVE-2026-23631.json>) — Redis / GitHub CNA; retrieved 2026-10-02T20:00:00Z.
- [Redis 8\.6\.3 security release](<https://github.com/redis/redis/releases/tag/8.6.3>) — Redis; retrieved 2026-10-02T20:00:00Z.
- [Redis May 2026 security advisory and product remediation table](<https://redis.io/blog/security-advisory-cve202623479-cve202625243-cve-2026-25588-cve202625589-cve-2026-23631/>) — Riaz Lakhani / Redis; retrieved 2026-10-02T20:00:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
