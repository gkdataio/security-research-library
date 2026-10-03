# Dolibarr portal accounts: credential writes need object authorization

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/dolibarr-2026-portal-object-authorization.json>) · [Official resource](<https://codeant.ai/security-research/cve-2026-71505-dolibarr-bola-enables-portal-account-takeover>)

**Publisher:** CodeAnt AI  
**Authors:** Amartya Jha  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization  
**Defensive skills:** Model access-control invariants; Review identity lifecycle; Verify remediation evidence

## Original summary

Research on CVE-2026-71505 describes inconsistent authorization between reading and modifying company portal accounts\. A role-level check did not establish authority over the particular company\. In researcher-owned fixtures, the omission enabled account takeover, invoice access and disclosure of stored password verifiers\.

## Defensive use

Apply actor-to-object checks consistently to every credential mutation\. The linked maintainer patch adds resource checks to account creation, update and deletion; the CNA identifies versions before 24\.0\.0 as affected\. Editorially, keep credential changes explicitly permissioned and sensitive verifiers out of responses\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic authentication and access-control concepts
- Familiarity with application trust boundaries

## Access and freshness

**Access cost at review:** free.

Public sources readable without an account\.

**Reviewed:** 2026-10-03T06:19:33Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary sources reviewed; no immutable article revision established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08-23; precision: day; basis: explicit; source: [CVE-2026-71505: Dolibarr BOLA Enables Portal Account Takeover](<https://codeant.ai/security-research/cve-2026-71505-dolibarr-bola-enables-portal-account-takeover>) (source ID: research).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-08-23; precision: day; basis: explicit; source: [CVE-2026-71505: Dolibarr BOLA Enables Portal Account Takeover](<https://codeant.ai/security-research/cve-2026-71505-dolibarr-bola-enables-portal-account-takeover>) (source ID: research).

## Caveats

- An authenticated principal with third-party creation rights is required\. The researcher's demonstrated fixture also held read-companies rights, although the article identifies creation rights as sufficient for the vulnerable write\.
- Observed evidence comes from a local development build with fixture companies, not customer accounts\. Disclosed password hashes were not shown cracked\.
- The researcher lists CVSS 8\.1; the CNA gives CVSS v4 7\.1\. Scores are preserved as different source claims, not reconciled\.
- Article publication \(August 23\) and CNA publication \(August 24, 2026\) are distinct\. Learning prerequisites are editorial\.

## Sources and attribution

- [CVE-2026-71505: Dolibarr BOLA Enables Portal Account Takeover](<https://codeant.ai/security-research/cve-2026-71505-dolibarr-bola-enables-portal-account-takeover>) — CodeAnt AI; source ID: research; provenance: official primary; retrieved 2026-10-03T06:19:33Z; supports: summary, dates.
- [Dolibarr &lt; 24\.0\.0 REST API Broken Object-Level Authorization via Third-Party Write Route](<https://www.vulncheck.com/advisories/dolibarr-rest-api-broken-object-level-authorization-via-third-party-write-route>) — VulnCheck; source ID: cna; provenance: official primary; retrieved 2026-10-03T06:19:33Z; supports: summary.
- [Fix prevent edit by external users - reported by VulnCheck](<https://github.com/Dolibarr/dolibarr/commit/4cf305ebb958eeffa921aad7c94de179b764f7e7>) — Dolibarr; source ID: maintainer-patch; provenance: official primary; retrieved 2026-10-03T06:19:33Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
