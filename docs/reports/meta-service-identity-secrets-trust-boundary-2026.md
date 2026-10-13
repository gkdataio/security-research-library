# Meta service-identity exposure amplified by excessive secret access

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

[Read the original source](<https://sectricity.com/blog/misconfigured-grafana-507-private-meta-repos/>) — Preben Ver Eecke, Sectricity · [Canonical JSON](<../../data/reports/meta-service-identity-secrets-trust-boundary-2026.json>)

<a id="what-the-evidence-establishes"></a>
## Main takeaway

An exposed Meta service identity had excessive access to secrets used by other integrations\. Researchers report potential read and write access to 507 private repositories, but say they only confirmed the count and did not browse or clone their contents\. Their organization reports a $150,000 base award\.

**Organization:** Meta  
**Product:** Internal development and cloud-service integrations

<a id="root-cause"></a>
## What went wrong

An exposed service identity had unnecessarily broad access to secrets, with downstream integration credentials extending the potential impact into private source repositories\. Apply strong service authentication, minimize identity permissions, and separate trust between integrations\.

<a id="bounded-impact"></a>
## What the evidence shows

Researchers report potential read/write access to 507 private repositories; their write-up says they confirmed the count and did not clone or browse repository contents\.

## Defensive lessons

- Require authenticated, explicitly authorized access to service identities\.
- Constrain secret access and integration privileges to the minimum required\.
- Document exposure without copying private customer or source data\.

## Award and evidence

**USD 150,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported\_with\_vendor\_quote. Use the $150,000 base award\. The headline says $157K, but the stated 5% bonus would imply $157,500; exact total is not asserted\. USD normalization of the dollar-denominated Meta award; the reproduced individual message uses $\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/meta-service-identity-secrets-trust-boundary-2026.json>).

## Dates

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

- **reported:** 2026-03-21; precision: day; basis: explicit
- **awarded:** 2026-04-29; precision: day; basis: explicit
- **fixed:** Unknown; precision: unknown; basis: not\_reported. The source says mitigated, not that a final software fix was released\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** 2026-03-23; precision: day; basis: explicit. Triaged and mitigated according to the researcher timeline\.
- **published:** 2026-05-28; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported. Earliest public disclosure has not been independently established\.

## Verification limits

Reviewed: 2026-10-02T03:54:00Z. Primary public sources read; reward distinguished from maximums and aggregates\. Historical defensive summary only; no vulnerability testing performed\.

- Headline states $157K, while $150,000 plus 5% arithmetically equals $157,500; use the undisputed $150,000 base and preserve this discrepancy
- Vendor response is reproduced by the researcher organization, not independently hosted by Meta
- The exposed Grafana dashboard was a discovery signal, not established as the underlying rewarded vulnerability

## Related conceptual diagrams

- [Keep workload authority tenant-scoped](<../diagram-gallery.md#workload-identity-tenant-scope>)

## Sources and attribution

- [Meta service-identity exposure amplified by excessive secret access](<https://sectricity.com/blog/misconfigured-grafana-507-private-meta-repos/>) — Preben Ver Eecke, Sectricity; retrieved 2026-10-02T03:54:00Z.
- [Supporting primary disclosure source](<https://sectricity.com/about/method-ethics/>) — Preben Ver Eecke, Sectricity; retrieved 2026-10-02T03:54:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
