# Google IDX worker messaging crossed browser trust boundaries

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Project IDX / Cloud Workstations

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

A browser-IDE trust-boundary report received a USD 22,500 award\.

### Root cause

The messaging boundary treated caller-influenced context as authority for extension-worker operations\. Browser framing permission did not independently establish that embedded content should control the worker\.

### Bounded impact

The researcher demonstrated script execution in a worker, without direct DOM access\. Same-origin requests were described as a possible consequence; broader account takeover was not established\. The reproduced award notice limits severity because prior access to an affected resource was required\.

### Defensive lessons

- Bind messaging trust to a verified origin and context\.
- Review nested rendering and worker privileges together\.
- Validate message authority independently of framing permission and keep untrusted rendered content separate from privileged extension operations\.

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

Reviewed: 2026-10-03T05:19:42Z. Fresh-read the article; retained previously inspected award-image and currency evidence without advancing their retrieval times\. No testing performed\.

- Award evidence is not an independently audited cash receipt\.
- The image is researcher-published, not independently retrieved vendor correspondence\.
- Exact original-report, award, payment, fix and first-disclosure dates are unavailable\. The linked Bug Hunters report returned no readable text\.
- Article credits Matan Berson for the underlying discovery and Sreeram and Sivanesh for supporting research; recipient split is not stated\.
- Parts of the explanation use a local Code OSS reconstruction; the author acknowledges incomplete historical IDX notes\. It is not a verified account of current product behavior\.

## Sources and attribution

- [XSS in Google IDX Workstation](<https://sudistark.github.io/2025/07/02/idx.html>) — sudi \(Sudistark\); retrieved 2026-10-03T05:19:42Z.
- [Researcher-published Google award email for IDX report](<https://sudistark.github.io/tmp/cdn-images/Pasted%20image%2020250729220436.png>) — sudi \(Sudistark\), reproducing a Google award notice; retrieved 2026-10-02T15:12:00Z.
- [Google and Alphabet VRP reward-denomination announcement, July 11, 2024](<https://bughunters.google.com/blog/increasing-google-alphabet-vrp-rewards-up-to-151515>) — Sam Erb and Krzysztof Kotowicz / Google; retrieved 2026-10-02T15:14:47Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
