# MLflow: destination validation must remain bound to the actual connection

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/mlflow/mlflow/security/advisories/GHSA-7gwp-5pfp-969j>) · [Canonical JSON](<../../data/resources/mlflow-2026-webhook-connection-destination-integrity.json>)

<a id="original-summary"></a>
## Main takeaway

MLflow's initial webhook destination check did not necessarily validate the address used for the actual connection\. The repair for CVE-2026-64849 explains that validation and connection setup could make different address decisions\. The lesson is to enforce destination restrictions when the connection is used, rather than rely only on an earlier check\.

## Defensive use

The connection-fix PR moves enforcement to the connected peer before TLS or HTTP exchange, retaining initial validation as defense in depth\. The classification-fix PR later gives initial and connection-time checks the same address-normalization policy\. Editorial lesson: define one destination invariant, enforce it at the point of use, and keep representation handling consistent across layers\. Review deployment controls and later remediation evidence together; historical fixed-version labels do not prove comprehensive or current protection\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** MLflow  
**Authors:** Not identified in the reviewed record  
**Resource type:** [Maintainer Advisory](<../resource-types.md#type-maintainer-advisory>)  
**Version:** Not established in the reviewed record  
**Topics:** [Web Foundations](<../resource-topics.md#topic-web-foundations>)  
**Defensive skills:** [Review input trust boundaries](<../skillsets.md#skill-untrusted-input-handling>); [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>); [Verify remediation evidence](<../skillsets.md#skill-patch-verification>); [Write bounded security evidence](<../skillsets.md#skill-defensive-evidence-writing>)

## Prerequisites

**Basis:** editorial guidance.

- Server-side HTTP clients and the distinction between configured destinations and connected peers
- Time-of-check versus time-of-use reasoning and consistent address classification

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory, GitHub Advisory Database entry, repair pull requests and release notes\.

**Reviewed:** 2026-10-05T21:43:33Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Read the original advisory, the differing database metadata, repair and hardening PRs, backport and official releases\. No reproduction, target testing or independent patch verification performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08-02; precision: day; basis: explicit; source: [MLflow webhook security advisory GHSA-7gwp-5pfp-969j](<https://github.com/mlflow/mlflow/security/advisories/GHSA-7gwp-5pfp-969j>) (source ID: advisory). Original repository-advisory publication; software releases and database events remain separate\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No educational-resource edition date established\. Software patch chronology is recorded in the caveats\.
- **source displayed:** 2026-08-02; precision: day; basis: explicit; source: [MLflow webhook security advisory GHSA-7gwp-5pfp-969j](<https://github.com/mlflow/mlflow/security/advisories/GHSA-7gwp-5pfp-969j>) (source ID: advisory). Publication date displayed by the selected primary advisory\.

## Caveats

- The described unauthenticated case requires a reachable OSS tracking server with SQL-backed webhooks and authentication absent\. It does not establish exposure for every deployment\.
- The repository advisory lists &gt;=3\.10\.0, &lt;3\.15\.0 as affected; the GitHub Advisory Database lists &gt;=3\.3\.0, &lt;3\.15\.0\. Both name 3\.15\.0 as the initial patched version\. The lower-bound disagreement remains unresolved here; versions before 3\.10\.0 must not be assumed unaffected\.
- The advisory reports a synthetic local-service response disclosure on 3\.13\.0\. Production compromise, actual cloud credential theft and service shutdown are not established by that demonstration\.
- Connection-fix PR \#24258 merged July 2, 2026; release 3\.15\.0 on July 31 includes it\. These software events precede the August 2 advisory publication\.
- Classification-fix PR \#25568 merged September 3, 2026; PR \#25578 backported it for 3\.16\.0 on September 4, the release date\. This follow-on hardening addresses address representations missed by the earlier classifier\. It qualifies the initial patch claim and is remediation context for this single case, not a separate counted finding or a guarantee about the latest safe release\.
- PattaraS published the advisory\. Credits name freeman-bb as Reporter and y011d4, ibondarenko1, h1-mrz and th3cyb3rc0p as Finders; the narrative separately credits AUTHENSOR with independent discovery\. No separate narrative-author byline was established, so authors remains empty\.
- The database records its own publication and review on August 17, 2026 and an October 2 update; neither replaces the original August 2 publication\. Its Analyst credit for cwchong is distinct from the repository Reporter and Finder credits\.
- No qualifying individual award is established\. Learning prerequisites and generalized design guidance are editorial\. This educational resource grants no testing authorization\.

## Sources and attribution

- [MLflow webhook security advisory GHSA-7gwp-5pfp-969j](<https://github.com/mlflow/mlflow/security/advisories/GHSA-7gwp-5pfp-969j>) — MLflow; source ID: advisory; provenance: official primary; retrieved 2026-10-05T21:41:13Z; supports: summary, dates.
- [GitHub Advisory Database entry for CVE-2026-64849](<https://github.com/advisories/GHSA-7gwp-5pfp-969j>) — GitHub Advisory Database; source ID: advisory-database; provenance: official primary; retrieved 2026-10-05T21:42:50Z; supports: summary, dates.
- [MLflow PR \#24258: connection-time webhook destination protection](<https://github.com/mlflow/mlflow/pull/24258>) — MLflow; source ID: connection-fix; provenance: official primary; retrieved 2026-10-05T21:41:13Z; supports: summary, dates.
- [MLflow 3\.15\.0 release notes](<https://github.com/mlflow/mlflow/releases/tag/v3.15.0>) — MLflow; source ID: release-3-15-0; provenance: official primary; retrieved 2026-10-05T21:41:45Z; supports: summary, dates.
- [MLflow PR \#25568: consistent address classification](<https://github.com/mlflow/mlflow/pull/25568>) — MLflow; source ID: classification-fix; provenance: official primary; retrieved 2026-10-05T21:41:37Z; supports: summary, dates.
- [MLflow PR \#25578: address-classification hardening backport](<https://github.com/mlflow/mlflow/pull/25578>) — MLflow; source ID: classification-backport; provenance: official primary; retrieved 2026-10-05T21:42:33Z; supports: summary, dates.
- [MLflow 3\.16\.0 release notes](<https://github.com/mlflow/mlflow/releases/tag/v3.16.0>) — MLflow; source ID: release-3-16-0; provenance: official primary; retrieved 2026-10-05T21:41:45Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
