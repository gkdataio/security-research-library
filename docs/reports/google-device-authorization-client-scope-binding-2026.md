# Google device grants lost client and permission binding

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Google OAuth device authorization

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

A researcher reports USD 13,337 for a device-grant authorization-boundary failure\.

### Root cause

The account completing authentication could authorize a different requesting device, while client identity and permissions were not preserved through the grant\. The researcher reasoned about consistency between initial authorization and final token authority\. Cross-device sign-in alone is expected behavior; the reported failure was loss of the intended recipient and permission binding\.

### Bounded impact

The author reports third-party account access, elevated permissions and mailbox access\. Reduced-interaction behavior required a signed-in user opening a link and relevant prior consent\. Universal reach, unrestricted persistence and uniform absence of alerts are not independently established\.

### Defensive lessons

- Editorial lesson: preserve one server-side authorization decision across device identity, client identity, subject and permitted actions; every completion path must respect it\.
- The researcher recommends server-side grant binding and explicit device confirmation\. These are proposed controls, not verified descriptions of the deployed fix\.

## Award and evidence

**USD 13,337** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. One chain award, counted once\. The researcher uses $\. USD is inferred from Google’s March 2017 program-wide denomination statement, about nine years before the April 2026 award\. That context does not independently establish this individual award’s currency or settlement; cash receipt is unverified\.

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

Reviewed: 2026-10-03T17:39:29Z. Fresh-read the primary narrative and award timeline with the older vendor currency context; explicitly qualified the temporal gap and inference\. No testing\.

- No independently reviewed vendor evidence establishes technical reach, award or settlement\.
- The March 28, 2026 marked-fixed status does not establish deployment timing or patch contents\.
- Specific client permissions, existing consent and downstream token acceptance constrain the reported impact; one broad title does not prove every integration was affected\.

## Sources and attribution

- [Confused Deputy: Google IdP Universal Account Takeover via Device Code Flow Hijacking](<https://weirdmachine64.github.io/research/google-oauth-device-code-hijacking.html>) — weirdmachine64; retrieved 2026-10-03T17:39:29Z.
- [VRP news from Nullcon](<https://security.googleblog.com/2017/03/vrp-news-from-nullcon.html>) — Google Security Blog; retrieved 2026-10-03T17:39:29Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
