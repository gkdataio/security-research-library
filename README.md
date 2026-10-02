# Security research library

Source-backed public security disclosures, organized for defensive learning and future authorized reviews. JSON is the source of truth; the export can later be adapted to vulns.co.

## Current inventory: October 2, 2026

38 individual report/chain awards meet the USD 10,000 threshold: 37 bug bounties and one explicitly labeled competition entry. Thirteen publication dates fall within October 2, 2025–October 2, 2026; 22 are clearly older, and three historical researcher pages have unknown publication dates. Historical examples are labeled rather than presented as recent discoveries.

The collection contains 38 records after source-backed historical expansion. It now covers account recovery, federated identity, API authorization and serialization, approval consistency, browser permissions, cloud isolation, build pipelines, and AI integration boundaries.

| Disclosure | Recorded award | Publication | Evidence |
|---|---:|---|---|
| [Chrome graphics input validation weakened an isolation boundary](data/reports/google-chrome-angle-input-validation-2026.json) | USD 250,000 | 2026-09-03 | Vendor confirmed |
| [Apple PCC startup archive processing lacked path confinement](data/reports/apple-pcc-boot-archive-path-validation-2026.json) | USD 150,000 | 2026-07-31 | Researcher reproduces vendor offer |
| [Google device grants lost client and permission binding](data/reports/google-device-authorization-client-scope-binding-2026.json) | USD 13,337 | 2026-07-15 | Researcher reported |
| [Meta service-identity exposure amplified by excessive secret access](data/reports/meta-service-identity-secrets-trust-boundary-2026.json) | USD 150,000 | 2026-05-28 | Researcher reproduces vendor message |
| [PostgreSQL text-encoding invariant failure caused memory corruption](data/reports/postgresql-multibyte-validation-cve-2026-2006.json) | USD 30,000 (competition entry) | 2026-05-04 | Competition organizer confirmed |
| [Google support API exposed customer and agent data](data/reports/google-support-api-authorization-2026.json) | USD 14,337 | 2026-03-31 | Researcher reproduces vendor message |
| [V8 optimized object handling retained invalid type assumptions](data/reports/google-chrome-v8-type-consistency-2025.json) | USD 50,000 | 2026-03-17 | Vendor confirmed |
| [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](data/reports/google-gemini-enterprise-connected-content-memory-integrity-2026.json) | USD 15,000 | 2026-03-12 | Researcher reported |
| [Angular automation trust and cache isolation weakness](data/reports/angular-ci-cache-trust-2026.json) | USD 31,337 | 2026-03-03 | Researcher reproduces vendor message |
| [V8 control-flow analysis omitted required initialization checks](data/reports/google-chrome-v8-initialization-checks-2025.json) | USD 50,000 | 2026-01-22 | Vendor confirmed |
| [Gemini-to-Colab rendering boundary exposed Workspace data](data/reports/google-gemini-colab-rendering-boundary-2025.json) | USD 20,000 | 2025-11 | Researcher reproduces vendor message |
| [Kestrel HTTP framing differed across proxy and application boundaries](data/reports/microsoft-kestrel-http-framing-consistency-2025.json) | USD 10,000 | 2025-11-07 | Researcher reported |
| [GitHub package-source trust allowed dependency confusion](data/reports/github-ruby-dependency-confusion-2025.json) | USD 20,000 | 2025-10-28 | Researcher reported |
| [GitHub comparison output lacked source-repository authorization](data/reports/github-cross-repository-comparison-authorization-2025.json) | USD 10,000 | 2025-09-23 (historical) | Vendor confirmed |
| [Support integration exposed internal Confluence documentation](data/reports/hackerone-support-confluence-access-boundary-2025.json) | USD 12,500 (one report; two recipients) | 2025-08 (historical) | Vendor confirmed |
| [Cloud Build approval was not bound to immutable code](data/reports/google-cloud-build-approval-toctou-2025.json) | USD 30,000 | 2025-07-21 (historical) | Researcher reported |
| [Google IDX worker messaging crossed browser trust boundaries](data/reports/google-idx-worker-message-trust-2025.json) | USD 22,500 | 2025-07-02 (historical) | Researcher reproduces vendor image |
| [Framework serialization change exposed private HackerOne user attributes](data/reports/hackerone-report-json-serialization-data-exposure-2025.json) | USD 25,000 | 2025-06-24 (historical) | Vendor confirmed |
| [Actifio driver execution exposed excessive shared-service authority](data/reports/google-actifio-driver-service-identity-isolation-2025.json) | USD 10,000 | 2025-05-04 (historical) | Researcher reported |
| [YouTube creator metadata exposed private email addresses](data/reports/youtube-creator-email-authorization-2025.json) | USD 20,000 | 2025-03-13 (historical) | Researcher reported |
| [GitLab recovery delivery lacked verified-address binding](data/reports/gitlab-recovery-address-binding-cve-2023-7028.json) | USD 35,000 | 2025-02-26 (historical) | Vendor confirmed |
| [YouTube and Pixel Recorder exposed cross-product identity links](data/reports/youtube-pixel-recorder-identity-privacy-2025.json) | USD 10,633 | 2025-02-12 (historical) | Researcher reported |
| [GraphQL object authorization exposed private-program metadata](data/reports/hackerone-private-program-graphql-object-authorization-2025.json) | USD 25,000 | 2025-01-21 (historical) | Vendor confirmed |
| [LiteSpeed Cache privileged user simulation relied on weak security tokens](data/reports/litespeed-cache-user-simulation-authentication-2024.json) | USD 14,400 (Zero Day component) | 2024-08-21 (historical) | Platform confirmed |
| [Bard Workspace integration weakened output-data boundaries](data/reports/google-bard-workspace-output-boundary-2024.json) | USD 20,000 | 2024-03-04 (historical) | Researcher reported |
| [Pixel lock-screen completion lost security-state binding](data/reports/google-pixel-lock-screen-state-binding-2022.json) | USD 70,000 | 2022-11-10 (historical) | Researcher reproduces vendor decision |
| [GitHub Actions trust depended on invalid repository references](data/reports/github-actions-reference-validation-2021.json) | USD 25,000 | 2021-03-17 (historical) | Researcher reported |
| [GitHub fork collaboration applied inconsistent authorization](data/reports/github-fork-collaboration-authorization-2021.json) | USD 20,000 | 2021-03-10 (historical) | Researcher reported |
| [GitHub GraphQL collaboration changes lacked author consent](data/reports/github-fork-collaboration-consent-2021.json) | USD 10,000 | 2021-03-10 (historical) | Researcher reported |
| [Microsoft account recovery lacked consistent attempt-limit enforcement](data/reports/microsoft-account-recovery-rate-limit-consistency-2021.json) | USD 50,000 | 2021-03-02 (historical) | Researcher reported |
| [Sign in with Apple failed to bind identity claims to the authenticated user](data/reports/apple-sign-in-identity-claim-binding-2020.json) | USD 100,000 | 2020-05-30 (historical) | Researcher reported |
| [GitHub OAuth consent failed across request-method semantics](data/reports/github-oauth-method-semantics-2019.json) | USD 25,000 | 2019-11-05 (historical) | Researcher reported |
| [Instagram recovery challenges were insufficiently bound to accounts](data/reports/instagram-recovery-challenge-account-binding-2019.json) | USD 10,000 | 2019-08-25 (historical) | Researcher reported |
| [Instagram mobile account recovery had inconsistent verification limits](data/reports/instagram-mobile-recovery-attempt-limits-2019.json) | USD 30,000 | 2019-07-14 (historical) | Researcher reported |
| [Shopify Exchange screenshot service crossed internal boundaries](data/reports/shopify-exchange-request-isolation-2019.json) | USD 25,000 | 2019-04-03 (historical) | Vendor confirmed |
| [Meta AI media access lacked object-ownership authorization](data/reports/meta-ai-media-object-authorization-2025.json) | USD 10,000 | Unknown; updated 2025-07-16 (historical) | Researcher reproduces vendor message |
| [Safari origin confusion undermined stored media permissions](data/reports/apple-safari-media-permission-origin-confusion-2020.json) | USD 75,000 | Unknown in primary source | Researcher reported |
| [iCloud sharing consent and Safari trust boundaries failed together](data/reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.json) | USD 100,500 | Unknown in primary source | Researcher reported |

The latest increment adds the historical Pixel lock-screen state-binding case (USD 70,000), with an explicitly dated researcher-published vendor award decision. A USENIX Security 2025 paper adds multi-app authorization-context lessons to the separate resource collection. Aggregate rewards remain excluded.

These are evidence-backed award reports, not independently audited bank transfers. Program maximums, researcher career totals, team event totals, and undisclosed amounts are excluded. Reward attribution and date uncertainty stay visible in every record. A chain or team entry is counted once, not once per CVE or person. An empty researcher array means the reviewed primary source did not identify the researcher.

## General resources and visual theory

Twelve official educational resources and six evidence-linked conceptual diagrams are maintained separately from the 38 award reports.

- [Official learning resources](docs/resources.md)
- [Visual guide with rendered SVGs and Mermaid sources](docs/visual-theory.md)
- [Separate resources and diagrams JSON export](exports/resources.json)

The visuals cover approval-version integrity, AI content/authority separation, identity-claim binding, tenant-scoped workload authority, server-request destination controls, and account-recovery challenge integrity. SVGs are rendered offline with Graphviz from the same source graph as the Mermaid files.

## Layout

- `data/reports/`: canonical JSON records; filename equals stable ID
- `data/taxonomy.json`: categories and defensive skillset definitions
- `data/candidates.json`: unqualified leads and exclusion reasons; excluded from qualified exports
- `schema/report.schema.json`: strict JSON Schema, version 1.1.0 (also accepts existing 1.0.0 records)
- `docs/learning-guide.md`: grouped defensive learning objectives
- `DATA_POLICY.md`: evidence, date, update, and safety rules
- `scripts/validate.py`: offline standard-library validation
- `scripts/export.py`: deterministic export generator
- `exports/vulns-co.json`: self-contained portable JSON with records and taxonomy

The export is not a claim of compatibility with an undocumented vulns.co API. No ingestion, deployment, network scanner, target testing, credential collection, or automated exploitation is included. Public disclosure does not grant testing permission.

## Local checks

Python 3.10 or later; no third-party packages or network access required:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/export.py
python3 scripts/export.py --check
python3 scripts/validate_extra.py
python3 scripts/render_diagrams.py --check
python3 scripts/export_resources.py --check
```

Recurring research maintenance is configured through the assistant. No GitHub Actions workflow is configured. `validate.py` implements the schema features used here plus cross-record editorial checks. If the JSON Schema gains new keywords, update the validator and tests.

## Updating the collection

Read primary public sources and retain short evidence excerpts and original summaries. Add qualifying reports or revise existing stable IDs with dated retrieval and explicit uncertainty. Keep candidates separate. Refresh all records' recency dates for each release and respect publication precision. Run checks and regenerate the export before committing. A check with no qualifying new source needs no filler record.

Sources remain copyrighted by their respective authors. This collection stores attribution, links, minimal quotations, and original high-level defensive summaries.
