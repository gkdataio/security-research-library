# Nhost: provider adapters must preserve identity-claim evidence

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/nhost-2026-provider-claim-verification-provenance.json>) · [Official resource](<https://github.com/nhost/nhost/security/advisories/GHSA-6g38-8j4p-j3pr>)

**Publisher:** Nhost  
**Authors:** dbarrosop  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization  
**Defensive skills:** Review identity lifecycle; Threat-model integrations; Verify remediation evidence

## Original summary

CVE-2026-41574 describes provider adapters converting email presence or fallback profile attributes into a verification claim\. An account-linking consumer then treated that normalized claim as ownership evidence\. The maintainer reports unauthorized identity merging and authenticated access to an existing account\.

## Defensive use

Editorial reasoning: normalization must retain the strength and origin of evidence\. A nonempty identity attribute is not interchangeable with proof of mailbox control\. Review adapter contracts and the account-linking decision together; rejecting absent or unverified evidence must remain consistent across providers\. Official auth@0\.49\.1 release notes dated 2026-04-17 corroborate stricter provider email-verification handling\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- OAuth identity-provider claims and local account-linking concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer disclosure and release notes\.

**Reviewed:** 2026-10-03T14:48:42Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory and release notes reviewed; no independent reproduction or deployment assessment\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-04-17; precision: day; basis: explicit; source: [Account Takeover via OAuth Email Verification Bypass](<https://github.com/nhost/nhost/security/advisories/GHSA-6g38-8j4p-j3pr>) (source ID: advisory). Maintainer advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource edition date established; software remediation is recorded separately\.
- **source displayed:** 2026-04-17; precision: day; basis: explicit; source: [Account Takeover via OAuth Email Verification Bypass](<https://github.com/nhost/nhost/security/advisories/GHSA-6g38-8j4p-j3pr>) (source ID: advisory). Maintainer advisory publication date\.

## Caveats

- The advisory lists auth service versions before 0\.49\.1 as affected\. Exposure depends on an affected provider adapter being enabled and an existing matching local identity\. Provider-specific prerequisites differ; no universal OAuth-provider compromise is established\.
- dbarrosop published the advisory; skoveit is credited as reporter\. Technical claims are maintainer-reported, not independently reproduced\.
- The advisory makes provider-specific assertions about Microsoft claims that were not independently corroborated; this record relies on the broader adapter-evidence boundary, not those assertions\.
- Maintainer disclosure, not a peer-reviewed paper or an award-backed report\. Software patch chronology is separate from resource edition metadata\.

## Sources and attribution

- [Account Takeover via OAuth Email Verification Bypass](<https://github.com/nhost/nhost/security/advisories/GHSA-6g38-8j4p-j3pr>) — Nhost; source ID: advisory; provenance: official primary; retrieved 2026-10-03T14:48:42Z; supports: summary, dates, version.
- [Release auth@0\.49\.1](<https://github.com/nhost/nhost/releases/tag/auth@0.49.1>) — Nhost; source ID: release; provenance: official primary; retrieved 2026-10-03T14:39:59\.794959Z; supports: summary, dates, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
