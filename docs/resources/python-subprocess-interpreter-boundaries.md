# Python subprocess: executable, argument, and interpreter boundaries

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/python-subprocess-interpreter-boundaries.json>) · [Official resource](<https://docs.python.org/3.14/library/subprocess.html#security-considerations>)

**Publisher:** Python Software Foundation  
**Authors:** Not identified in the reviewed record  
**Resource type:** Implementation Guide  
**Version:** Python 3\.14 documentation branch  
**Topics:** Interpreter Boundaries  
**Defensive skills:** Review input trust boundaries; Review parsing and serialization

## Original summary

Runtime documentation distinguishes the selected executable, its arguments, and shell interpretation\. Python does not implicitly select a shell, but Windows may launch batch files through one\. The companion shlex reference limits its quoting guarantees to Unix shells; quoting is not a portable substitute for understanding the receiving interpreter\.

## Defensive use

Editorial learning objective: distinguish preserving argument boundaries from authorizing their meaning\. Review which executable and interpreter receive data, what actions the receiving program assigns to arguments, and whether those actions fit the intended authority\. This resource supports conceptual design review, without execution recipes\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic familiarity with processes, arguments, and operating-system differences\.

## Access and freshness

**Access cost at review:** free.

Public runtime documentation; no account was needed for the reviewed sections\.

**Reviewed:** 2026-10-03T23:22:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed the versioned Python 3\.14 subprocess security considerations and shlex\.quote warning\. Documentation can change; this is not an implementation or platform compatibility test\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. The reviewed sections do not establish this educational resource date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. The reviewed sections do not establish this educational resource date\.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded. The reviewed sections do not establish this educational resource date\.

## Caveats

- Windows batch-file handling can involve shell parsing even when the application has not explicitly selected a shell\. The runtime guidance for this case is conditional, not a universal recommendation to enable shell execution\.
- shlex quoting is not guaranteed correct for non-POSIX shells or Windows shells\.
- The authorization distinction is editorial synthesis, not a claim that these Python APIs enforce application policy\.
- No vulnerability finding, award, payload, reproduction sequence, or testing authorization is established\.

## Sources and attribution

- [subprocess: Security Considerations](<https://docs.python.org/3.14/library/subprocess.html#security-considerations>) — Python Software Foundation; source ID: python-subprocess-security; provenance: official primary; retrieved 2026-10-03T23:22:00Z; supports: summary, version.
- [shlex\.quote: Unix-shell portability warning](<https://docs.python.org/3.14/library/shlex.html#shlex.quote>) — Python Software Foundation; source ID: python-shlex-quote; provenance: official primary; retrieved 2026-10-03T23:22:00Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
