# Axios: enforce upload budgets across transport implementations

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/axios-2026-streamed-upload-budget-enforcement.json>) · [Official resource](<https://github.com/axios/axios/security/advisories/GHSA-mwf2-3pr3-8698>)

**Publisher:** Axios  
**Authors:** jasonsaayman  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Verification  
**Defensive skills:** Review input trust boundaries; Verify remediation evidence; Write bounded security evidence

## Original summary

CVE-2026-68948 documents a transport-contract mismatch: an application configured an outbound body limit, but the HTTP/2 stream path delegated to a transport that did not enforce it\. The maintainer-published report describes local observation of transmission beyond that budget\. Bandwidth, quota and availability consequences are application-dependent; the advisory excludes code execution, credential disclosure and destination control\.

## Defensive use

The maintainer identifies 1\.18\.0 as patched\. Review byte-budget enforcement as an invariant shared by transport adapters\. The merged remediation describes consistent upload/content limits and regression coverage\. Editorial lesson: enforce limits during consumption of unknown-length input and ensure failure cancels downstream work; configuration metadata alone is not enforcement\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- HTTP transport adapters and streamed request bodies
- Resource budgets and failure propagation

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and remediation references readable without an account\.

**Reviewed:** 2026-10-03T07:39:01Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed maintainer advisory, release and merged remediation discussion; no vulnerability reproduction or independent patch testing performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-07-06; precision: day; basis: explicit; source: [HTTP/2 streamed uploads bypass maxBodyLength](<https://github.com/axios/axios/security/advisories/GHSA-mwf2-3pr3-8698>) (source ID: advisory). Maintainer advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource-edition release established; software patch chronology is retained in the caveats\.
- **source displayed:** 2026-07-06; precision: day; basis: explicit; source: [HTTP/2 streamed uploads bypass maxBodyLength](<https://github.com/axios/axios/security/advisories/GHSA-mwf2-3pr3-8698>) (source ID: advisory). Publication date displayed beside the advisory publisher\.

## Caveats

- Exposure requires untrusted stream influence, the Node HTTP adapter using HTTP/2, and a finite configured body limit\. Buffered bodies and browser adapters are excluded from this advisory\.
- The advisory credits asadeddin as reporter; jasonsaayman is the publishing maintainer, not an inferred discoverer\.
- The advisory retains old prose saying no fixed release exists, while its patched-version metadata identifies 1\.18\.0 and the dated release corroborates stream-limit hardening\. These distinct source states are preserved\.
- No production incident, measured billing loss or bounty amount was established\. Learning prerequisites and generalized design advice are editorial\.
- The cited software release is dated 2026-06-13; it is distinct from the advisory publication and is not a claim about the latest available release\.
- The advisory lists affected versions as &gt;=1\.13\.0 and patched versions as &gt;=1\.18\.0; its affected-range metadata lacks an upper bound\. These overlapping published fields do not establish that patched releases remain vulnerable\.

## Sources and attribution

- [HTTP/2 streamed uploads bypass maxBodyLength](<https://github.com/axios/axios/security/advisories/GHSA-mwf2-3pr3-8698>) — Axios; source ID: advisory; provenance: official primary; retrieved 2026-10-03T07:39:01Z; supports: summary, dates.
- [Axios v1\.18\.0 release](<https://github.com/axios/axios/releases/tag/v1.18.0>) — Axios; source ID: release; provenance: official primary; retrieved 2026-10-03T07:39:01Z; supports: summary, dates, version.
- [Merged request hardening and stream-limit changes](<https://github.com/axios/axios/pull/11000>) — Axios; source ID: remediation; provenance: official primary; retrieved 2026-10-03T07:39:01Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
