# NIST SSDF 1\.1: Component Governance and Release Provenance

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/nist-ssdf-1-1-dependency-governance.json>) · [Official resource](<https://csrc.nist.gov/pubs/sp/800/218/final>)

**Publisher:** NIST  
**Authors:** Murugiah Souppaya; Karen Scarfone; Donna Dodson  
**Resource type:** Implementation Guide  
**Version:** SSDF 1\.1 \(NIST SP 800-218\)  
**Topics:** Software Supply Chain; Verification  
**Defensive skills:** Review dependency provenance; Model build and release trust

## Original summary

Provides lifecycle practices for acquiring, maintaining, and assessing software components\. PW\.4\.1 and PW\.4\.4 cover component selection, organizational requirements, ongoing vulnerability and maintenance status, and integrity\. PS\.3\.2 connects release records to component provenance\.

## Defensive use

Give each dependency an owner, acceptance requirements, provenance records, and a plan for maintenance or replacement\. Revisit these decisions throughout the component’s lifetime\. Make the boundary between external supplier evidence and the organization’s own release decision explicit\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic dependency management
- Software development lifecycle and release familiarity

## Access and freshness

**Access cost at review:** free.

Publicly accessible official documentation; no account required for reading\.

**Reviewed:** 2026-10-12T18:31:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

The final SSDF 1\.1 resource and current NIST publication index were reviewed\. The index separately lists SSDF 1\.2 as an Initial Public Draft\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2022-02-03; precision: day; basis: explicit; source: [Secure Software Development Framework: Publications](<https://csrc.nist.gov/projects/ssdf/publications>) (source ID: nist-ssdf-index). NIST’s project publication index explicitly lists the release date of the final SP 800-218\.
- **version released:** 2022-02-03; precision: day; basis: explicit; source: [Secure Software Development Framework: Publications](<https://csrc.nist.gov/projects/ssdf/publications>) (source ID: nist-ssdf-index). Release date of this SSDF 1\.1 resource edition, not a software patch date\.
- **source displayed:** 2022-02; precision: month; basis: explicit; source: [Secure Software Development Framework \(SSDF\) Version 1\.1: Recommendations for Mitigating the Risk of Software Vulnerabilities](<https://csrc.nist.gov/pubs/sp/800/218/final>) (source ID: nist-ssdf-landing). The resource landing page displays Date Published: February 2022\.

## Caveats

- This is a risk-based high-level framework, not a product certification or an exhaustive technical recipe\.
- At review, NIST lists SSDF 1\.1 as Final and SSDF 1\.2 as an Initial Public Draft dated 2025-12-17\. The draft’s status and dates must not be merged into this edition’s record\.

## Sources and attribution

- [Secure Software Development Framework \(SSDF\) Version 1\.1: Recommendations for Mitigating the Risk of Software Vulnerabilities](<https://csrc.nist.gov/pubs/sp/800/218/final>) — NIST; source ID: nist-ssdf-landing; provenance: official primary; retrieved 2026-10-12T18:31:00Z; supports: summary, version, dates.
- [Secure Software Development Framework \(SSDF\) Version 1\.1: Recommendations for Mitigating the Risk of Software Vulnerabilities](<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf>) — NIST; source ID: nist-ssdf-pdf; provenance: official primary; retrieved 2026-10-12T18:31:00Z; supports: summary, version.
- [Secure Software Development Framework: Publications](<https://csrc.nist.gov/projects/ssdf/publications>) — NIST; source ID: nist-ssdf-index; provenance: official primary; retrieved 2026-10-12T18:31:00Z; supports: version, dates.
- [Secure Software Development Framework \(SSDF\) Version 1\.2: Initial Public Draft](<https://csrc.nist.gov/pubs/sp/800/218/r1/ipd>) — NIST; source ID: nist-ssdf-draft; provenance: official primary; retrieved 2026-10-12T18:31:00Z; supports: version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
