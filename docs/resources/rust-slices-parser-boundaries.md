# Rust Slices: Bounds, Borrowing, and Text Boundaries

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://doc.rust-lang.org/book/ch04-03-slices.html>) · [Canonical JSON](<../../data/resources/rust-slices-parser-boundaries.json>)

<a id="original-summary"></a>
## Main takeaway

The Rust Book uses text processing to show why a borrowed slice stays tied to its source buffer while an integer position can become detached from the data it describes\. The language reference explains that safe slice access checks bounds\. The strings chapter separately explains why byte positions must respect UTF-8 character boundaries\.

## Defensive use

Keep a parser’s view connected to its backing storage and represent absence or invalid boundaries explicitly\. Distinguish memory safety, valid encoding, and acceptance of a meaningful message\. Prefer checked, fallible access where input may be incomplete, and document the transition from raw input to borrowed byte or text views\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** The Rust Project  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Memory Safety and Process Isolation  
**Defensive skills:** Review memory-safety assumptions; Review parsing and serialization; Review text-encoding invariants

## Prerequisites

**Basis:** editorial guidance.

- Rust ownership and borrowing
- Bytes versus Unicode text

## Access and freshness

**Access cost at review:** free.

Publicly accessible official documentation; no account required for reading\.

**Reviewed:** 2026-10-12T18:31:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Official book, reference, and API pages reviewed\. Page publication and revision dates are not displayed; individual API stabilization versions are not resource edition dates\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No publication or revision date is displayed on the reviewed page\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No publication or revision date is displayed on the reviewed page\.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No publication or revision date is displayed on the reviewed page\.

## Caveats

- The introductory text-processing example assumes ASCII\.
- Bounds-checked indexing may panic\. Memory safety does not itself establish graceful error handling or valid application semantics\.
- Method stabilization versions in the API reference describe individual software APIs, not the publication or revision date of this educational resource\.

## Sources and attribution

- [The Slice Type](<https://doc.rust-lang.org/book/ch04-03-slices.html>) — The Rust Project; source ID: rust-slices; provenance: official primary; retrieved 2026-10-12T18:31:00Z; supports: summary.
- [Slice types](<https://doc.rust-lang.org/reference/types/slice.html>) — The Rust Project; source ID: rust-slice-reference; provenance: official primary; retrieved 2026-10-12T18:31:00Z; supports: summary.
- [Storing UTF-8 Encoded Text with Strings](<https://doc.rust-lang.org/book/ch08-02-strings.html>) — The Rust Project; source ID: rust-strings; provenance: official primary; retrieved 2026-10-12T18:31:00Z; supports: summary.
- [Primitive Type slice](<https://doc.rust-lang.org/std/primitive.slice.html>) — The Rust Project; source ID: rust-slice-api; provenance: official primary; retrieved 2026-10-12T18:31:00Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
