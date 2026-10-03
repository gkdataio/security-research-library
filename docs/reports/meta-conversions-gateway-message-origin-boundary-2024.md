# Meta Conversions API Gateway trusted message origins as script authority

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Meta  
**Product:** Conversions API Gateway

## What the evidence establishes

Publication window: uncertain original publication date; reviewed as of 2026-10-03.

The researcher assigns a separate $62,500 award to the client-side finding labeled Bug \#1\.

### Root cause

A browser message origin became trusted script-host configuration without origin authorization\.

### Bounded impact

The researcher reports script execution and describes possible account takeover\. The scenario depends on specific embedded-browser, initialization and content-policy conditions plus influence over permitted third-party content\. Account impact additionally assumes user interaction and an authenticated session; universal or interaction-free exploitation is not established\.

### Defensive lessons

- Authorize message origins and senders independently of message content; treat an integration identifier as data rather than proof of authority\.
- Keep script-source authority separate from mutable messaging configuration, and review it together with browser isolation and content policy\.
- Define regression coverage for initialization state, embedded-browser behavior and third-party trust; distinguish observed execution from modeled account impact\.

## Award and evidence

**USD 62,500** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. Separate from Bug \#2; no aggregation\. The dollar sign is interpreted as USD using official 2020 program context, nearly five years earlier\. This does not establish individual settlement currency or payment\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/meta-conversions-gateway-message-origin-boundary-2024.json>).

## Dates

- **published:** Unknown; precision: unknown; basis: not\_reported. Current header: January 13, 2026\. Original publication is unestablished; archive dating cannot establish first disclosure\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported. Earliest public disclosure is not established\.
- **reported:** 2024-11-24; precision: day; basis: explicit. Explicit Timeline entry labeled Bug \#1\.
- **awarded:** 2024-12-24; precision: day; basis: explicit. Explicit Timeline entry labeled Bug \#1\.
- **fixed:** 2024-12-11; precision: day; basis: explicit. Explicit Timeline entry labeled Bug \#1\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T12:49:20Z. Freshly read the primary article and official denomination context; compared report boundaries against the existing backend record\. No live testing\.

- Researcher-reported award, not vendor-confirmed payment; settlement date remains unknown\.
- USD is contextual inference with an almost five-year gap, not an individual receipt\.
- Original publication and earliest disclosure remain unknown\.
- The narrative puts Bug \#2 after reporting Bug \#1; the labeled timeline orders reports oppositely\. Dates follow labels without reconciling the conflict\.
- Execution is researcher-reported; completed account takeover, population-wide exposure and exact patch coverage are not independently established\.
- The article-wide zero-click framing should not be generalized to this interaction-dependent finding\.

## Sources and attribution

- [Multiple XSS in Meta Conversion API Gateway Leading to Zero-Click Account Takeover](<https://ysamm.com/uncategorized/2026/01/13/capig-xss.html>) — Youssef Sammouda; retrieved 2026-10-03T12:49:20Z.
- [Facebook Bug Bounty and BountyCon US-dollar reporting](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook; retrieved 2026-10-03T12:49:20Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
