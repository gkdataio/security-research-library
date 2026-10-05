# Cloud Build approval was not bound to immutable code

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Google  
**Product:** Google Cloud Build GitHub integration

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-03.

A researcher-published Google award notice for $30,000 \(USD contextually inferred\) illustrates a gap between approval of a contribution and selection of the code executed\.

### Root cause

The researcher compared the identity available to the approval event with the revision later selected by the build\. Approval referred to mutable contribution state without preserving the exact reviewed version\. The execution boundary therefore relied on an assumption that the approved and executed content remained identical\.

### Bounded impact

The controlled demonstration executed a newer, unreviewed revision\. Access to secrets or cloud resources was a potential consequence of the build’s assigned privileges, not evidence that all pipelines exposed those assets\.

### Defensive lessons

- Bind approval and execution to immutable content identities, with explicit confirmation when the intended revision is ambiguous\.
- The researcher’s fix analysis describes check-to-commit binding and explicit commit selection; it does not establish a universal patch recipe\.
- Limit build identity privileges and secret availability independently of human approval\.

## Award and evidence

**USD 30,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported\_with\_vendor\_quote. The researcher-published Google notice states $30000\.00 without an explicit currency code\. USD is inferred from Google’s March 2017 program-wide USD statement, almost eight years before the January 2025 award, with October 2024 official context linking Cloud rewards to the broader Google VRP\. This is denomination context, not independent proof of the individual award’s currency or cash settlement\. Older reference; original report was in 2024\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/google-cloud-build-approval-toctou-2025.json>).

## Dates

- **published:** 2025-07-21; precision: day; basis: explicit
- **public disclosure:** 2025-07-21; precision: day; basis: explicit. Publication of this write-up; earliest disclosure elsewhere was not independently established\.
- **reported:** 2024-11-13; precision: day; basis: explicit
- **awarded:** 2025-01-28; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported. The researcher says Google marked the issue fixed on June 18, 2025\. The exact deployment date is not established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported. Cash settlement date not independently established\.
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-05T21:13:58Z. Reviewed the researcher-published award image and official currency and Cloud-program continuity context\. Bound the amount and reproduced vendor wording to award-image; used the official sources only for qualified USD inference\. Preserved prior technical and event-date evidence\. No target interaction or exploit reproduction\. The award-image retrieval timestamp records the immediate post-review clock observation, not an exact image-capture time\.

- The award notice is vendor correspondence reproduced by the researcher, not independently retrieved vendor evidence or proof of cash settlement\.
- The June 18, 2025 status change confirms the issue was marked fixed, not the exact deployment date\.
- The public account’s broader security consequences depend on pipeline permissions; no universal secret exposure is established\.
- The notice uses $ without spelling out USD\. Currency is inferred from March 2017 Google VRP context, almost eight years before the award, and October 2024 Cloud-program continuity, about three months before it; neither independently proves this individual award’s denomination or settlement\.

## Related conceptual diagrams

- [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>)

## Sources and attribution

- [Who's SHA is it Anyway: Bypassing Google Cloud Build Comment Control for $30,000](<https://adnanthekhan.com/posts/cloud-build-toctou/>) — Adnan Khan; retrieved 2026-10-02T20:00:00Z.
- [Researcher-published Google award notice for the Cloud Build report](<https://adnanthekhan.com/_astro/images/google-bounty-payment.BiMCzkaR_287nKC.webp>) — Adnan Khan, reproducing a Google award notice; retrieved 2026-10-05T21:08:43Z.
- [VRP news from Nullcon](<https://security.googleblog.com/2017/03/vrp-news-from-nullcon.html>) — Josh Armour / Google; retrieved 2026-10-05T21:11:25Z.
- [Introducing Google Cloud’s new Vulnerability Reward Program](<https://cloud.google.com/blog/products/identity-security/google-cloud-launches-new-vulnerability-rewards-program>) — Michael Cote and Sri Tulasiram / Google Cloud; retrieved 2026-10-05T21:11:25Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
