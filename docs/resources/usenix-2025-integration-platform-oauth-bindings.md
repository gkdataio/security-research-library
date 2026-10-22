# Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://www.usenix.org/conference/usenixsecurity25/presentation/luo-kaixuan>) · [Canonical JSON](<../../data/resources/usenix-2025-integration-platform-oauth-bindings.json>)

<a id="original-summary"></a>
## Main takeaway

This study finds that integration platforms can lose track of which app an OAuth account-linking approval belongs to\. The authors propose tying each authorization to the specific app throughout the flow\. The findings are historical; the review used the publisher's abstract and prepublication manuscript because the final PDF exceeded retrieval limits\.

## Defensive use

Review whether an owned integration preserves the intended app and authorization issuer throughout account linking, including compatibility migrations\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** USENIX Association  
**Authors:** Kaixuan Luo; Xianbo Wang; Pui Ho Adonis Fung; Wing Cheong Lau; Julien Lecomte  
**Resource type:** [Research Paper](<../resource-types.md#type-research-paper>)  
**Version:** USENIX Security 2025  
**Topics:** [Identity](<../resource-topics.md#topic-identity>); [Authorization](<../resource-topics.md#topic-authorization>); [Cloud Security](<../resource-topics.md#topic-cloud-security>)  
**Defensive skills:** [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>); [Model access-control invariants](<../skillsets.md#skill-authorization-modeling>); [Review identity lifecycle](<../skillsets.md#skill-identity-lifecycle-review>)

## Prerequisites

**Basis:** editorial guidance.

- OAuth client and authorization-server roles
- Authorization response and session binding

## Access and freshness

**Access cost at review:** free.

Official open-access publication page and publisher-hosted prepublication paper\.

**Reviewed:** 2026-10-02T17:12:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed the official publication record and relevant sections of its linked prepublication manuscript; no testing artifact was retrieved or executed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-08; precision: month; basis: explicit; source: [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<https://www.usenix.org/conference/usenixsecurity25/presentation/luo-kaixuan>) (source ID: primary). Month in the publisher’s proceedings citation; an earlier prepublication date is not established\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Research measurements are historical, not a statement of current vendor exposure\.
- The paper reports $35K across multiple vendors; no individual qualifying award is inferred\.
- The final PDF exceeded retrieval limits\. The official abstract, bibliography and prepublication defense/disclosure sections were reviewed\.

## Sources and attribution

- [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<https://www.usenix.org/conference/usenixsecurity25/presentation/luo-kaixuan>) — USENIX Association; source ID: primary; provenance: official primary; retrieved 2026-10-02T17:12:00Z; supports: summary, version, dates.
- [Publisher-hosted prepublication manuscript](<https://www.usenix.org/system/files/conference/usenixsecurity25/sec24winter-prepub-332-luo.pdf>) — USENIX Association; source ID: prepublication; provenance: official primary; retrieved 2026-10-02T17:12:00Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
