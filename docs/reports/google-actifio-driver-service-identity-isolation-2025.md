# Actifio driver execution exposed excessive shared-service authority

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

[Read the original source](<https://stazot.com/?article=dataprep-actifio-jar-swapping-rce>) — Sivanesh Ashok · [Canonical JSON](<../../data/reports/google-actifio-driver-service-identity-isolation-2025.json>)

<a id="what-the-evidence-establishes"></a>
## Main takeaway

Actifio did not adequately separate user-supplied driver code from a privileged shared service account\. Researchers observed access across many compute instances, but broader customer-project compromise was not independently verified\. They report a USD 10,000 award after Google doubled the base award for collaboration\.

**Organization:** Google  
**Product:** Actifio cloud backup service

<a id="root-cause"></a>
## What went wrong

Insufficient separation between user-supplied driver code and a privileged shared service identity\.

<a id="bounded-impact"></a>
## What the evidence shows

Researchers demonstrated execution and observed service-account access across many compute instances\. Broader customer-project compromise was claimed, not independently verified\.

## Defensive lessons

- Isolate extension execution from service credentials\.
- Scope delegated identities to the minimum tenant and resource set\.
- Distinguish observed permissions from untested downstream impact\.

## Award and evidence

**USD 10,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. One report: USD 5,000 base doubled by a collaboration grant\. The separate Dataprep finding in this article received no cash bounty\. USD denomination follows official Google program context; recipient split and cash settlement unknown\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-actifio-driver-service-identity-isolation-2025.json>).

## Dates

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

- **published:** 2025-05-04; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** Unknown; precision: unknown; basis: not\_reported. The narrative gives approximate historical context but no distinct submission date for this Actifio report\.
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T15:31:00Z. Full researcher article read in the cloud browser after text retrieval returned only the page shell\. Award paragraph isolated from the unrelated unrewarded finding\.

- Award is researcher-reported; no cash receipt or per-contributor split is supplied\.
- Exact original-report, award, payment, fix and first-disclosure dates are unavailable\.
- Broad cross-customer impact is the researcher’s assessment, not evidence of customer-data extraction\.

## Related conceptual diagrams

- [Keep workload authority tenant-scoped](<../diagram-gallery.md#workload-identity-tenant-scope>)

## Sources and attribution

- [Two RCEs in Google Cloud products and Nike Air Max 90s](<https://stazot.com/?article=dataprep-actifio-jar-swapping-rce>) — Sivanesh Ashok; retrieved 2026-10-02T15:31:00Z.
- [VRP news from Nullcon: Google web VRP USD denomination](<https://security.googleblog.com/2017/03/vrp-news-from-nullcon.html>) — Josh Armour / Google; retrieved 2026-10-02T15:11:49Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
