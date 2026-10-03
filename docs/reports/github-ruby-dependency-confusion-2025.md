# GitHub package-source trust allowed dependency confusion

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** GitHub  
**Product:** GitHub build and development services

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

A researcher reported one dependency-confusion finding affecting GitHub build and development services and a $20,000 award\.

### Root cause

Dependency resolution crossed the intended boundary between internal Ruby packages and a public package source\.

### Bounded impact

The researcher observed code execution across multiple service contexts\. The disclosed account does not establish a broader compromise beyond those observations\.

### Defensive lessons

- Define explicit package sources and reserve internal namespaces where applicable\.
- Treat build and developer environments as separate trust zones and minimize their credentials\.

## Award and evidence

**USD 20,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. The researcher states this was a critical report and that the bounty was paid; no separate payment date or public HackerOne report is supplied\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/github-ruby-dependency-confusion-2025.json>).

## Dates

- **published:** 2025-10-28; precision: day; basis: url\_date. Date encoded in the researcher publication permalink; earliest disclosure elsewhere was not independently established\.
- **public disclosure:** 2025-10-28; precision: day; basis: url\_date. Date encoded in the researcher publication permalink; earliest disclosure elsewhere was not independently established\.
- **reported:** 2025-09-01; precision: day; basis: inferred. The timeline supplies September 1; year is inferred from the 2025 publication context\.
- **awarded:** 2025-10-21; precision: day; basis: inferred. The timeline supplies October 21; year is inferred from the 2025 publication context\.
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported. Cash settlement date not independently established\.
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T03:49:00Z. Primary public source read; award distinguished from program maximums and aggregate earnings\. No vulnerability testing performed\.

- The reward is an actual award reported in a primary researcher account; payment settlement was not independently audited\.

## Sources and attribution

- [Vibecoding my way to a crit on Github](<https://furbreeze.github.io/2025/10/28/vibecoding-my-way-to-a-crit-on-github.html>) — Furbreeze; retrieved 2026-10-02T03:49:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
