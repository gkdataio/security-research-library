# Chromium Rule of Two: input trust, memory safety and privilege

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/rule-of-2.md>) · [Canonical JSON](<../../data/resources/chromium-rule-of-two-input-isolation.json>)

<a id="original-summary"></a>
## Main takeaway

Chromium's Rule of Two says to avoid combining untrusted input, memory-unsafe code and high privilege in one component\. The architecture policy covers safer parsing, separating privileges and reviewing unsafe code even when it sits behind a safe interface\.

## Defensive use

For an owned component, map input origin, language guarantees and execution privilege\. Keep semantic authorization separate from successful parsing\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Chromium Project  
**Authors:** Not identified in the reviewed record  
**Resource type:** Architecture Guide  
**Version:** Not established in the reviewed record  
**Topics:** Memory Safety and Process Isolation; Verification  
**Defensive skills:** Review memory-safety assumptions; Review parsing and serialization; Review client isolation; Review input trust boundaries

## Prerequisites

**Basis:** editorial guidance.

- Basic understanding of parsing, process privileges and memory lifetime

## Access and freshness

**Access cost at review:** free.

Official source-tree documentation is publicly readable\.

**Reviewed:** 2026-10-02T17:52:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Current HEAD documentation reviewed; no original publication or last-update date inferred\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- Memory safety does not establish data trust or permission to perform an operation\.
- Chromium-specific exceptions are not blanket guarantees for other projects\.

## Related conceptual diagrams

- [Parsing safety and action authority](<../diagram-gallery.md#parsing-safety-action-authority>)

## Sources and attribution

- [The Rule Of 2](<https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/rule-of-2.md>) — Chromium Project; source ID: primary; provenance: official primary; retrieved 2026-10-02T17:52:00Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
