# HTML COOP: opener separation and same-origin authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/whatwg-coop-opener-and-origin-authority.json>) · [Official resource](<https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policies>)

**Publisher:** WHATWG  
**Authors:** Not identified in the reviewed record  
**Resource type:** Technical Standard  
**Version:** HTML Living Standard \(reviewed 2026-10-03\)  
**Topics:** Web Foundations; Authorization  
**Defensive skills:** Review client isolation; Threat-model integrations

## Original summary

Defines how opener policies affect browsing-context separation during navigation\. The standard expressly distinguishes severing an opener relationship from a robust boundary between same-origin documents: storage, service workers, messaging and server responses can preserve shared authority\.

## Defensive use

Model window references separately from origin-wide data and service authority\. For an owned application, document every shared client capability and server data path before relying on opener separation; combine appropriate embedding, cookie and response controls with an explicit trust-domain design\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Browser origin and navigation concepts
- HTTP session and response-cache fundamentals

## Access and freshness

**Access cost at review:** free.

Official documentation readable without an account at review time\.

**Reviewed:** 2026-10-03T05:39:10Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed the current opener-policy definitions and same-origin limitations\. The page remains mutable and is not an immutable versioned edition\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. The reviewed section does not establish its original publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Living specification without a separately identified release for this section\.
- **source displayed:** 2026-10-02; precision: day; basis: explicit; source: [HTML Standard: Cross-origin opener policies](<https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policies>) (source ID: primary). Displayed last-updated date for the HTML Living Standard; not proof this section changed on that date\.

## Caveats

- A specification defines intended behavior; this review does not establish per-value support in deployed browsers\.
- Opener separation alone does not partition origin-wide storage or grant application-level authorization\.
- This resource complements message validation and request-context resources by modeling the isolation boundary itself\.

## Sources and attribution

- [HTML Standard: Cross-origin opener policies](<https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policies>) — WHATWG; source ID: primary; provenance: official primary; retrieved 2026-10-03T05:39:10Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
