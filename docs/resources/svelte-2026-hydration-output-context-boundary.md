# Svelte hydration: serialization must preserve the enclosing output context

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/svelte-2026-hydration-output-context-boundary.json>) · [Official resource](<https://caverav.cl/posts/svelte-hydratable-xss/svelte-hydratable-xss/>)

**Publisher:** Camilo Vera  
**Authors:** Camilo Vera  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations  
**Defensive skills:** Review parsing and serialization; Review input trust boundaries; Verify remediation evidence

## Original summary

Research on CVE-2025-15265 explains a data-to-code boundary failure: hydration keys received JavaScript-string serialization without the HTML-context protection already used for values\. The researcher demonstrates browser script execution in a minimal application\. Account compromise is an application-dependent consequence, not evidence of a compromised production account\.

## Defensive use

Compare all fields crossing rendering contexts, including metadata keys\. The researcher describes replacement with an HTML-safe serializer and regression coverage\. The maintainer identifies Svelte 5\.46\.4 as patched\. Preserve one encoding contract across keys and values, rather than treating valid JSON as sufficient for every output context\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Server-side rendering and framework integration concepts
- Basic trust-boundary and secure-input review

## Access and freshness

**Access cost at review:** free.

Public researcher article and maintainer advisory readable without an account\.

**Reviewed:** 2026-10-03T05:49:32Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Researcher article and maintainer advisory reviewed; no immutable article revision established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-03-17; precision: day; basis: explicit; source: [CVE-2025-15265: Svelte Hydratable Key SSR XSS - Lydian](<https://caverav.cl/posts/svelte-hydratable-xss/svelte-hydratable-xss/>) (source ID: research). Article displays this publication date; advisory disclosure is a separate event\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-03-17; precision: day; basis: explicit; source: [CVE-2025-15265: Svelte Hydratable Key SSR XSS - Lydian](<https://caverav.cl/posts/svelte-hydratable-xss/svelte-hydratable-xss/>) (source ID: research). Article displays this publication date; advisory disclosure is a separate event\.

## Caveats

- Affected behavior requires experimental async rendering and hydration keys influenced by untrusted input; ordinary Svelte use alone does not establish exposure\.
- The advisory version table lists 5\.46\.0 through 5\.46\.3, while its summary says 5\.46\.0-2; the researcher and Fluid Attacks advisory support the broader table range\.
- March 17 is the article publication; the researcher dates the separate fix and disclosure to January 15, 2026\. Learning prerequisites are editorial\.

## Sources and attribution

- [CVE-2025-15265: Svelte Hydratable Key SSR XSS - Lydian](<https://caverav.cl/posts/svelte-hydratable-xss/svelte-hydratable-xss/>) — Camilo Vera; source ID: research; provenance: official primary; retrieved 2026-10-03T05:49:32Z; supports: summary, dates.
- [Improper Neutralization of Input During Web Page Generation \('Cross-site Scripting'\) in svelte](<https://github.com/sveltejs/svelte/security/advisories/GHSA-6738-r8g5-qwp3>) — Svelte; source ID: maintainer; provenance: official primary; retrieved 2026-10-03T05:49:32Z; supports: summary.
- [Svelte 5\.46\.0 - Hydratable Key Script-Breakout XSS \(SSR\)](<https://fluidattacks.com/advisories/lydian>) — Fluid Attacks; source ID: research-advisory; provenance: official primary; retrieved 2026-10-03T05:49:32Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
