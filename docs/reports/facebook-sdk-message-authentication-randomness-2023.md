# Facebook SDK message authentication relied on insecure randomness

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Meta  
**Product:** Facebook JavaScript SDK and mobile application web content

## What the evidence establishes

Publication window: uncertain original publication date; reviewed as of 2026-10-02.

A USD 66,000 researcher-reported award illustrates how weak message authentication and unsafe rendering can invalidate an SDK trust boundary\.

### Root cause

The researcher followed messages from an embedded plugin into SDK handlers and examined their authority checks\. A callback identifier was treated as an authentication secret despite coming from non-cryptographic randomness\. Separately, a handler interpreted supplied content as active HTML\. An origin check alone did not establish that the message content was authorized or safe to render\.

### Bounded impact

The researcher reports script execution and Facebook account takeover under mobile in-app browser conditions\. Impact on an arbitrary embedding site depended on its framing controls\. The article does not establish that every website using the SDK was affected equally\.

### Defensive lessons

- Use cryptographic randomness and context binding for values that authorize message handling\.
- Validate the sender, expected message relationship and permitted operation independently of rendering safety\.
- Keep externally supplied content inert and review embedded-browser permissions as a separate trust boundary\.
- Treat these as defensive design recommendations; the source dates a fix but does not establish the precise vendor patch implementation\.

## Award and evidence

**USD 66,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. One researcher-reported bug bounty, not an event total\. The article uses $; prior official Meta program reporting supplies USD context\. Actual cash settlement is not established\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/facebook-sdk-message-authentication-randomness-2023.json>).

## Dates

- **published:** Unknown; precision: unknown; basis: not\_reported. Current archive page displays 2026-01-17\. Original publication versus migration/republication is not established, so this date is not used as a recent disclosure\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported. Earliest public disclosure remains unverified; the current archive header does not resolve it\.
- **reported:** 2023-06-22; precision: day; basis: explicit
- **awarded:** 2023-06-28; precision: day; basis: explicit
- **fixed:** 2023-12-15; precision: day; basis: explicit. Researcher timeline explicitly labels this as the vendor fix date\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T19:21:00Z. Re-read the SDK introduction, trust checks, randomness analysis, bounded impact and timeline\. Expanded conceptual reasoning without adding reproduction instructions\. Original publication remains unknown\.

- Researcher-reported award; no independent vendor confirmation or audited transfer\.
- January 2026 page dates may reflect publication or archive migration; original disclosure is not established\.
- USD normalization uses earlier official program context rather than an award receipt\.

## Related conceptual diagrams

- [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>)

## Sources and attribution

- [Account Takeover in Facebook mobile app due to usage of cryptographically unsecure random number generator and XSS in Facebook JS SDK](<https://ysamm.com/uncategorized/2026/01/17/math-random-facebook-sdk.html>) — Youssef Sammouda; retrieved 2026-10-02T19:21:00Z.
- [Facebook Bug Bounty and BountyCon US-dollar reporting](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook; retrieved 2026-10-02T18:24:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
