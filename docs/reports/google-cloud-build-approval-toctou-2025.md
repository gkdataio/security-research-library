# Cloud Build approval was not bound to immutable code

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Google Cloud Build GitHub integration

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

A researcher-reported USD 30,000 award illustrates a gap between approval of a contribution and selection of the code executed\.

### Root cause

The researcher compared the identity available to the approval event with the revision later selected by the build\. Approval referred to mutable contribution state without preserving the exact reviewed version\. The execution boundary therefore relied on an assumption that the approved and executed content remained identical\.

### Bounded impact

The controlled demonstration executed a newer, unreviewed revision\. Access to secrets or cloud resources was a potential consequence of the build’s assigned privileges, not evidence that all pipelines exposed those assets\.

### Defensive lessons

- Bind approval and execution to immutable content identities, with explicit confirmation when the intended revision is ambiguous\.
- The researcher’s fix analysis describes check-to-commit binding and explicit commit selection; it does not establish a universal patch recipe\.
- Limit build identity privileges and secret availability independently of human approval\.

## Award and evidence

**USD 30,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. Older reference: public write-up predates the preferred 12-month window; original report was in 2024\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-cloud-build-approval-toctou-2025.json>).

## Dates

- **published:** 2025-07-21; precision: day; basis: explicit
- **public disclosure:** 2025-07-21; precision: day; basis: explicit. Publication of this write-up; earliest disclosure elsewhere was not independently established\.
- **reported:** 2024-11-13; precision: day; basis: explicit
- **awarded:** 2025-01-28; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported. The researcher says Google marked the issue fixed on June 18, 2025\. The exact deployment date is not established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported. Cash settlement date not independently established\.
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T20:00:00Z. Re-read the approval model, observed build result, fix analysis and timeline; separated demonstrated behavior, conditional consequences and vendor fix-status confirmation\.

- Researcher-reported award; cash settlement was not independently audited\.
- The June 18, 2025 status change confirms the issue was marked fixed, not the exact deployment date\.
- The public account’s broader security consequences depend on pipeline permissions; no universal secret exposure is established\.

## Related conceptual diagrams

- [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>)

## Sources and attribution

- [Who's SHA is it Anyway: Bypassing Google Cloud Build Comment Control for $30,000](<https://adnanthekhan.com/posts/cloud-build-toctou/>) — Adnan Khan; retrieved 2026-10-02T20:00:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
