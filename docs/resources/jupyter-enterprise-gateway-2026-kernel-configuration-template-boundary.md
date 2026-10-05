# Jupyter Enterprise Gateway: keep kernel configuration outside template authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/jupyter-enterprise-gateway-2026-kernel-configuration-template-boundary.json>) · [Official resource](<https://github.com/jupyter-server/enterprise_gateway/security/advisories/GHSA-f49j-v924-fx9w>)

**Publisher:** Jupyter Enterprise Gateway maintainers  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Interpreter Boundaries; Cloud Security  
**Defensive skills:** Review input trust boundaries; Review cloud IAM boundaries; Verify remediation evidence

## Original summary

CVE-2026-44181 describes untrusted kernel-start configuration becoming Jinja2 template source during Kubernetes pod-name generation\. The advisory demonstrates template evaluation and operating-system execution inside the Enterprise Gateway pod\. Conceptual root cause: configuration data acquired server-side interpreter authority before the generated name was normalized\. This is server-side template injection \(SSTI\), explicitly classified as CWE-1336\.

## Defensive use

The advisory and 3\.3\.0 release identify that version as patched\. Editorial lesson: keep trusted template structure separate from external configuration and avoid evaluating configuration as template source\. Name normalization and output escaping do not establish that separation\. Review the deployed fixed version and its intended data-only substitution behavior\. Restricting gateway access and service-account authority provides defense in depth; neither replaces correction of the template boundary\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Data/code separation and server-side template concepts
- Kubernetes workload identities and configuration trust boundaries

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and supporting release history\.

**Reviewed:** 2026-10-05T00:33:17Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Advisory, release notes and remediation pull request reviewed\. No vulnerability reproduction, target testing or independent patch execution performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-03; precision: day; basis: explicit; source: [Jinja2 Template Server Side Template Injection resulting in Remote Code Execution](<https://github.com/jupyter-server/enterprise_gateway/security/advisories/GHSA-f49j-v924-fx9w>) (source ID: advisory). Explicit advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No educational-resource edition date established; software remediation chronology is separate\.
- **source displayed:** 2026-06-03; precision: day; basis: explicit; source: [Jinja2 Template Server Side Template Injection resulting in Remote Code Execution](<https://github.com/jupyter-server/enterprise_gateway/security/advisories/GHSA-f49j-v924-fx9w>) (source ID: advisory). The advisory header displays its publication date\.

## Caveats

- Applicability requires Kubernetes-backed Enterprise Gateway and the ability to supply kernel-start configuration\. The no-privileges severity rating does not establish universal deployment reachability\.
- The affected-version field states &gt;= v2\.0\.0rc2 without an upper bound; the patched-version field names 3\.3\.0\. Both source fields are retained rather than silently repairing the range\.
- Broader cluster impact depends on effective service-account permissions and deployment isolation\. Complete cluster compromise and production exploitation are not established by the published demonstration\.
- lresende published the advisory and is credited for remediation; ben-elttam is credited as Reporter\. No separate author byline was established, so authors remains empty\.
- The release notes link remediation pull request 1412, merged August 9, 2025\. Its merge date is remediation chronology, not this advisory's publication or an educational-resource edition date\.
- The release separately lists Kubernetes manifest injection as CVE-2026-44182; it is not the SSTI case summarized here\. No award qualification is established\. Learning prerequisites and generalized defensive guidance are editorial\.

## Sources and attribution

- [Jinja2 Template Server Side Template Injection resulting in Remote Code Execution](<https://github.com/jupyter-server/enterprise_gateway/security/advisories/GHSA-f49j-v924-fx9w>) — Jupyter Enterprise Gateway maintainers; source ID: advisory; provenance: official primary; retrieved 2026-10-05T00:29:13Z; supports: summary, dates.
- [Jupyter Enterprise Gateway 3\.3\.0](<https://github.com/jupyter-server/enterprise_gateway/releases/tag/v3.3.0>) — Jupyter Enterprise Gateway maintainers; source ID: release; provenance: official primary; retrieved 2026-10-05T00:28:57Z; supports: summary.
- [Fix pod-name substitution to avoid SSTI \(pull request 1412\)](<https://github.com/jupyter-server/enterprise_gateway/pull/1412>) — Jupyter Enterprise Gateway maintainers; source ID: remediation; provenance: official primary; retrieved 2026-10-05T00:29:13Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
