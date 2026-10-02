# Sign in with Apple failed to bind identity claims to the authenticated user

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Apple  
**Product:** Sign in with Apple

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

The cited researcher documents a USD 100,000 award for this finding\.

### Root cause

Token issuance failed to maintain a trustworthy relationship between the authenticated identity and identity claims used by relying applications\. Cryptographic validity alone did not establish correct claim ownership\.

### Bounded impact

Potential takeover of third-party application accounts using the integration without additional safeguards\. Named third-party applications were not tested by the researcher\.

### Defensive lessons

- Validate identity-claim ownership in addition to token cryptographic validity\.
- Document relying-party assumptions and additional authentication safeguards\.

## Award and evidence

**USD 100,000** — bug\_bounty; single\_report; status: paid.

Evidence level: researcher\_reported. Researcher explicitly says they were paid; exact settlement date is not supplied\.

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

Reviewed: 2026-10-02T14:43:00Z. Primary public sources read; individual reward, dates, and attribution reviewed\. No target testing performed\.

- No exact report, fix, or payment date stated
- Researcher says Apple's investigation found no misuse; independent vendor payout confirmation was not retrieved

## Related conceptual diagrams

- [An identity claim must belong to the user](<../diagram-gallery.md#identity-claim-binding>)

## Sources and attribution

- [Sign in with Apple failed to bind identity claims to the authenticated user](<https://bhavukjain.com/blog/2020/05/30/zeroday-signin-with-apple/>) — Bhavuk Jain; retrieved 2026-10-02T14:43:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
