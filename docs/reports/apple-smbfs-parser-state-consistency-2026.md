# macOS SMBFS error handling left inconsistent kernel parser state

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Apple  
**Product:** macOS SMB filesystem

## What the evidence establishes

Publication window: uncertain original publication date; reviewed as of 2026-10-02.

A rejected network response left inconsistent filesystem state\. The researcher reports a $20,000 award and subsequent payment\.

### Root cause

The parser published a count before validating the associated allocation\. Error cleanup did not restore the count and pointer together\. The researcher compared parsing, cleanup and later consumption to explain why a failed validation still contaminated trusted kernel state\.

### Bounded impact

A Mac had to connect to a malicious SMB share; guest access was sufficient\. The researcher demonstrated kernel panics on Apple silicon\. Apple describes possible system termination or kernel-memory corruption\. General-purpose code execution was not demonstrated\.

### Defensive lessons

- Publish related parser fields atomically only after validation succeeds; reset them consistently on every failure\.
- Require consumers to validate compound state, not merely individual fields\.
- Apple reports improved bounds checking; the researcher's temporary-state design is a recommendation, not a verified patch description\.

## Award and evidence

**USD 20,000** — bug\_bounty; single\_vulnerability; status: paid.

Evidence level: researcher\_reported. One CVE-specific award, not the researcher's cumulative earnings\. Source uses $; Apple's official bounty announcement supplies US-dollar program context only\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/apple-smbfs-parser-state-consistency-2026.json>).

## Dates

- **published:** Unknown; precision: unknown; basis: not\_reported. Original detailed README publication date was not established; advisory release is not substituted\.
- **public disclosure:** 2026-09-14; precision: day; basis: explicit. Vendor security advisory; the researcher README publication date is not established\.
- **reported:** 2026-05-03; precision: day; basis: explicit
- **awarded:** 2026-05-14; precision: day; basis: explicit
- **fixed:** 2026-09-14; precision: day; basis: explicit. Golden Gate 27 release and matching SMB advisory\.
- **paid:** 2026-06-15; precision: day; basis: explicit
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T23:06:13Z. Read primary public disclosures and corroborating sources; checked individual award scope\. No target interaction or exploit reproduction\.

- Payment is researcher-reported, not independently audited\.
- Detailed disclosure publication date remains unknown\.
- Researcher did not independently verify the production patch\.
- USD denomination is inferred from Apple’s 2022 program announcement; the researcher states only $, and no contemporaneous currency-specific payment evidence was reviewed\.

## Sources and attribution

- [CVE-2026-84543: a remote kernel vulnerability in macOS SMBFS](<https://github.com/petermalone/CVE-2026-84543>) — Peter Malone; retrieved 2026-10-02T23:01:00Z.
- [About the security content of macOS Golden Gate 27](<https://support.apple.com/en-us/149035>) — Apple; retrieved 2026-10-02T23:01:00Z.
- [Apple expands industry-leading commitment to protect users from highly targeted mercenary spyware](<https://www.apple.com/nz/newsroom/2022/07/apple-expands-commitment-to-protect-users-from-mercenary-spyware/>) — Apple; retrieved 2026-10-02T23:01:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
