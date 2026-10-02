# Google device grants lost client and permission binding

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Google OAuth device authorization

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-02.

The researcher reports a USD 13,337 award for one device-authorization chain\.

### Root cause

Sign-in state and the grant’s client identity and permissions were not consistently bound throughout authorization\.

### Bounded impact

The author reports unauthorized downstream account access and broader data permissions\. Universal-impact claims are not independently verified\.

### Defensive lessons

- Preserve the original client, subject and permission binding throughout a grant’s lifecycle\.
- Require meaningful device confirmation and accurate authorization audit records\.

## Award and evidence

**USD 13,337** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. One chain award, counted once\. The source uses $; USD follows official program currency context, not a reward-table inference\. Cash receipt is unverified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-device-authorization-client-scope-binding-2026.json>).

## Dates

- **published:** 2026-07-15; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** 2026-02-25; precision: day; basis: explicit
- **awarded:** 2026-04-02; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Researcher records marked-fixed status on March 28, 2026; deployment date is not independently established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T17:03:00Z. Read the full primary disclosure and award timeline; checked USD program context and existing-record identity\.

- No independent vendor-hosted confirmation of the individual award or reported reach was retrieved\.
- The issue-status date does not establish the deployment date\.
- No bank settlement or exact public disclosure earlier than the article is verified\.

## Sources and attribution

- [Confused Deputy: Google IdP Universal Account Takeover via Device Code Flow Hijacking](<https://weirdmachine64.github.io/research/google-oauth-device-code-hijacking.html>) — weirdmachine64; retrieved 2026-10-02T17:03:00Z.
- [VRP news from Nullcon](<https://security.googleblog.com/2017/03/vrp-news-from-nullcon.html>) — Google Security Blog; retrieved 2026-10-02T17:03:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
