# Server-side template injection \(SSTI\)

[2025–2026 category index](../vulnerability-reports-2025-2026.md) · [Broad vulnerability families](../vulnerability-types.md) · [Library home](../../README.md)

**0 award-backed reports · 1 educational case study · 0 learning references**

Source-established untrusted input being interpreted as server-side template syntax\. Broad injection labels, unsafe reflection, template use and server rendering alone do not establish SSTI\.

Search aliases: server-side-template-injection.

Publication groups use original selected-source publication dates, retaining their recorded precision and uncertainty. Learning relevance is editorial, not evidence that a vulnerability remains present. Review dates, CVE years and later page updates are not publication dates. [Date and classification rules](../vulnerability-navigation.md).

On this page: [Award-backed reports](#award-reports) · [Educational case studies](#case-studies) · [Learning references](#learning)

<a id="award-reports"></a>
## Award-backed reports

No award-backed reports currently mapped from reviewed evidence. This is a collection gap, not evidence that this vulnerability type does not occur.

<a id="case-studies"></a>
## Related educational case studies

Maintainer advisories and researcher publications remain educational resources; they do not establish a qualifying individual award.

### 2026 publications

- **[Jupyter Enterprise Gateway: keep kernel configuration outside template authority](<../resources/jupyter-enterprise-gateway-2026-kernel-configuration-template-boundary.md>)**
  Maintainer Advisory; publication: 2026-06-03; precision: day; basis: explicit.
  Publication evidence: [Jinja2 Template Server Side Template Injection resulting in Remote Code Execution](<https://github.com/jupyter-server/enterprise_gateway/security/advisories/GHSA-f49j-v924-fx9w>).
  Date qualification: Explicit advisory publication date\.
  Classification: Server-side template injection \(SSTI\) (source explicit). The maintainer explicitly identifies SSTI: untrusted configuration becomes server-side template source, rather than merely supplying data to a trusted template\.
  Evidence: [Jinja2 Template Server Side Template Injection resulting in Remote Code Execution](<https://github.com/jupyter-server/enterprise_gateway/security/advisories/GHSA-f49j-v924-fx9w>); location: Advisory Summary and Details; Weaknesses CWE-1336.
  2025–2026 learning relevance (editorial): For 2025–2026 review, separate configuration data from interpreter authority and distinguish fixing that boundary from limiting workload privileges\. The publication date and earlier remediation history answer different questions\.

### 2025 publications

No mapped records with an established publication date in this year.

<a id="learning"></a>
## Related learning references

General guidance is kept separate from individual disclosures and is not counted as a case study.

No related learning references currently mapped from reviewed evidence. This is a collection gap, not evidence that this vulnerability type does not occur.

---

Generated offline from [evidence-backed navigation metadata](<../../data/vulnerability-navigation.json>) and unchanged canonical records. [Schema](<../../schema/vulnerability-navigation.schema.json>) · [Maintenance and limitations](../vulnerability-navigation.md). No target requests, tests or exploit instructions.
