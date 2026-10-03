# Open WebUI: preserve role-policy meaning across identity flows

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/open-webui-2026-role-claim-provenance-and-revocation.json>) · [Official resource](<https://github.com/open-webui/open-webui/security/advisories/GHSA-2rr4-q6pg-m5g3>)

**Publisher:** Open WebUI  
**Authors:** doge-woof  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization  
**Defensive skills:** Model access-control invariants; Threat-model integrations; Review identity lifecycle; Verify remediation evidence

## Original summary

GHSA-2rr4-q6pg-m5g3 documents a shared-policy input mismatch: browser sign-in supplied identity-token claims, while token exchange supplied only provider user information\. Missing role evidence preserved an old role\. The maintainer reports local verification of continued access on 0\.11\.3 and rejection on 0\.11\.4; consequences beyond the prior role are not demonstrated\.

## Defensive use

Version 0\.11\.4 is identified as patched\. The linked change and release notes corroborate expanded claim handling and rejection when role evidence cannot be read\. Editorial lesson: sharing policy code is insufficient when callers provide different evidence; document claim provenance and make missing-evidence behavior explicit\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- OIDC claims and application-role mapping
- Account linking, role revocation and fail-closed policy behavior

## Access and freshness

**Access cost at review:** free.

Public maintainer sources readable without an account\.

**Reviewed:** 2026-10-03T08:39:25Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed maintainer advisory and corroborating project sources\. No software executed or deployment tested\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-09-27; precision: day; basis: explicit; source: [Revoked users keep signing in via token exchange when roles are only in the ID token](<https://github.com/open-webui/open-webui/security/advisories/GHSA-2rr4-q6pg-m5g3>) (source ID: advisory). Maintainer advisory publication; not software release date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separately versioned resource edition established; product fix versions are recorded below\.
- **source displayed:** 2026-09-27; precision: day; basis: explicit; source: [Revoked users keep signing in via token exchange when roles are only in the ID token](<https://github.com/open-webui/open-webui/security/advisories/GHSA-2rr4-q6pg-m5g3>) (source ID: advisory). Publication date beside the advisory publisher\.

## Caveats

- Publisher prerequisites: non-default token exchange and role management enabled, a non-wildcard allowed-role policy, roles absent from provider user information, and a previously linked account still able to receive valid provider tokens\.
- The advisory covers 0\.11\.1 through 0\.11\.3\. Prior access persists; no new account or privilege elevation is established\. Browser sign-in remains policy-enforcing\.
- The September 9 advisory identified 0\.11\.1 as fixing omitted role evaluation\. The September 27 disclosure establishes that claim-source differences required further remediation; the earlier fix must not be presented as sufficient for this case\.
- The primary advisory credits manus-pi as reporter and Classic298 for remediation\. Its local-provider experiment does not independently verify every identity-provider configuration or deployed installation\.
- The remedy addresses newly issued sessions; immediate invalidation of all previously issued sessions is not established by these sources\. Resource publication and product patch release are distinct\.
- Conceptual defensive summary only; public disclosure grants no testing authorization\.

## Sources and attribution

- [Revoked users keep signing in via token exchange when roles are only in the ID token](<https://github.com/open-webui/open-webui/security/advisories/GHSA-2rr4-q6pg-m5g3>) — Open WebUI; source ID: advisory; provenance: official primary; retrieved 2026-10-03T08:39:25Z; supports: summary, dates.
- [Users denied by the OAuth role policy can still sign in via token exchange](<https://github.com/open-webui/open-webui/security/advisories/GHSA-wvm9-9g5j-623f>) — Open WebUI; source ID: earlier-advisory; provenance: official primary; retrieved 2026-10-03T08:39:25Z; supports: summary, dates.
- [Role-claim handling remediation commit](<https://github.com/open-webui/open-webui/commit/10d1cfe6375f207acaa531e857edb575ded2cfc3>) — Open WebUI; source ID: patch; provenance: official primary; retrieved 2026-10-03T08:39:25Z; supports: summary.
- [Open WebUI v0\.11\.4 release notes](<https://github.com/open-webui/open-webui/releases/tag/v0.11.4>) — Open WebUI; source ID: release; provenance: official primary; retrieved 2026-10-03T08:39:25Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
