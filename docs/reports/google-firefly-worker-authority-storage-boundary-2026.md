# Google Firefly confused worker authority and storage boundaries

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Firefly partner-management API

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

Firefly received a separately identified USD 60,000 award\. The case illustrates how delegated worker authority and storage permissions can diverge from caller authorization\.

### Root cause

Missing caller authorization, unverified worker-result authority and unconstrained storage abstraction crossed service boundaries\. The researcher questioned whether a narrowly named field actually limited backend authority\.

### Bounded impact

The researcher demonstrated storage reads and a local test-file write under a production identity\. Broader access remained permission-dependent; universal infrastructure compromise is not established\.

### Defensive lessons

- Editorial lesson: authenticate scheduler callbacks against the assigned worker and bind completion to an immutable task\.
- Editorial lesson: enforce explicit storage capabilities rather than relying on field names; apply resource authorization before delegated execution\.

## Award and evidence

**USD 60,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported\_with\_vendor\_quote. Separate report award; headline total is not used\. Payment is unverified\. USD follows the linked official denomination context\. No component is counted separately\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-firefly-worker-authority-storage-boundary-2026.json>).

## Dates

- **published:** 2026-09-11; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** 2026-07-14; precision: day; basis: explicit
- **awarded:** 2026-07-24; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Article states resolution without a date\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T16:00:54Z. Read both primary pages in the cloud browser after search returned no article body\. Matched exact report labels to separate timeline awards\. No target testing\.

- Researcher narrative is hosted by Google and authored by a researcher who subsequently joined Google; conservatively classified as researcher-reported panel correspondence, without independent payment evidence\.
- Resolution is stated, but deployment date and patch implementation are unspecified\.
- The dollar denomination is inferred from Google’s July 2024 USD program announcement, approximately two years before the awards; it does not prove individual settlement\.
- The article demonstrates requests with a caller session but does not fully specify minimum account prerequisites; missing authorization is not treated as proof of anonymous Firefly access\.

## Sources and attribution

- [Breaking into Google's GFile for $100k](<https://bughunters.google.com/blog/breaking-into-googles-gfile-for-100k>) — Arvin Shivram \(Brutecat\), published on Google Bug Hunters; retrieved 2026-10-03T16:00:54Z.
- [Increasing Google &amp; Alphabet VRP rewards up to $151,515](<https://bughunters.google.com/blog/increasing-google-alphabet-vrp-rewards-up-to-151515>) — Sam Erb and Krzysztof Kotowicz, Google; retrieved 2026-10-03T16:00:54Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
