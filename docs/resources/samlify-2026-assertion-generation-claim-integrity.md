# samlify: signing does not establish claim provenance

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/samlify-2026-assertion-generation-claim-integrity.json>) · [Official resource](<https://github.com/tngan/samlify/security/advisories/GHSA-34r5-q4jw-r36m>)

**Publisher:** samlify  
**Authors:** tngan  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization  
**Defensive skills:** Review identity lifecycle; Review parsing and serialization; Verify remediation evidence

## Original summary

The maintainer describes inconsistent escaping between XML attribute and element-text contexts during SAML assertion generation\. User-controlled profile values could change assertion structure before the identity provider signed it\. The service provider subsequently accepted extra attributes as authenticated claims; privilege escalation depends on using those attributes for authorization\.

## Defensive use

Editorial reasoning: signatures protect the generated representation, not the authority of each input used to construct it\. Keep profile text separate from authorization-claim structure, use context-correct serialization before signing, and review which upstream actors may supply claims consumed as roles\. A signature check alone cannot repair a compromised issuance boundary\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- SAML issuer/relying-party roles, XML contexts and claim-based authorization

## Access and freshness

**Access cost at review:** free.

Public maintainer disclosure\.

**Reviewed:** 2026-10-03T16:19:37Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary source reviewed; no independent reproduction or deployment assessment\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-05-14; precision: day; basis: explicit; source: [SAML attribute-generation integrity advisory](<https://github.com/tngan/samlify/security/advisories/GHSA-34r5-q4jw-r36m>) (source ID: advisory). Maintainer advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition established\.
- **source displayed:** 2026-05-14; precision: day; basis: explicit; source: [SAML attribute-generation integrity advisory](<https://github.com/tngan/samlify/security/advisories/GHSA-34r5-q4jw-r36m>) (source ID: advisory). Maintainer advisory publication date\.

## Caveats

- The advisory identifies master/v2\.10\.2 as affected and 2\.13\.0 as patched; it does not establish a complete affected-version interval\. Exposure requires user-controlled values reaching assertion generation and a relying party trusting the resulting attributes\.
- The published example supports added attributes being parsed; downstream privileged application actions are conditional consequences, not evidence of a breached deployment\.
- tngan published the advisory; RootUp is credited as reporter in both advisory and release notes\. The 2\.13\.0 release explicitly references this advisory\. Its displayed May 14 timestamp omits the year in retrieved text, so no full patch date is asserted\. Resource edition remains null\.

## Sources and attribution

- [SAML attribute-generation integrity advisory](<https://github.com/tngan/samlify/security/advisories/GHSA-34r5-q4jw-r36m>) — samlify; source ID: advisory; provenance: official primary; retrieved 2026-10-03T16:19:37Z; supports: summary, dates, version.
- [Release v2\.13\.0](<https://github.com/tngan/samlify/releases/tag/v2.13.0>) — samlify; source ID: release; provenance: official primary; retrieved 2026-10-03T16:19:37Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
