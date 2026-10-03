# LiteSpeed Cache privileged user simulation relied on weak security tokens

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** LiteSpeed Technologies  
**Product:** LiteSpeed Cache WordPress plugin

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

Patchstack confirmed a USD 14,400 Zero Day award for an authentication-boundary flaw\.

### Root cause

Privileged user simulation relied on a predictable, reusable token without adequate context binding\.

### Bounded impact

Unauthenticated users could obtain administrator privileges on affected installations\. The advisory identifies an operating-system limitation, so plugin installation totals do not establish affected-site counts\.

### Defensive lessons

- Use cryptographically secure token generation, explicit authorization, context binding and limited lifetimes\.
- Treat impersonation and user-simulation features as privileged authentication boundaries\.

## Award and evidence

**USD 14,400** — bug\_bounty; single\_vulnerability; status: awarded.

Evidence level: platform\_confirmed. Records the explicitly isolated Zero Day component\. Later platform sources report USD 16,400 paid for this single finding; the USD 2,000 difference is not apportioned or counted separately\. The researcher acknowledges receiving payment; exact component settlement dates are unknown\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/litespeed-cache-user-simulation-authentication-2024.json>).

## Dates

- **published:** 2024-08-21; precision: day; basis: explicit
- **public disclosure:** 2024-08-19; precision: day; basis: explicit. Initial platform vulnerability-database publication preceded the full advisory\.
- **reported:** 2024-08-01; precision: day; basis: explicit. Report received by Patchstack; vendor contacted August 5\.
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** 2024-08-13; precision: day; basis: explicit. Release of version 6\.4\.
- **paid:** Unknown; precision: unknown; basis: not\_reported. Payment acknowledged in September 6, 2024 interview, without a settlement date\.
- **award announced:** 2024-08-21; precision: day; basis: explicit. Direct award amount stated in the advisory; earliest announcement not independently established\.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T16:42:07Z. Read platform advisory, coordinated timeline, researcher interview and later platform retrospective\.

- Exact award and payment dates are absent\. The recorded component is not the later reported total\.
- The advisory describes Windows-specific limitations\.
- The disclosed patch added token checks and lifetime controls; the researcher’s recommended random-generator improvement was deferred for compatibility\.

## Sources and attribution

- [LiteSpeed Cache CVE-2024-28000 coordinated advisory](<https://patchstack.com/articles/critical-privilege-escalation-in-litespeed-cache-plugin-affecting-5-million-sites/>) — Rafie Muhammad / Patchstack; retrieved 2026-10-02T16:42:07Z.
- [Interview with John Blackbourn](<https://patchstack.com/articles/interview-with-john-blackbourn/>) — Maciek Palmowski / Patchstack; retrieved 2026-10-02T16:42:07Z.
- [State of WordPress Security 2025](<https://patchstack.com/whitepaper/state-of-wordpress-security-in-2025/>) — Patchstack; retrieved 2026-10-02T16:42:07Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
