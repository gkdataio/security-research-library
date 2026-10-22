# GitHub Artifact Attestations: Provenance and Consumer Policy

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://docs.github.com/en/actions/concepts/security/artifact-attestations>) · [Canonical JSON](<../../data/resources/github-artifact-attestations.json>)

<a id="original-summary"></a>
## Main takeaway

GitHub's guide explains what signed artifact attestations say about a build, including its workflow, repository, organization, environment, commit, triggering event and OIDC identity information\. Consumers use those claims to decide whether an artifact meets their own acceptance rules\. The guide also explains how a software bill of materials can accompany build provenance\.

## Defensive use

Separate the question of where an artifact came from from whether its source and build process meet release requirements\. Compare the expected build identity with recorded provenance before accepting a release\. Treat claims from build infrastructure as evidence that still needs an explicit consumer policy\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** GitHub  
**Authors:** Not identified in the reviewed record  
**Resource type:** [Architecture Guide](<../resource-types.md#type-architecture-guide>)  
**Version:** Not established in the reviewed record  
**Topics:** [Software Supply Chain](<../resource-topics.md#topic-supply-chain>); [Identity](<../resource-topics.md#topic-identity>); [Verification](<../resource-topics.md#topic-verification>)  
**Defensive skills:** [Model build and release trust](<../skillsets.md#skill-pipeline-trust-modeling>); [Review dependency provenance](<../skillsets.md#skill-dependency-provenance>)

## Prerequisites

**Basis:** editorial guidance.

- Git commits and repositories
- Basic CI workflows
- Provenance and digital-signature concepts

## Access and freshness

**Access cost at review:** free.

Publicly accessible official documentation; no account required for reading\.

**Reviewed:** 2026-10-12T18:31:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Official primary source reviewed\. No explicit publication or revision date is displayed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No publication or revision date is displayed on the reviewed page\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No publication or revision date is displayed on the reviewed page\.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No publication or revision date is displayed on the reviewed page\.

## Caveats

- Generating attestations alone provides no benefit without verification, and attestations do not establish that code is secure\.
- Public repository attestations use public transparency infrastructure; GitHub’s private instance has no transparency log and only federates with GitHub Actions\.
- The page’s SLSA discussion explicitly refers to v1\.0\. Its claims should not be silently recast as v1\.2 certification\.

## Sources and attribution

- [Artifact attestations](<https://docs.github.com/en/actions/concepts/security/artifact-attestations>) — GitHub; source ID: github-attestations; provenance: official primary; retrieved 2026-10-12T18:31:00Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
