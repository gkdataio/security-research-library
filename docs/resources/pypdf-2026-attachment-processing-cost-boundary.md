# pypdf: bound repeated work when reading embedded attachments

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/pypdf-2026-attachment-processing-cost-boundary.json>) · [Official resource](<https://github.com/py-pdf/pypdf/security/advisories/GHSA-v247-6f48-mgcj>)

**Publisher:** py-pdf / pypdf  
**Authors:** stefan6419846  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Verification  
**Defensive skills:** Review parsing and serialization; Review input trust boundaries; Verify remediation evidence

## Original summary

CVE-2026-102999 concerns excessive processing time in the dictionary-based embedded-file interface\. The maintainer explains that retrieving each attachment repeatedly parsed the full attachment list\. Thus input structure could multiply processing work even when each individual retrieval looked ordinary\. The advisory identifies versions before 6\.19\.0 as affected\.

## Defensive use

The maintainer identifies 6\.19\.0 as patched\. The merged correction records file objects by name so subsequent retrieval mostly accesses the corresponding stream directly\. Editorial lesson for document-processing services: review aggregate complexity across convenience APIs, not only individual parsing calls, and maintain independent worker time and resource budgets\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Document-processing pipelines and PDF embedded-file concepts
- Basic algorithmic complexity and resource isolation

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory and remediation references readable without an account\.

**Reviewed:** 2026-10-03T07:39:01Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed maintainer advisory, release and merged remediation discussion; no vulnerability reproduction or independent patch testing performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-09-16; precision: day; basis: explicit; source: [Possible long runtimes with large amount of embedded files](<https://github.com/py-pdf/pypdf/security/advisories/GHSA-v247-6f48-mgcj>) (source ID: advisory). Maintainer advisory publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource-edition release established; software patch chronology is retained in the caveats\.
- **source displayed:** 2026-09-16; precision: day; basis: explicit; source: [Possible long runtimes with large amount of embedded files](<https://github.com/py-pdf/pypdf/security/advisories/GHSA-v247-6f48-mgcj>) (source ID: advisory). Publication date displayed beside the advisory publisher\.

## Caveats

- The advisory requires use of the dictionary-based embedded-file API\. Merely receiving a PDF or using unrelated pypdf functionality does not establish exposure\.
- The public advisory confirms long-runtime impact but does not provide measured production outage evidence; no execution or confidentiality impact is established\.
- jungmingi-lab is credited as reporter; stefan6419846 published the advisory and authored the remediation explanation\.
- The correction merged September 14, 2026; release and advisory publication occurred September 16\. The release classifies this change as a performance improvement, while the separate advisory identifies its security relevance\.
- No bounty claim is made\. Learning prerequisites and service-level budget recommendations are editorial\.
- The cited software release is dated 2026-09-16; it is distinct from the advisory publication and is not a claim about the latest available release\.

## Sources and attribution

- [Possible long runtimes with large amount of embedded files](<https://github.com/py-pdf/pypdf/security/advisories/GHSA-v247-6f48-mgcj>) — py-pdf / pypdf; source ID: advisory; provenance: official primary; retrieved 2026-10-03T07:39:01Z; supports: summary, dates.
- [Version 6\.19\.0, 2026-09-16](<https://github.com/py-pdf/pypdf/releases/tag/6.19.0>) — py-pdf / pypdf; source ID: release; provenance: official primary; retrieved 2026-10-03T07:39:01Z; supports: summary, version, dates.
- [Reduce number of full data lookups for attachment mapping API](<https://github.com/py-pdf/pypdf/pull/4081>) — py-pdf / pypdf; source ID: remediation; provenance: official primary; retrieved 2026-10-03T07:39:01Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
