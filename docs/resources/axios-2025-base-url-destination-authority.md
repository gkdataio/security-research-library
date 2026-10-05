# Axios: URL construction does not establish destination authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/axios-2025-base-url-destination-authority.json>) · [Official resource](<https://github.com/axios/axios/security/advisories/GHSA-jr5f-v2jv-69x6>)

**Publisher:** Axios  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Web Foundations  
**Defensive skills:** Review input trust boundaries; Threat-model integrations; Review secrets containment; Verify remediation evidence

## Original summary

CVE-2025-27152 explicitly identifies possible SSRF when an application assumes baseURL confines destinations but accepts unvalidated caller-controlled URL input\. An absolute URL can select another destination; configured sensitive headers may then reach an unintended recipient\. The contained demonstration returns content from a different destination; it does not establish production compromise\. Conceptual boundary: constructing a URL and authorizing its destination are separate responsibilities\.

## Defensive use

Current official Axios documentation treats baseURL as a convenience rather than an access-control boundary\. Absolute destinations can override it by default; disabling that behavior does not constrain relative-path normalization\. Editorial lesson: validate the resolved destination against application policy, scope credentials to their intended recipients, and apply least-privilege egress controls\. Review the selected transport and deployed version together\. A software upgrade or configuration toggle alone does not make arbitrary caller input safe\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- URL resolution and the distinction between construction and destination authorization
- Server-side HTTP clients and credential-bearing request configuration

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory, official releases and documentation, and GitHub Advisory Database metadata\.

**Reviewed:** 2026-10-05T01:43:39Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Read the maintainer advisory, database entry, tagged changelog, release notes and current documentation\. The Axios repository links axios\.rest as its official documentation\. No reproduction, target testing or independent patch execution performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2025-03-07; precision: day; basis: explicit; source: [Axios absolute-URL security advisory GHSA-jr5f-v2jv-69x6](<https://github.com/axios/axios/security/advisories/GHSA-jr5f-v2jv-69x6>) (source ID: advisory). Original maintainer-advisory publication\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No educational-resource edition date established; software release events remain separate\.
- **source displayed:** 2025-03-07; precision: day; basis: explicit; source: [Axios absolute-URL security advisory GHSA-jr5f-v2jv-69x6](<https://github.com/axios/axios/security/advisories/GHSA-jr5f-v2jv-69x6>) (source ID: advisory). Publication date shown on the selected primary advisory\.

## Caveats

- SSRF requires server-side execution and unvalidated caller influence over the requested URL\. Credential exposure additionally requires sensitive request configuration and delivery to an unintended recipient\. The advisory also covers client-side use, which alone is not SSRF\.
- The maintainer lists affected versions &lt;=1\.7\.9 and &lt;=0\.29\.0, while the database lists &gt;=1\.0\.0, &lt;1\.8\.2 and &lt;0\.30\.0\. Both identify 1\.8\.2 and 0\.30\.0 as patched\. The range disagreement is preserved; intervening versions are not silently classified\.
- The v1\.8\.2 release and tagged changelog describe HTTP-adapter support for the absolute-URL option on March 7, 2025\. The v0\.30\.0 release, dated March 26, 2025, identifies the backport\. These are software events, not educational-resource edition dates or claims about the latest safe release\.
- jasonsaayman published the advisory; lambdasawa is credited as Reporter\. No separate author byline was established, so authors remains empty\.
- The database shows a November 27, 2025 update; it does not change the original March 7 publication\. Current request-configuration guidance is living documentation, not proof of what the March release documented\.
- No production incident, account takeover or qualifying individual award is established\. The reported demonstration and conditional credential risk remain separate\. Learning prerequisites and generalized design guidance are editorial; this educational case grants no testing authorization\.

## Sources and attribution

- [Axios absolute-URL security advisory GHSA-jr5f-v2jv-69x6](<https://github.com/axios/axios/security/advisories/GHSA-jr5f-v2jv-69x6>) — Axios; source ID: advisory; provenance: official primary; retrieved 2026-10-05T01:41:40Z; supports: summary, dates.
- [GitHub Advisory Database entry for CVE-2025-27152](<https://github.com/advisories/GHSA-jr5f-v2jv-69x6>) — GitHub Advisory Database; source ID: advisory-database; provenance: official primary; retrieved 2026-10-05T01:42:13Z; supports: summary, dates.
- [Axios v1\.8\.2 release notes](<https://github.com/axios/axios/releases/tag/v1.8.2>) — Axios; source ID: release-1-8-2; provenance: official primary; retrieved 2026-10-05T01:41:40Z; supports: summary.
- [Axios tagged changelog for v1\.8\.2](<https://github.com/axios/axios/blob/v1.8.2/CHANGELOG.md>) — Axios; source ID: changelog-1-8-2; provenance: official primary; retrieved 2026-10-05T01:42:31Z; supports: summary, dates.
- [Axios v0\.30\.0 backport release notes](<https://github.com/axios/axios/releases/tag/v0.30.0>) — Axios; source ID: release-0-30-0; provenance: official primary; retrieved 2026-10-05T01:43:17Z; supports: summary, dates.
- [Axios request configuration: destination and base-URL semantics](<https://axios.rest/pages/advanced/request-config>) — Axios; source ID: request-config; provenance: official primary; retrieved 2026-10-05T01:42:13Z; supports: summary.
- [Axios official repository and documentation links](<https://github.com/axios/axios>) — Axios; source ID: project; provenance: official primary; retrieved 2026-10-05T01:42:02Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
