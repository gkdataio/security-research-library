# GitHub internal metadata: preserve the boundary between user data and service authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/github-2026-internal-metadata-authority.json>) · [Official resource](<https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854>)

**Publisher:** Wiz Research  
**Authors:** Sagi Tzadik  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Web Foundations; Cloud Security  
**Defensive skills:** Threat-model integrations; Review parsing and serialization; Review input trust boundaries; Write bounded security evidence; Verify remediation evidence

## Original summary

Wiz's CVE-2026-3854 research examines a data-to-authority boundary in GitHub's backend\. User-controlled operation metadata reached downstream services as trusted configuration\. Code execution was demonstrated on Enterprise Server and hosted infrastructure\. Wiz bounded cross-tenant content validation to its own accounts; broader repository exposure was a capability inference, not demonstrated theft of customer content\.

## Defensive use

Editorial lessons: preserve provenance when internal services exchange mixed-trust data, keep policy decisions independent of user-controlled metadata, and remove environment-inappropriate execution paths\. GitHub confirms input sanitization and removal of unnecessary code paths as remediation\. Review the vendor's maintained release guidance rather than treating a researcher version table as definitive\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Familiarity with service-to-service trust boundaries
- Basic authorization and serialization concepts

## Access and freshness

**Access cost at review:** free.

Public researcher and vendor articles readable without an account\.

**Reviewed:** 2026-10-03T06:29:29Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Researcher and vendor accounts reviewed\. This is historical educational evidence, not a finding that a current deployment is vulnerable\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-04-28; precision: day; basis: explicit; source: [Securing GitHub: Wiz Research uncovers Remote Code Execution in GitHub\.com and GitHub Enterprise Server \(CVE-2026-3854\)](<https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854>) (source ID: research). Researcher article publication and public disclosure\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No immutable article revision is identified; this field is not a product patch date\.
- **source displayed:** 2026-04-28; precision: day; basis: explicit; source: [Securing GitHub: Wiz Research uncovers Remote Code Execution in GitHub\.com and GitHub Enterprise Server \(CVE-2026-3854\)](<https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854>) (source ID: research).

## Caveats

- Technical precondition: an authenticated user needed repository push permission \(vendor\)\. Learning prerequisites above are editorial\.
- Wiz reports controlled cross-tenant validation with its own accounts and says it did not access other tenants' repository contents\. GitHub's investigation attributes observed activity to the researchers and reports no customer-data access, modification or exfiltration\.
- Wiz dates reporting and hosted remediation to March 4, 2026, Enterprise Server patch release to March 10, and disclosure to April 28\. GitHub corroborates hosted remediation on March 4; its article was updated April 29\.
- Remediation-version disagreement: Wiz lists 3\.19\.3 among fixed versions, while GitHub's updated guidance recommends 3\.19\.4 or later and newer patch levels across other branches\. The difference is preserved rather than resolved by inference; no independent patch verification was performed\.
- The exact award amount and payment settlement are undisclosed in the reviewed articles\. This educational resource does not qualify or promote the existing award-report candidate\.

## Sources and attribution

- [Securing GitHub: Wiz Research uncovers Remote Code Execution in GitHub\.com and GitHub Enterprise Server \(CVE-2026-3854\)](<https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854>) — Wiz Research; source ID: research; provenance: official primary; retrieved 2026-10-03T06:28:56Z; supports: summary, dates.
- [Securing the git push pipeline: Responding to a critical remote code execution vulnerability](<https://github.blog/security/securing-the-git-push-pipeline-responding-to-a-critical-remote-code-execution-vulnerability/>) — GitHub; source ID: vendor; provenance: official primary; retrieved 2026-10-03T06:29:29Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
