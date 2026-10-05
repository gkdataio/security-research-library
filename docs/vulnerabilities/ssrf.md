# Server-side request forgery \(SSRF\)

[2025–2026 category index](../vulnerability-reports-2025-2026.md) · [Broad vulnerability families](../vulnerability-types.md) · [Library home](../../README.md)

**1 award-backed report · 3 educational case studies · 1 learning reference**

Source-established failures of server request-destination authority\. Keep affected configurations, runtime reachability and bounded impact in the linked evidence\.

Search aliases: server-side-request-forgery.

Publication groups use original selected-source publication dates, retaining their recorded precision and uncertainty. Learning relevance is editorial, not evidence that a vulnerability remains present. Review dates, CVE years and later page updates are not publication dates. [Date and classification rules](../vulnerability-navigation.md).

On this page: [Award-backed reports](#award-reports) · [Educational case studies](#case-studies) · [Learning references](#learning)

<a id="award-reports"></a>
## Award-backed reports

### 2026 publications

No mapped records with an established publication date in this year.

### 2025 publications

No mapped records with an established publication date in this year.

### Historical publications (before 2025)

- **[Shopify Exchange screenshot service crossed internal boundaries](<../reports/shopify-exchange-request-isolation-2019.md>)**
  bug bounty; publication: 2019-04-03; precision: day; basis: explicit.
  Publication evidence: [One Million Dollars in Bug Bounties](<https://shopify.engineering/one-million-dollars-in-bug-bounties>).
  Classification: Server-side request forgery \(SSRF\) (source explicit). The vendor explicitly identifies server-side request forgery affecting a bounded screenshot-service infrastructure subset\.
  Evidence: [One Million Dollars in Bug Bounties](<https://shopify.engineering/one-million-dollars-in-bug-bounties>); location: Screenshot-service vulnerability example.
  2025–2026 learning relevance (editorial): Request-destination policy, metadata isolation and least privilege remain useful service-design lessons; the historical case excludes Shopify core\.

<a id="case-studies"></a>
## Related educational case studies

Maintainer advisories and researcher publications remain educational resources; they do not establish a qualifying individual award.

### 2026 publications

- **[Formie: integration settings need operation and attribute authority](<../resources/formie-2026-integration-settings-credential-authority.md>)**
  Maintainer Advisory; publication: 2026-07-09; precision: day; basis: explicit.
  Publication evidence: [Formie integration-settings security advisory](<https://github.com/verbb/formie/security/advisories/GHSA-v3f3-cmj4-cvj9>).
  Date qualification: Maintainer publication; separate from the later database entry\.
  Classification: Server-side request forgery \(SSRF\) (source explicit). The maintainer explicitly identifies SSRF with responses returned to an authenticated caller; the classification is not inferred from destination settings alone\.
  Evidence: [Formie integration-settings security advisory](<https://github.com/verbb/formie/security/advisories/GHSA-v3f3-cmj4-cvj9>); location: Advisory title; Description / Impact; Weaknesses CWE-918.
  2025–2026 learning relevance (editorial): Integration permission checks and restrictions on security-sensitive settings must preserve destination authority and credential confinement; retain the affected-configuration requirement and avoid inferring a production incident\.

- **[SvelteKit: origin construction and routing must preserve server request authority](<../resources/sveltekit-2026-origin-routing-trust-boundary.md>)**
  Research Paper; publication: 2026-01; precision: month; basis: explicit.
  Publication evidence: [Avoiding the paradox: A native full-read SSRF and one-shot DoS in SvelteKit](<https://zhero-web-sec.github.io/research-and-things/avoiding-the-paradox-a-native-full-read-ssrf-and-oneshot-dos-in-sveltekit>).
  Date qualification: Article displays this publication date; advisory disclosure is a separate event\.
  Classification: Server-side request forgery \(SSRF\) (source explicit). The researcher and maintainer explicitly identify conditional SSRF involving framework origin construction and server request authority\.
  Evidence: [Denial of service and possible SSRF when using prerendering](<https://github.com/sveltejs/kit/security/advisories/GHSA-j62c-4x62-9r35>), [Avoiding the paradox: A native full-read SSRF and one-shot DoS in SvelteKit](<https://zhero-web-sec.github.io/research-and-things/avoiding-the-paradox-a-native-full-read-ssrf-and-oneshot-dos-in-sveltekit>); location: Research title and conclusion; maintainer advisory CWE-918 classification.
  2025–2026 learning relevance (editorial): Keep origin trust, deployment prerequisites, runtime reachability and authentication limits explicit; do not substitute patch dates for publication\.

### 2025 publications

- **[Axios: URL construction does not establish destination authority](<../resources/axios-2025-base-url-destination-authority.md>)**
  Maintainer Advisory; publication: 2025-03-07; precision: day; basis: explicit.
  Publication evidence: [Axios absolute-URL security advisory GHSA-jr5f-v2jv-69x6](<https://github.com/axios/axios/security/advisories/GHSA-jr5f-v2jv-69x6>).
  Date qualification: Original maintainer-advisory publication\.
  Classification: Server-side request forgery \(SSRF\) (source explicit). The maintainer explicitly identifies SSRF when caller-controlled URL input defeats an application assumption about destination confinement\.
  Evidence: [Axios absolute-URL security advisory GHSA-jr5f-v2jv-69x6](<https://github.com/axios/axios/security/advisories/GHSA-jr5f-v2jv-69x6>); location: Advisory title, Summary and Impact.
  2025–2026 learning relevance (editorial): Treat destination policy and credential scope as explicit application invariants; preserve runtime prerequisites and distinguish historical patch evidence from current safe-input requirements\.

<a id="learning"></a>
## Related learning references

General guidance is kept separate from individual disclosures and is not counted as a case study.

### 2026 publications

No mapped records with an established publication date in this year.

### 2025 publications

No mapped records with an established publication date in this year.

### Unknown original publication date

- **[OWASP Server-Side Request Forgery Prevention](<../resources/owasp-server-request-destination-boundaries.md>)**
  Implementation Guide; publication: Unknown original publication date; precision: unknown; basis: not reported.
  Classification: Server-side request forgery \(SSRF\) (source explicit). OWASP explicitly provides server-side request forgery prevention guidance rather than an individual disclosure\.
  Evidence: [Server-Side Request Forgery Prevention Cheat Sheet](<https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html>); location: SSRF prevention guidance.
  2025–2026 learning relevance (editorial): Use destination-policy and network-isolation principles for service review; the living reference has no established original publication date\.

---

Generated offline from [evidence-backed navigation metadata](<../../data/vulnerability-navigation.json>) and unchanged canonical records. [Schema](<../../schema/vulnerability-navigation.schema.json>) · [Maintenance and limitations](../vulnerability-navigation.md). No target requests, tests or exploit instructions.
