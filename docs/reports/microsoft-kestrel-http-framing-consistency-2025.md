# Kestrel HTTP framing differed across proxy and application boundaries

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Microsoft  
**Product:** ASP\.NET Core / Kestrel

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

A Kestrel request-framing report earned a researcher-reported USD 10,000 award\.

### Root cause

Permissive HTTP framing validation could disagree with an upstream parser about message boundaries\.

### Bounded impact

Security controls could be bypassed in affected deployments\. Consequences depended on the complete proxy/application architecture, not merely the presence of Kestrel\.

### Defensive lessons

- Define consistent message-boundary contracts across intermediaries and application servers; reject ambiguous framing\.
- Verify deployed runtimes and self-contained applications receive the applicable vendor updates\.

## Award and evidence

**USD 10,000** — bug\_bounty; single\_vulnerability; status: awarded.

Evidence level: researcher\_reported. Exact award comes from the researcher\. The July 31, 2025 official program announcement supplies USD context only; its later award-table changes do not establish this amount\. Payment completion is unverified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/microsoft-kestrel-http-framing-consistency-2025.json>).

## Dates

- **published:** 2025-11-07; precision: day; basis: explicit. Detailed article date; vendor disclosure preceded it\.
- **public disclosure:** 2025-10-14; precision: day; basis: explicit
- **reported:** 2025-06-22; precision: day; basis: explicit
- **awarded:** 2025-07-21; precision: day; basis: explicit
- **fixed:** 2025-10-14; precision: day; basis: explicit. Public patch release; vendor advisory independently identifies patched versions\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported. First public award-announcement date is not established\.
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T16:21:00Z. Read the primary researcher article and timeline, vendor advisory and July 2025 official USD-denominated program announcement\.

- The award and its date are researcher-reported, not independently vendor-confirmed\.
- Impact varies with deployment architecture; generic consequences are not evidence of actual victim compromise\.
- Dollar notation is interpreted through official program currency context; no conversion is used\.

## Sources and attribution

- [ASP\.NET Core CVE-2025-55315 disclosure and award timeline](<https://www.praetorian.com/blog/how-i-found-the-worst-asp-net-vulnerability-a-10k-bug-cve-2025-55315/>) — Siddhant Kalgutkar / Praetorian; retrieved 2026-10-02T16:20:00Z.
- [Microsoft Security Advisory CVE-2025-55315](<https://github.com/dotnet/aspnetcore/security/advisories/GHSA-5rrx-jjjq-q2r5>) — Microsoft \.NET security team; retrieved 2026-10-02T16:20:00Z.
- [\.NET Bounty Program update, July 31, 2025](<https://www.microsoft.com/en-us/msrc/blog/2025/07/net-bounty-program-now-offers-up-to-40000-in-awards>) — Madeline Eckert and Barry Dorrans / Microsoft; retrieved 2026-10-02T16:21:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
