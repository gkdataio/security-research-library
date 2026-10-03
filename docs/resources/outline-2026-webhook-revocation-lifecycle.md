# Outline: integration authority must end with its owning account

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/outline-2026-webhook-revocation-lifecycle.json>) · [Official resource](<https://github.com/outline/outline/security/advisories/GHSA-33jq-x32c-3ccw>)

**Publisher:** Outline  
**Authors:** tommoor  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Identity; Business Logic and State Integrity  
**Defensive skills:** Review identity lifecycle; Threat-model integrations; Model access-control invariants

## Original summary

GHSA-33jq-x32c-3ccw describes webhook authority surviving deletion of its creator\. Account cleanup omitted webhook subscriptions, while delivery trusted their enabled state\. The maintainer-published report describes a local demonstration of document content delivery after the administrator account was deleted\.

## Defensive use

Editorial lesson: revocation must cover durable integrations and every terminal account state, with delivery-time checks as defense in depth\. The advisory identifies 1\.8\.0 as patched\. Its proposed cleanup changes are recommendations, not evidence of the implemented patch\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic server-side authorization concepts

## Access and freshness

**Access cost at review:** free.

Public disclosure readable without an account\.

**Reviewed:** 2026-10-03T07:59:36Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Public primary disclosure reviewed; deployed remediation and source immutability were not established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-06-06; precision: day; basis: explicit; source: [Webhook subscription persists after creator's account deletion](<https://github.com/outline/outline/security/advisories/GHSA-33jq-x32c-3ccw>) (source ID: research).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** 2026-06-06; precision: day; basis: explicit; source: [Webhook subscription persists after creator's account deletion](<https://github.com/outline/outline/security/advisories/GHSA-33jq-x32c-3ccw>) (source ID: research).

## Caveats

- Requires a webhook previously configured by an administrator, followed by account deletion and a matching document event\. The demonstrated deployment used 0\.86\.0; the maintainer lists versions through 1\.7\.1 as affected\.
- Continued delivery was demonstrated locally; no production incident, measured duration or customer exposure is established\. Persistent exposure is the report’s inference from absent expiry and revalidation\.
- Published June 6, 2026 by tommoor, with dizconnectz credited as reporter\. Publication does not establish the release date of 1\.8\.0\. Learning prerequisites are editorial\.

## Sources and attribution

- [Webhook subscription persists after creator's account deletion](<https://github.com/outline/outline/security/advisories/GHSA-33jq-x32c-3ccw>) — Outline; source ID: research; provenance: official primary; retrieved 2026-10-03T07:59:36Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
