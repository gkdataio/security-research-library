# Angular automation trust and cache isolation weakness

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Angular development and release infrastructure

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

A Google-rewarded report connected an adjacent CI misconfiguration with insufficient separation of automation trust, creating a potential Angular supply-chain impact\.

### Root cause

Untrusted workflow input and shared build state crossed trust boundaries; bot-specific approval assumptions increased the potential consequence\.

### Bounded impact

The researcher demonstrated credential exposure and modeled the remaining path to repository control without executing the final supply-chain modification\. Google classified the report as a flagship supply-chain compromise\.

### Defensive lessons

- Separate caches and artifacts according to trust level\.
- Apply consistent review invalidation and least-privilege rules to automated identities\.
- Record which impacts were directly demonstrated versus established through design evidence\.

## Award and evidence

**USD 31,337** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported\_with\_vendor\_quote. A Google award email is quoted within the researcher publication\. This is researcher-published evidence, not an independently accessed vendor award record\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/angular-ci-cache-trust-2026.json>).

## Dates

- **published:** 2026-03-03; precision: day; basis: explicit
- **public disclosure:** 2026-03-03; precision: day; basis: explicit. Publication of this write-up; earliest disclosure elsewhere was not independently established\.
- **reported:** 2025-12-11; precision: day; basis: explicit
- **awarded:** 2026-01-28; precision: day; basis: explicit
- **fixed:** 2025-12-21; precision: day; basis: explicit
- **paid:** Unknown; precision: unknown; basis: not\_reported. Cash settlement date not independently established\.
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T03:49:00Z. Primary public source read; award distinguished from program maximums and aggregate earnings\. No vulnerability testing performed\.

- The reward is an actual award reported in a primary researcher account; payment settlement was not independently audited\.

## Sources and attribution

- [Turning Almost Nothing into a Supply Chain Compromise of Angular with GitHub Actions Cache Poisoning](<https://adnanthekhan.com/posts/angular-compromise-through-dev-infra/>) — Adnan Khan; retrieved 2026-10-02T03:49:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
