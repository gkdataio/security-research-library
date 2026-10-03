# Zammad: overridden serialization must preserve group authorization

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/zammad-2026-asset-serialization-group-authorization.json>) · [Official resource](<https://securitylab.github.com/advisories/GHSL-2026-049_Zammad/>)

**Publisher:** GitHub Security Lab  
**Authors:** Man Yue Mo  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Web Foundations  
**Defensive skills:** Model access-control invariants; Verify remediation evidence

## Original summary

GHSL-2026-049 describes a ticket asset serializer that overrode a permission-aware base implementation without preserving its group-access check\. GitHub Security Lab reports confidential ticket and associated-user disclosure in tested Zammad 6\.5\.2; the vendor corroborates unauthorized asset access\.

## Defensive use

Editorial lesson: a model override must retain the security contract of its base implementation\. Bind serialization to the requesting actor and the resource group before response construction; review inherited and specialized serializers together\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic understanding of server-side object authorization and resource ownership

## Access and freshness

**Access cost at review:** free.

Public sources readable without an account\.

**Reviewed:** 2026-10-03T13:10:00Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary disclosure and maintainer evidence reviewed; no deployment inspection or vulnerability testing performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-03-06; precision: day; basis: explicit; source: [GHSL-2026-049: An Insecure Direct Object Reference \(IDOR\) in Zammad Leads to Access Control Violations](<https://securitylab.github.com/advisories/GHSL-2026-049_Zammad/>) (source ID: research).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource edition is stated; software fix chronology is recorded in caveats\.
- **source displayed:** 2026-03-06; precision: day; basis: explicit; source: [GHSL-2026-049: An Insecure Direct Object Reference \(IDOR\) in Zammad Leads to Access Control Violations](<https://securitylab.github.com/advisories/GHSL-2026-049_Zammad/>) (source ID: research).

## Caveats

- The case requires an authenticated agent-role user\. Documented impact is reading tickets and associated information outside permitted groups\. The research summary mentions possible manipulation, but its impact section and vendor notice substantiate disclosure; this record makes no demonstrated-write claim\.
- GitHub Security Lab reported February 17, 2026; the maintainer identified it as a duplicate February 18\. GHSL credits Taskflow Agent discovery with manual verification by Peter Stöckli and Man Yue Mo\. Vendor ZAA-2026-05 credits Sho Odagiri of GMO Cybersecurity; preserve both attributions\.
- Vendor ZAA-2026-05 displays March 4, 2026 above a February 25 advisory-detail date\. It lists fixes in 7\.0\.0 and 6\.5\.3 and says SaaS remediation was handled\. GHSL dates the 7\.0\.0 patch release March 4\. A release-specific date for 6\.5\.3 is not established here\.
- The reviewed notice still says CVE assignment pending\. No bounty amount, customer incident count, or independent deployment verification is supplied\. Learning prerequisites and design lessons are editorial\.

## Sources and attribution

- [GHSL-2026-049: An Insecure Direct Object Reference \(IDOR\) in Zammad Leads to Access Control Violations](<https://securitylab.github.com/advisories/GHSL-2026-049_Zammad/>) — GitHub Security Lab; source ID: research; provenance: official primary; retrieved 2026-10-03T13:10:00Z; supports: summary, dates.
- [Security Advisory ZAA-2026-05](<https://zammad.com/en/advisories/zaa-2026-05>) — Zammad; source ID: vendor; provenance: official primary; retrieved 2026-10-03T13:10:00Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
