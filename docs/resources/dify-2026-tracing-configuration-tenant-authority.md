# Dify: telemetry destination changes carry tenant data-disclosure authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/dify-2026-tracing-configuration-tenant-authority.json>) · [Official resource](<https://www.zafran.io/resources/difytap-zafran-discovers-how-attackers-can-silently-wiretap-ai-data-across-tenants-on-a-platform-powering-1m-apps>)

**Publisher:** Zafran Labs  
**Authors:** Ido Shani; Gal Zaban  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Ai Security; Authorization  
**Defensive skills:** Model access-control invariants; Review AI authority boundaries; Verify remediation evidence; Threat-model integrations

## Original summary

Zafran’s tracing case, CVE-2026-41947, explains that console authentication did not bind configuration changes to the application’s tenant\. Traces contain prompts and responses, so changing telemetry routing also changes their recipients\. The researcher reports cross-tenant configuration control and resulting disclosure; the merged maintainer fix corroborates the missing tenant restriction\.

## Defensive use

The merged fix resolves applications under the authenticated tenant before tracing operations and returns the same denial as an absent application\. It covers configuration and tracing handlers and later adds cross-tenant regression coverage\. Editorial lesson: treat observability configuration as data-export authority, with authorization independent of ordinary application-client access\.

Educational reference only; linked material does not authorize testing unrelated systems.

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
