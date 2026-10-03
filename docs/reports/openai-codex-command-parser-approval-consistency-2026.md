# Codex command approval relied on inconsistent parser semantics

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** OpenAI  
**Product:** Codex CLI and Codex Desktop

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

ZDI awarded Compass Security USD 40,000 for this distinct Pwn2Own Berlin entry\.

### Root cause

Command-safety analysis and the invoked shell interpreted control syntax differently, so the approval decision did not consistently describe the resulting operation\.

### Bounded impact

The vendor describes possible code execution with user privileges after untrusted repository instructions are followed\. Shell availability and filesystem protections constrain impact; command approval failure does not itself disable the filesystem sandbox\.

### Defensive lessons

- Keep safety classification consistent with actual command interpretation\.
- Apply independent filesystem restrictions and protect security-sensitive configuration\.

## Award and evidence

**USD 40,000** — competition\_award; single\_competition\_entry; status: awarded.

Evidence level: organizer\_confirmed. Single competition entry awarded to the Compass team; individual recipient splits and cash-transfer date are unknown\. Event rules explicitly denominate prizes in US currency; cash settlement is unverified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/openai-codex-command-parser-approval-consistency-2026.json>).

## Dates

- **published:** 2026-09-01; precision: day; basis: explicit. Vendor-authored technical CNA publication\. ZDI published its advisory on September 10\.
- **public disclosure:** 2026-05-14; precision: day; basis: explicit. Public competition demonstration and result, before technical CNA publication\.
- **reported:** Unknown; precision: unknown; basis: not\_reported. Original submission to the competition organizer is unknown\. ZDI later lists 2026-06-02 as reported to vendor; this is a separate event, not the original submission date\.
- **awarded:** 2026-05-14; precision: day; basis: explicit. Individual-entry award reported in the day’s results\.
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Vendor CNA lists fixed versions, but an exact release/deployment date was not established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2026-05-14; precision: day; basis: explicit
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T17:23:00Z. Matched organizer result to the credited team, product and distinct CVE in the vendor CNA and Pwn2Own-tagged ZDI advisory; checked official currency and one-entry-per-target rules\.

- Competition award, not an ordinary vendor bounty or a team’s total earnings\.
- Original organizer submission and cash-transfer dates are unknown\.
- Public demonstration, later vendor notification and technical publication are distinct events\.

## Sources and attribution

- [OpenAI CNA record for CVE-2026-19591](<https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/19xxx/CVE-2026-19591.json>) — OpenAI CNA, distributed through the CVE Program; retrieved 2026-10-02T17:23:00Z.
- [Pwn2Own Berlin 2026 daily results](<https://www.zerodayinitiative.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results>) — Dustin Childs / Zero Day Initiative; retrieved 2026-10-02T17:23:00Z.
- [Pwn2Own Berlin 2026 rules](<https://www.zerodayinitiative.com/Pwn2OwnBerlin2026Rules.html>) — Trend Micro Zero Day Initiative; retrieved 2026-10-02T17:23:00Z.
- [ZDI-26-649 Codex advisory](<https://www.zerodayinitiative.com/advisories/ZDI-26-649/>) — Zero Day Initiative; retrieved 2026-10-02T17:23:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
