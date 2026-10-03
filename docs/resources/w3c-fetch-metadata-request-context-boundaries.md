# Fetch Metadata Request Headers

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/w3c-fetch-metadata-request-context-boundaries.json>) · [Official resource](<https://www.w3.org/TR/2026/WD-fetch-metadata-20260921/>)

**Publisher:** World Wide Web Consortium  
**Authors:** Mike West  
**Resource type:** Technical Standard  
**Version:** Working Draft, 21 September 2026  
**Topics:** Web Foundations; Authorization  
**Defensive skills:** Review client isolation; Threat-model integrations

## Original summary

Defines browser-provided request context covering site relationship, destination, mode, and user activation\. Explains how redirect history affects that context and why context-dependent responses need matching cache behavior\. This supports reasoning about which browser interactions an application intends to accept\.

## Defensive use

Review an owned service’s documented request-context policy, including redirects, legitimate cross-origin use, and caching\. Treat browser context as an additional policy input rather than proof of a user’s resource permissions\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- HTTP requests and response caching
- Same-origin and same-site distinctions

## Access and freshness

**Access cost at review:** free.

Official specification readable without an account at review time\.

**Reviewed:** 2026-10-03T04:49:39Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed this identified edition and its relevant design and security sections\. Retrieval date is separate from publication; later revisions or errata may exist\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2019-06-27; precision: day; basis: explicit; source: [Fetch Metadata Request Headers publication history](<https://www.w3.org/standards/history/fetch-metadata/>) (source ID: publication-history). Date of the First Public Working Draft in W3C’s publication history; the reviewed edition was published separately on 2026-09-21\.
- **version released:** 2026-09-21; precision: day; basis: explicit; source: [Fetch Metadata Request Headers](<https://www.w3.org/TR/2026/WD-fetch-metadata-20260921/>) (source ID: primary). Publication date of the reviewed Working Draft; not the origin date of the specification series\.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- The reviewed edition is a Working Draft, not a final W3C Recommendation\.
- The draft does not establish support in every deployed browser or non-browser client\.

## Sources and attribution

- [Fetch Metadata Request Headers](<https://www.w3.org/TR/2026/WD-fetch-metadata-20260921/>) — World Wide Web Consortium; source ID: primary; provenance: official primary; retrieved 2026-10-03T04:40:00Z; supports: summary, version, dates.
- [Fetch Metadata Request Headers publication history](<https://www.w3.org/standards/history/fetch-metadata/>) — World Wide Web Consortium; source ID: publication-history; provenance: official primary; retrieved 2026-10-03T04:49:18Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
