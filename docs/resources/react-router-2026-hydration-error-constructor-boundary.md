# React Router: hydrated error metadata must not select client behavior

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/react-router-2026-hydration-error-constructor-boundary.json>) · [Official resource](<https://github.com/remix-run/react-router/security/advisories/GHSA-337j-9hxr-rhxg>)

**Publisher:** React Router / Remix  
**Authors:** brophdawg11  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Verification  
**Defensive skills:** Review parsing and serialization; Review input trust boundaries; Review secure error behavior

## Original summary

The maintainer describes an SSR-to-hydration trust failure: application code that lets untrusted input alter aspects of caught server errors could cause unexpected client constructor execution and outbound network activity\. The prerequisite is unusually specific application behavior\. The case distinguishes transporting error data from granting that data authority over client reconstruction\.

## Defensive use

The advisory identifies 7\.18\.0 as patched\. Editorial lesson: preserve a narrow, inert contract for errors crossing the server/client boundary, including metadata used to reconstruct them\. Review error transport separately from visible error text, and constrain client interpretation to explicitly supported representations\. The reviewed advisory does not establish the exact patch implementation\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Server-side rendering and client hydration
- Error serialization and data-versus-behavior boundaries

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and release page\.

**Reviewed:** 2026-10-03T14:19:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory and release page read\. No live testing or independent patch execution\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-07-22; precision: day; basis: explicit; source: [Arbitrary client-side constructor injection via React Router SSR Hydration](<https://github.com/remix-run/react-router/security/advisories/GHSA-337j-9hxr-rhxg>) (source ID: advisory). Advisory publication\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition established\.
- **source displayed:** 2026-07-22; precision: day; basis: explicit; source: [Arbitrary client-side constructor injection via React Router SSR Hydration](<https://github.com/remix-run/react-router/security/advisories/GHSA-337j-9hxr-rhxg>) (source ID: advisory). Explicit advisory publication date\.

## Caveats

- CVE-2026-53666\. brophdawg11 published the advisory; yoyomiski is credited as reporter\. The affected range is at least 6\.4\.0 and below 7\.18\.0\.
- The maintainer limits applicability to Framework Mode and Data Mode with manual SSR/hydration, excluding Declarative Mode\. Do not infer general client code execution, server compromise, or demonstrated data theft from the bounded description\.
- The software release page displays June 16 without a year in retrieved text\. A full patch-release date is not asserted or substituted for educational-resource chronology\.
- No individual bounty is established\. Learning prerequisites and generalized review guidance are editorial\.

## Sources and attribution

- [Arbitrary client-side constructor injection via React Router SSR Hydration](<https://github.com/remix-run/react-router/security/advisories/GHSA-337j-9hxr-rhxg>) — React Router / Remix; source ID: advisory; provenance: official primary; retrieved 2026-10-03T14:18:30Z; supports: summary, dates.
- [React Router v7\.18\.0 release](<https://github.com/remix-run/react-router/releases/tag/react-router@7.18.0>) — React Router / Remix; source ID: release; provenance: official primary; retrieved 2026-10-03T14:18:52Z; supports: dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
