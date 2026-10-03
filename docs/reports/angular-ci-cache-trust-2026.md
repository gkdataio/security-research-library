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

Evidence level: researcher\_reported\_with\_vendor\_quote. A Google award email is quoted within the researcher publication; it is not an independently accessed vendor award record\. The quote uses only $\. USD is a contextual currency inference from the official OSS VRP rules \(currency-context\), whose Reward amounts section explicitly denominates discretionary bonuses in USD\. Those living rules were reviewed on October 3, 2026, after the January 28 award; their wording at award time was not established\. They are denomination context only, not proof of this individual award or settlement\. No bonus is established or added\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/angular-ci-cache-trust-2026.json>).

## Dates

- **published:** 2026-03-03; precision: day; basis: explicit
- **public disclosure:** 2026-03-03; precision: day; basis: explicit. Publication of this write-up; earliest disclosure elsewhere was not independently established\.
- **reported:** 2025-12-11; precision: day; basis: explicit
- **awarded:** 2026-01-28; precision: day; basis: explicit
- **fixed:** 2025-12-21; precision: day; basis: explicit. Researcher timeline says the report was marked fixed on this date; deployment timing and patch effectiveness were not independently verified\.
- **paid:** Unknown; precision: unknown; basis: not\_reported. Cash settlement date not independently established\.
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** 2025-12-12; precision: day; basis: explicit. Researcher timeline records disabling the workflow as mitigation\.

## Verification limits

Reviewed: 2026-10-03T19:54:00Z. Primary researcher award and timeline reread; official OSS VRP rules read for contextual denomination only\. Award distinguished from program maximums and aggregate earnings\. No vulnerability testing performed\.

- The reward is an actual award reported in a primary researcher account; payment settlement was not independently audited\.
- USD is contextually inferred from later program-level denomination wording, not explicitly stated in the quoted individual award\. No conflicting denomination was identified in the reviewed sources\.

## Related conceptual diagrams

- [Build evidence must match the artifact and trusted builder](<../diagram-gallery.md#build-artifact-provenance-boundary>)

## Sources and attribution

- [Turning Almost Nothing into a Supply Chain Compromise of Angular with GitHub Actions Cache Poisoning](<https://adnanthekhan.com/posts/angular-compromise-through-dev-infra/>) — Adnan Khan; retrieved 2026-10-03T19:52:01Z.
- [Google Open Source Software Vulnerability Reward Program Rules — Reward amounts](<https://bughunters.google.com/about/rules/open-source/google-open-source-software-vulnerability-reward-program-rules#reward-amounts>) — Google; retrieved 2026-10-03T19:53:20Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
