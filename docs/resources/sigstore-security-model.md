# Sigstore Security Model

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/sigstore-security-model.json>) · [Official resource](<https://docs.sigstore.dev/about/security/>)

**Publisher:** Sigstore  
**Authors:** Not identified in the reviewed record  
**Resource type:** Architecture Guide  
**Version:** Not established in the reviewed record  
**Topics:** Software Supply Chain; Identity; Verification  
**Defensive skills:** Model build and release trust; Review machine identities

## Original summary

Explains how identity-based artifact signing combines an OIDC issuer and subject, Fulcio’s short-lived certificates, a managed trust root, and Rekor’s auditable signature history\. Identity certification, artifact integrity, and transparency are separate guarantees with different dependencies\.

## Defensive use

Identify the expected publisher or workload and its issuer, document which certificate authority and log are trusted, and assign responsibility for detecting unexpected signing events\. Trace the trust boundary from identity issuer through certificate and artifact to the consumer’s acceptance policy\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic hashes and digital signatures
- Familiarity with CI and workload identity

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

- A compromised identity issuer or certificate authority can issue unauthorized certificates\. Transparency makes misuse detectable only when someone monitors the logs\.
- Signing is not a code-quality assessment; consumers still need an acceptance policy\.

## Sources and attribution

- [Security Model](<https://docs.sigstore.dev/about/security/>) — Sigstore; source ID: sigstore-security; provenance: official primary; retrieved 2026-10-12T18:31:00Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
