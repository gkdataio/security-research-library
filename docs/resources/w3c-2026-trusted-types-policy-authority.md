# Trusted Types: typed sinks depend on trustworthy policy creation

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/w3c-2026-trusted-types-policy-authority.json>) · [Official resource](<https://www.w3.org/TR/2026/WD-trusted-types-20260623/>)

**Publisher:** World Wide Web Consortium  
**Authors:** Krzysztof Kotowicz  
**Resource type:** Technical Standard  
**Version:** Working Draft, 23 June 2026  
**Topics:** Web Foundations  
**Defensive skills:** Review client isolation; Review input trust boundaries; Review parsing and serialization

## Original summary

Defines a browser-enforced boundary between ordinary strings and typed values accepted by injection-sensitive APIs\. The underlying failure is allowing untrusted text to acquire executable interpretation\. Policies centralize creation of accepted values; matching types preserve intended use, but do not independently establish that a policy's transformation is safe\.

## Defensive use

Editorial reasoning: review two invariants separately: sensitive consumers accept only policy-produced values, and each producer enforces an adequate trust contract\. Minimize policy creation authority, keep policy dependencies reviewable and avoid global state silently changing decisions\. The maintainer FAQ explains why sanitization must be consistently applied, rather than merely available in a library\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- JavaScript DOM data flow and Content Security Policy

## Access and freshness

**Access cost at review:** free.

Public primary-source guidance\.

**Reviewed:** 2026-10-03T15:20:45Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed the dated draft, publication history and explanatory FAQ; no conformance tests were run\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2022-09-27; precision: day; basis: explicit; source: [Trusted Types publication history](<https://www.w3.org/standards/history/trusted-types/>) (source ID: history). First Public Working Draft of the specification series\.
- **version released:** 2026-06-23; precision: day; basis: explicit; source: [Trusted Types](<https://www.w3.org/TR/2026/WD-trusted-types-20260623/>) (source ID: standard). Date of the reviewed educational specification edition\.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- The reviewed edition is a Working Draft, not a final W3C Recommendation\. Krzysztof Kotowicz is its listed editor; Mike West is listed as former editor\.
- Unsafe policies can preserve DOM injection risk\. The design does not isolate actively malicious first-party code or guard every DOM operation\.
- The FAQ distinguishes client-side sink controls from server-generated injection and complementary CSP defenses\. Its 2021 browser-support discussion is historical and is not used as current compatibility evidence\.

## Sources and attribution

- [Trusted Types](<https://www.w3.org/TR/2026/WD-trusted-types-20260623/>) — World Wide Web Consortium; source ID: standard; provenance: official primary; retrieved 2026-10-03T15:20:45Z; supports: summary, version, dates.
- [Trusted Types publication history](<https://www.w3.org/standards/history/trusted-types/>) — World Wide Web Consortium; source ID: history; provenance: official primary; retrieved 2026-10-03T15:20:45Z; supports: dates.
- [Trusted Types FAQ](<https://github.com/w3c/trusted-types/wiki/FAQ>) — W3C Trusted Types project; source ID: faq; provenance: official primary; retrieved 2026-10-03T15:20:45Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
