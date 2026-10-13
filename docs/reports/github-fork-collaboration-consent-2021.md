# GitHub GraphQL collaboration changes lacked author consent

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

[Read the original source](<https://blog.teddykatz.com/2021/03/10/fork-collab-abuse.html>) — Teddy Katz · [Canonical JSON](<../../data/reports/github-fork-collaboration-consent-2021.json>)

<a id="what-the-evidence-establishes"></a>
## Main takeaway

One GitHub API allowed collaboration consent to change without the pull-request author's permission\. A base-repository maintainer could consequently gain unauthorized write access to a contributor's branch\. This second finding received its own researcher-reported USD 10,000 award\.

**Organization:** GitHub  
**Product:** GitHub fork collaboration / GraphQL

<a id="root-cause"></a>
## What went wrong

One API path omitted the pull-request-author entitlement required to change collaboration consent\.

<a id="bounded-impact"></a>
## What the evidence shows

A base-repository maintainer could gain unauthorized write access to a contributor branch\.

## Defensive lessons

- Keep collaboration consent separate from ordinary metadata privileges\.
- Enforce identical ownership rules across API implementations\.

## Award and evidence

**USD 10,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. Separate report and award, initially marked duplicate then reopened after its distinct fix requirement was confirmed\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/github-fork-collaboration-consent-2021.json>).

## Dates

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

- **published:** 2021-03-10; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** 2021-01-24; precision: day; basis: explicit
- **awarded:** 2021-03-02; precision: day; basis: explicit
- **fixed:** 2021-01-28; precision: day; basis: explicit. github\.com deployment; Enterprise Server releases followed March 2, 2021\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T15:12:00Z. Primary public source read; individual award and source provenance verified\. No target testing or exploit reproduction performed\.

- Award remains researcher-reported; vendor release notes corroborate the distinct CVE and remediation\.

## Sources and attribution

- [Messing with GitHub’s fork collaboration for fun and profit](<https://blog.teddykatz.com/2021/03/10/fork-collab-abuse.html>) — Teddy Katz; retrieved 2026-10-02T15:12:00Z.
- [GitHub Enterprise Server 3\.0\.1 security fixes](<https://docs.github.com/en/enterprise-server@3.0/admin/release-notes>) — GitHub; retrieved 2026-10-02T15:12:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
