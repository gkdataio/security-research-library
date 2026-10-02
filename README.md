# Security research library

Source-backed public security disclosures, organized for defensive learning and future authorized reviews. JSON is the source of truth; the export can later be adapted to vulns.co.

## Initial inventory: October 2, 2026

Six individual reported awards meet the USD 10,000 threshold: five bug bounties and one explicitly labeled competition entry. Five detailed publications fall within October 2, 2025–October 2, 2026. The Cloud Build example is an older reference.

| Disclosure | Recorded award | Publication | Evidence |
|---|---:|---|---|
| [Meta service-identity and secret-access boundaries](data/reports/meta-service-identity-secrets-trust-boundary-2026.json) | USD 150,000 base | May 28, 2026 | Researcher reproduces vendor award message; exact bonus total uncertain |
| [PostgreSQL encoding invariant, CVE-2026-2006](data/reports/postgresql-multibyte-validation-cve-2026-2006.json) | USD 30,000 | May 4, 2026 detailed write-up | Competition organizer confirms this entry's award |
| [Gemini Enterprise persistent-memory integrity](data/reports/google-gemini-enterprise-connected-content-memory-integrity-2026.json) | USD 15,000 | March 12, 2026; earlier researcher post March 9 | Researcher-reported payment |
| [Angular build-cache and automation trust](data/reports/angular-ci-cache-trust-2026.json) | USD 31,337 | March 3, 2026 | Researcher quotes vendor award email |
| [GitHub dependency-source trust](data/reports/github-ruby-dependency-confusion-2025.json) | USD 20,000 | October 28, 2025 permalink date | Researcher-reported award |
| [Cloud Build approval consistency](data/reports/google-cloud-build-approval-toctou-2025.json) | USD 30,000 | July 21, 2025 (older) | Researcher-reported award |

These are evidence-backed award reports, not independently audited bank transfers. Program maximums, researcher career totals, team event totals, and undisclosed amounts are excluded. Reward attribution and date uncertainty stay visible in every record. The PostgreSQL award was for a team entry, not necessarily that amount per person.

## Layout

- `data/reports/`: one canonical JSON record per disclosure; filename equals stable ID
- `data/taxonomy.json`: categories and defensive skillset definitions
- `data/candidates.json`: unqualified leads and exclusion reasons; never included in qualified exports
- `schema/report.schema.json`: strict JSON Schema, version 1.0.0
- `docs/learning-guide.md`: grouped defensive learning objectives
- `DATA_POLICY.md`: evidence, date, update, and safety rules
- `scripts/validate.py`: offline, standard-library validation
- `scripts/export.py`: deterministic export generator
- `exports/vulns-co.json`: self-contained portable JSON with records and taxonomy

The export is not a claim of compatibility with an undocumented vulns.co API. No ingestion, deployment, network scanner, target testing, credential collection, or automated exploitation is included. Public disclosure does not grant testing permission.

## Local checks

Python 3.10 or later, no third-party packages or network access required:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/export.py
python3 scripts/export.py --check
```

Daily research maintenance is configured through the assistant. No GitHub Actions workflow is configured. `validate.py` implements the schema features used here plus cross-record editorial checks. If the JSON Schema is expanded to new keywords, update the validator and its tests as well.

## Updating the collection

Read primary public sources; preserve short evidence excerpts and original summaries rather than copying articles. Add qualifying reports or revise existing stable IDs, with dated source retrieval and explicit uncertainty. Keep candidates separate. Refresh `recency.as_of` and `window_start` across all records for each release; update recency flags to match publication-date precision. Run all checks and regenerate the export before committing. A quiet day with no qualifying case needs no filler record.

Sources remain copyrighted by their respective authors. The collection stores attribution, links, minimal quotations, and original high-level defensive summaries.
