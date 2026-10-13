# Pterodactyl: delegated tokens must preserve action-specific authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://github.com/pterodactyl/panel/security/advisories/GHSA-8r6w-3qq5-4p4r>) · [Canonical JSON](<../../data/resources/pterodactyl-2026-delegated-token-purpose-binding.json>)

<a id="original-summary"></a>
## Main takeaway

Pterodactyl's maintainer-published report describes a subuser uploading files to an already accessible server without the required creation permission \(GHSA-8r6w-3qq5-4p4r\)\. Tokens established the user and server but did not adequately restrict the operation\. The Panel and Wings therefore disagreed about what the token authorized\.

## Defensive use

Editorial lesson: trusted issuer and valid signature establish token provenance, not authorization for every consumer\. Require explicit purpose at issuance and matching operation scope at consumption\. Panel 1\.12\.3 release notes require a scope when generating tokens; Wings 1\.12\.2 release notes describe verifying subsystem-required scopes\. Review the producer and consumer together\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** Pterodactyl  
**Authors:** anthonyphysgun  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Business Logic and State Integrity; Identity; API Security  
**Defensive skills:** Model access-control invariants; Verify remediation evidence; Review security-token design; Threat-model integrations

## Prerequisites

**Basis:** editorial guidance.

- Basic server-side authorization concepts

## Access and freshness

**Access cost at review:** free.

Public primary sources readable without an account\.

**Reviewed:** 2026-10-03T10:50:10Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Primary advisory and linked remediation evidence reviewed; deployment status was not assessed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-06; precision: day; basis: explicit; source: [Improper JWT scoping permits uploads without file-creation permission](<https://github.com/pterodactyl/panel/security/advisories/GHSA-8r6w-3qq5-4p4r>) (source ID: advisory).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-06-06; precision: day; basis: explicit; source: [Improper JWT scoping permits uploads without file-creation permission](<https://github.com/pterodactyl/panel/security/advisories/GHSA-8r6w-3qq5-4p4r>) (source ID: advisory).

## Caveats

- Requires existing subuser access with a lower-privilege capability such as console connection or downloads\. The advisory explicitly excludes users without subuser access to the server\. Unauthorized upload is supported; cross-server takeover or command execution is not established here\.
- CVE-2026-54593\. The advisory lists Panel before 1\.12\.3 and Wings before 1\.12\.2 as affected, with those versions patched\. Release notes support the stated remediation design; exact patch implementation and deployed coverage were not independently verified\.
- Published June 6, 2026 by anthonyphysgun; TrixterTheTux is credited as reporter\. Product version numbers are not educational-resource editions\. No award evidence is claimed\.

## Sources and attribution

- [Improper JWT scoping permits uploads without file-creation permission](<https://github.com/pterodactyl/panel/security/advisories/GHSA-8r6w-3qq5-4p4r>) — Pterodactyl; source ID: advisory; provenance: official primary; retrieved 2026-10-03T10:50:10Z; supports: summary, version, dates.
- [Panel v1\.12\.3 release notes](<https://github.com/pterodactyl/panel/releases/tag/v1.12.3>) — Pterodactyl; source ID: panel-release; provenance: official primary; retrieved 2026-10-03T10:50:10Z; supports: summary, version.
- [Wings v1\.12\.2 release notes](<https://github.com/pterodactyl/wings/releases/tag/v1.12.2>) — Pterodactyl; source ID: wings-release; provenance: official primary; retrieved 2026-10-03T10:50:10Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
