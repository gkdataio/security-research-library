# SearchLeak: streamed output needs policy enforcement before browser activation

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/microsoft-copilot-2026-streaming-output-activation-boundary.json>) · [Official resource](<https://www.varonis.com/blog/searchleak>)

**Publisher:** Varonis Threat Labs  
**Authors:** Dolev Taler  
**Resource type:** Research Paper  
**Version:** Not established in the reviewed record  
**Topics:** Ai Security; Web Foundations; Interpreter Boundaries  
**Defensive skills:** Review AI authority boundaries; Review input trust boundaries; Reason about concurrent state

## Original summary

SearchLeak \(CVE-2026-42824\) illustrates a timing gap between streamed AI output becoming active in a browser and final-response sanitization\. Varonis reports email-subject disclosure in a larger chain containing this failure\. Cleaning the completed response cannot reverse effects that already occurred\.

## Defensive use

Define output-safety invariants for every observable intermediate state, not just the completed answer\. Keep generated content inert until applicable policy checks have passed\. Review rendering and data-disclosure boundaries together; a clean final display is insufficient evidence that no earlier side effect occurred\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Browser rendering, sanitization and content-security-policy concepts
- AI output trust boundaries and ordering of security checks

## Access and freshness

**Access cost at review:** free.

Public researcher article and Microsoft-authored CNA record\.

**Reviewed:** 2026-10-04T19:43:06Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Researcher article, publisher catalog and Microsoft CNA record read\. Microsoft's direct advisory returned a JavaScript shell; vendor corroboration here comes from the CNA record\. No behavior was independently reproduced\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded. The catalog lists June 15, 2026, but does not distinguish original publication from later updating\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition is established\.
- **source displayed:** 2026-06-15; precision: day; basis: explicit; source: [SearchLeak: How We Turned M365 Copilot Into a One-Click Data Exfiltration Weapon](<https://www.varonis.com/blog/searchleak>) (source ID: researcher). The article labels this date as last updated\.

## Caveats

- The reported conditions require affected enterprise search, relevant content accessible to the victim and the victim opening a supplied link\. This resource isolates the timing boundary; disclosure also depended on additional weaknesses\.
- Wider indexed-content exposure depends on the victim's access\. Account takeover is a proposed consequence, not a demonstrated result in this record\.
- Varonis says Microsoft patched the issue\. The exact fix date and implementation are not established by the reviewed evidence\.
- The Microsoft CNA record corroborates network information disclosure requiring user interaction and identifies an exclusively hosted service\. It supplies no usable affected-version range\. Its CWE-77 classification does not establish operating-system command execution\.
- The CNA's June 4, 2026 public-disclosure date and September 24 update date describe the vulnerability record, not this article's publication or remediation chronology\.
- No individual award amount or affected-victim count is established\. This educational record grants no testing authorization\.

## Sources and attribution

- [SearchLeak: How We Turned M365 Copilot Into a One-Click Data Exfiltration Weapon](<https://www.varonis.com/blog/searchleak>) — Varonis Threat Labs; source ID: researcher; provenance: official primary; retrieved 2026-10-04T19:41:28Z; supports: summary, dates.
- [Varonis Blog catalog: SearchLeak entry](<https://www.varonis.com/blog/all>) — Varonis; source ID: publisher-catalog; provenance: official primary; retrieved 2026-10-04T19:41:39Z; supports: dates.
- [Microsoft CNA record for CVE-2026-42824](<https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/42xxx/CVE-2026-42824.json>) — Microsoft via CVE Program; source ID: microsoft-cna; provenance: official primary; retrieved 2026-10-04T19:42:30Z; supports: summary, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
