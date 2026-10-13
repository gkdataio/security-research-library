# Open WebUI: revocation must cross HTTP and realtime boundaries

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/open-webui/open-webui/security/advisories/GHSA-855v-hq7w-jmjw>) · [Canonical JSON](<../../data/resources/open-webui-2026-realtime-revocation-consistency.json>)

<a id="original-summary"></a>
## Main takeaway

Open WebUI's maintainer advisory describes revoked tokens being rejected over HTTP but accepted for new realtime connections in a local comparison \(CVE-2026-59219\)\. Realtime authentication checked the signature and expiry without consulting revocation state\. A token could therefore remain cryptographically valid after the session had lost permission to connect\.

## Defensive use

Editorial lesson: model revocation as a shared invariant across every transport\. The advisory identifies 0\.10\.0 as patched through shared revocation checks\. Distinguish denial of new connections from termination of existing ones when reviewing remediation guarantees\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Open WebUI  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; Web Foundations; API Security  
**Defensive skills:** Review identity lifecycle; Review security-token design; Threat-model integrations; Verify remediation evidence

## Prerequisites

**Basis:** editorial guidance.

- JWT validity, session revocation and asynchronous transports

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory\.

**Reviewed:** 2026-10-03T13:38:43Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer source reviewed; no software executed or deployment tested\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-07-02; precision: day; basis: explicit; source: [Realtime endpoints accept Redis-revoked JWTs after signout/backchannel logout](<https://github.com/open-webui/open-webui/security/advisories/GHSA-855v-hq7w-jmjw>) (source ID: advisory). Maintainer publication, not advisory-database ingestion or software release\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational edition established\.
- **source displayed:** 2026-07-02; precision: day; basis: explicit; source: [Realtime endpoints accept Redis-revoked JWTs after signout/backchannel logout](<https://github.com/open-webui/open-webui/security/advisories/GHSA-855v-hq7w-jmjw>) (source ID: advisory). Publication beside the publishing account\.

## Caveats

- Applies to Redis-backed versions 0\.9\.0 through versions before 0\.10\.0 and requires possession of an otherwise valid revoked token\. Without Redis, per-token invalidation is unsupported by design\.
- Realtime disclosure and impersonation are maintainer-described consequences; broader production exploitation is not established\. Terminal access additionally depends on terminal configuration; HTTP remains protected\.
- Existing-connection termination is not established\. The advisory identifies doge-woof as the publishing account and credits huslayer826 as Reporter and Classic298 as Coordinator\. The reviewed advisory provides no explicit article byline; these publication and credit roles do not establish article authorship\. Separate from the catalog's role-claim provenance advisory\.

## Sources and attribution

- [Realtime endpoints accept Redis-revoked JWTs after signout/backchannel logout](<https://github.com/open-webui/open-webui/security/advisories/GHSA-855v-hq7w-jmjw>) — Open WebUI; source ID: advisory; provenance: official primary; retrieved 2026-10-03T13:38:43Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
