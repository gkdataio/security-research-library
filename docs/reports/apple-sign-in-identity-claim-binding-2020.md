# Sign in with Apple failed to bind identity claims to the authenticated user

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Apple  
**Product:** Sign in with Apple

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

Bhavuk Jain reports being paid $100,000 for this finding\. The recorded USD denomination is a contextual inference from Apple's May 2019 program documentation, published about one year before the May 2020 disclosure\.

### Root cause

Token issuance failed to maintain a trustworthy relationship between the authenticated identity and identity claims used by relying applications\. Cryptographic validity alone did not establish correct claim ownership\.

### Bounded impact

Potential takeover of third-party application accounts using the integration without additional safeguards\. Named third-party applications were not tested by the researcher\.

### Defensive lessons

- Validate identity-claim ownership in addition to token cryptographic validity\.
- Document relying-party assumptions and additional authentication safeguards\.

## Award and evidence

**USD 100,000** — bug\_bounty; single\_report; status: paid.

Evidence level: researcher\_reported. The researcher explicitly reports being paid $100,000 but supplies no currency code or exact settlement date\. USD is contextually inferred from Apple's May 2019 iOS Security guide \(currency-context\), whose Apple Security Bounty table on printed page 87 labels maximum payments in USD\. This source describes the then-existing iOS program and predates the May 2020 disclosure by about one year\. It supplies denomination context only and does not independently establish this individual payment's currency, amount, category or settlement\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/apple-sign-in-identity-claim-binding-2020.json>).

## Dates

- **published:** 2020-05-30; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-04T14:44:04Z. Primary researcher payment statement reread; Apple's May 2019 iOS Security guide reviewed for earlier program-level denomination context only\. Individual payment attribution remains researcher-reported\. No target testing performed\.

- No exact report, fix, or payment date stated
- Researcher says Apple's investigation found no misuse; independent vendor payout confirmation was not retrieved
- USD is inferred from earlier program-level context, not explicitly stated in the individual payment report\. The May 2019 guide does not establish the payment's category or the program wording at payment time\. No conflicting denomination was identified in the reviewed sources\.

## Related conceptual diagrams

- [An identity claim must belong to the user](<../diagram-gallery.md#identity-claim-binding>)

## Sources and attribution

- [Sign in with Apple failed to bind identity claims to the authenticated user](<https://bhavukjain.com/blog/2020/05/30/zeroday-signin-with-apple/>) — Bhavuk Jain; retrieved 2026-10-04T14:42:20Z.
- [iOS Security, iOS 12\.3, May 2019, printed page 87: denomination context only](<https://www.apple.com/jp/business/site/docs/site/iOS_Security_Guide.pdf>) — Apple; retrieved 2026-10-04T14:42:30Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
