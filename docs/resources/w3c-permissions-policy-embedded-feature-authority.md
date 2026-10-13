# Permissions Policy: inherited browser-feature authority across embedded documents

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://w3c.github.io/webappsec-permissions-policy/>) · [Canonical JSON](<../../data/resources/w3c-permissions-policy-embedded-feature-authority.json>)

<a id="original-summary"></a>
## Main takeaway

The Permissions Policy draft defines how a page limits browser features for itself and embedded documents\. Embedded pages inherit restrictions and cannot re-enable a feature their parent disabled; defaults apply where no rule is declared\. This work-in-progress specification complements sandboxing but does not replace user consent, application permissions or a full isolation design\.

## Defensive use

Editorial guidance: document which component owns each capability decision and distinguish intended delegation from effective restrictions\. Keep browser-feature controls separate from application authorization and user consent in integration reviews\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** World Wide Web Consortium  
**Authors:** Ian Clelland; Ari Chivukula  
**Resource type:** Technical Standard  
**Version:** Editor's Draft, 22 September 2026  
**Topics:** Web Foundations; Authorization; Browser Security  
**Defensive skills:** Review client isolation; Threat-model integrations

## Prerequisites

**Basis:** editorial guidance.

- Browser origins, embedded documents and HTTP response headers

## Access and freshness

**Access cost at review:** free.

Public specification draft\.

**Reviewed:** 2026-10-03T21:42:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Read the official draft's status, framework, delivery and introspection sections; no browser conformance testing\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Original publication date not established in this review\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Living editor's draft; no released edition established\.
- **source displayed:** 2026-09-22; precision: day; basis: explicit; source: [Permissions Policy](<https://w3c.github.io/webappsec-permissions-policy/>) (source ID: standard). Displayed draft date, not original publication or a released edition\.

## Caveats

- Work in progress, not a final Recommendation or deployed-compatibility guarantee\. Listed authors are the draft's editors\.
- User agents need not support every feature\. Frame-level observable policy omits child response policy and later navigation, so it does not establish the loaded document's effective access\.
- Complements iframe sandboxing; it is not a complete isolation model\.

## Sources and attribution

- [Permissions Policy](<https://w3c.github.io/webappsec-permissions-policy/>) — World Wide Web Consortium; source ID: standard; provenance: official primary; retrieved 2026-10-03T21:41:20Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
