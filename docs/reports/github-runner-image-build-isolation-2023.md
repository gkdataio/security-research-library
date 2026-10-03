# GitHub runner-image builds shared persistent infrastructure with untrusted workflows

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** GitHub  
**Product:** GitHub Actions runner-image build infrastructure

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

An isolation misconfiguration exposed runner-image build infrastructure; the researcher reports a $20,000 payment\.

### Root cause

Contributor status was treated as sufficient trust for workflows using persistent self-hosted infrastructure\. The researcher connected approval policy, runner reuse and privileged build context to identify a boundary failure between outside contributions and trusted image production\.

### Bounded impact

With contributor access under the affected configuration, the researcher demonstrated infrastructure access and build-secret exposure\. Downstream compromise of distributed runner images remained a modeled consequence: intervening production controls were unknown\.

### Defensive lessons

- Separate untrusted contribution processing from privileged build infrastructure and secrets\.
- Bind review to the workflow being executed; prior contribution history is not continuing authorization\.
- Use isolated disposable execution environments and independently verify release provenance\.

## Award and evidence

**USD 20,000** — bug\_bounty; single\_report; status: paid.

Evidence level: researcher\_reported. One report\. GitHub’s official January 2017 article \(updated June 2021\) explicitly denominates standard bounties in USD; current platform guidelines corroborate context, not this individual award\. Earlier researcher post explicitly says paid\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/github-runner-image-build-isolation-2023.json>).

## Dates

- **published:** 2023-12-20; precision: day; basis: explicit. Detailed article date\.
- **public disclosure:** 2023-12-16; precision: day; basis: explicit. Earlier public summary; not the detailed article date\.
- **reported:** 2023-07-22; precision: day; basis: explicit
- **awarded:** 2023-11-14; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** 2023-11-14; precision: day; basis: explicit
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** 2023-07-25; precision: day; basis: explicit. Detailed timeline: initial mitigations\. Earlier summary says immediate fixes July 26; final technical fix date remains unknown\.

## Verification limits

Reviewed: 2026-10-02T23:05:44Z. Read primary public disclosures and corroborating sources; checked individual award scope\. No target interaction or exploit reproduction\.

- Payment is researcher-reported, not independently audited\.
- The reviewed HackerOne currency guideline is the current page, not a preserved 2023 policy snapshot\.
- Resolution on November 14 does not establish an exact final remediation date\.

## Sources and attribution

- [One Supply Chain Attack to Rule Them All - Poisoning GitHub's Runner Images](<https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/>) — Adnan Khan; retrieved 2026-10-02T23:01:00Z.
- [Welcome to my blog - there is more to come\!](<https://adnanthekhan.com/2023/12/16/welcome-to-my-blog-there-is-more-to-come/>) — Adnan Khan; retrieved 2026-10-02T23:01:00Z.
- [Vulnerability Disclosure Guidelines](<https://www.hackerone.com/terms/disclosure-guidelines>) — HackerOne; retrieved 2026-10-02T23:01:00Z.
- [Bug bounty anniversary promotion: Bigger bounties in January and February](<https://github.blog/news-insights/company-news/bug-bounty-anniversary-promotion-bigger-bounties-in-january-and-february/>) — Neil Matatall / GitHub; retrieved 2026-10-02T23:05:17Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
