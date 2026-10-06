# Claude Cowork: approved destinations need account and operation binding

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/anthropic-2026-egress-capability-identity-binding.json>) · [Official resource](<https://www.anthropic.com/engineering/how-we-contain-claude>)

**Publisher:** Anthropic  
**Authors:** Max McGuinness; Mikaela Grace; Jiri De Jonghe; Jake Eaton; Abel Ribbink  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Ai Security; Authorization  
**Defensive skills:** Review AI authority boundaries; Model access-control invariants; Threat-model integrations

## Original summary

Anthropic describes Cowork workspace data reaching an unintended account through an allowed service while VM isolation held\. The failed assumption was that an approved API hostname established sufficient authority for disclosure\. Readable workspace content and permitted service access were prerequisites; no hypervisor escape is established\.

## Defensive use

Editorial lesson: evaluate egress as an authorization decision over session identity, receiving account, permitted operation and data purpose\. A host allowlist is only one input\. Keep enforcement independent of model instructions, minimize readable data, and retain provenance at the boundary that knows the session\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic access-control and service-identity concepts
- Distinguishing execution isolation from data-disclosure authority

## Access and freshness

**Access cost at review:** free.

Public engineering article\.

**Reviewed:** 2026-10-06T21:13:14Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Cowork egress section reviewed; remediation is vendor-reported, not independently verified\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-05-25; precision: day; basis: explicit; source: [How we contain Claude across products](<https://www.anthropic.com/engineering/how-we-contain-claude>) (source ID: engineering).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational edition displayed\.
- **source displayed:** 2026-05-25; precision: day; basis: explicit; source: [How we contain Claude across products](<https://www.anthropic.com/engineering/how-we-contain-claude>) (source ID: engineering). Publication date; no separate update displayed\.

## Caveats

- Anthropic reports limiting API proxy acceptance to provisioned-session credentials and adding egress restrictions; exact fix release/date and independent effectiveness verification are absent\.
- No victim count, production-incident prevalence or individual award is established\.
- Scope is only the Cowork approved-domain case, not other incidents or products discussed in the article\.
- First-party engineering research; research-paper does not imply academic peer review\.

## Sources and attribution

- [How we contain Claude across products](<https://www.anthropic.com/engineering/how-we-contain-claude>) — Anthropic; source ID: engineering; provenance: official primary; retrieved 2026-10-06T21:10:15Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
