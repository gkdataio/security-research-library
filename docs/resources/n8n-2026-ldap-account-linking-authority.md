# n8n: directory-attribute authority in durable account linking

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/n8n-io/n8n/security/advisories/GHSA-c545-x2rh-82fc>) · [Canonical JSON](<../../data/resources/n8n-2026-ldap-account-linking-authority.json>)

<a id="original-summary"></a>
## Main takeaway

n8n's maintainer advisory describes account linking that treated a matching LDAP email attribute as proof of account ownership \(CVE-2026-33665\)\. It reports that access to the linked account, including administrator permissions, persisted even after the directory attribute changed back\.

## Defensive use

Editorial lesson: an identity association is a security grant with its own approval and revocation requirements\. Attribute equality alone should not establish account ownership\. Review claim provenance, linking consent and existing association cleanup independently\. The maintainer identifies software versions 1\.121\.0 and 2\.4\.0 as fixes for their respective release lines\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** n8n  
**Authors:** Jubke  
**Resource type:** [Maintainer Advisory](<../resource-types.md#type-maintainer-advisory>)  
**Version:** Not established in the reviewed record  
**Topics:** [Identity](<../resource-topics.md#topic-identity>); [Authorization](<../resource-topics.md#topic-authorization>); [Business Logic and State Integrity](<../resource-topics.md#topic-business-logic>)  
**Defensive skills:** [Review identity lifecycle](<../skillsets.md#skill-identity-lifecycle-review>); [Model access-control invariants](<../skillsets.md#skill-authorization-modeling>); [Verify remediation evidence](<../skillsets.md#skill-patch-verification>)

## Prerequisites

**Basis:** editorial guidance.

- Basic understanding of authentication, account state and authorization

## Access and freshness

**Access cost at review:** free.

Public maintainer disclosure\.

**Reviewed:** 2026-10-03T13:09:31Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory reviewed; no deployment assessment or independent reproduction performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-03-25; precision: day; basis: explicit; source: [LDAP Email-Based Account Linking Allows Privilege Escalation and Account Takeover](<https://github.com/n8n-io/n8n/security/advisories/GHSA-c545-x2rh-82fc>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition date established; software fix versions are discussed separately\.
- **source displayed:** 2026-03-25; precision: day; basis: explicit; source: [LDAP Email-Based Account Linking Allows Privilege Escalation and Account Takeover](<https://github.com/n8n-io/n8n/security/advisories/GHSA-c545-x2rh-82fc>) (source ID: advisory).

## Caveats

- Requires enabled LDAP authentication, which is non-default, and an authenticated directory user able to alter their own email attribute\. This is a maintainer-described impact, not evidence of a production compromise\.
- The advisory recommends temporary LDAP restriction or disabling and account-association review, but calls those measures incomplete\. It does not establish automatic removal of previously incorrect links or a patch-release date\.
- Jubke published the advisory\. Credited reporters are weblover12, 34selen, B0RI, bde574786 and jh-hack\. Original report date is not established\. Learning prerequisites and design lessons are editorial\.

## Sources and attribution

- [LDAP Email-Based Account Linking Allows Privilege Escalation and Account Takeover](<https://github.com/n8n-io/n8n/security/advisories/GHSA-c545-x2rh-82fc>) — n8n; source ID: advisory; provenance: official primary; retrieved 2026-10-03T13:09:31Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
