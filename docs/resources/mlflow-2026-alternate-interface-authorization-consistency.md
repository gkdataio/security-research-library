# MLflow: authorization must survive alternate resource interfaces

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/mlflow-2026-alternate-interface-authorization-consistency.json>) · [Official resource](<https://tachyon.so/blog/cve-2025-14297-mlflow-authorization-bypass>)

**Publisher:** Tachyon  
**Authors:** Aakash Japi  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Web Foundations  
**Defensive skills:** Model access-control invariants; Threat-model integrations; Verify remediation evidence; Write bounded security evidence

## Original summary

Tachyon’s 2026 account of CVE-2025-14297 describes resource permissions depending on incomplete interface registration\. Authentication could succeed while a missing authorization mapping permitted resource access\. The researcher demonstrates restricted artifact reads and describes unauthorized writes and metadata access; the maintainer’s artifact-interface change corroborates a concrete enforcement gap\.

## Defensive use

Document one actor/action/resource policy shared by all interfaces\. Treat new helper interfaces as additions to the authorization model, and make missing enforcement fail closed\. Compare remediation claims with the actual maintainer change: the reviewed artifact patch aligns alternate interface recognition with permission enforcement\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Authentication versus object-level authorization
- Applications with multiple interfaces to shared resources

## Access and freshness

**Access cost at review:** free.

Public primary sources readable without an account\.

**Reviewed:** 2026-10-03T07:19:04Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed primary disclosure and maintainer corroboration; no independent vulnerability reproduction performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-02-03; precision: day; basis: explicit; source: [CVE-2025-14297: MLflow Authorization Bypass](<https://tachyon.so/blog/cve-2025-14297-mlflow-authorization-bypass>) (source ID: research). Publication of the detailed researcher article, not initial vulnerability reporting or first public disclosure\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Artifact enforcement patch merged January 19, 2026; the first containing release was not established\.
- **source displayed:** 2026-02-03; precision: day; basis: explicit; source: [CVE-2025-14297: MLflow Authorization Bypass](<https://tachyon.so/blog/cve-2025-14297-mlflow-authorization-bypass>) (source ID: research). Article publication date\.

## Caveats

- The researcher limits exposure to self-hosted OSS basic-auth deployments with authenticated non-admin users; Databricks-managed MLflow is excluded\.
- Downstream code execution is a conditional modeled consequence in the article, not demonstrated production compromise or an automatic result of data access\.
- The article links a GraphQL commit that adds an authorization configuration switch; that commit alone does not establish the original GraphQL enforcement implementation or its complete patch chronology\.
- The maintainer artifact patch merged January 19, 2026, separately from February 3 publication\. Exact affected-version and first-fixed-release bounds were not established from reviewed primary sources\.
- The underlying finding predates this article; 2026 labels the detailed educational publication\. No bounty amount or independent exploit verification is claimed\.

## Sources and attribution

- [CVE-2025-14297: MLflow Authorization Bypass](<https://tachyon.so/blog/cve-2025-14297-mlflow-authorization-bypass>) — Tachyon; source ID: research; provenance: official primary; retrieved 2026-10-03T07:19:04Z; supports: summary, dates.
- [Enforce authorization on AJAX proxy artifact APIs](<https://github.com/mlflow/mlflow/pull/20035>) — MLflow; source ID: artifact-fix; provenance: official primary; retrieved 2026-10-03T07:19:04Z; supports: summary, dates.
- [Add an env var for controlling whether to enable GraphQL routes authorization](<https://github.com/mlflow/mlflow/commit/87dc3fcab10bb79980b33d5485bb60fc1ef76f6d>) — MLflow; source ID: graphql-change; provenance: official primary; retrieved 2026-10-03T07:19:04Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
