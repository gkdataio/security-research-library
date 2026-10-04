# TanStack Start: preserve server-owned response authority through errors

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/tanstack-2026-server-function-response-authority.json>) · [Official resource](<https://github.com/TanStack/router/security/advisories/GHSA-qx66-fv34-fjm8>)

**Publisher:** TanStack  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Interpreter Boundaries  
**Defensive skills:** Review input trust boundaries; Review secure error behavior; Verify remediation evidence

## Original summary

TanStack's CVE-2026-102989 advisory describes client request data entering internal middleware state\. Failure handling could retain an untrusted result that response processing then accepted as an HTTP response\. The maintainer confirms reflected same-origin XSS and classifies it as CWE-79\. The boundary failure is client data acquiring server response authority, including on an error path\.

## Defensive use

The announced fix narrows accepted client input and checks server responses\. Update dependencies and the lockfile, verify resolved @tanstack/start-server-core is at least 1\.169\.39, then rebuild and redeploy; local upgrades alone leave deployed code unchanged\. Editorial lesson: keep internal state separate from public input, and preserve response provenance through exceptions\. Supplementary edge controls do not replace the package fix\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- HTTP response handling, browser same-origin authority and reflected XSS concepts
- Middleware error handling and dependency-resolution basics

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and supporting security announcement\.

**Reviewed:** 2026-10-04T20:23:24Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Both maintainer publications read\. This is source review, not independent reproduction or verification of deployed fixes\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-09-30; precision: day; basis: explicit; source: [Unauthenticated reflected XSS in TanStack Start server-function responses](<https://github.com/TanStack/router/security/advisories/GHSA-qx66-fv34-fjm8>) (source ID: advisory). GitHub explicitly labels this as the advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition date is established\.
- **source displayed:** 2026-09-30; precision: day; basis: explicit; source: [TanStack Start security update: CVE-2026-102989](<https://tanstack.com/blog/tanstack-start-security-update-cve-2026-102989>) (source ID: announcement). The supporting announcement is dated September 30, 2026\.

## Caveats

- Exposure requires an affected deployed server function and a visitor opening the supplied link\. The described script authority is limited to that visitor's same-origin access; neither source provides a public demonstration transcript or evidence of production compromise or actual theft\.
- Both sources give affected ranges beginning at 1\.143\.12, inclusive, and ending before each package's first patched version: @tanstack/react-start 1\.168\.60; @tanstack/solid-start 1\.168\.57; @tanstack/vue-start 1\.168\.56; @tanstack/start-server-core 1\.169\.39\.
- The September 30 announcement states that patched packages were available by then; it does not establish a separate resource edition or each package's exact release date\.
- GitHub identifies tannerlinsley as advisory publisher, not an explicit author byline; authors therefore remains empty\. The supporting blog names Tanner Linsley\. The advisory credits Lovable for helping discover and report the issue\.
- This concerns reflected response authority, distinct from the library's Next\.js Re:CACHE metadata and shared-cache case\. No individual bounty amount is established\. This educational record grants no testing authorization\.

## Sources and attribution

- [Unauthenticated reflected XSS in TanStack Start server-function responses](<https://github.com/TanStack/router/security/advisories/GHSA-qx66-fv34-fjm8>) — TanStack; source ID: advisory; provenance: official primary; retrieved 2026-10-04T20:22:22Z; supports: summary, dates.
- [TanStack Start security update: CVE-2026-102989](<https://tanstack.com/blog/tanstack-start-security-update-cve-2026-102989>) — TanStack; source ID: announcement; provenance: official primary; retrieved 2026-10-04T20:22:22Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
