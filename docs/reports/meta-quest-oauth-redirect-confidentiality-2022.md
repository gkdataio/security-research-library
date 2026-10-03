# Meta Quest login migration lost OAuth credential confinement

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Meta  
**Product:** Meta Quest / Oculus account login

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

Meta confirms a USD 44,250 total award, including bonuses, for this Quest OAuth account-access report\.

### Root cause

The researcher compared login behavior across an identity-system migration\. A previously permitted OAuth return destination began forwarding credentials through a changed redirect flow, losing an earlier containment control\. Trust in the initial destination did not establish that the eventual recipient was authorized to receive the credential\.

### Bounded impact

The researcher reports exposure of a privileged first-party credential with account-access implications\. Meta confirms possible account takeover requiring user interaction and says its investigation found no abuse\. Those statements do not establish that customer accounts were actually compromised\.

### Defensive lessons

- Reassess credential handling and destination trust whenever an identity provider or login flow changes\.
- Preserve authorization checks through the full return flow; an initially permitted destination is not a guarantee about later recipients\.
- Treat recommendations here as defensive design principles, not a reconstruction of the vendor’s undisclosed patch\.

## Award and evidence

**USD 44,250** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. Vendor-confirmed total attached to one report\. Researcher identifies BountyCon and Highest Impact Report bonuses but gives no component allocation; they are not added again\. USD uses earlier official program context\. Award confirmation does not establish cash settlement\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/meta-quest-oauth-redirect-confidentiality-2022.json>).

## Dates

- **published:** 2023-01-29; precision: day; basis: explicit. Article date also appears in the researcher’s archive index; historical publication, not the archive’s separate January 2026 entries\.
- **public disclosure:** 2022-12-15; precision: day; basis: explicit. Dated vendor summary precedes the technical article\. The page’s December 2024 update explicitly concerns another report\.
- **reported:** 2022-08-27; precision: day; basis: explicit
- **awarded:** 2022-09-25; precision: day; basis: explicit. Researcher’s dated total including bonuses; exact funds-transfer date is not established\.
- **fixed:** 2022-09-25; precision: day; basis: explicit. Researcher labels this as the Meta fix date\. The article withholds details of a separate redirect component that it says was not fully fixed; this is not a claim that every component was remediated that day\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2022-12-15; precision: day; basis: explicit
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T19:39:00Z. Matched the researcher, Quest/Oculus OAuth issue and identical report-specific total across the researcher timeline and Meta retrospective\. Summarized the migration-related trust failure without reproducing the operational flow\.

- Bonus components are not individually quantified; the documented total is counted once\.
- The technical article says an associated redirect detail was withheld because it was not fully fixed at publication\. No current vulnerability or exact patch implementation is inferred\.
- The vendor reports no evidence of abuse; this is not proof that abuse was impossible\.
- Cash settlement is unverified; USD denomination uses earlier official program context\.

## Sources and attribution

- [Account takeover of Facebook/Oculus accounts due to First-Party access\_token stealing](<https://ysamm.com/uncategorized/2023/01/29/account-takeover-of-facebook-oculus-accounts-due-to-first-party-access_token-stealing.html>) — Youssef Sammouda; retrieved 2026-10-02T19:39:00Z.
- [Looking Back at Our Bug Bounty Program in 2022](<https://about.fb.com/news/2022/12/metas-bug-bounty-program-2022/>) — Neta Oren / Meta; retrieved 2026-10-02T19:39:00Z.
- [Facebook Bug Bounty and BountyCon US-dollar reporting](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook; retrieved 2026-10-02T18:24:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
