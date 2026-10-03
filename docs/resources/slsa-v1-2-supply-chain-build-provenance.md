# SLSA v1\.2: supply-chain security and build provenance

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/slsa-v1-2-supply-chain-build-provenance.json>) · [Official resource](<https://slsa.dev/spec/v1.2/>)

**Publisher:** SLSA Community  
**Authors:** Not identified in the reviewed record  
**Resource type:** Security Standard  
**Version:** 1\.2  
**Topics:** Software Supply Chain; Verification  
**Defensive skills:** Model build and release trust; Review artifact isolation; Review dependency provenance; Write bounded security evidence

## Original summary

Learn to assess software supply-chain assurance using distinct source and build tracks\. The build track progresses from recording provenance to authenticated hosted builds and stronger platform isolation\. Build provenance connects an artifact to its builder, inputs, and build definition so consumers can evaluate whether its production matches expectations\.

## Defensive use

Map documented build controls and provenance expectations to an approved architecture review; distinguish attestation presence from trusted verification\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic familiarity with version control and continuous integration
- Understanding of software artifacts, hashes, and digital-signature concepts

## Access and freshness

**Access cost at review:** free.

Official documentation was publicly readable at review time; implementation services can have separate costs\.

**Reviewed:** 2026-10-02T15:32:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Version-specific approved specification; stable entry point currently redirects to v1\.2\. Working Draft is separately labeled and was not treated as a stable release\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** 2025-11-24; precision: day; basis: explicit; source: [SLSA Community release announcement dated 24 November 2025](<https://slsa.dev/blog/2025/11/announce-slsa-v1.2>) (source ID: release).
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Build L1 provenance alone does not provide tamper protection\.
- The specification version is 1\.2, while the build-provenance predicate identifier remains https://slsa\.dev/provenance/v1; the page explains this major-version convention\.
- A recorded attestation is useful only within an explicit trust and verification model\.

## Related conceptual diagrams

- [Build evidence must match the artifact and trusted builder](<../diagram-gallery.md#build-artifact-provenance-boundary>)

## Sources and attribution

- [Official stable entry point redirects to v1\.2](<https://slsa.dev/spec/>) — SLSA Community; source ID: stable-entry; provenance: official primary; retrieved 2026-10-02T15:32:00Z; supports: version.
- [Version 1\.2 and Approved status](<https://slsa.dev/spec/v1.2/>) — SLSA Community; source ID: primary; provenance: official primary; retrieved 2026-10-02T15:32:00Z; supports: summary, version.
- [SLSA Community release announcement dated 24 November 2025](<https://slsa.dev/blog/2025/11/announce-slsa-v1.2>) — SLSA Community; source ID: release; provenance: official primary; retrieved 2026-10-02T15:32:00Z; supports: dates, version.
- [Build-level distinctions and provenance limitations](<https://slsa.dev/spec/v1.2/build-track-basics>) — SLSA Community; source ID: build-levels; provenance: official primary; retrieved 2026-10-02T15:32:00Z; supports: summary, version.
- [Build provenance model and predicate-version convention](<https://slsa.dev/spec/v1.2/build-provenance>) — SLSA Community; source ID: build-provenance; provenance: official primary; retrieved 2026-10-02T15:32:00Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
