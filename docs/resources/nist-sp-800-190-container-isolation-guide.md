# NIST SP 800-190: Application Container Security Guide

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://csrc.nist.gov/pubs/sp/800/190/final>) · [Canonical JSON](<../../data/resources/nist-sp-800-190-container-isolation-guide.json>)

<a id="original-summary"></a>
## Main takeaway

NIST's container security guide explains the risks of sharing an operating-system kernel and the need to separate workloads and limit runtime permissions\. It covers images, registries, orchestration, runtimes and hosts, including maintenance throughout their lifecycle\.

## Defensive use

Build an owned environment’s boundary-and-responsibility map, then compare product-specific controls with current vendor guidance\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** National Institute of Standards and Technology  
**Authors:** Murugiah Souppaya; John Morello; Karen Scarfone  
**Resource type:** [Architecture Guide](<../resource-types.md#type-architecture-guide>)  
**Version:** SP 800-190 \(2017 final\)  
**Topics:** [Cloud Security](<../resource-topics.md#topic-cloud-security>); [Software Supply Chain](<../resource-topics.md#topic-supply-chain>)  
**Defensive skills:** [Threat-model integrations](<../skillsets.md#skill-integration-threat-modeling>); [Review dependency provenance](<../skillsets.md#skill-dependency-provenance>); [Verify remediation evidence](<../skillsets.md#skill-patch-verification>)

## Prerequisites

**Basis:** publisher explicit.

- Operating-system, networking and security expertise
- Familiarity with hypervisors and virtual machines

## Access and freshness

**Access cost at review:** free.

Official publication and PDF are publicly available\.

**Reviewed:** 2026-10-02T17:52:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Historical 2017 final publication\. Reviewed catalog, audience, executive summary, and container/runtime/host countermeasure sections; no claim of a new 2026 edition\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2017-09-25; precision: day; basis: explicit; source: [NIST SP 800-190 publication catalog](<https://csrc.nist.gov/pubs/sp/800/190/final>) (source ID: catalog). Exact final-publication date from NIST document history; the PDF cover gives September 2017\.
- **version released:** 2017-09-25; precision: day; basis: explicit; source: [NIST SP 800-190 publication catalog](<https://csrc.nist.gov/pubs/sp/800/190/final>) (source ID: catalog).
- **source displayed:** 2017-09; precision: month; basis: explicit; source: [NIST SP 800-190 publication catalog](<https://csrc.nist.gov/pubs/sp/800/190/final>) (source ID: catalog). Catalog publication label\. The September 2020 planning note concerns a translation, not a new edition\.

## Caveats

- Historical architectural guidance; use current vendor documentation for versions and configuration details\.
- The guide itself advises consulting newer material because container technology changes\.

## Sources and attribution

- [NIST SP 800-190 publication catalog](<https://csrc.nist.gov/pubs/sp/800/190/final>) — NIST; source ID: catalog; provenance: official primary; retrieved 2026-10-02T17:52:00Z; supports: summary, version, dates.
- [NIST SP 800-190, audience and sections 4\.4–4\.5](<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf>) — NIST; source ID: publication; provenance: official primary; retrieved 2026-10-02T17:52:00Z; supports: summary, prerequisites, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
