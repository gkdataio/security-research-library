# Sentry: resource ownership must match the authorized organization

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/sentry-2026-organization-object-authorization.json>) · [Official resource](<https://securitylab.github.com/advisories/GHSL-2025-130_Sentry/>)

**Publisher:** GitHub Security Lab  
**Authors:** Peter Stöckli  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Identity  
**Defensive skills:** Model access-control invariants; Verify remediation evidence

## Original summary

CVE-2026-26004 concerned a missing organization constraint in event retrieval\. A permission check on the active organization did not establish ownership of the requested object\. GitHub Security Lab reports cross-organization event disclosure in tested Sentry 25\.12\.0\.

## Defensive use

Editorial lesson: carry tenant identity into resource resolution, rather than checking actor permissions and object lookup independently\. The maintainer patch adds the organization constraint and regression coverage for cross-organization denial\. Review equivalent response paths against the same invariant\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic server-side authentication and authorization concepts

## Access and freshness

**Access cost at review:** free.

Public sources readable without an account\.

**Reviewed:** 2026-10-03T09:29:37Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Research and maintainer evidence reviewed; no live deployment or remediation testing performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-02-20; precision: day; basis: explicit; source: [GHSL-2025-130: Unauthorized access to event data across organizational boundaries in Sentry - CVE-2026-26004](<https://securitylab.github.com/advisories/GHSL-2025-130_Sentry/>) (source ID: research).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Resource has no stated release version; software fixes are described separately\.
- **source displayed:** 2026-02-20; precision: day; basis: explicit; source: [GHSL-2025-130: Unauthorized access to event data across organizational boundaries in Sentry - CVE-2026-26004](<https://securitylab.github.com/advisories/GHSL-2025-130_Sentry/>) (source ID: research).

## Caveats

- The reported case requires an authenticated user with event-read permission in their own organization\. It establishes unauthorized reading, not modification or account takeover; no customer incident or measured data-loss total is supplied\.
- Research was reported December 23, 2025\. Maintainer pull request 105601 was merged January 2, 2026\. Reviewed sources do not establish a packaged fixed release or production rollout date; merge is not deployment\.
- The researcher says Sentry fixed the issue but declined to issue a CVE; GitHub assigned it February 10\. Preserve this provenance rather than implying vendor-issued CVE publication\.
- Byline: Peter Stöckli\. Discovery is credited to a GitHub Security Lab AI agent, reviewed by Peter Stöckli and Man Yue Mo\. Learning prerequisites are editorial\.

## Sources and attribution

- [GHSL-2025-130: Unauthorized access to event data across organizational boundaries in Sentry - CVE-2026-26004](<https://securitylab.github.com/advisories/GHSL-2025-130_Sentry/>) — GitHub Security Lab; source ID: research; provenance: official primary; retrieved 2026-10-03T09:29:37Z; supports: summary, dates.
- [Add functional org filter to GroupEventJsonView \(\#105601\)](<https://github.com/getsentry/sentry/commit/45bc78fd57514a04eb62e73dd1eeb3ca2d723997>) — Sentry; source ID: maintainer-patch; provenance: official primary; retrieved 2026-10-03T09:29:37Z; supports: summary.
- [Add functional org filter to GroupEventJsonView](<https://github.com/getsentry/sentry/pull/105601>) — Sentry; source ID: maintainer-merge; provenance: official primary; retrieved 2026-10-03T09:29:37Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
