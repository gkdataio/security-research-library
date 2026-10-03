# Support integration exposed internal Confluence documentation

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** HackerOne  
**Product:** HackerOne support and internal documentation

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

A support-system misconfiguration allowed external access to internal Confluence documentation, including limited content modification\. One report received USD 12,500 split between two researchers\.

### Root cause

The vendor attributes the issue to a support-system misconfiguration that allowed support workflows to cross the boundary into internal documentation\. The public summary does not reveal the precise configuration, authentication prerequisites or permission-propagation mechanism; an identity-entitlement failure is a defensive interpretation, not a documented implementation detail\.

### Bounded impact

The vendor confirms access to nonpublic internal documentation and the ability to view and modify limited Confluence content\. It does not establish unrestricted administrative control, the volume of material exposed, or broader compromise\. The timeline records accepted retesting and Resolved status on June 3, 2025; redacted comment bodies do not reveal the corrective configuration or exact deployment date\.

### Defensive lessons

- Editorial lesson: assess whether external support workflows can confer access to employee-only documentation\.
- Editorial lesson: review integration permissions separately for read and write access; limited modification is distinct from unrestricted control\.
- Editorial lesson: verify the corrected access boundary after configuration changes without treating a resolution status as evidence of the precise fix\.

## Award and evidence

**USD 12,500** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. Dollar notation appears in the report UI; USD denomination is contextual from HackerOne’s disclosure policy\. Award events do not establish cash receipt\. One-report total: USD 5,000 to red\_darkin and USD 7,500 to madara\_; neither recipient individually received USD 10,000\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/hackerone-support-confluence-access-boundary-2025.json>).

## Dates

- **published:** 2025-08; precision: month; basis: inferred. Disclosure events appear August 13 and August 15, 2025\. The sidebar shows August 15; month retained because first public day is ambiguous\.
- **public disclosure:** 2025-08; precision: month; basis: inferred. Disclosure events appear August 13 and August 15, 2025\. The sidebar shows August 15; month retained because first public day is ambiguous\.
- **reported:** 2025-04-26; precision: day; basis: explicit
- **awarded:** 2025-05-30; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Report marked Resolved June 3, 2025; exact deployment date is unknown\. A later edited retest comment is not a deployment timestamp\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T08:59:00Z. Freshly read the public vendor summary, expanded award events, accepted-retest and resolution events in the cloud browser\. Technical and comment bodies remain redacted\. Existing currency evidence retained without a fresh review; no target testing\.

- Award events establish an award, not independently audited settlement\.
- Exact fix-deployment date is unavailable; a Resolved status date is not treated as deployment\.
- Technical report and comment bodies are redacted; interpretation is limited to the vendor’s public summary and event metadata\.
- Exact access prerequisites and the corrective configuration are not disclosed; no specific identity provisioning or entitlement mechanism is established by the public summary\.

## Sources and attribution

- [Support integration exposed internal Confluence documentation \(report 3113398\)](<https://hackerone.com/reports/3113398>) — HackerOne and the credited researchers; retrieved 2026-10-03T08:59:00Z.
- [Vulnerability Disclosure Standards: Bug Bounty payment denomination](<https://www.hackerone.com/terms/disclosure-guidelines>) — HackerOne; retrieved 2026-10-02T15:43:47Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
