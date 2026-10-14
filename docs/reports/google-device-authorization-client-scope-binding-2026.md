# Google device grants lost client and permission binding

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

[Read the original source](<https://weirdmachine64.github.io/research/google-oauth-device-code-hijacking.html>) — weirdmachine64 · [Canonical JSON](<../../data/reports/google-device-authorization-client-scope-binding-2026.json>)

<a id="what-the-evidence-establishes"></a>
## Main takeaway

Google's device authorization flow did not consistently preserve the intended device, application and permissions through sign-in\. The researcher reports account and mailbox access; the reduced-interaction case required a signed-in user to open a link and have relevant prior consent\. The researcher reports a USD 13,337 award, but the evidence does not establish that every integration was affected\.

**Organization:** Google  
**Product:** Google OAuth device authorization

<a id="root-cause"></a>
## What went wrong

The account completing sign-in could authorize a different requesting device, and the grant did not preserve the intended client and permissions\. The researcher compared the initial approval with the authority of the final token\. Cross-device sign-in is expected behavior; the flaw was losing the link to the intended recipient and permissions\.

<a id="bounded-impact"></a>
## What the evidence shows

The author reports third-party account access, elevated permissions and mailbox access\. Reduced-interaction behavior required a signed-in user opening a link and relevant prior consent\. Universal reach, unrestricted persistence and uniform absence of alerts are not independently established\.

## Defensive lessons

- Editorial lesson: preserve one server-side authorization decision across device identity, client identity, subject and permitted actions; every completion path must respect it\.
- The researcher recommends server-side grant binding and explicit device confirmation\. These are proposed controls, not verified descriptions of the deployed fix\.

## Award and evidence

**USD 13,337** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. One chain award, counted once\. The researcher uses $\. USD is inferred from Google’s March 2017 program-wide denomination statement, about nine years before the April 2026 award\. That context does not independently establish this individual award’s currency or settlement; cash receipt is unverified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-device-authorization-client-scope-binding-2026.json>).

## Dates

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

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

## Related conceptual diagrams

- [Delegated authority stays within the approved grant](<../diagram-gallery.md#delegated-grant-authority-continuity>)

## Sources and attribution

- [Confused Deputy: Google IdP Universal Account Takeover via Device Code Flow Hijacking](<https://weirdmachine64.github.io/research/google-oauth-device-code-hijacking.html>) — weirdmachine64; retrieved 2026-10-03T17:39:29Z.
- [VRP news from Nullcon](<https://security.googleblog.com/2017/03/vrp-news-from-nullcon.html>) — Google Security Blog; retrieved 2026-10-03T17:39:29Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
