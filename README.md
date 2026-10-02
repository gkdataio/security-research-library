# Security Research Library

Source-backed public security disclosures, official learning resources, and original diagrams for understanding defensive security design. Each report connects a documented award with its evidence, root cause, bounded impact, and defensive lessons.

[Browse reports](#report-index) · [Learning guide](docs/learning-guide.md) · [Resources](docs/resources.md) · [Visual guide](docs/visual-theory.md) · [Use the JSON](#use-the-json)

## At a glance

**Snapshot: October 2, 2026**

- **52 qualifying report records:** 42 bug-bounty awards and 10 explicitly labeled competition entries
- **15 educational resources** and **7 conceptual diagrams**, maintained separately from award reports
- **USD 10,000 minimum reported award** per qualifying report or competition entry
- **Publication coverage:** 21 within October 2, 2025–October 2, 2026; 26 older; 5 with unknown original publication dates

These counts describe the collection at the review date. Award evidence is attributed to its source; it is not an independent audit of payment. Historical records and uncertain dates remain explicitly labeled.

## Start here

| If you want to… | Start with… |
|---|---|
| Find a disclosure and inspect its evidence | [Complete report index](#report-index), then the linked JSON record |
| Study defensive design principles by topic | [Defensive learning guide](docs/learning-guide.md) |
| Find standards, documentation, and controlled training | [Official learning resources](docs/resources.md) |
| Understand a security boundary visually | [Visual guide](docs/visual-theory.md), with SVGs, source graphs, and evidence links |
| Build a local catalog or analysis | [JSON exports and schemas](#use-the-json) |
| Understand inclusion and editorial decisions | [Evidence and maintenance policy](DATA_POLICY.md) |

### Explore by topic

- [Account recovery and identity binding](docs/learning-guide.md#6-account-recovery-and-identity-binding)
- [Authorization consistency and safe serialization](docs/learning-guide.md#7-cross-api-consistency-and-safe-serialization)
- [Cloud identities and integration permissions](docs/learning-guide.md#2-cloud-identities-and-integration-permissions)
- [Build systems and dependency provenance](docs/learning-guide.md#3-build-systems-and-dependency-provenance)
- [AI tools and persistent-state authorization](docs/learning-guide.md#4-ai-tools-and-persistent-state-authorization)
- [Parser contracts and memory safety](docs/learning-guide.md#5-parser-contracts-and-memory-safety)
- [Approval and concurrency integrity](docs/learning-guide.md#1-approval-and-concurrency-integrity)
- [Browser permission and consent lifecycle](docs/learning-guide.md#8-browser-permission-and-consent-lifecycle)

## What each report contains

Records contain original explanations, not just source links: `root_cause` describes the failed security assumption, `impact` qualifies what the evidence establishes, and `defensive_takeaways` captures review and remediation principles. Award evidence, distinct event dates, classifications and verification limits remain machine-readable. Where the source supports it, the explanation includes the researcher’s conceptual reasoning. Specific discovery methods or patch implementations stay unknown when the source does not establish them.

## Use the JSON

Canonical records live in `data/`; files in `exports/` are deterministic, generated snapshots. A record's filename matches its stable `id`.

| Collection | Canonical records | Schema | Portable export |
|---|---|---|---|
| Award-backed reports | [data/reports/](data/reports/) | [Report schema](schema/report.schema.json) | [exports/vulns-co.json](exports/vulns-co.json) |
| Educational resources | [data/resources/](data/resources/) | [Resource schema](schema/resource.schema.json) | [exports/resources.json](exports/resources.json) |
| Conceptual diagrams | [data/diagrams/](data/diagrams/) | [Diagram schema](schema/diagram.schema.json) | Included in [resources.json](exports/resources.json) |

- **Report export:** includes reports, taxonomy, counts, review dates, and inclusion policy. `reports[]` contains the records. The export uses schema version `1.1.0`; the report schema accepts record versions `1.0.0` and `1.1.0`.
- **Resource export:** includes `resources[]`, `diagrams[]`, resource taxonomy, and skillset definitions. Asset paths are relative to this repository.
- **Taxonomies:** [Report categories and defensive skills](data/taxonomy.json) · [Resource types and topics](data/resource-taxonomy.json)
- **Candidate queues:** [Report candidates](data/candidates.json) · [Resource candidates](data/resource-candidates.json). These are research leads and exclusion decisions, not included records.
- **Diagram assets:** [diagrams/](diagrams/) contains SVG, Mermaid (`.mmd`), and Graphviz (`.dot`) companions. Both text formats come from the canonical graph; the SVGs are rendered with Graphviz, not a Mermaid engine.

The `vulns-co.json` filename identifies a future adaptation target. Compatibility with a vulns.co ingestion API has not been established; this repository does not perform ingestion or deployment.

### What a report contains

Read `summary`, `root_cause`, `impact`, and `defensive_takeaways` for the substantive original analysis. Use `sources`, `reward`, `dates`, and `verification` to inspect the evidence, award scope, chronology, and remaining limitations. Category and skillset IDs connect cases to the learning taxonomy.

### Interpret the evidence carefully

- **Award type and scope matter.** Competition entries are labeled separately from bug bounties. A chain or team entry is counted once, not once per CVE or researcher. Program maximums, career earnings, and event totals do not qualify.
- **Awarded is different from paid.** Use `reward.status`, `reward.evidence_level`, the evidence source, and the record's limitations together. Researcher-published vendor correspondence remains researcher-published evidence.
- **Dates have different meanings.** Publication, reporting, award, mitigation, fix, and payment dates are stored separately with precision and provenance. Unknown values remain `null`.
- **Recency follows publication.** `recency.as_of` is a review date, not evidence that a vulnerability is still present. An archive timestamp or later page update does not establish the original publication date.
- **Attribution stays explicit.** An empty researcher array means the reviewed source did not identify a researcher. Editorial CWE mappings are distinguished from source-supplied classifications.

See [DATA_POLICY.md](DATA_POLICY.md) for the complete rules.

## Validate and regenerate

Validation, tests, and export checks use **Python 3.10+**, the standard library, and local files. They require no network access or third-party Python packages.

```sh
python3 scripts/validate.py
python3 scripts/validate_extra.py
python3 -m unittest discover -s tests -v
python3 scripts/render_diagrams.py --check
python3 scripts/export.py --check
python3 scripts/export_resources.py --check
```

After editing canonical records, regenerate the exports:

```sh
python3 scripts/export.py
python3 scripts/export_resources.py
```

Regenerating SVGs also requires an installed **Graphviz `dot`** executable. Run `python3 scripts/render_diagrams.py` and visually inspect the resulting SVGs after graph edits. The renderer's `--check` compares generated source text; it does not rerender SVGs or replace visual review.

The validator implements the schema features used by this project, plus cross-record editorial checks. Extend its tests when adding schema features.

## Report index

Each link opens the canonical record with source URLs, evidence notes, date provenance, and defensive takeaways. Amounts retain their scope and qualifications; they are not a severity ranking.

| Disclosure | Recorded award | Publication | Evidence |
|---|---:|---|---|
| [Chrome graphics input validation weakened an isolation boundary](data/reports/google-chrome-angle-input-validation-2026.json) | USD 250,000 | 2026-09-03 | Vendor confirmed |
| [Codex command approval relied on inconsistent parser semantics](data/reports/openai-codex-command-parser-approval-consistency-2026.json) | USD 40,000 (competition entry) | 2026-09-01 | Competition organizer confirmed |
| [Codex automated Git operations trusted repository hook settings](data/reports/openai-codex-repository-hook-execution-trust-2026.json) | USD 20,000 (competition entry) | 2026-09-01 | Competition organizer confirmed |
| [Codex metadata collection trusted repository execution helpers](data/reports/openai-codex-repository-metadata-helper-trust-2026.json) | USD 10,000 (competition entry) | 2026-09-01 | Competition organizer confirmed |
| [Apple PCC startup archive processing lacked path confinement](data/reports/apple-pcc-boot-archive-path-validation-2026.json) | USD 150,000 | 2026-07-31 | Researcher reproduces vendor offer |
| [Google device grants lost client and permission binding](data/reports/google-device-authorization-client-scope-binding-2026.json) | USD 13,337 | 2026-07-15 | Researcher reported |
| [Redis deserialization cleanup violated object-ownership invariants](data/reports/redis-deserialization-object-ownership-2026.json) | USD 30,000 (competition entry) | 2026-06-02 (year inferred) | Competition organizer confirmed |
| [Meta service-identity exposure amplified by excessive secret access](data/reports/meta-service-identity-secrets-trust-boundary-2026.json) | USD 150,000 | 2026-05-28 | Researcher reproduces vendor message |
| [PostgreSQL cryptographic parsing omitted a buffer-capacity check](data/reports/postgresql-pgcrypto-buffer-capacity-validation-2026.json) | USD 30,000 (competition entry) | 2026-05-04 (year inferred) | Competition organizer confirmed |
| [MariaDB JSON normalization exceeded allocated buffer capacity](data/reports/mariadb-json-normalization-buffer-capacity-2026.json) | USD 30,000 (competition entry) | 2026-05-04 (year inferred) | Competition organizer confirmed |
| [PostgreSQL text-encoding invariant failure caused memory corruption](data/reports/postgresql-multibyte-validation-cve-2026-2006.json) | USD 30,000 (competition entry) | 2026-05-04 | Competition organizer confirmed |
| [Google support API exposed customer and agent data](data/reports/google-support-api-authorization-2026.json) | USD 14,337 | 2026-03-31 | Researcher reproduces vendor message |
| [V8 optimized object handling retained invalid type assumptions](data/reports/google-chrome-v8-type-consistency-2025.json) | USD 50,000 | 2026-03-17 | Vendor confirmed |
| [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](data/reports/google-gemini-enterprise-connected-content-memory-integrity-2026.json) | USD 15,000 | 2026-03-12 | Researcher reported |
| [Angular automation trust and cache isolation weakness](data/reports/angular-ci-cache-trust-2026.json) | USD 31,337 | 2026-03-03 | Researcher reproduces vendor message |
| [PostgreSQL extension estimator trusted an unchecked input type](data/reports/postgresql-extension-input-type-validation-2026.json) | USD 30,000 (competition entry) | 2026-02-12 (vendor advisory) | Competition organizer confirmed |
| [V8 control-flow analysis omitted required initialization checks](data/reports/google-chrome-v8-initialization-checks-2025.json) | USD 50,000 | 2026-01-22 | Vendor confirmed |
| [Gemini-to-Colab rendering boundary exposed Workspace data](data/reports/google-gemini-colab-rendering-boundary-2025.json) | USD 20,000 | 2025-11 | Researcher reproduces vendor message |
| [Kestrel HTTP framing differed across proxy and application boundaries](data/reports/microsoft-kestrel-http-framing-consistency-2025.json) | USD 10,000 | 2025-11-07 | Researcher reported |
| [GitHub package-source trust allowed dependency confusion](data/reports/github-ruby-dependency-confusion-2025.json) | USD 20,000 | 2025-10-28 | Researcher reported |
| [Redis Lua object lifetime failure crossed the scripting boundary](data/reports/redis-lua-object-lifetime-isolation-2025.json) | USD 40,000 (competition entry) | 2025-10-06 | Competition organizer confirmed |
| [GitHub comparison output lacked source-repository authorization](data/reports/github-cross-repository-comparison-authorization-2025.json) | USD 10,000 | 2025-09-23 (historical) | Vendor confirmed |
| [Support integration exposed internal Confluence documentation](data/reports/hackerone-support-confluence-access-boundary-2025.json) | USD 12,500 (one report; two recipients) | 2025-08 (historical) | Vendor confirmed |
| [Cloud Build approval was not bound to immutable code](data/reports/google-cloud-build-approval-toctou-2025.json) | USD 30,000 | 2025-07-21 (historical) | Researcher reported |
| [NVIDIA container initialization inherited untrusted execution context](data/reports/nvidia-container-runtime-environment-trust-2025.json) | USD 30,000 (competition entry) | 2025-07-17 (historical) | Competition organizer confirmed |
| [Google IDX worker messaging crossed browser trust boundaries](data/reports/google-idx-worker-message-trust-2025.json) | USD 22,500 | 2025-07-02 (historical) | Researcher reproduces vendor image |
| [Framework serialization change exposed private HackerOne user attributes](data/reports/hackerone-report-json-serialization-data-exposure-2025.json) | USD 25,000 | 2025-06-24 (historical) | Vendor confirmed |
| [Actifio driver execution exposed excessive shared-service authority](data/reports/google-actifio-driver-service-identity-isolation-2025.json) | USD 10,000 | 2025-05-04 (historical) | Researcher reported |
| [YouTube creator metadata exposed private email addresses](data/reports/youtube-creator-email-authorization-2025.json) | USD 20,000 | 2025-03-13 (historical) | Researcher reported |
| [GitLab recovery delivery lacked verified-address binding](data/reports/gitlab-recovery-address-binding-cve-2023-7028.json) | USD 35,000 | 2025-02-26 (historical) | Vendor confirmed |
| [YouTube and Pixel Recorder exposed cross-product identity links](data/reports/youtube-pixel-recorder-identity-privacy-2025.json) | USD 10,633 | 2025-02-12 (historical) | Researcher reported |
| [GraphQL object authorization exposed private-program metadata](data/reports/hackerone-private-program-graphql-object-authorization-2025.json) | USD 25,000 | 2025-01-21 (historical) | Vendor confirmed |
| [LiteSpeed Cache privileged user simulation relied on weak security tokens](data/reports/litespeed-cache-user-simulation-authentication-2024.json) | USD 14,400 (Zero Day component) | 2024-08-21 (historical) | Platform confirmed |
| [Bard Workspace integration weakened output-data boundaries](data/reports/google-bard-workspace-output-boundary-2024.json) | USD 20,000 | 2024-03-04 (historical) | Researcher reported |
| [Instagram embedding fallback changed the authorization context](data/reports/instagram-embedding-privileged-fallback-2023.json) | USD 14,500 (including bonuses) | 2023-10-12 (historical) | Researcher reported |
| [Meta account verification weakened linked SMS authentication state](data/reports/meta-account-verification-attempt-state-binding-2022.json) | USD 27,200 | 2023-01-20 (historical) | Vendor confirmed |
| [Pixel lock-screen completion lost security-state binding](data/reports/google-pixel-lock-screen-state-binding-2022.json) | USD 70,000 | 2022-11-10 (historical) | Researcher reproduces vendor decision |
| [GitHub Actions trust depended on invalid repository references](data/reports/github-actions-reference-validation-2021.json) | USD 25,000 | 2021-03-17 (historical) | Researcher reported |
| [GitHub fork collaboration applied inconsistent authorization](data/reports/github-fork-collaboration-authorization-2021.json) | USD 20,000 | 2021-03-10 (historical) | Researcher reported |
| [GitHub GraphQL collaboration changes lacked author consent](data/reports/github-fork-collaboration-consent-2021.json) | USD 10,000 | 2021-03-10 (historical) | Researcher reported |
| [Microsoft account recovery lacked consistent attempt-limit enforcement](data/reports/microsoft-account-recovery-rate-limit-consistency-2021.json) | USD 50,000 | 2021-03-02 (historical) | Researcher reported |
| [Sign in with Apple failed to bind identity claims to the authenticated user](data/reports/apple-sign-in-identity-claim-binding-2020.json) | USD 100,000 | 2020-05-30 (historical) | Researcher reported |
| [Facebook error responses exposed unintended application data](data/reports/facebook-error-response-data-isolation-2019.json) | USD 65,000 | 2020-02-07 (historical) | Vendor confirms payment |
| [GitHub OAuth consent failed across request-method semantics](data/reports/github-oauth-method-semantics-2019.json) | USD 25,000 | 2019-11-05 (historical) | Researcher reported |
| [Instagram recovery challenges were insufficiently bound to accounts](data/reports/instagram-recovery-challenge-account-binding-2019.json) | USD 10,000 | 2019-08-25 (historical) | Researcher reported |
| [Instagram mobile account recovery had inconsistent verification limits](data/reports/instagram-mobile-recovery-attempt-limits-2019.json) | USD 30,000 | 2019-07-14 (historical) | Researcher reported |
| [Shopify Exchange screenshot service crossed internal boundaries](data/reports/shopify-exchange-request-isolation-2019.json) | USD 25,000 | 2019-04-03 (historical) | Vendor confirmed |
| [Facebook SDK message authentication relied on insecure randomness](data/reports/facebook-sdk-message-authentication-randomness-2023.json) | USD 66,000 | Original unknown; archive shows 2026-01-17 | Researcher reported |
| [Meta Pixel cross-window handling lost message and token authority](data/reports/meta-pixel-cross-window-authority-binding-2024.json) | USD 32,500 | Original unknown; archive shows 2026-01-16 | Researcher reported |
| [Meta AI media access lacked object-ownership authorization](data/reports/meta-ai-media-object-authorization-2025.json) | USD 10,000 | Unknown; updated 2025-07-16 (historical) | Researcher reproduces vendor message |
| [Safari origin confusion undermined stored media permissions](data/reports/apple-safari-media-permission-origin-confusion-2020.json) | USD 75,000 | Unknown in primary source | Researcher reported |
| [iCloud sharing consent and Safari trust boundaries failed together](data/reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.json) | USD 100,500 | Unknown in primary source | Researcher reported |

## Scope, maintenance, and attribution

The collection uses public primary sources, minimal attributed quotations, and original summaries, under a [public-content-only policy](DATA_POLICY.md#public-content-only-rule). It excludes private user, client, and internal information, secret values, exploit payloads, reproduction steps, operational attack chains, and live-target inventories. Public disclosure does not grant permission to test a system.

The diagrams are conceptual learning models, not claims about a vendor's exact architecture. The scripts validate, render, and export repository data; they do not discover vulnerabilities or test targets.

For updates, follow the [maintenance policy](DATA_POLICY.md#release-procedure): verify primary sources, preserve stable identities and uncertainty, refresh recency, validate, and regenerate the affected outputs. A review that finds no qualifying new source needs no filler record.

Sources remain copyrighted by their respective authors. Attribution and source links are retained with each record.
