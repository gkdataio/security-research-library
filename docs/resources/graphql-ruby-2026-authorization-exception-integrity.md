# GraphQL-Ruby: authorization exceptions must stop execution

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/graphql-ruby-2026-authorization-exception-integrity.json>) · [Official resource](<https://securitylab.github.com/advisories/GHSL-2026-152_graphql-ruby/>)

**Publisher:** GitHub Security Lab  
**Authors:** Bas Alberts  
**Resource type:** Research Paper  
**Version:** GHSL-2026-152 / GHSA-j7xr-4g94-r9h3  
**Topics:** Authorization; Web Foundations  
**Defensive skills:** Model access-control invariants; Review secure error behavior; Verify remediation evidence

## Original summary

A GraphQL-Ruby execution-engine path converted a resolver authorization exception into permission to continue\. Research demonstrates a denied resolver running and returning a fixture value, while the legacy engine stopped it\. This illustrates why error handling must preserve the security meaning of a denial\.

## Defensive use

The maintainer identifies versions 2\.5\.23 through 2\.6\.5 as affected and 2\.6\.6 as patched\. Only the newer Execution::Next mode and resolver-thrown authorization errors are implicated; other authorization forms worked correctly\. Editorial lesson: preserve denial semantics across execution engines and keep error formatting separate from authority to execute\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic API access-control concepts
- Familiarity with server-side data processing

## Access and freshness

**Access cost at review:** free.

Public sources readable without an account\.

**Reviewed:** 2026-10-03T07:28:33Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary research and maintainer evidence reviewed\. Article immutability and deployment remediation were not established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-08-08; precision: day; basis: explicit; source: [GHSL-2026-152: Privilege escalation via authorization bypass in graphql-ruby](<https://securitylab.github.com/advisories/GHSL-2026-152_graphql-ruby/>) (source ID: research).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. A separate resource-version release is not established\. Software patch-release chronology is preserved in the caveats\.
- **source displayed:** 2026-08-08; precision: day; basis: explicit; source: [GHSL-2026-152: Privilege escalation via authorization bypass in graphql-ruby](<https://securitylab.github.com/advisories/GHSL-2026-152_graphql-ruby/>) (source ID: research).

## Caveats

- The research reports testing 2\.6\.5 and reproducing the behavior on 2\.6\.1\. Its fixture demonstrates resolver execution and returned data; database deletion, external calls and broader privilege escalation are possible application-dependent consequences, not demonstrated production incidents\.
- The application must use the affected execution mode and deny access by raising the relevant authorization exception\. This is not a claim that all GraphQL-Ruby deployments bypassed authorization\.
- Research timeline: reported July 16, acknowledged and fixed July 17, 2026\. Maintainer advisory and patched release date are July 21; detailed research publication is August 8\.
- No CVE is identified in the maintainer advisory\. Discovery is credited to GitHub Security Lab Taskflow Agent with manual verification; Bas Alberts is the research byline\. No patch reproduction was performed\.

## Sources and attribution

- [GHSL-2026-152: Privilege escalation via authorization bypass in graphql-ruby](<https://securitylab.github.com/advisories/GHSL-2026-152_graphql-ruby/>) — GitHub Security Lab; source ID: research; provenance: official primary; retrieved 2026-10-03T07:10:00Z; supports: summary, dates.
- [Authorization Bypass in Execution::Next](<https://github.com/rmosolgo/graphql-ruby/security/advisories/GHSA-j7xr-4g94-r9h3>) — GraphQL-Ruby; source ID: maintainer-advisory; provenance: official primary; retrieved 2026-10-03T07:10:00Z; supports: summary, version, dates.
- [GraphQL-Ruby 2\.6\.6 changelog](<https://raw.githubusercontent.com/rmosolgo/graphql-ruby/v2.6.6/CHANGELOG.md>) — GraphQL-Ruby; source ID: maintainer-changelog; provenance: official primary; retrieved 2026-10-03T07:28:33Z; supports: version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
