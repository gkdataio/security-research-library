# Dify: telemetry destination changes carry tenant data-disclosure authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://www.zafran.io/resources/difytap-zafran-discovers-how-attackers-can-silently-wiretap-ai-data-across-tenants-on-a-platform-powering-1m-apps>) · [Canonical JSON](<../../data/resources/dify-2026-tracing-configuration-tenant-authority.json>)

<a id="original-summary"></a>
## Main takeaway

Dify let console users change tracing settings without checking that the application belonged to their tenant\. Zafran's CVE-2026-41947 research reports cross-tenant control and disclosure of traces containing prompts and responses, because changing the tracing destination changes who receives that data\. The merged maintainer fix confirms the missing tenant restriction\.

## Defensive use

The merged fix resolves applications under the authenticated tenant before tracing operations and returns the same denial as an absent application\. It covers configuration and tracing handlers and later adds cross-tenant regression coverage\. Editorial lesson: treat observability configuration as data-export authority, with authorization independent of ordinary application-client access\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Zafran Labs  
**Authors:** Ido Shani; Gal Zaban  
**Resource type:** [Research Paper](<../resource-types.md#type-research-paper>)  
**Version:** Not established in the reviewed record  
**Topics:** [Ai Security](<../resource-topics.md#topic-ai-security>); [Authorization](<../resource-topics.md#topic-authorization>)  
**Defensive skills:** [Model access-control invariants](<../skillsets.md#skill-authorization-modeling>); [Review AI authority boundaries](<../skillsets.md#skill-ai-authority-boundaries>); [Verify remediation evidence](<../skillsets.md#skill-patch-verification>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>)

## Prerequisites

**Basis:** editorial guidance.

- Tenant-scoped object authorization
- AI telemetry flows and external data recipients

## Access and freshness

**Access cost at review:** free.

Public primary-source disclosure\.

**Reviewed:** 2026-10-03T14:59:14Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Public primary sources reviewed; no software execution or deployment testing\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-22; precision: day; basis: explicit; source: [DifyTap research](<https://www.zafran.io/resources/difytap-zafran-discovers-how-attackers-can-silently-wiretap-ai-data-across-tenants-on-a-platform-powering-1m-apps>) (source ID: research). Displayed publication date of the primary educational source; not software patch timing\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separately versioned educational edition established\.
- **source displayed:** 2026-06-22; precision: day; basis: explicit; source: [DifyTap research](<https://www.zafran.io/resources/difytap-zafran-discovers-how-attackers-can-silently-wiretap-ai-data-across-tenants-on-a-platform-powering-1m-apps>) (source ID: research). Displayed publication date of the primary educational source; not software patch timing\.

## Caveats

- The detailed research requires a console account and an application identifier\. Its introductory unauthenticated framing must not replace these stated prerequisites\. Application-client access is not administration permission\.
- The researcher’s article covers four findings; this resource covers only tracing authorization\. No production victim, exposure count or individual award is established\.
- The fix merged May 14, 2026\. Official v1\.14\.2 notes include it; the researcher dates that software release May 19, 2026 and discusses v1\.15\.0 as the broader four-finding remediation\. These are not educational-edition dates\.
- The research timeline also places an April 2025 last-report publication before its December 2025 first report, and lists a June 25 release after its displayed June 22 publication\. Those inconsistent dates are not silently repaired\.
- No regression tests were executed in this review\. Public disclosure grants no testing authorization\.

## Sources and attribution

- [DifyTap research](<https://www.zafran.io/resources/difytap-zafran-discovers-how-attackers-can-silently-wiretap-ai-data-across-tenants-on-a-platform-powering-1m-apps>) — Zafran Labs; source ID: research; provenance: official primary; retrieved 2026-10-03T14:59:14Z; supports: summary, dates.
- [Tenant-scoping fix for tracing configuration](<https://github.com/langgenius/dify/pull/35793>) — Dify; source ID: fix; provenance: official primary; retrieved 2026-10-03T14:59:14Z; supports: summary, dates.
- [Dify v1\.14\.2 release notes](<https://github.com/langgenius/dify/releases/tag/1.14.2>) — Dify; source ID: release; provenance: official primary; retrieved 2026-10-03T14:59:14Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
