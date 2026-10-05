# CI4MS: keep stored diagnostic content inert in administrative log views

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/ci4ms-2026-log-viewer-stored-blind-xss-boundary.json>) · [Official resource](<https://github.com/ci4-cms-erp/ci4ms/security/advisories/GHSA-r4v5-rwr2-q7r4>)

**Publisher:** CI4MS maintainers  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Web Foundations; Interpreter Boundaries  
**Defensive skills:** Review input trust boundaries; Review client isolation; Verify remediation evidence

## Original summary

CVE-2026-34560 concerns user-influenced error content retained in CI4MS logs and later interpreted as active browser content in the administrative viewer\. The maintainer explicitly identifies stored DOM blind XSS and CWE-79\. The supporting GitHub Advisory Database narrative describes delayed execution when an administrator opens the logs\. Conceptual boundary: diagnostic storage does not make external data trustworthy for browser interpretation; persistence and a separate observation context explain the two supported subtype labels\.

## Defensive use

Editorial lesson: keep logged values inert throughout storage, retrieval and display\. Use text-only rendering or encoding appropriate to the actual output context, including diagnostic interfaces used by privileged staff\. Review all log-viewing paths for the same data/code separation\. Access restrictions and browser policy are defense in depth, not substitutes for safe rendering\. Verify remediation against the deployed version and its migration requirements; the historical patched-version designation alone is not a current deployment recommendation\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Browser rendering contexts and the distinction between stored data and executable interpretation
- Logging lifecycles and administrative-interface trust boundaries

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory, supporting GitHub Advisory Database entry and release notes\.

**Reviewed:** 2026-10-05T01:03:50Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Read the advisory, database narrative and release notes\. The written demonstration describes browser execution; the external demonstration was not opened\. No reproduction, target testing or independent patch verification performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-03-31; precision: day; basis: explicit; source: [CI4MS log-viewer security advisory GHSA-r4v5-rwr2-q7r4](<https://github.com/ci4-cms-erp/ci4ms/security/advisories/GHSA-r4v5-rwr2-q7r4>) (source ID: advisory). Original maintainer-advisory publication; later database events are separate\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No educational-resource edition date established; a software release is a different event\.
- **source displayed:** 2026-03-31; precision: day; basis: explicit; source: [CI4MS log-viewer security advisory GHSA-r4v5-rwr2-q7r4](<https://github.com/ci4-cms-erp/ci4ms/security/advisories/GHSA-r4v5-rwr2-q7r4>) (source ID: advisory). Publication date displayed on the selected primary advisory\.

## Caveats

- Applicability requires affected CI4MS software, influence over logged content and a later administrator view\. The severity metadata specifies low privileges but no exact application role; its no-user-interaction value conflicts with the narrative's viewing requirement\. Neither point is silently resolved\.
- The sources claim privilege escalation, administrator account takeover and full application compromise\. These broader outcomes are not independently established by this review or the written browser-execution demonstration; production exploitation is not established\.
- The advisory lists affected versions through 0\.28\.6\.0 and patched version 0\.31\.0\.0\. The intervening version range is not classified by this record\.
- bertugfahriozer published the advisory; bugmithlegend is credited as Reporter\. No separate author byline was established, so authors remains empty\.
- The linked 0\.31\.0\.0 release is marked prerelease and includes a replacement log viewer, a framework upgrade and an authentication migration\. These broad release notes do not independently prove the specific patch's effectiveness\.
- The database records publication there on April 1, 2026 and an April 6 update\. Neither replaces the March 31 original advisory publication\.
- No qualifying individual award is established\. Learning prerequisites and generalized defensive guidance are editorial; this educational case grants no testing authorization\.

## Sources and attribution

- [CI4MS log-viewer security advisory GHSA-r4v5-rwr2-q7r4](<https://github.com/ci4-cms-erp/ci4ms/security/advisories/GHSA-r4v5-rwr2-q7r4>) — CI4MS maintainers; source ID: advisory; provenance: official primary; retrieved 2026-10-05T01:01:37Z; supports: summary, dates.
- [GitHub Advisory Database entry for CVE-2026-34560](<https://github.com/advisories/GHSA-r4v5-rwr2-q7r4>) — GitHub Advisory Database; source ID: advisory-database; provenance: official primary; retrieved 2026-10-05T01:01:20Z; supports: summary, dates.
- [CI4MS 0\.31\.0\.0 security and framework release notes](<https://github.com/ci4-cms-erp/ci4ms/releases/tag/0.31.0.0>) — CI4MS maintainers; source ID: release; provenance: official primary; retrieved 2026-10-05T01:01:37Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
