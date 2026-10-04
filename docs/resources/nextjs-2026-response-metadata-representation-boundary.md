# Next\.js: response metadata must preserve representation boundaries

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/nextjs-2026-response-metadata-representation-boundary.json>) · [Official resource](<https://zhero-web-sec.github.io/research-and-things/re-cache-excessive-reflection-type-confusion-and-0-click-sxss-on-nextjs>)

**Publisher:** zhero\_web\_security  
**Authors:** Rachid Allam \(zhero;\); inzo\_  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Interpreter Boundaries  
**Defensive skills:** Review input trust boundaries; Review parsing and serialization; Review artifact isolation

## Original summary

Researchers describe client-supplied metadata becoming authoritative response metadata through unusual middleware header copying\. This changed how a dynamic App Router representation was interpreted; an external shared cache preserved the mismatch for later visitors\. They report stored browser script execution in an anonymized production application\. The core failure is a representation contract losing its integrity when request data controls response meaning\.

## Defensive use

Keep ownership of response interpretation with the component that creates the body\. Next\.js documentation warns that copying incoming headers into responses can override framework expectations and recommends selective forwarding\. Editorial lesson: review body format, response metadata and cache variation as one contract\. Data safe for one consumer may be unsafe for another; persistence does not repair that mismatch\. An application review should distinguish intended upstream request metadata from browser-facing response metadata and document which layer owns each decision\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- HTTP request and response metadata, content negotiation and shared-cache concepts
- Basic server-rendered framework and browser interpretation concepts

## Access and freshness

**Access cost at review:** free.

Public researcher article and supporting framework documentation\.

**Reviewed:** 2026-10-04T16:19:24Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Researcher publication and framework guidance read\. The documentation supports the general boundary warning, not independent confirmation of the reported production outcomes\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06; precision: month; basis: explicit; source: [Re:CACHE: Next\.js response-reflection research](<https://zhero-web-sec.github.io/research-and-things/re-cache-excessive-reflection-type-confusion-and-0-click-sxss-on-nextjs>) (source ID: research). The article displays June 2026; no publication day is established\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-06; precision: month; basis: explicit; source: [Re:CACHE: Next\.js response-reflection research](<https://zhero-web-sec.github.io/research-and-things/re-cache-excessive-reflection-type-confusion-and-0-click-sxss-on-nextjs>) (source ID: research). The article displays June 2026; no publication day is established\.

## Caveats

- Exposure requires the described header-copying behavior, a dynamic representation and external caching\. This is configuration-specific; the article does not establish a universal Next\.js flaw\.
- The reported effect still requires a visitor to load affected content\. The publication supplies no independently corroborated vendor incident account, verified fixed version or remediation date\.
- The unspecified five-figure award establishes neither an exact amount nor a currency\. This resource does not qualify as an award-backed report\.

## Sources and attribution

- [Re:CACHE: Next\.js response-reflection research](<https://zhero-web-sec.github.io/research-and-things/re-cache-excessive-reflection-type-confusion-and-0-click-sxss-on-nextjs>) — zhero\_web\_security; source ID: research; provenance: official primary; retrieved 2026-10-04T16:19:24Z; supports: summary, dates.
- [NextResponse documentation: request forwarding and response headers](<https://nextjs.org/docs/app/api-reference/functions/next-response#next>) — Next\.js; source ID: framework; provenance: official primary; retrieved 2026-10-04T16:19:24Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
