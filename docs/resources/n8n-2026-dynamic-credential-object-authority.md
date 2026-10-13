# n8n Dynamic Credentials: authorize credential lifecycle operations

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/n8n-io/n8n/security/advisories/GHSA-2j5h-858j-5mpf>) · [Canonical JSON](<../../data/resources/n8n-2026-dynamic-credential-object-authority.json>)

<a id="original-summary"></a>
## Main takeaway

n8n's maintainer advisory reports missing ownership and scope checks in authenticated Dynamic Credentials operations \(CVE-2026-54305\)\. The reported effects include unauthorized access to credential metadata, replacement of an OAuth identity and token revocation; later integration runs may use the replacement identity\. The advisory does not establish exploitation in production\.

## Defensive use

Apply object authorization consistently to discovery, authorization and revocation, including indirect workflow references\. Maintainers list fixes in 1\.123\.55, 2\.25\.7 and 2\.26\.2\. Restricting access to trusted users or disabling the feature is temporary mitigation, explicitly not full remediation\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** n8n  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; API Security  
**Defensive skills:** Model access-control invariants; Review identity lifecycle; Threat-model integrations

## Prerequisites

**Basis:** editorial guidance.

- Basic federation and object-level authorization concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory\.

**Reviewed:** 2026-10-03T11:49:44Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory reviewed; no immutable educational edition established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-10; precision: day; basis: explicit; source: [Cross-Tenant Credential Takeover via Dynamic Credentials EE Endpoints](<https://github.com/n8n-io/n8n/security/advisories/GHSA-2j5h-858j-5mpf>) (source ID: maintainer). Advisory publication, not software patch release\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-06-10; precision: day; basis: explicit; source: [Cross-Tenant Credential Takeover via Dynamic Credentials EE Endpoints](<https://github.com/n8n-io/n8n/security/advisories/GHSA-2j5h-858j-5mpf>) (source ID: maintainer). Advisory publication, not software patch release\.

## Caveats

- Requires an Enterprise instance with Dynamic Credentials enabled and an authenticated session, without requiring project membership or credential sharing\.
- Jubke is the publishing account; Solidscripting and Har1sh-k are credited reporters\. Article authorship is not established\.
- Impact statements lack separate observed-versus-modeled demonstrations\. Exfiltration and persistence remain maintainer-described consequences\.
- Fixed versions apply within respective release lines; software release dates are not established\.
- Distinct from the existing refresh-grant audience-binding resource\.

## Sources and attribution

- [Cross-Tenant Credential Takeover via Dynamic Credentials EE Endpoints](<https://github.com/n8n-io/n8n/security/advisories/GHSA-2j5h-858j-5mpf>) — n8n; source ID: maintainer; provenance: official primary; retrieved 2026-10-03T11:49:44Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
