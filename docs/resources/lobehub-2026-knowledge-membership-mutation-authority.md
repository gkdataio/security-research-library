# LobeHub: knowledge-base membership changes require ownership authorization

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/lobehub-2026-knowledge-membership-mutation-authority.json>) · [Official resource](<https://github.com/lobehub/lobehub/security/advisories/GHSA-j7xp-4mg9-x28r>)

**Publisher:** LobeHub  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Ai Security; Authorization  
**Defensive skills:** Model access-control invariants; Review AI authority boundaries; Verify remediation evidence

## Original summary

The maintainer advisory attributes cross-user knowledge-base file removal to an omitted ownership restriction in a database mutation\. Its reported demonstration shows one deletion result\. The boundary is between being authenticated and being authorized to change another user’s retrieval corpus\.

## Defensive use

Editorial review principle: enforce ownership at the mutation, including every relationship being removed\. Random identifiers reduce accidental discovery but do not prove permission\. Review negative cross-owner cases and verify which underlying objects a removal actually changes\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Object ownership and relationship-level authorization
- Retrieval-augmented generation knowledge-base lifecycle

## Access and freshness

**Access cost at review:** free.

Public primary-source disclosure\.

**Reviewed:** 2026-10-03T14:59:14Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Public primary sources reviewed; no software execution or deployment testing\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-01-19; precision: day; basis: explicit; source: [IDOR in Knowledge Base File Removal Allows Cross User File Deletion](<https://github.com/lobehub/lobehub/security/advisories/GHSA-j7xp-4mg9-x28r>) (source ID: advisory). Displayed publication date of the primary educational source; not software patch timing\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separately versioned educational edition established\.
- **source displayed:** 2026-01-19; precision: day; basis: explicit; source: [IDOR in Knowledge Base File Removal Allows Cross User File Deletion](<https://github.com/lobehub/lobehub/security/advisories/GHSA-j7xp-4mg9-x28r>) (source ID: advisory). Displayed publication date of the primary educational source; not software patch timing\.

## Caveats

- The advisory credits DenizParlak as Reporter but does not display an explicit author byline\. Reporter credit alone does not establish advisory authorship, so named authors remain unestablished\.
- CVE-2026-23522 requires authentication and knowledge of both relevant identifiers according to the narrative; its displayed severity vector instead says no privileges\. Preserve that discrepancy\.
- The source lists versions through v2\.0\.0-next\.192 as affected and v2\.0\.0-next\.193 as patched; it supplies no patch date or implementation detail\.
- Reported removal could disrupt retrieval\. Permanent erasure of underlying stored documents, production compromise and an award are not independently established\.
- Conceptual defensive summary only; public disclosure grants no testing authorization\.

## Sources and attribution

- [IDOR in Knowledge Base File Removal Allows Cross User File Deletion](<https://github.com/lobehub/lobehub/security/advisories/GHSA-j7xp-4mg9-x28r>) — LobeHub; source ID: advisory; provenance: official primary; retrieved 2026-10-03T14:59:14Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
