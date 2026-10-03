# Qwik: resumability metadata must preserve HTML serialization boundaries

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/qwik-2026-resumability-comment-serialization-boundary.json>) · [Official resource](<https://github.com/QwikDev/qwik/security/advisories/GHSA-m6jq-g7gq-5w3c>)

**Publisher:** QwikDev  
**Authors:** Varixo  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Verification  
**Defensive skills:** Review parsing and serialization; Review input trust boundaries; Review client isolation

## Original summary

The maintainer describes unsafe serialization of virtual-component metadata into server-rendered HTML comments\. Application-controlled attributes could cross from serialized state into browser interpretation when user influence reached their names or values\. The reported impact is same-origin browser script execution, with possible resumability-state disruption\. The advisory does not document a production compromise or independently measured downstream data loss\.

## Defensive use

The maintainer identifies 1\.19\.0 as patched\. Editorial lesson: serialization safety depends on the actual browser context, including structural metadata and comment boundaries, rather than only visible text or conventional attributes\. Review all server-to-client state representations and preserve the contract between their encoder and consumer\. A patch for this mechanism is not proof that every application output path is safe\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Server-rendered HTML and browser parsing contexts
- Framework resumability and serialized component metadata

## Access and freshness

**Access cost at review:** free.

Public maintainer security advisory\.

**Reviewed:** 2026-10-03T11:10:39Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary maintainer evidence reviewed\. No exploit reproduction, live testing, or independent patch verification performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-02-03; precision: day; basis: explicit; source: [Qwik SSR XSS via Unsafe Virtual Node Serialization](<https://github.com/QwikDev/qwik/security/advisories/GHSA-m6jq-g7gq-5w3c>) (source ID: advisory). Maintainer advisory publication, not software patch release\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition release established\.
- **source displayed:** 2026-02-03; precision: day; basis: explicit; source: [Qwik SSR XSS via Unsafe Virtual Node Serialization](<https://github.com/QwikDev/qwik/security/advisories/GHSA-m6jq-g7gq-5w3c>) (source ID: advisory). Explicit advisory publication date\.

## Caveats

- CVE-2026-25148\. Varixo published the advisory; wodzen is credited as reporter\.
- The application prerequisite is user influence over dynamically populated virtual-node attribute names or values\. The maintainer excludes hard-coded attributes\.
- The package table names qwik, while the prose names qwik-city\. Preserve this naming inconsistency rather than inferring package equivalence\.
- Advisory publication is February 3, 2026\. The exact software patch release date was not established and is not substituted into resource-edition chronology\.
- The reviewed official core changelog contains a 1\.19\.0 section but does not independently explain this security fix\. Remediation attribution rests on the maintainer advisory\.
- No bounty is established\. Learning prerequisites and generalized defensive guidance are editorial\.

## Sources and attribution

- [Qwik SSR XSS via Unsafe Virtual Node Serialization](<https://github.com/QwikDev/qwik/security/advisories/GHSA-m6jq-g7gq-5w3c>) — QwikDev; source ID: advisory; provenance: official primary; retrieved 2026-10-03T11:10:39Z; supports: summary, dates.
- [Qwik core changelog](<https://github.com/QwikDev/qwik/blob/main/packages/qwik/CHANGELOG.md>) — QwikDev; source ID: changelog; provenance: official primary; retrieved 2026-10-03T11:10:39Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
