# GitHub OAuth consent failed across request-method semantics

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** GitHub  
**Product:** GitHub OAuth authorization

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

A researcher-reported $25,000 award illustrates how differing framework and controller assumptions can remove an OAuth consent boundary; USD denomination is contextually inferred from non-contemporaneous official program evidence\.

### Root cause

The researcher compared the consent screen’s intended state change with routing and controller logic\. The framework accepted a wider set of request semantics than the controller expected\. Application logic treated the unexpected case as permission to grant access, even though the usual consent safeguards did not apply\. The failed invariant was that every new grant required the user’s explicit, validated approval\.

### Bounded impact

The researcher reports that a user visiting a malicious website could unintentionally grant an application access to read or modify private GitHub data\. This demonstrates unauthorized delegated access, rather than evidence that the attacker learned the account password or that all unrelated account controls failed\.

### Defensive lessons

- Require positive validation of the intended state-changing operation; reject unrecognized alternatives rather than defaulting to a privileged action\.
- Model framework routing, request interpretation and consent enforcement as separate layers whose assumptions must agree\.
- Verify that consent and request-integrity checks remain attached to every path that creates a grant\.
- The source dates the production fix and later Enterprise releases, but does not document the exact patch here; these lessons are defensive recommendations\.

## Award and evidence

**USD 25,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. Individual report; production fix date is for github\.com, with enterprise releases following June 26\. The researcher uses $ without an explicit currency\. USD is a contextual inference from github-currency-context-2017: GitHub's January 9, 2017 program article, updated June 25, 2021, explicitly names USD\. Its publication predates the June 26, 2019 award and its displayed update postdates it; this is non-contemporaneous program-wide context, not proof of this individual award's currency or settlement\. No conflicting denomination was found in the reviewed sources\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/github-oauth-method-semantics-2019.json>).

## Dates

- **published:** 2019-11-05; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** 2019-06-19; precision: day; basis: explicit
- **awarded:** 2019-06-26; precision: day; basis: explicit
- **fixed:** 2019-06-20; precision: day; basis: explicit
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-05T20:41:30Z. Re-read the researcher's award statement and timeline, and GitHub's official program article for denomination context\. Kept primary as the amount and award-date evidence; used github-currency-context-2017 only for qualified USD inference, with its publication and update dates distinguished from the 2019 award\. No target interaction or exploit reproduction\.

- Researcher-reported award; cash settlement is not independently audited\.
- The reported impact requires user interaction\. Exact vendor patch implementation and evidence of real-world abuse are not supplied\.
- USD is inferred from a program-wide article published in 2017 and updated in 2021, not contemporaneous individual-award evidence from 2019\. The reviewed sources do not independently establish this award's denomination or cash settlement; payment date remains unknown\.

## Related conceptual diagrams

- [An identity claim must belong to the user](<../diagram-gallery.md#identity-claim-binding>)

## Sources and attribution

- [Bypassing GitHub’s OAuth flow](<https://blog.teddykatz.com/2019/11/05/github-oauth-bypass.html>) — Teddy Katz; retrieved 2026-10-05T20:39:26Z.
- [Bug Bounty anniversary promotion: bigger bounties in January and February](<https://github.blog/news-insights/company-news/bug-bounty-anniversary-promotion-bigger-bounties-in-january-and-february/>) — Neil Matatall; retrieved 2026-10-05T20:39:26Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
