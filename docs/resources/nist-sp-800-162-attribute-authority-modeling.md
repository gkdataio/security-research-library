# NIST SP 800-162: attribute authority and policy traceability

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://csrc.nist.gov/pubs/sp/800/162/upd2/final>) · [Canonical JSON](<../../data/resources/nist-sp-800-162-attribute-authority-modeling.json>)

<a id="original-summary"></a>
## Main takeaway

NIST explains how access policies use attributes of the user, resource, requested action and environment to decide whether to allow access\. It connects business rules to software-enforced decisions and explains why organizations need consistent attribute meanings\. Who supplies an attribute, how it is maintained and how it is protected are part of the access-control design\.

## Defensive use

For an owned policy design, identify who may assert each attribute, how it is bound to its subject or object, and how changes reach decision points\. Compare resulting permissions with the written policy\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** National Institute of Standards and Technology  
**Authors:** Vincent C\. Hu; David Ferraiolo; Rick Kuhn; Adam Schnitzer; Kenneth Sandlin; Robert Miller; Karen Scarfone  
**Resource type:** [Architecture Guide](<../resource-types.md#type-architecture-guide>)  
**Version:** SP 800-162 \(January 2014; updated August 2, 2019\)  
**Topics:** [Authorization](<../resource-topics.md#topic-authorization>); [Identity](<../resource-topics.md#topic-identity>)  
**Defensive skills:** [Model access-control invariants](<../skillsets.md#skill-authorization-modeling>); [Review identity lifecycle](<../skillsets.md#skill-identity-lifecycle-review>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>)

## Prerequisites

**Basis:** publisher explicit.

- Basic understanding of access-control concepts

## Access and freshness

**Access cost at review:** free.

Official public guidance; no account required to read\.

**Reviewed:** 2026-10-03T01:41:34Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed the catalog and publication scope, audience, errata, attribute management and policy traceability sections; historical edition retained explicitly\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2014-01; precision: month; basis: explicit; source: [Guide to Attribute Based Access Control \(ABAC\) Definition and Considerations](<https://csrc.nist.gov/pubs/sp/800/162/upd2/final>) (source ID: primary). Original publication month; distinct from later updates\.
- **version released:** 2019-08-02; precision: day; basis: explicit; source: [NIST SP 800-162: scope, audience, attribute management and policy traceability](<https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-162.pdf>) (source ID: publication). Errata update adds environment conditions to the ABAC trust-chain figure; not a new original publication\.
- **source displayed:** 2019-08-02; precision: day; basis: explicit; source: [Guide to Attribute Based Access Control \(ABAC\) Definition and Considerations](<https://csrc.nist.gov/pubs/sp/800/162/upd2/final>) (source ID: primary). Catalog identifies updates through this date\.

## Caveats

- Assumes subjects are bound to trusted identities; it does not comprehensively cover authentication or identity management\.
- Historical conceptual guidance, not a product certification or a complete deployment checklist\.

## Sources and attribution

- [Guide to Attribute Based Access Control \(ABAC\) Definition and Considerations](<https://csrc.nist.gov/pubs/sp/800/162/upd2/final>) — National Institute of Standards and Technology; source ID: primary; provenance: official primary; retrieved 2026-10-03T01:39:33Z; supports: summary, version, dates.
- [NIST SP 800-162: scope, audience, attribute management and policy traceability](<https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-162.pdf>) — National Institute of Standards and Technology; source ID: publication; provenance: official primary; retrieved 2026-10-03T01:39:49Z; supports: summary, version, dates, prerequisites.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
