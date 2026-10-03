# Better Auth: single-use authorization requires atomic state consumption

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/better-auth-2026-authorization-code-consumption-integrity.json>) · [Official resource](<https://github.com/better-auth/better-auth/security/advisories/GHSA-7w99-5wm4-3g79>)

**Publisher:** Better Auth  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; Business Logic and State Integrity  
**Defensive skills:** Reason about concurrent state; Review security-token design; Review approval-state integrity; Verify remediation evidence

## Original summary

The maintainer disclosure for CVE-2026-53518 identifies separated reading and deletion of a single-use OAuth authorization record\. Under concurrent processing, multiple successful consumers could receive independent token sets\. The established impact is duplicate authority within the original approved scope, not expansion of that scope\.

## Defensive use

Model consuming a grant as one indivisible state transition, including across service replicas and storage adapters\. A successful read must not itself authorize issuance\. Maintainer release 1\.6\.11 adds atomic consumption and corroborates the OAuth fix; review adapter guarantees rather than relying on process-local serialization\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- OAuth authorization-code and token lifecycle concepts
- Atomic database transitions and concurrent request handling

## Access and freshness

**Access cost at review:** free.

Public primary sources readable without an account\.

**Reviewed:** 2026-10-03T07:19:04Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed primary disclosure and maintainer corroboration; no independent vulnerability reproduction performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-05-31; precision: day; basis: explicit; source: [@better-auth/oauth-provider: Parallel requests can reuse one authorization code](<https://github.com/better-auth/better-auth/security/advisories/GHSA-7w99-5wm4-3g79>) (source ID: maintainer). Maintainer advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Release page displays May 12 without a year in retrieved text; exact patch-release date not established\.
- **source displayed:** 2026-05-31; precision: day; basis: explicit; source: [@better-auth/oauth-provider: Parallel requests can reuse one authorization code](<https://github.com/better-auth/better-auth/security/advisories/GHSA-7w99-5wm4-3g79>) (source ID: maintainer). Advisory publication, distinct from patch availability\.

## Caveats

- Requires an affected OAuth/OIDC provider deployment and a redeemable authorization code; the source does not establish bypass of code possession or PKCE\.
- Maintainer-reported behavior, not evidence of production compromise\. The advisory covers @better-auth/oauth-provider 1\.6\.0 before 1\.6\.11 and specified legacy plugins; an effective external atomic single-use control changes exposure\.
- The source credits chdanielmueller as reporter; no advisory author byline is established\.
- This is a substantive maintainer disclosure corroborated by release notes, not an independently peer-reviewed paper or an award-backed record\.

## Sources and attribution

- [@better-auth/oauth-provider: Parallel requests can reuse one authorization code](<https://github.com/better-auth/better-auth/security/advisories/GHSA-7w99-5wm4-3g79>) — Better Auth; source ID: maintainer; provenance: official primary; retrieved 2026-10-03T07:19:04Z; supports: summary, dates.
- [Release v1\.6\.11](<https://github.com/better-auth/better-auth/releases/tag/v1.6.11>) — Better Auth; source ID: release; provenance: official primary; retrieved 2026-10-03T07:19:04Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
