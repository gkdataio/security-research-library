# C\+\+ Core Guidelines: Bounds and Lifetime Safety

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/cpp-core-guidelines-bounds-lifetime.json>) · [Official resource](<https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines>)

**Publisher:** C\+\+ Core Guidelines project  
**Authors:** Bjarne Stroustrup; Herb Sutter  
**Resource type:** Implementation Guide  
**Version:** Not established in the reviewed record  
**Topics:** Memory Safety and Process Isolation  
**Defensive skills:** Review memory-safety assumptions; Review parsing and serialization

## Original summary

Separates three mutually supporting properties: objects must be used with valid types, accesses must stay inside their allocated bounds, and references must not outlive the objects they designate\. The bounds and lifetime profiles translate these ideas into interface and ownership guidance, including range-carrying views and avoiding potentially invalid pointers\.

## Defensive use

During parser design review, document extent, ownership, and validity duration together\. Identify where array-to-pointer conversion discards bounds and where views may outlive storage\. Use the Pro\.bounds, Pro\.lifetime, and GSL\.view sections to reason about these component-boundary contracts\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- C\+\+ pointers and references
- Containers and RAII

## Access and freshness

**Access cost at review:** free.

Publicly accessible official documentation; no account required for reading\.

**Reviewed:** 2026-10-12T18:31:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed the living document displaying 2026-06-14, especially Pro\.bounds, Pro\.lifetime, and GSL\.view\. No original publication date was established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. The original publication date was not established from the reviewed living document\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No dated educational-resource edition release was established\.
- **source displayed:** 2026-06-14; precision: day; basis: explicit; source: [C\+\+ Core Guidelines](<https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines>) (source ID: cpp-guidelines). Date displayed at the head of the living document; not asserted to be original publication or an edition release\.

## Caveats

- Bjarne Stroustrup and Herb Sutter are credited by the source as editors\.
- These evolving project guidelines are not the normative ISO language standard or an automatic safety guarantee\. Their guarantees depend on enforcement and surrounding code\.
- The document distinguishes bounds-checked GSL span from std::span; do not infer that every span implementation checks bounds\.

## Sources and attribution

- [C\+\+ Core Guidelines](<https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines>) — C\+\+ Core Guidelines project; source ID: cpp-guidelines; provenance: official primary; retrieved 2026-10-12T18:31:00Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
