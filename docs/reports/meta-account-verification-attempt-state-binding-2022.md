# Meta account verification weakened linked SMS authentication state

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Meta  
**Product:** Meta Accounts Center, Instagram and Facebook SMS verification

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

Meta confirms a USD 27,200 total award for this account-verification report\.

### Root cause

Insufficient verification-attempt limits undermined phone ownership checks, while linked-account state changes could affect an existing SMS authentication factor\.

### Bounded impact

The vendor confirms possible SMS-based two-factor authentication bypass\. The researcher demonstrated factor revocation; this alone does not establish password disclosure or an authenticated session\.

### Defensive lessons

- Enforce verification-attempt limits consistently across linked applications\.
- Require verified ownership before changing another account’s recovery or second-factor state\.

## Award and evidence

**USD 27,200** — bug\_bounty; single\_report; status: awarded.

Evidence level: vendor\_confirmed. Vendor total for one report\. Researcher describes an initial September award and a December adjustment; component amounts are unknown and are not added on top\. USD is contextualized by earlier official program reporting; settlement is unverified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/meta-account-verification-attempt-state-binding-2022.json>).

## Dates

- **published:** 2023-01-20; precision: day; basis: explicit. Primary technical article date; distinct from the earlier vendor summary\.
- **public disclosure:** 2022-12-15; precision: day; basis: explicit. Vendor’s high-level public summary\. Researcher confirms this same-day highlight; a 2024 update concerns another case\.
- **reported:** 2022-09-14; precision: day; basis: explicit
- **awarded:** 2022-12-15; precision: day; basis: explicit. Final additional award; initial amount was awarded September 24, 2022\.
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Researcher received fix confirmation October 17, 2022; exact deployment date is not established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** 2022-12-15; precision: day; basis: explicit
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T19:03:00Z. Matched the researcher’s explicit vendor-retrospective link, name and account-verification issue to Meta’s per-report award\. Retained final reward adjustment separately from cash settlement and fix confirmation\.

- Exact reward-component amounts and cash-transfer date are unknown\.
- Fix-confirmation date does not prove an exact deployment date\.
- USD notation uses earlier official program context\.

## Sources and attribution

- [Two Factor Authentication Bypass On Facebook](<https://medium.com/pentesternepal/two-factor-authentication-bypass-on-facebook-3f4ac3ea139c>) — Gtm Mänôz; retrieved 2026-10-02T19:03:00Z.
- [Looking Back at Our Bug Bounty Program in 2022](<https://about.fb.com/news/2022/12/metas-bug-bounty-program-2022/>) — Neta Oren / Meta; retrieved 2026-10-02T19:03:00Z.
- [Facebook Bug Bounty and BountyCon US-dollar reporting](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook; retrieved 2026-10-02T18:24:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
