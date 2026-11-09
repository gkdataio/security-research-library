# GitHub fork collaboration applied inconsistent authorization

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

[Read the original source](<https://blog.teddykatz.com/2021/03/10/fork-collab-abuse.html>) — Teddy Katz · [Canonical JSON](<../../data/reports/github-fork-collaboration-authorization-2021.json>)

<a id="what-the-evidence-establishes"></a>
## Main takeaway

GitHub checked fork-collaboration permissions differently when a setting was created and when it was changed\. This could give an unauthorized user write access to affected public forks\. The researcher reports a USD 20,000 award for this first finding in the article\.

**Organization:** GitHub  
**Product:** GitHub fork collaboration

<a id="root-cause"></a>
## What went wrong

Permission checks differed between creation and modification of the same collaboration setting\.

<a id="bounded-impact"></a>
## What the evidence shows

An unauthorized user could obtain write access to affected public forks\.

## Defensive lessons

- Centralize entitlement checks across mutation paths\.
- Verify that only an authorized owner can grant collaboration privileges\.

## Award and evidence

**USD 20,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. First report only; the separately awarded CVE-2021-22863 is a different record\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/github-fork-collaboration-authorization-2021.json>).

## Dates

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

- **published:** 2021-03-10; precision: day; basis: explicit; source: [Messing with GitHub’s fork collaboration for fun and profit](<https://blog.teddykatz.com/2021/03/10/fork-collab-abuse.html>) (source ID: primary).
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported; source: Not recorded.
- **reported:** 2021-01-22; precision: day; basis: explicit; source: [Messing with GitHub’s fork collaboration for fun and profit](<https://blog.teddykatz.com/2021/03/10/fork-collab-abuse.html>) (source ID: primary).
- **awarded:** 2021-03-02; precision: day; basis: explicit; source: [Messing with GitHub’s fork collaboration for fun and profit](<https://blog.teddykatz.com/2021/03/10/fork-collab-abuse.html>) (source ID: primary).
- **fixed:** 2021-01-27; precision: day; basis: explicit; source: [Messing with GitHub’s fork collaboration for fun and profit](<https://blog.teddykatz.com/2021/03/10/fork-collab-abuse.html>) (source ID: primary). github\.com deployment; Enterprise Server releases followed March 2, 2021\.
- **paid:** Unknown; precision: unknown; basis: not\_reported; source: Not recorded.
- **award announced:** Unknown; precision: unknown; basis: not\_reported; source: Not recorded.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported; source: Not recorded.

## Verification limits

Reviewed: 2026-10-02T15:12:00Z. Primary public source read; individual award and source provenance verified\. No target testing or exploit reproduction performed\.

- Award is reported by the cited source; cash settlement is not independently audited\.

## Sources and attribution

- [Messing with GitHub’s fork collaboration for fun and profit](<https://blog.teddykatz.com/2021/03/10/fork-collab-abuse.html>) — Teddy Katz; source ID: primary; retrieved 2026-10-02T15:12:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
