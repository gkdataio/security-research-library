# Facebook phone linking lacked account-specific authorization

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Meta \(Facebook\)  
**Product:** Facebook phone linking and account recovery

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

A 2013 researcher disclosure reports a $20,000 award for unauthorized recovery-phone binding\. Its enduring lesson for 2026 applications is that recovery-factor possession and account-change authority require separate checks\.

### Root cause

Phone possession and requester reauthentication did not establish permission to change the selected account\. The missing boundary was authorization over the account receiving a recovery factor\.

### Bounded impact

The researcher describes account takeover without victim interaction, requiring a researcher-controlled account and phone\. The demonstrated flow reached password recovery; broader account coverage is the researcher’s claim\.

### Defensive lessons

- Bind recovery-factor enrollment to the authenticated subject and authorized account\.
- Possession of a new factor cannot substitute for authority over the account it will recover\.

## Award and evidence

**USD 20,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. The researcher states an assigned award, not a settlement\. USD is a contextual inference from Facebook’s later official US-dollar program reporting in February 2020, nearly seven years after this disclosure; that source does not independently establish this award’s denomination or payment\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/facebook-phone-linking-account-authorization-2013.json>).

## Dates

- **published:** 2013-06-26; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** 2013-05-23; precision: day; basis: explicit
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** 2013-05-28; precision: day; basis: explicit
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T14:00:08Z. Read the original dated researcher article and its report-specific award statement\. Reviewed later official denomination context separately\.

- Exact award and payment dates are unknown; assigned does not establish paid\.
- Currency is inferred from later official program context, not explicit in the individual award statement\.
- Researcher reports the fix added account-specific permission validation; implementation and discovery history are not supplied\.

## Sources and attribution

- [Hijacking a Facebook Account with SMS](<https://whitton.io/articles/hijacking-a-facebook-account-with-sms/>) — Jack Whitton; retrieved 2026-10-03T14:00:08Z.
- [Facebook 2019 Bug Bounty retrospective, official Spanish edition](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook; retrieved 2026-10-03T14:00:08Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
