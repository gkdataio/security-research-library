# Instagram embedding fallback changed the authorization context

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Meta  
**Product:** Instagram media embedding

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

The researcher documents USD 14,500 for one report: a 10,000 base bounty and two event bonuses\.

### Root cause

A client-specific error path retrieved media under an elevated service identity, losing the original requester’s privacy constraints\.

### Bounded impact

Private post text and media could be exposed\. The researcher did not establish the same effect for profile embedding\.

### Defensive lessons

- Preserve requester authorization across error handling and fallback paths\.
- Keep policy decisions consistent across client-specific code paths\.
- Distinguish demonstrated data exposure from unverified adjacent features\.

## Award and evidence

**USD 14,500** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. One report: 10,000 base plus 2,000 and 2,500 bonuses\. Classified as a bug bounty with event bonuses, not a separate placement prize\. The article uses $; USD is contextualized by Facebook’s official program and BountyCon reporting, which predates this award\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/instagram-embedding-privileged-fallback-2023.json>).

## Dates

- **published:** 2023-10-12; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported. This article is dated October 12, 2023\. November 9, 2022 is permission to disclose, not proof of public publication\.
- **reported:** 2022-09-20; precision: day; basis: explicit
- **awarded:** 2022-09-25; precision: day; basis: explicit. All three report-linked reward components share this timeline date\.
- **fixed:** Unknown; precision: unknown; basis: not\_reported. The article says the issue was fixed, without an exact deployment date\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T18:24:00Z. Read researcher timeline, bounded impact and attributed vendor explanation\. Summed only the three reward components explicitly attached to this report; used official program context for USD notation\.

- Researcher-reported award, not independent vendor confirmation or audited settlement\.
- Currency context comes from an earlier official program retrospective, not a reproduced award receipt\.
- The account-restriction root cause is the researcher’s account of vendor clarification\.

## Sources and attribution

- [How I Exposed Instagram's Private Posts by Blocking Users](<https://003random.com/posts/meta-bountycon-instagram-writeup/>) — 003random; retrieved 2026-10-02T18:24:00Z.
- [Facebook Bug Bounty and BountyCon US-dollar reporting](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook; retrieved 2026-10-02T18:24:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
