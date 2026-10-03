# Google Mamba temporary outputs lacked access isolation

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Mamba frame-metrics pipeline

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

Mamba received a distinct USD 37,604\.40 award\. The case illustrates why temporary processing output needs explicit access isolation, with retrieval dependencies kept separate from standalone impact\.

### Root cause

Untrusted file selection reached privileged storage copying\. Shared temporary outputs relied on obscurity, while diagnostic metadata weakened filename secrecy\.

### Bounded impact

Unauthenticated copying was possible, but demonstrated retrieval required the separately reported Firefly capability\. The panel explicitly discounted difficult exploitation and additional access requirements\.

### Defensive lessons

- Editorial lesson: isolate temporary outputs by authenticated principal and enforce access controls independent of filename secrecy\.
- Editorial lesson: restrict file-source capabilities and minimize diagnostic disclosure; document dependencies before assigning standalone impact\.

## Award and evidence

**USD 37,604.4** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported\_with\_vendor\_quote. Separate report award; headline total is not used\. Payment is unverified\. USD follows the linked official denomination context\. No component is counted separately\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-mamba-temporary-output-isolation-2026.json>).

## Dates

- **published:** 2026-09-11; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** 2026-07-18; precision: day; basis: explicit
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
- Mamba is a separately reported and separately awarded finding; its retrieval demonstration depends on Firefly\. The combined demonstration is not an additional record or award\.

## Sources and attribution

- [Breaking into Google's GFile for $100k](<https://bughunters.google.com/blog/breaking-into-googles-gfile-for-100k>) — Arvin Shivram \(Brutecat\), published on Google Bug Hunters; retrieved 2026-10-03T16:00:54Z.
- [Increasing Google &amp; Alphabet VRP rewards up to $151,515](<https://bughunters.google.com/blog/increasing-google-alphabet-vrp-rewards-up-to-151515>) — Sam Erb and Krzysztof Kotowicz, Google; retrieved 2026-10-03T16:00:54Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
