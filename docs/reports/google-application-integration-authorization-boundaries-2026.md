# Google Application Integration mixed resource and service authority

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Google Cloud Application Integration

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

A researcher reports a $75,000 base award for a distinct Application Integration report\.

### Root cause

Resource-ownership checks and task-authority checks were inconsistent\. The researcher compared customer-project permissions with the authority of backend integration services, identifying gaps between authorized customer activity and privileged service operations\.

### Bounded impact

The authenticated-user research reports cross-project access and test execution\. Production compromise potential was reportedly confirmed by Google, which stopped further testing; completed code execution in production was not demonstrated\. Wider impact remains unverified\.

### Defensive lessons

- Editorial lesson: authorize the actual resource owner at every service boundary rather than relying on an enclosing project context\.
- Editorial lesson: independently constrain service-task authority even when the initiating user may legitimately configure an integration\.
- Editorial lesson: use cross-tenant negative tests and track observed effects separately from vendor-assessed potential\.

## Award and evidence

**USD 75,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. Only the second report’s base award; excludes the later $13,337 and first report\. USD remains contextual: Google’s July 2024 USD-denominated VRP announcement and October 2024 Cloud-program continuity statement, not settlement evidence\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-application-integration-authorization-boundaries-2026.json>).

## Dates

- **published:** 2026-05-22; precision: day; basis: explicit. Visible article header supplies May 22, 2026 and author Arvin Shivram\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** 2026-03-21; precision: day; basis: explicit
- **awarded:** 2026-04-28; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T02:35:33Z. Read primary article text, including the dated byline, and official Google sources\. The July 2024 USD announcement was read in rendered browser text\. No target testing\.

- Award and vendor impact assessment are researcher-published claims, not independently reviewed vendor correspondence\.
- The article-level CVE is not assigned here because its scope across the separate reports is ambiguous\.
- No precise fix date, payment occurrence or settlement date is established\.
- Currency inference uses 2024 program context, about two years before the award\. The current Cloud policy uses a dollar symbol without an explicit USD statement; no independent settlement evidence is claimed\.

## Sources and attribution

- [StubZero: $148,337 RCE in Google Cloud Production](<https://brutecat.com/articles/google-cloud-rce/>) — Arvin Shivram \(Brutecat\); retrieved 2026-10-03T02:35:33Z.
- [Increasing Google &amp; Alphabet VRP rewards up to $151,515](<https://bughunters.google.com/blog/increasing-google-alphabet-vrp-rewards-up-to-151515>) — Sam Erb and Krzysztof Kotowicz / Google; retrieved 2026-10-03T02:35:33Z.
- [Introducing Google Cloud’s new Vulnerability Reward Program](<https://cloud.google.com/blog/products/identity-security/google-cloud-launches-new-vulnerability-rewards-program>) — Michael Cote and Sri Tulasiram / Google Cloud; retrieved 2026-10-03T02:35:33Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
