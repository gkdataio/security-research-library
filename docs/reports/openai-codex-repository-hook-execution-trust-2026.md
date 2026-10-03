# Codex automated Git operations trusted repository hook settings

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** OpenAI  
**Product:** Codex Desktop

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

ZDI awarded Summoning Team USD 20,000 for this distinct Pwn2Own Berlin entry\.

### Root cause

Automated repository operations honored repository-local Git hook configuration outside the intended command-approval boundary\.

### Bounded impact

The vendor confirms possible user-privilege code execution when specially prepared local repository configuration is preserved\. An ordinary Git clone does not preserve that configuration\.

### Defensive lessons

- Treat repository-local execution settings as untrusted input\.
- Apply execution policy to background tooling as well as user-visible agent commands\.

## Award and evidence

**USD 20,000** — competition\_award; single\_competition\_entry; status: awarded.

Evidence level: organizer\_confirmed. The successful second-round entry earned USD 20,000\. The advertised first-round maximum and researcher’s other event entries are not this award\. Event rules explicitly denominate prizes in US currency; cash settlement is unverified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/openai-codex-repository-hook-execution-trust-2026.json>).

## Dates

- **published:** 2026-09-01; precision: day; basis: explicit. Vendor-authored technical CNA publication\. ZDI published its advisory on September 10\.
- **public disclosure:** 2026-05-15; precision: day; basis: explicit. Public competition demonstration and result, before technical CNA publication\.
- **reported:** Unknown; precision: unknown; basis: not\_reported. Original submission to the competition organizer is unknown\. ZDI later lists 2026-06-02 as reported to vendor; this is a separate event, not the original submission date\.
- **awarded:** 2026-05-15; precision: day; basis: explicit. Individual-entry award reported in the day’s results\.
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Vendor CNA lists fixed versions, but an exact release/deployment date was not established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2026-05-15; precision: day; basis: explicit
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T17:23:00Z. Matched organizer result to the credited team, product and distinct CVE in the vendor CNA and Pwn2Own-tagged ZDI advisory; checked official currency and one-entry-per-target rules\.

- Competition award, not an ordinary vendor bounty or a team’s total earnings\.
- Original organizer submission and cash-transfer dates are unknown\.
- Public demonstration, later vendor notification and technical publication are distinct events\.

## Sources and attribution

- [OpenAI CNA record for CVE-2026-19590](<https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/19xxx/CVE-2026-19590.json>) — OpenAI CNA, distributed through the CVE Program; retrieved 2026-10-02T17:23:00Z.
- [Pwn2Own Berlin 2026 daily results](<https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results>) — Dustin Childs / Zero Day Initiative; retrieved 2026-10-02T17:23:00Z.
- [Pwn2Own Berlin 2026 rules](<https://www.zerodayinitiative.com/Pwn2OwnBerlin2026Rules.html>) — Trend Micro Zero Day Initiative; retrieved 2026-10-02T17:23:00Z.
- [ZDI-26-648 Codex advisory](<https://www.zerodayinitiative.com/advisories/ZDI-26-648/>) — Zero Day Initiative; retrieved 2026-10-02T17:23:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
