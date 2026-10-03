# Umbraco: editing an account does not authorize assigning every role

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/umbraco-2026-group-assignment-authority.json>) · [Official resource](<https://securitylab.github.com/advisories/GHSL-2026-065_Umbraco_CMS/>)

**Publisher:** GitHub Security Lab  
**Authors:** Jaroslav Lobačevski  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Authorization; Web Foundations  
**Defensive skills:** Model access-control invariants; Verify remediation evidence

## Original summary

CVE-2026-31834 separates authority over an account from authority to grant its roles\. Research on Umbraco CMS 17\.2\.0 found that group-membership changes checked access to target users but omitted restrictions applied by the ordinary user-editing flow\. A qualifying non-administrator API account could obtain administrator membership\.

## Defensive use

Editorial lesson: model both the target account and the proposed privilege as authorization inputs, using consistent policy across bulk and individual operations\. The maintainer confirms the role-assignment defect and fixes in 16\.5\.1 and 17\.2\.2; upgrade affected installations rather than relying on interface restrictions\.

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

- **published:** 2026-09-21; precision: day; basis: explicit; source: [GHSL-2026-065: Unauthorized group assignment enables privilege escalation in Umbraco CMS](<https://securitylab.github.com/advisories/GHSL-2026-065_Umbraco_CMS/>) (source ID: research).
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate resource-edition release established\. The research dates software fixes 16\.5\.1 and 17\.2\.2 to March 10, 2026, separately from its September publication\.
- **source displayed:** 2026-09-21; precision: day; basis: explicit; source: [GHSL-2026-065: Unauthorized group assignment enables privilege escalation in Umbraco CMS](<https://securitylab.github.com/advisories/GHSL-2026-065_Umbraco_CMS/>) (source ID: research).

## Caveats

- Requires an authenticated backoffice API user with access to the Users section\. The vendor notes that this is ordinarily restricted to administrators, making custom delegation important to exposure\.
- The research reports administrator membership; the vendor describes resulting administrative control\. Neither source establishes a customer incident or exploitation prevalence\.
- Research reported February 25, 2026; acknowledged as a duplicate the next day\. The vendor advisory was published March 10; detailed research September 21\.
- The maintainer lists affected versions as &gt;=15\.3\.1, &lt;17\.2\.1, while listing 16\.5\.1 and 17\.2\.2 as patched\. These fields conflict; no corrected affected interval is inferred\.
- The byline is Jaroslav Lobačevski; discovery is credited to the GitHub Security Lab Taskflow Agent with his manual verification\. The maintainer credits odgrso separately\. Learning prerequisites are editorial\.

## Sources and attribution

- [GHSL-2026-065: Unauthorized group assignment enables privilege escalation in Umbraco CMS](<https://securitylab.github.com/advisories/GHSL-2026-065_Umbraco_CMS/>) — GitHub Security Lab; source ID: research; provenance: official primary; retrieved 2026-10-03T07:59:36Z; supports: summary, dates.
- [Vertical Privilege Escalation via Missing Authorization Checks](<https://github.com/umbraco/Umbraco-CMS/security/advisories/GHSA-rhcg-3h8r-v6vp>) — Umbraco; source ID: maintainer-advisory; provenance: official primary; retrieved 2026-10-03T07:59:36Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
