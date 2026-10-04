# Microsoft compensating transactions: recovery must preserve valid concurrent state

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/microsoft-compensating-transaction-state-integrity.json>) · [Official resource](<https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction>)

**Publisher:** Microsoft Azure Architecture Center  
**Authors:** Not identified in the reviewed record  
**Resource type:** Architecture Guide  
**Version:** Not established in the reviewed record  
**Topics:** Business Logic and State Integrity  
**Defensive skills:** Reason about concurrent state; Threat-model integrations

## Original summary

Explains recovery after partial completion across services or data stores\. Compensation applies domain-specific corrective effects; restoring an earlier snapshot can overwrite valid concurrent changes\. Recovery can itself fail, and some committed effects cannot be meaningfully reversed\.

## Defensive use

Editorial lesson: distinguish an atomic transaction boundary from a process spanning independently committed operations\. Model completion evidence, compensable effects and irreversible commitments\. Preserve recovery progress and repeat-safe corrective actions while respecting concurrent work and business entitlements\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic distributed operations, eventual consistency and application state invariants

## Access and freshness

**Access cost at review:** free.

The official architecture article and its public source were readable without sign-in\.

**Reviewed:** 2026-10-04T05:52:30Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Official page, pinned first-party source and two later file changes reviewed\. Maintained living guidance without a numbered edition\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Original publication was not established\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No dated resource edition is identified\.
- **source displayed:** 2026-04-20; precision: day; basis: explicit; source: [Compensating Transaction pattern](<https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction>) (source ID: primary). Rendered page’s Last updated date; not original publication or latest repository modification\.

## Caveats

- Compensation does not guarantee restoration of the original state\. It is unsuitable where temporary inconsistency is unacceptable or valid recovery cannot be assured\.
- Recovery remains domain-specific and may require human intervention\. Repeat-safe recovery steps do not make irreversible commitments undoable or guarantee eventual completion\.
- The rendered page displays 2026-04-20; the pinned source metadata says 2026-04-16\. The reviewed August 14 and September 28, 2026 changes only update links in this file\. These are distinct maintenance signals, not publication or edition-release dates\.
- Architecture guidance, not an incident, vulnerability disclosure, implementation audit, bounty claim or testing authorization\.

## Sources and attribution

- [Compensating Transaction pattern](<https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction>) — Microsoft; source ID: primary; provenance: official primary; retrieved 2026-10-04T05:50:04Z; supports: summary, dates.
- [Compensating Transaction pattern source at reviewed revision](<https://github.com/MicrosoftDocs/architecture-center/blob/498e83a207cfd512b396489e95ed3f791b372364/docs/patterns/compensating-transaction.md>) — MicrosoftDocs; source ID: source-metadata; provenance: official primary; retrieved 2026-10-04T05:52:09Z; supports: summary, dates.
- [August 2026 idempotent-command link maintenance](<https://github.com/MicrosoftDocs/architecture-center/commit/d73cd1632ffa489eff78a16bba4d101c510a1810>) — MicrosoftDocs; source ID: august-link-maintenance; provenance: official primary; retrieved 2026-10-04T05:51:29Z; supports: dates.
- [September 2026 related-document link maintenance](<https://github.com/MicrosoftDocs/architecture-center/commit/498e83a207cfd512b396489e95ed3f791b372364>) — MicrosoftDocs; source ID: september-link-maintenance; provenance: official primary; retrieved 2026-10-04T05:51:29Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
