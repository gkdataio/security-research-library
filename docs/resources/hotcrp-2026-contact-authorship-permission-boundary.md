# HotCRP: separate submission visibility from authorship authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/hotcrp-2026-contact-authorship-permission-boundary.json>) · [Official resource](<https://github.com/kohler/hotcrp/security/advisories/GHSA-v8jx-vq6p-jq52>)

**Publisher:** HotCRP  
**Authors:** kohler  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; Business Logic and State Integrity  
**Defensive skills:** Review identity lifecycle; Model access-control invariants; Verify remediation evidence

## Original summary

GHSA-v8jx-vq6p-jq52 describes an API permission gap between viewing a submission and changing contact authorship\. The maintainer reports that reviewers and program-committee members could obtain author-level access to submissions they could already view, affecting anonymity and integrity\.

## Defensive use

Editorial lesson: authority-changing metadata needs its own permission check; visibility alone must not authorize membership changes\. The advisory identifies versions 3\.0\.0–3\.3\.1 as affected and 3\.4 as fixed\. Release notes date 3\.4 to August 5, before disclosure on August 11\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic server-side identity and authorization concepts

## Access and freshness

**Access cost at review:** free.

Public maintainer disclosure\.

**Reviewed:** 2026-10-03T10:29:18Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Maintainer advisory and release notes reviewed\. Deployment state and source immutability are not established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08-11; precision: day; basis: explicit; source: [Escalation to author access by reviewers](<https://github.com/kohler/hotcrp/security/advisories/GHSA-v8jx-vq6p-jq52>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource-edition release established\. Software patch-release date 2026-08-05 is distinct from resource publication\.
- **source displayed:** 2026-08-11; precision: day; basis: explicit; source: [Escalation to author access by reviewers](<https://github.com/kohler/hotcrp/security/advisories/GHSA-v8jx-vq6p-jq52>) (source ID: advisory).

## Caveats

- Requires an authenticated reviewer or program-committee member and existing submission visibility; this is not an unauthenticated access claim\.
- The maintainer reports an action-log review finding no exploitation on its hosted service\. That statement does not establish absence of incidents in other deployments\. The advisory reports capability and consequences, without a separate production-incident narrative\.
- kohler published the advisory; discovery is credited to an internal audit without a named individual reporter\. The original report date is unknown\.
- This review did not independently verify the patch implementation or deployed state\. Upgrade evidence does not establish reversal of any prior unauthorized authorship changes\. Learning prerequisites are editorial\.

## Sources and attribution

- [Escalation to author access by reviewers](<https://github.com/kohler/hotcrp/security/advisories/GHSA-v8jx-vq6p-jq52>) — HotCRP; source ID: advisory; provenance: official primary; retrieved 2026-10-03T10:29:18Z; supports: summary, version, dates.
- [HotCRP release notes: version 3\.4](<https://github.com/kohler/hotcrp/blob/master/NEWS.md>) — HotCRP; source ID: release-notes; provenance: official primary; retrieved 2026-10-03T10:29:18Z; supports: version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
