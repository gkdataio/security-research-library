# Google IDX worker messaging crossed browser trust boundaries

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Project IDX / Cloud Workstations

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

A browser-IDE trust-boundary report received a USD 22,500 award\.

### Root cause

Messaging and embedded-content trust assumptions allowed untrusted input to reach a privileged worker context\.

### Bounded impact

The researcher demonstrated worker-context script execution\. The reproduced award notice limits severity because prior access to an affected resource was required\.

### Defensive lessons

- Bind messaging trust to a verified origin and context\.
- Review nested rendering and worker privileges together\.

## Award and evidence

**USD 22,500** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported\_with\_vendor\_quote. The image states a $22,500 award\. USD follows Google web VRP denomination documented by google-usd-context; no currency conversion\. Bonus mentioned but not separately itemized\. Settlement date unknown\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-idx-worker-message-trust-2025.json>).

## Dates

- **published:** 2025-07-02; precision: day; basis: explicit. Date displayed by the researcher article\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** 2024; precision: year; basis: inferred. Article says the report was submitted last year; year inferred from its 2025 publication header\.
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T15:14:47Z. Researcher article read; award image visually inspected in the cloud browser\. Google program currency context read separately\. Official 2024 program announcement was read in the cloud browser for USD denomination only; its advertised maximum is not award evidence\.

- Award evidence is not an independently audited cash receipt\.
- The image is researcher-published, not independently retrieved vendor correspondence\.
- Exact original-report, award, payment, fix and first-disclosure dates are unavailable\. The linked Bug Hunters report returned no readable text\.
- Article credits Matan Berson for the underlying discovery and Sreeram and Sivanesh for supporting research; recipient split is not stated\.

## Sources and attribution

- [XSS in Google IDX Workstation](<https://sudistark.github.io/2025/07/02/idx.html>) — sudi \(Sudistark\); retrieved 2026-10-02T15:12:00Z.
- [Researcher-published Google award email for IDX report](<https://sudistark.github.io/tmp/cdn-images/Pasted%20image%2020250729220436.png>) — sudi \(Sudistark\), reproducing a Google award notice; retrieved 2026-10-02T15:12:00Z.
- [Google and Alphabet VRP reward-denomination announcement, July 11, 2024](<https://bughunters.google.com/blog/increasing-google-alphabet-vrp-rewards-up-to-151515>) — Sam Erb and Krzysztof Kotowicz / Google; retrieved 2026-10-02T15:14:47Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
