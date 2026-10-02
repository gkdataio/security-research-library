# Gemini Enterprise connected-content trust failure allowed persistent-memory modification

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Gemini Enterprise Jira integration

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-02.

A researcher reports a $15,000 Google bounty for a Gemini Enterprise integration issue affecting persistent assistant memory\.

### Root cause

The researcher compared user-confirmed actions with persistent memory changes\. Retrieved collaboration content could influence an operation that changed saved state without equivalent confirmation\. The failed boundary was between permission to read connected data and authority to mutate the user’s lasting assistant state\.

### Bounded impact

In a two-account setup, the researcher confirmed deletion of the test recipient’s saved memories\. The scenario required shared-project content access and user-initiated retrieval\. Broader cross-tenant access, mailbox compromise and lasting changes to every future response were not demonstrated\.

### Defensive lessons

- Model persistent memory as a security-sensitive write operation with its own authorization decision\.
- Preserve provenance when retrieved content passes between a connector, model and state-changing component\.
- Require a trusted authorization signal for each write; permission to summarize content should not imply permission to alter saved preferences\.
- Separate observed state changes from speculative downstream behavior in impact reports; the public article does not establish the vendor’s remediation design\.

## Award and evidence

**USD 15,000** — bug\_bounty; single\_report; status: paid.

Evidence level: researcher\_reported. The researcher reports being paid $15,000 for this distinct finding; do not combine the separate $1,337 example\. Exact award/settlement date is unknown\. Dollar-denominated Google bounty; USD normalization\. The individual write-up uses the $ symbol rather than spelling out USD\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-gemini-enterprise-connected-content-memory-integrity-2026.json>).

## Dates

- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported
- **published:** 2026-03-12; precision: day; basis: inferred. DEV article March 12, 2026; the researcher's Reddit write-up is dated March 9, 2026\. Original X post is linked but its exact date was not independently established\. No exact report, award, or fix dates were found\.
- **public disclosure:** 2026-03-09; precision: day; basis: explicit. Earlier researcher publication on Reddit; linked original X post might be earlier\.

## Verification limits

Reviewed: 2026-10-02T20:20:00Z. Re-read the researcher’s primary article, preserving its individual payout attribution and distinguishing the observed test-account memory deletion from broader inferred impact\.

- No vendor-hosted confirmation of this individual payout found
- Do not confuse this finding with the separate $1,337 memory issue mentioned in the introduction
- Remediation date, exact patch design and current status are not independently established
- The reported demonstration used two researcher-controlled accounts; it does not establish actual customer compromise

## Related conceptual diagrams

- [Retrieved content is data, not authority](<../diagram-gallery.md#ai-content-authority-separation>)

## Sources and attribution

- [Google paid me $15,000 for this Prompt Injection bug\.](<https://dev.to/behi_sec/google-paid-me-15000-for-this-prompt-injection-bug-5fn6>) — Behi; retrieved 2026-10-02T20:20:00Z.
- [Supporting primary disclosure source](<https://www.reddit.com/r/bugbounty/comments/1row41z/google_paid_me_15000_for_this_prompt_injection_bug/>) — Behi; retrieved 2026-10-02T03:54:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
