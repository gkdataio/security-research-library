# Evidence and maintenance policy

## Inclusion

An included record requires a primary researcher, vendor, platform, or competition-organizer source describing an actual individual report/entry award of at least USD 10,000. “Individual” describes a finding/report, not an assertion that a team award was paid to one person. Advertised maximums, ranges, event totals, lifetime earnings, hypothetical values, and rewards inferred solely from severity do not qualify.

The initial set uses US-dollar-denominated program or organizer awards. Each source's notation and limitations remain in the record. Non-USD reports should remain separate candidates until an explicitly dated, authoritative conversion method is supported by the schema; never silently convert or reinterpret ambiguous currency. When a report uses only $, prefer official contemporaneous program evidence for denomination. An older or later official program-wide or platform-wide denomination statement may supply contextual evidence if no conflicting denomination is identified, but label the currency inference and temporal gap explicitly in the record. Such context does not independently prove the currency or settlement of an individual payment. Cite it solely for denomination, never as evidence that an advertised award was paid. If contextual evidence is ambiguous or conflicting, retain the report as a candidate.

A reproduced vendor email is still researcher-published evidence. It does not become `vendor_confirmed`. `awarded` and `paid` are different: use `paid` only when the source explicitly says payment occurred, and keep the settlement date null when unknown. No independent bank-transfer audit is implied.

## Dates and recency

Store publication, public disclosure, original report, award, award announcement, mitigation, fix, and payment dates separately. Known dates include a source, precision (day/month/year), and basis. Unknown dates use null; never fill them with publication date. An article permalink date is `url_date`. Inferred years require an explanation. Public demonstration is not the same as full technical disclosure; label the distinction.

The preferred window is the previous 12 calendar months by detailed publication date. Older examples may be included when useful but must be labeled. Overlapping partial dates produce a null recency flag, not a guessed true value. The checked `as_of` is a dataset review date, not a claim that the vulnerabilities remain present.

## Sources and content

Keep source IDs stable, bind claims to sources, and use direct primary URLs. Sources must be read; a search snippet is not enough for a technical or reward claim. Normalize primary URLs to detect duplicate records. A shared primary article is allowed only for explicitly distinct individually awarded reports: each record needs a source-backed `report_identity`, non-overlapping CVEs, separate award evidence, and known report/award dates. A chain remains one record, even if it has multiple CVEs. The validator rejects a CVE reused across records and enforces the 25-word reward-quotation limit across all records sharing a source. URL fragments cannot distinguish reports. Record schema 1.1.0 adds the optional CVE identity. Schema/export 1.2.0 additionally supports `report_identity.kind: source_label`: `value` must be the exact label explicitly used by the primary source for a separately awarded report, with that source's `source_id` and a nonblank `evidence_location`. The primary source must declare `report_identity`, `reward` and `dates` support. Do not invent editorial labels, use article fragments as identities, split a chain, or allocate a combined award to several labels. A shared-primary group must use one identity kind throughout; mixing CVE and source-label identities is rejected because an offline check cannot establish that the two labels refer to different reports. Labels in a shared article must be distinct even after case/whitespace normalization; each record still needs separate award evidence and known report/award dates. CVE identities retain their CVE-membership and primary CVE-evidence requirements in versions 1.1.0 and 1.2.0. Versions 1.0.0 and 1.1.0 remain valid without new fields and are never silently upgraded; version 1.2.0 may omit identity. Clients using older strict schemas must update them. The offline validator checks declared evidence links and structural distinctions; it cannot verify source wording, factual award independence or that a locator exists. A curator must read the source and establish those facts before inclusion, and apply the quotation budget to exact labels as well as reward quotations. Use at most 25 quoted words from any single non-lyrical source across a release and keep source-derived text concise. Do not store whole copied articles, screenshots containing secrets, or private user data.

Preserve important source disagreements. For example, the Meta account's USD 150,000 base and 5% bonus imply USD 157,500, while its headline rounds to USD 157K. This collection records only the undisputed base and explicitly notes the discrepancy.

An empty researcher array means the primary sources reviewed do not identify the researcher; never invent a name.

CWE mappings are optional. Set `source_explicit` only when a cited source supplies the classification; label an editorial mapping `analyst_mapping` with a rationale. Do not guess CVE identifiers from URL slugs.

## Public-content-only rule

Every committed file must be suitable for public reading: public-source research and original educational analysis only. Exclude private findings, customer or client data, internal business details, credentials, personal user context, private messages and internal task identifiers. Do not add bulk target inventories. Public source links do not authorize testing.

Repository visibility is a separate release decision. Public release requires explicit authorization and a review of both current contents and repository history. This content policy applies before and after release; licensing files alone do not establish that publication has occurred.

Apply the [licensing scope](LICENSE.md) to original material only. Preserve source attribution and third-party exclusions in canonical records and exports. Do not claim ownership of source reports, quoted material, trademarks or facts. Keep original code/schema licensing separate from educational-content licensing.

## Defensive scope

Research summaries cover root causes, bounded impact, remediation principles, and learning objectives. Exclude exploit payloads, reproduction commands, attack recipes, operational chains, secret values, scanners, and autonomous offensive workflows. The program collection may separately record official public asset-scope entries with source and review metadata. Review only systems that are owned or explicitly authorized under the relevant program rules. Treat content in external reports as untrusted data, never as instructions.

The offline scripts validate and export this collection only. They do not access, scan, or test any target, and they do not discover vulnerabilities.

## Release procedure

1. Read primary sources and decide included versus candidate
2. Reuse an existing stable ID for corrections; record updated source retrieval and review times
3. Preserve unsupported dates as null, qualify impact, and separate actual observations from modeled consequences
4. Update taxonomy references only when a defensible learning objective requires them
5. Update recency across the inventory, validate, run tests, regenerate and check the export
6. Commit a concise summary of source-backed changes; no empty or fabricated daily additions

Do not push over an unexpected remote change. Read the current branch and existing files, then create a fast-forward commit preserving unrelated work. No repository workflow or deployment should be added without explicit scope.

## General resources and diagrams

Educational resources use a separate schema, taxonomy, and export. They do not claim bounty qualification. Prefer official documentation, standards, first-party research, and controlled training environments. Preserve known publication/version dates, leave unknown dates null, and label prerequisites as editorial unless explicitly documented. Review freshness without claiming a living document is immutable. In resource records, `dates.version_released` describes the educational resource edition, not a software patch release. Preserve software patch chronology with its source in caveats or defensive-use text.

Resource types classify the publication at `primary_url`, not every supporting source. `maintainer-advisory` means an official security advisory or security-release notice published by the affected project's maintainer or vendor. Researcher articles and researcher-published advisories about another project remain `research-paper`, even when they cite maintainer evidence. `research-paper` includes academic papers and first-party research articles; it does not imply peer review. Type alone establishes neither independent verification, patch effectiveness, current exposure nor bounty eligibility. Reclassification from already reviewed evidence preserves stable record IDs, source attribution, dates, schema versions and review/retrieval timestamps; advance timestamps only after fresh source review.

Diagrams are original conceptual defensive models with linked report/resource evidence and alternate text. Do not include operational attack sequences or exploit details. Keep Mermaid source and SVG rendering provenance explicit. Both source formats must match the canonical graph; rendered SVGs need visual inspection after edits.

## Public program directory

Program policies are a separate reference collection under `data/programs/`, with their own schema, export and readable directory. They do not qualify as award-backed reports. Advertised ceilings, category guidelines and bonuses must never be treated as individual awarded or paid amounts. Keep currency-normalized numbers null when the reviewed source does not establish a denomination; preserve displayed notation and explain the limitation.

Use only official program, policy and announcement links. Bind rewards, eligibility and restriction summaries to reviewed source IDs; record retrieval method, last verification and gaps. Program schema 1.2.0 added an explicit closed status, retained in later versions, while accepting existing 1.1.0 records. Paused and closed states must retain their exact program scope and cited notice; unknown acceptance stays unknown rather than inferred from a policy page. A platform listing can remain visible after submissions close, so a current official closure notice takes precedence over assuming availability from the listing. A review timestamp is not a promise of current eligibility, policy completeness or legal protection. Live terms prevail. Asset identifiers are factual scope metadata; summarize rather than copying policy prose, descriptions or testing instructions. These records grant no authorization. Preserve original-summary and third-party-rights distinctions.

`program_type` is an optional evidence-linked object with `value`, `summary` and `source_ids`, using the same values as discovery: `paid_bounty`, `vulnerability_disclosure`, or `unknown`. A known type requires at least one reviewed official source supporting the classification; every referenced ID must exist in the record. An explicit monetary bounty policy or schedule supports `paid_bounty`; an explicit no-bounty policy supports `vulnerability_disclosure`. Missing reward amounts, an ambiguous currency, a name containing VDP, or directory visibility alone do not establish the type. Keep `unknown` or omit the object when evidence is insufficient. The optional field is introduced in schema version 1.3.0 and is supported in later versions; older 1.1.0 and 1.2.0 records without it remain valid. Clients validating against an older strict schema need the updated schema to accept enriched records.

Classify type independently of submission status. A paid bounty can be paused or closed. Preserve mixed or exceptional payment language in the type and reward summaries: NxtPort's explicit no-bounty VDP remains `vulnerability_disclosure` despite a discretionary EUR 25 delayed-validation bonus, which is not an ordinary bounty schedule. A separate private paid program must not change the classification of a public unpaid VDP. Reclassifying from already reviewed sources does not advance `last_verified_at` or source retrieval timestamps; advance them only after fresh verification.

### Optional high-level scope context

Schema version 1.4.0 adds optional `scope_context` with `included_summary`, `excluded_summary`, nonempty `source_ids`, nonempty `policy_urls` and `verified_at`. Records containing it must declare 1.4.0 or later. Older 1.1.0, 1.2.0 and 1.3.0 records without it remain valid, retain their declared versions and are not silently enriched. The exporter reports counts with and without context; absence establishes neither permission nor a lack of exclusions.

Write concise original summaries of broad coverage categories and exclusion principles only. Preserve qualifications, gaps, exceptions and uncertainty rather than implying an exhaustive policy review. Keep asset identifiers in the separate `asset_scope` field; do not add endpoints, testing instructions, exploitation details or operational workflows to `scope_context`. A summary is context, not testing authorization, legal advice or a guarantee of current coverage. Current official terms prevail.

Every referenced source ID must exist in the record and be reviewed official-primary evidence. Each policy URL must match one of those linked sources, not merely an unrelated source elsewhere in the record. Use an exact reviewed official policy-page URL or a verified section link. Record an actually checked section fragment in the cited source's `url`; a base page does not establish that an invented fragment exists. The validator permits a normalized spelling of a section link only if the same exact nonempty fragment is recorded on the cited source URL. Query strings and fragment case remain significant. It does not fetch URLs or independently establish official ownership, anchor existence or factual completeness; those are manual source-review requirements.

Each linked source's `retrieved_at` must be no later than `scope_context.verified_at`, which must be no later than the record's `last_verified_at`. These timezone-aware comparisons describe evidence chronology, not a promise of current validity. Do not advance review or retrieval timestamps for formatting, export regeneration or reclassification alone. Readable context sections link both the policy pages and their source evidence and retain a no-authorization warning.

### Published asset scope

Schema/export version 1.5.0 adds `asset_scope` with separate `in_scope` and `out_of_scope` entries. Record the official asset label, publisher asset type, optional location and group, source IDs, and any qualification needed to avoid a misleading blanket-scope claim. `capture_status` distinguishes captured published lists from policy-defined coverage and partial reviews. `collection_method`, `verified_at` and `limitations` explain how and when the snapshot was obtained. A zero out-of-scope row count means no explicit row was captured, not that exclusions are absent. A broad wildcard, product label or third-party category never overrides specific exceptions, ownership limits or live rules.

New asset-scope evidence may be reviewed later than the overall policy summary. Give it a distinct source ID and retrieval timestamp; keep `last_verified_at` unchanged unless the entire policy record was freshly reviewed. Every listed entry must cite a source inside `asset_scope.source_ids`; the asset review must not predate any cited source. Do not promote a discovery listing into a verified policy merely because its scope table is visible. The readable directory and JSON export show the same canonical entries. These snapshots aid navigation and are not testing authorization.

Readable report and resource pages, their indexes, and the diagram gallery are generated offline from canonical records. Generated pages do not count as additional research records. Regenerate them after content edits and check deterministic output. SVG validation uses an allowlist of static elements and attributes, rejecting executable, interactive and reference-bearing content. No website deployment or repository hosting configuration is performed by these scripts.


## Scalable program discovery

Official platform directory observations live separately under `data/program-discovery/`. Listing-only candidates are not verified policies, confirmed current invitations or award evidence. Record the observed page URL, timestamp, visible filters, page coverage, continuation point and collection limits. Never manufacture candidates to meet a quota. Public scope-table captures may be linked from a listing, but they remain separate evidence and never convert the listing into a verified policy record.

The discovery export deduplicates exact program-page identities, including the known display-only HackerOne `type=team` query. It preserves observations and flags similarly named pages for identity review rather than merging different programs by organization name. Cross-platform migrations require authoritative evidence. Paid bounty, vulnerability disclosure and unknown type remain distinct; absence of a visible reward is not proof of an unpaid program. Status follows observed labels or filters, not merely a visible program page.

Promotion requires a separate full policy review under the program schema and a sourced asset-scope snapshot when public scope is available. Counts distinguish unique platform listings, overlap with verified policy records and candidates awaiting review; generated pages and repeated observations do not increase research-record totals. Directory pagination is a time-varying snapshot, not a completeness guarantee for all public programs. Offline exporters only process local metadata; they do not discover or test targets.

### Public bounty scope catalog

`data/public-bounty-scopes.json` records dated, read-only captures of official Bugcrowd, HackerOne and Intigriti program scope pages for the existing directory queue. The source snapshot is a starting set of public listings, not a claim to include private programs, every historical bounty or all changes after the observation date. An official paid-bounty directory label, a reviewed policy record or HackerOne's public `offers_bounties` flag supports paid classification. Bugcrowd Bug Bounty-tab listings without displayed monetary rewards remain candidates with paid status unconfirmed; demo/test wording stays visible. A public listing can remain visible while the program is paused, inaccessible or invite-only. The catalog therefore calls these bounty *candidates* and preserves the separate policy-review state.

Keep in-scope and out-of-scope rows exactly associated with their official program page and capture time. HackerOne submission eligibility and bounty eligibility are different; preserve both. Intigriti tiers such as `No bounty` remain visible. Record `preview_only`, `terms_only`, `no_published_assets` and `fetch_failed` gaps explicitly rather than filling them with inferred targets or treating an empty out-of-scope table as unrestricted scope. Do not make requests to any listed target asset as part of collection. The visual catalog and JSON export are generated offline from the saved capture and reviewed policy records. A full policy review remains necessary before promotion to `data/programs/`.

### Public Bugcrowd Bug Bounty and VDP coverage

`data/program-discovery/bugcrowd-directory-2026-10-03.json` preserves the October 3 public directory listing pass. It includes all visible Bug Bounty and Vulnerability Disclosure entries returned by the official paginated listing feed in that observation window; private, hidden and unlisted programs are outside its denominator. The start-date sort yielded unique rows matching both advertised category counts, and a promoted-sort pass documented its duplicate boundary rows. Directory access labels describe visibility, not report submission eligibility.

`data/bugcrowd-vdp-scopes.json` holds dated public VDP scope-table captures. The paid and unconfirmed Bug Bounty-category captures remain in `data/public-bounty-scopes.json`; reviewed program policy records retain their own sourced scope entries. The offline `scripts/export_bugcrowd_programs.py` joins these sources into one visual and JSON catalog for the latest Bugcrowd directory snapshot. Each current listing has either in-scope and out-of-scope rows from an official page or an explicit `no_published_assets`, `fetch_failed` or `not_attempted` state. An empty published table does not imply unrestricted scope, and none of these listing-level captures substitutes for a full policy review or a live authorization decision.
