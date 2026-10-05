# Cross-site scripting \(XSS\)

[2025–2026 category index](../vulnerability-reports-2025-2026.md) · [Broad vulnerability families](../vulnerability-types.md) · [Library home](../../README.md)

**5 award-backed reports · 11 educational case studies · 2 learning references**

Source-established cross-site scripting, including evidence-backed subtypes below and broader browser-origin or worker cases whose narrower subtype is not established\.

Search aliases: cross-site-scripting.

Subtypes: [Blind XSS](<blind-xss.md>) · [Reflected XSS \(RXSS\)](<reflected-xss.md>) · [Stored XSS](<stored-xss.md>). Each record appears once on this parent page even when supported by several subtype mappings.

Publication groups use original selected-source publication dates, retaining their recorded precision and uncertainty. Learning relevance is editorial, not evidence that a vulnerability remains present. Review dates, CVE years and later page updates are not publication dates. [Date and classification rules](../vulnerability-navigation.md).

On this page: [Award-backed reports](#award-reports) · [Educational case studies](#case-studies) · [Learning references](#learning)

<a id="award-reports"></a>
## Award-backed reports

### 2026 publications

No mapped records with an established publication date in this year.

### 2025 publications

- **[Google IDX worker messaging crossed browser trust boundaries](<../reports/google-idx-worker-message-trust-2025.md>)**
  bug bounty; publication: 2025-07-02; precision: day; basis: explicit.
  Publication evidence: [XSS in Google IDX Workstation](<https://sudistark.github.io/2025/07/02/idx.html>).
  Date qualification: Date displayed by the researcher article\.
  Classification: Cross-site scripting \(XSS\) (source explicit). The primary researcher labels the finding XSS; execution in a worker does not establish direct DOM access or a narrower subtype\.
  Evidence: [XSS in Google IDX Workstation](<https://sudistark.github.io/2025/07/02/idx.html>); location: Article title and worker-execution impact discussion.
  2025–2026 learning relevance (editorial): Review message authority across browser and worker boundaries while preserving the prior-resource-access requirement and bounded impact\.

### Unknown original publication date

- **[Facebook SDK message authentication relied on insecure randomness](<../reports/facebook-sdk-message-authentication-randomness-2023.md>)**
  bug bounty; publication: Unknown original publication date; precision: unknown; basis: not reported.
  Date qualification: Current archive page displays 2026-01-17\. Original publication versus migration/republication is not established, so this date is not used as a recent disclosure\.
  Classification: Cross-site scripting \(XSS\) (source explicit). The source explicitly describes DOM-XSS; it does not establish stored, reflected or blind classification for this navigation\.
  Evidence: [Account Takeover in Facebook mobile app due to usage of cryptographically unsecure random number generator and XSS in Facebook JS SDK](<https://ysamm.com/uncategorized/2026/01/17/math-random-facebook-sdk.html>); location: DOM-XSS discussion and message-handler analysis.
  2025–2026 learning relevance (editorial): Treat message authenticity and safe browser rendering as separate requirements; unknown original publication remains separate from its later archive header\.

- **[iCloud sharing consent and Safari trust boundaries failed together](<../reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.md>)**
  bug bounty; publication: Unknown original publication date; precision: unknown; basis: not reported.
  Date qualification: The primary researcher page does not supply a publication date; no exact date is inferred\.
  Classification: Cross-site scripting \(XSS\) (source explicit). The researcher explicitly identifies universal cross-site scripting involving browser-origin isolation; persisted sharing consent is not evidence of stored XSS\.
  Evidence: [iCloud sharing consent and Safari trust boundaries failed together](<https://www.ryanpickren.com/safari-uxss>); location: Universal cross-site scripting discussion.
  2025–2026 learning relevance (editorial): Review whether consent survives material content changes and whether cross-application handling preserves browser-origin isolation\.

- **[Meta Conversions API Gateway mixed configuration data with executable output](<../reports/meta-conversions-gateway-generated-script-boundary-2025.md>)**
  bug bounty; publication: Unknown original publication date; precision: unknown; basis: not reported.
  Date qualification: Current page header is January 13, 2026; a separately indexed 2025 URL also exists\. Original publication versus archive migration or republication is not established\.
  Classification: Stored XSS (source explicit). The source identifies stored XSS where persisted configuration becomes generated JavaScript consumed by browsers\.
  Evidence: [Multiple XSS in Meta Conversion API Gateway Leading to Zero-Click Account Takeover](<https://ysamm.com/uncategorized/2026/01/13/capig-xss.html>); location: Bug \#2 backend finding.
  2025–2026 learning relevance (editorial): Preserve context-safe serialization when configuration is later emitted as executable browser content; the archive header does not establish a 2026 publication\.

- **[Meta Conversions API Gateway trusted message origins as script authority](<../reports/meta-conversions-gateway-message-origin-boundary-2024.md>)**
  bug bounty; publication: Unknown original publication date; precision: unknown; basis: not reported.
  Date qualification: Current header: January 13, 2026\. Original publication is unestablished; archive dating cannot establish first disclosure\.
  Classification: Cross-site scripting \(XSS\) (source explicit). The source identifies client-side XSS caused by message-origin data acquiring script authority; Bug \#2's stored classification is not transferred to this separate report\.
  Evidence: [Multiple XSS in Meta Conversion API Gateway Leading to Zero-Click Account Takeover](<https://ysamm.com/uncategorized/2026/01/13/capig-xss.html>); location: Bug \#1 client-side finding.
  2025–2026 learning relevance (editorial): Review origin authorization and initialization trust while retaining the recorded content-policy, interaction and authenticated-session limits\.

<a id="case-studies"></a>
## Related educational case studies

Maintainer advisories and researcher publications remain educational resources; they do not establish a qualifying individual award.

### 2026 publications

- **[Angular host bindings: bind sanitization to the concrete output element](<../resources/angular-2026-host-binding-context-authority.md>)**
  Maintainer Advisory; publication: 2026-08-18; precision: day; basis: explicit.
  Publication evidence: [Sanitization bypass via directive host bindings on concrete host elements in @angular/core and @angular/compiler](<https://github.com/angular/angular/security/advisories/GHSA-hh8m-fm6v-7cvg>).
  Date qualification: Publication of the selected maintainer advisory; earlier public discussion is separately noted\.
  Classification: Cross-site scripting \(XSS\) (source explicit). The maintainer identifies XSS where concrete host context loses the expected sanitization protection\.
  Evidence: [Sanitization bypass via directive host bindings on concrete host elements in @angular/core and @angular/compiler](<https://github.com/angular/angular/security/advisories/GHSA-hh8m-fm6v-7cvg>); location: Advisory impact and CWE-79 classification.
  2025–2026 learning relevance (editorial): Resolve security policy against the actual output context rather than a context assumed before composition\.

- **[Angular SSR: preserve output context through serialization and post-processing](<../resources/angular-2026-raw-content-serialization-context.md>)**
  Maintainer Advisory; publication: 2026-07-29; precision: day; basis: explicit.
  Publication evidence: [Missing Fallback Raw-Content Serialization Escaping leads to Cross-Site Scripting \(XSS\) in Angular SSR](<https://github.com/angular/angular/security/advisories/GHSA-vpx6-8pjr-4g3v>).
  Date qualification: Publication of the selected maintainer advisory; earlier public discussion is separately noted\.
  Classification: Cross-site scripting \(XSS\) (source explicit). The maintainer explicitly identifies SSR XSS; the reviewed evidence does not establish stored, reflected or blind input lifecycle\.
  Evidence: [Missing Fallback Raw-Content Serialization Escaping leads to Cross-Site Scripting \(XSS\) in Angular SSR](<https://github.com/angular/angular/security/advisories/GHSA-vpx6-8pjr-4g3v>); location: Advisory title and Impact.
  2025–2026 learning relevance (editorial): Preserve inert text meaning across serialization and re-parsing, and retain follow-up advisories that qualify the original remediation\.

- **[CI4MS: keep stored diagnostic content inert in administrative log views](<../resources/ci4ms-2026-log-viewer-stored-blind-xss-boundary.md>)**
  Maintainer Advisory; publication: 2026-03-31; precision: day; basis: explicit.
  Publication evidence: [CI4MS log-viewer security advisory GHSA-r4v5-rwr2-q7r4](<https://github.com/ci4-cms-erp/ci4ms/security/advisories/GHSA-r4v5-rwr2-q7r4>).
  Date qualification: Original maintainer-advisory publication; later database events are separate\.
  Classification: Blind XSS (source explicit). Both sources explicitly identify blind XSS; the database describes execution in a later administrative view rather than immediate observation by the contributor of logged data\.
  Evidence: [CI4MS log-viewer security advisory GHSA-r4v5-rwr2-q7r4](<https://github.com/ci4-cms-erp/ci4ms/security/advisories/GHSA-r4v5-rwr2-q7r4>), [GitHub Advisory Database entry for CVE-2026-34560](<https://github.com/advisories/GHSA-r4v5-rwr2-q7r4>); location: Maintainer Description; Advisory Database Summary and Description.
  2025–2026 learning relevance (editorial): Treat diagnostic displays as browser trust boundaries, even when input and execution occur in separate contexts\. Preserve the required administrator view and the conflicting interaction metric\.
  Classification: Stored XSS (source explicit). The maintainer explicitly identifies stored DOM XSS; the database describes retained log content later becoming active in the browser\. Persistence is supported independently of the blind observation context\.
  Evidence: [CI4MS log-viewer security advisory GHSA-r4v5-rwr2-q7r4](<https://github.com/ci4-cms-erp/ci4ms/security/advisories/GHSA-r4v5-rwr2-q7r4>), [GitHub Advisory Database entry for CVE-2026-34560](<https://github.com/advisories/GHSA-r4v5-rwr2-q7r4>); location: Maintainer title and Description; Advisory Database Summary and Description.
  2025–2026 learning relevance (editorial): Keep persisted diagnostic values inert when read and rendered\. Storing a value does not confer trust, and the advisory publication remains separate from later database dates and software-release events\.

- **[DOMPurify: accepted DOM realms must retain complete sanitization](<../resources/dompurify-2026-cross-realm-sanitization-consistency.md>)**
  Maintainer Advisory; publication: 2026-05-26; precision: day; basis: explicit.
  Publication evidence: [Cross-realm IN\_PLACE sanitization leaves executable markup intact via realm-bound instanceof checks](<https://github.com/cure53/DOMPurify/security/advisories/GHSA-hpcv-96wg-7vj8>).
  Date qualification: Publication of the selected advisory\.
  Classification: Cross-site scripting \(XSS\) (source explicit). The maintainer identifies XSS when accepted foreign-realm DOM input misses protective checks; later activation alone does not establish stored or blind XSS\.
  Evidence: [Cross-realm IN\_PLACE sanitization leaves executable markup intact via realm-bound instanceof checks](<https://github.com/cure53/DOMPurify/security/advisories/GHSA-hpcv-96wg-7vj8>); location: Advisory impact and CWE-79 classification.
  2025–2026 learning relevance (editorial): Apply equivalent sanitization controls to all accepted input representations and realm boundaries\.

- **[Next\.js: response metadata must preserve representation boundaries](<../resources/nextjs-2026-response-metadata-representation-boundary.md>)**
  Research Paper; publication: 2026-06; precision: month; basis: explicit.
  Publication evidence: [Re:CACHE: Next\.js response-reflection research](<https://zhero-web-sec.github.io/research-and-things/re-cache-excessive-reflection-type-confusion-and-0-click-sxss-on-nextjs>).
  Date qualification: The article displays June 2026; no publication day is established\.
  Classification: Stored XSS (source explicit). The researcher identifies cache-mediated stored XSS and distinguishes it from classic reflected XSS\.
  Evidence: [Re:CACHE: Next\.js response-reflection research](<https://zhero-web-sec.github.io/research-and-things/re-cache-excessive-reflection-type-confusion-and-0-click-sxss-on-nextjs>); location: Override, mutation and \(S\)XSS section.
  2025–2026 learning relevance (editorial): Review response meaning and shared-cache persistence together while retaining the source's configuration-specific limits\.

- **[Parse Server: preserve safe file interpretation across storage and browsers](<../resources/parse-server-2026-upload-metadata-consumer-boundary.md>)**
  Maintainer Advisory; publication: 2026-06-25; precision: day; basis: explicit.
  Publication evidence: [Stored XSS via malformed Content-Type bypassing file upload extension blocklist](<https://github.com/parse-community/parse-server/security/advisories/GHSA-r899-h629-j84r>).
  Date qualification: Maintainer advisory publication\.
  Classification: Stored XSS (source explicit). The maintainer explicitly identifies stored XSS across uploaded-object metadata, storage and browser interpretation\.
  Evidence: [Stored XSS via malformed Content-Type bypassing file upload extension blocklist](<https://github.com/parse-community/parse-server/security/advisories/GHSA-r899-h629-j84r>); location: Advisory title and Impact.
  2025–2026 learning relevance (editorial): Keep upload acceptance and delivery interpretation in one security contract, with the affected storage configuration and user-interaction requirements preserved\.

- **[Qwik: resumability metadata must preserve HTML serialization boundaries](<../resources/qwik-2026-resumability-comment-serialization-boundary.md>)**
  Maintainer Advisory; publication: 2026-02-03; precision: day; basis: explicit.
  Publication evidence: [Qwik SSR XSS via Unsafe Virtual Node Serialization](<https://github.com/QwikDev/qwik/security/advisories/GHSA-m6jq-g7gq-5w3c>).
  Date qualification: Maintainer advisory publication, not software patch release\.
  Classification: Cross-site scripting \(XSS\) (source explicit). The maintainer identifies SSR XSS through virtual-node serialization; dynamic attributes alone do not establish persistence or request reflection\.
  Evidence: [Qwik SSR XSS via Unsafe Virtual Node Serialization](<https://github.com/QwikDev/qwik/security/advisories/GHSA-m6jq-g7gq-5w3c>); location: Advisory title and Summary.
  2025–2026 learning relevance (editorial): Keep server-to-browser state serialization safe in comment and structural metadata contexts, not only visible text\.

- **[Svelte hydration: serialization must preserve the enclosing output context](<../resources/svelte-2026-hydration-output-context-boundary.md>)**
  Research Paper; publication: 2026-03-17; precision: day; basis: explicit.
  Publication evidence: [CVE-2025-15265: Svelte Hydratable Key SSR XSS - Lydian](<https://caverav.cl/posts/svelte-hydratable-xss/svelte-hydratable-xss/>).
  Date qualification: Article displays this publication date; advisory disclosure is a separate event\.
  Classification: Reflected XSS \(RXSS\) (source explicit). The researcher advisory explicitly labels reflected XSS involving user-influenced hydration keys and HTML output context\.
  Evidence: [Svelte 5\.46\.0 - Hydratable Key Script-Breakout XSS \(SSR\)](<https://fluidattacks.com/advisories/lydian>); location: Summary: Vulnerability name and Vulnerability type.
  2025–2026 learning relevance (editorial): Use the article's March publication date separately from the January advisory event, and preserve a consistent encoding contract across keys and values\.

- **[TanStack Start: preserve server-owned response authority through errors](<../resources/tanstack-2026-server-function-response-authority.md>)**
  Maintainer Advisory; publication: 2026-09-30; precision: day; basis: explicit.
  Publication evidence: [Unauthenticated reflected XSS in TanStack Start server-function responses](<https://github.com/TanStack/router/security/advisories/GHSA-qx66-fv34-fjm8>).
  Date qualification: GitHub explicitly labels this as the advisory publication date\.
  Classification: Reflected XSS \(RXSS\) (source explicit). The maintainer explicitly describes reflected same-origin XSS when untrusted request data acquires response authority\.
  Evidence: [Unauthenticated reflected XSS in TanStack Start server-function responses](<https://github.com/TanStack/router/security/advisories/GHSA-qx66-fv34-fjm8>); location: Advisory title and Impact.
  2025–2026 learning relevance (editorial): Preserve server-owned response state through failure handling and verify deployment remediation separately from local dependency changes\.

### 2025 publications

- **[Laravel: preserve output encoding in debug diagnostics](<../resources/laravel-2025-debug-diagnostic-output-encoding.md>)**
  Research Paper; publication: 2025-03-10; precision: day; basis: explicit.
  Publication evidence: [SBA Research advisory SBA-ADV-20241209-02](<https://github.com/sbaresearch/advisories/tree/public/2024/SBA-ADV-20241209-02_Laravel_Reflected_XSS_via_Route_Parameter_in_Debug-Mode_Error_Page>).
  Date qualification: Public disclosure in the researcher timeline, corroborated by the dated mailing-list message\.
  Classification: Reflected XSS \(RXSS\) (source explicit). The researcher explicitly identifies reflected XSS from request-derived route data in a debug error response\.
  Evidence: [SBA Research advisory SBA-ADV-20241209-02](<https://github.com/sbaresearch/advisories/tree/public/2024/SBA-ADV-20241209-02_Laravel_Reflected_XSS_via_Route_Parameter_in_Debug-Mode_Error_Page>); location: Advisory title, Vulnerability Overview and Impact.
  2025–2026 learning relevance (editorial): Apply output-context protection to diagnostic views and preserve the debug-mode, error-path and interaction requirements\. Publication and software-fix dates remain separate\.

- **[Trix: validate stored attachment data before link interpretation](<../resources/trix-2025-attachment-link-interpretation-boundary.md>)**
  Maintainer Advisory; publication: 2025-12-30; precision: day; basis: explicit.
  Publication evidence: [Trix attachment-link security advisory GHSA-g9jg-w8vm-g96v](<https://github.com/basecamp/trix/security/advisories/GHSA-g9jg-w8vm-g96v>).
  Date qualification: Original maintainer-advisory publication; later database events are separate\.
  Classification: Stored XSS (source explicit). The maintainer explicitly identifies stored XSS involving attachment metadata later rendered as browser content and clicked by a user\.
  Evidence: [Trix attachment-link security advisory GHSA-g9jg-w8vm-g96v](<https://github.com/basecamp/trix/security/advisories/GHSA-g9jg-w8vm-g96v>); location: Advisory title and Impact.
  2025–2026 learning relevance (editorial): Preserve semantic validation when stored metadata becomes link authority\. Keep the affected integration and interaction prerequisites explicit; the 2025 publication is separate from later database events\.

<a id="learning"></a>
## Related learning references

General guidance is kept separate from individual disclosures and is not counted as a case study.

### 2026 publications

No mapped records with an established publication date in this year.

### 2025 publications

No mapped records with an established publication date in this year.

### Historical publications (before 2025)

- **[Trusted Types: typed sinks depend on trustworthy policy creation](<../resources/w3c-2026-trusted-types-policy-authority.md>)**
  Technical Standard; publication: 2022-09-27; precision: day; basis: explicit.
  Publication evidence: [Trusted Types publication history](<https://www.w3.org/standards/history/trusted-types/>).
  Date qualification: First Public Working Draft of the specification series\.
  Classification: Cross-site scripting \(XSS\) (source explicit). The standard describes protection of browser injection sinks against DOM-based cross-site scripting\.
  Evidence: [Trusted Types](<https://www.w3.org/TR/2026/WD-trusted-types-20260623/>); location: Trusted Types introduction and injection-sink definitions.
  2025–2026 learning relevance (editorial): The reviewed 2026 edition supports browser policy design, while the canonical 2022 original publication remains historical rather than a 2026 disclosure\.

### Unknown original publication date

- **[HTML5 Security Cheat Sheet: Web Messaging](<../resources/owasp-browser-message-trust-boundaries.md>)**
  Implementation Guide; publication: Unknown original publication date; precision: unknown; basis: not reported.
  Classification: Cross-site scripting \(XSS\) (source explicit). The guide explicitly addresses DOM-based XSS prevention when handling browser messages\.
  Evidence: [HTML5 Security Cheat Sheet: Web Messaging](<https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html>); location: Web Messaging guidance.
  2025–2026 learning relevance (editorial): Keep origin validation and safe handling of message content distinct; a living guide with unknown publication date is not a new disclosure\.

---

Generated offline from [evidence-backed navigation metadata](<../../data/vulnerability-navigation.json>) and unchanged canonical records. [Schema](<../../schema/vulnerability-navigation.schema.json>) · [Maintenance and limitations](../vulnerability-navigation.md). No target requests, tests or exploit instructions.
