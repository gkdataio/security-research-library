# OWASP WebGoat: Web-Application Security Lessons

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Official resource](<https://owasp.org/projects/webgoat>) · [Canonical JSON](<../../data/resources/owasp-webgoat-controlled-training.json>)

<a id="original-summary"></a>
## Main takeaway

OWASP WebGoat is a deliberately insecure teaching application for common server-side web flaws\. Its interactive lessons offer a controlled setting for understanding security failures and the defenses they need\.

## Defensive use

Study lesson concepts in an isolated local training setup, recording the relevant trust assumption and prevention principle\. Use the material to improve secure-design reasoning without extending exercise activity to third-party systems\.

Educational reference only; linked material does not authorize testing unrelated systems.

## About this resource

**Publisher:** OWASP Foundation  
**Authors:** Not identified in the reviewed record  
**Resource type:** [Training Lab](<../resource-types.md#type-training-lab>)  
**Version:** v2026\.5  
**Topics:** [CTF and Controlled Practice](<../resource-topics.md#topic-ctf-and-practice>); [Web Foundations](<../resource-topics.md#topic-web-foundations>)  
**Defensive skills:** [Learn through controlled practice](<../skillsets.md#skill-controlled-practice>); [Review input trust boundaries](<../skillsets.md#skill-untrusted-input-handling>)

## Prerequisites

**Basis:** editorial guidance.

- A web browser and the ability to run a local teaching application using a supported deployment option\.
- Basic HTTP and web-application concepts are helpful\.

## Access and freshness

**Access cost at review:** free.

OWASP identifies its educational resources as free\. Local computing or optional hosting may involve separate costs; no environment was provisioned\.

**Reviewed:** 2026-10-12T18:30:00Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Official project guidance, README, and release metadata reviewed\. The GitHub release API records v2026\.5 published October 12, 2026 at 06:56:08 UTC\. No runtime verification was performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Original publication date is not stated on the reviewed resource pages\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. Packaged training-application release dates are retained in the maintenance note, not treated as a dated document edition\.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No resource-page publication or revision date is displayed; review time is not a publication date\.

## Caveats

- The publisher warns that running WebGoat makes the host vulnerable, recommends disconnecting from the Internet, and notes that its default configuration binds to localhost\.
- Use only an isolated, explicitly authorized training environment\. No application was installed, started, or tested\.
- The release date belongs to the educational training application, not the original project-page publication\.
- Prerequisites vary with the selected release and deployment method; consult current official documentation before setup\.
- Training application release v2026\.5 is dated 2026-10-12 in the official release source\. It is retained as maintenance evidence; no dated document edition is asserted\.

## Sources and attribution

- [OWASP WebGoat](<https://owasp.org/projects/webgoat>) — OWASP Foundation; source ID: primary; provenance: official primary; retrieved 2026-10-12T18:30:00Z; supports: summary.
- [WebGoat: A deliberately insecure Web Application](<https://github.com/WebGoat/WebGoat>) — OWASP WebGoat; source ID: documentation; provenance: official primary; retrieved 2026-10-12T18:30:00Z; supports: summary, prerequisites.
- [WebGoat v2026\.5](<https://github.com/WebGoat/WebGoat/releases/tag/v2026.5>) — OWASP WebGoat; source ID: release; provenance: official primary; retrieved 2026-10-12T18:30:00Z; supports: version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
