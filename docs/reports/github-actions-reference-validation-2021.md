# GitHub Actions trust depended on invalid repository references

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

[Read the original source](<https://blog.teddykatz.com/2021/03/17/github-actions-write-access.html>) — Teddy Katz · [Canonical JSON](<../../data/reports/github-actions-reference-validation-2021.json>)

<a id="what-the-evidence-establishes"></a>
## Main takeaway

GitHub Actions could give an unauthorized workflow access to repository secrets and write permissions because repository references were not checked consistently\. The researcher reports a USD 25,000 award for this finding\.

**Organization:** GitHub  
**Product:** GitHub Actions and GitHub Enterprise Server

<a id="root-cause"></a>
## What went wrong

Object validation differed between creation and mutation; automation relied on a branch-type invariant that was not consistently enforced\.

<a id="bounded-impact"></a>
## What the evidence shows

Repository secrets and write authority could become available to an unauthorized workflow\.

## Defensive lessons

- Enforce security invariants at every mutation and at their privileged consumers\.
- Keep repository secrets confined to explicitly trusted execution contexts\.

## Award and evidence

**USD 25,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. Single finding; the later 2022 follow-up earned USD 7,500 and is excluded\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/github-actions-reference-validation-2021.json>).

## Dates

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

- **published:** 2021-03-17; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** 2021-02-04; precision: day; basis: explicit
- **awarded:** 2021-03-03; precision: day; basis: explicit
- **fixed:** 2021-03-02; precision: day; basis: explicit. GitHub Enterprise Server 3\.0\.1 release; github\.com was fixed earlier in February, without an exact final timestamp in the source\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T14:39:00Z. Primary public source read; individual award and source provenance verified\. No target testing or exploit reproduction performed\.

- Award is reported by the cited source; cash settlement is not independently audited\.

## Related conceptual diagrams

- [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>)

## Sources and attribution

- [Stealing arbitrary GitHub Actions secrets](<https://blog.teddykatz.com/2021/03/17/github-actions-write-access.html>) — Teddy Katz; retrieved 2026-10-02T14:39:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
