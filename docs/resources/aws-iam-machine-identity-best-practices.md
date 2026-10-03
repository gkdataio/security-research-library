# AWS IAM security best practices for workload identities

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/aws-iam-machine-identity-best-practices.json>) · [Official resource](<https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html>)

**Publisher:** Amazon Web Services  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Cloud Security; Identity; Authorization  
**Defensive skills:** Review cloud IAM boundaries; Review machine identities; Review identity lifecycle; Review secrets containment

## Original summary

Use this guide to review machine identity design: favor short-lived role credentials for workloads, limit permissions to required actions and resources, and retire unnecessary access\. It also explains policy validation, access reviews, and organizational guardrails that help keep workload access aligned with its purpose\.

## Defensive use

Compare an owned workload’s documented identity lifecycle and minimum permission needs with the guide, recording unnecessary access for review\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic understanding of cloud workloads, roles, and identity policies
- Familiarity with authentication versus authorization

## Access and freshness

**Access cost at review:** free.

Official documentation was publicly readable at review time; implementation services can have separate costs\.

**Reviewed:** 2026-10-02T15:32:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Living guidance checked on the verification date; no numerical release or documented update date claimed

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- AWS-managed policies may need further narrowing for a specific workload\.
- Organization-level guardrails constrain permissions; they do not grant access by themselves\.

## Related conceptual diagrams

- [Keep workload authority tenant-scoped](<../diagram-gallery.md#workload-identity-tenant-scope>)

## Sources and attribution

- [Temporary workload credentials, least privilege, access cleanup, policy validation, and permissions guardrails](<https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html>) — Amazon Web Services; source ID: primary; provenance: official primary; retrieved 2026-10-02T15:32:00Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
