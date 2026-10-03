# n8n: directory-attribute authority in durable account linking

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/n8n-2026-ldap-account-linking-authority.json>) · [Official resource](<https://github.com/n8n-io/n8n/security/advisories/GHSA-c545-x2rh-82fc>)

**Publisher:** n8n  
**Authors:** Jubke  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; Business Logic and State Integrity  
**Defensive skills:** Review identity lifecycle; Model access-control invariants; Verify remediation evidence

## Original summary

CVE-2026-33665 describes local-account linkage that trusted a matching LDAP email attribute\. The maintainer reports persistent access to the linked account, including administrator authority, even after the directory attribute changed back\.

## Defensive use

Editorial lesson: an identity association is a security grant with its own approval and revocation requirements\. Attribute equality alone should not establish account ownership\. Review claim provenance, linking consent and existing association cleanup independently\. The maintainer identifies software versions 1\.121\.0 and 2\.4\.0 as fixes for their respective release lines\.

Educational reference only; linked material does not authorize testing unrelated systems.

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
