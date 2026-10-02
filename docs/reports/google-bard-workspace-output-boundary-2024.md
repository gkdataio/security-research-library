# Bard Workspace integration weakened output-data boundaries

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Bard Workspace integration

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

One Workspace data-disclosure finding within a broader research article earned USD 20,000\.

### Root cause

Generated content and browser output restrictions did not maintain the intended boundary around connected Workspace data\.

### Bounded impact

The researchers demonstrated disclosure of email content from a controlled account\.

### Defensive lessons

- Independently constrain external destinations for sensitive model output\.
- Review connector data access and rendering as a single end-to-end trust boundary\.

## Award and evidence

**USD 20,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. Records the individual base award, not the article’s USD 50,000 aggregate\. A USD 1,337 event bonus for this finding is stated separately\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-bard-workspace-output-boundary-2024.json>).

## Dates

- **published:** 2024-03-04; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T14:39:00Z. Primary public source read; individual award and source provenance verified\. No target testing or exploit reproduction performed\.

- Award is reported by the cited source; cash settlement is not independently audited\.

## Sources and attribution

- [We Hacked Google A\.I\. for $50,000](<https://depi.security/blog/20240304-google-hack-50000/>) — Roni Carta; retrieved 2026-10-02T14:39:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
