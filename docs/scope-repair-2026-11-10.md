# Scope source repair review: November 10, 2026

This repair separates fetched historical rows from visible public asset identifiers and current source access. It does not test assets, recover concealed identifiers, sign in, accept terms, or remove access exclusions.

## Corrected collector behavior

The HTTP reader now requires status 200 and rejects any `Content-Range` header before reading the body. A syntactically valid partial response cannot update a scope record. Offline fake-response tests verify that 206 responses, other non-200 statuses and range-marked 200 responses preserve every prior capture and policy byte.

Bugcrowd responses containing only block-redacted asset names, with no visible location, previously counted as refreshed scope tables. The collector now records `bugcrowd_scope_redacted`, retains the prior record and capture date, and does not count that response as a successful scope refresh. A mixed table or a masked display name with a visible location remains distinct evidence; no rows are guessed or silently dropped.

A fresh read of [Cash App's official public page](https://bugcrowd.com/engagements/cashapp) and its [current linked brief](https://bugcrowd.com/engagements/cashapp/changelog/73ca7ddf-de6c-437a-8e3f-43a77efa9e3a.json) verified four redacted-only rows. The repaired parser rejected that response with a response digest and counts, without publishing raw response content or changing the canonical capture. Its SHA-256 digest, `cda150127a164a45b78b3fee425e63c58f40fc227db89100bfb2dacdbf872e92`, matches the same brief in the earlier daily audit.

The existing November 10 daily audit remains an unchanged historical run: **807 refreshed, 48 failed, 5 deferred, 236 unsupported**. Of those 807 refreshed results, 29 correspond to currently stored redacted-only tables. The repaired code will classify an unchanged response differently on the next run. This is not a new full daily refresh and does not claim recovered scope coverage.

## Corrected coverage presentation

The reconciled catalog retains **808 historical captured tables** and **42 original capture gaps**. Of those tables, **30 contain only redacted identifiers (293 rows)**; **778 contain at least one non-redacted row**. A visible row is not full scope verification or permission to test. Historical row counts and dates remain unchanged.

- Both bounty and VDP detail pages now flag redacted-only tables, including the Cisco VDP page.
- Detail pages show the latest failed or deferred refresh beside the retained capture status and date. A newer capture or successful refresh supersedes an older failure warning.
- [Scope audit JSON](../exports/program-scope-audit.json) version 1.1.0 adds redacted-only counts and the affected program list. Existing historical count fields keep their meanings.
- [Source review notes](../data/scope-source-reviews.json) are separate dated observations, not replacement scope tables or revised bounty classifications.

## Official source transitions

### CFPB, TVA and U.S. DOT

The official migration pages for [CFPB](https://bugcrowd.com/engagements/cfpb-vdp/migrated), [TVA](https://bugcrowd.com/engagements/tva-vdp/migrated), and [U.S. DOT](https://bugcrowd.com/engagements/usdot-vdp/migrated) name Bugcrowd Gov (US). Each linked transition page states that a separate Gov login is required. Review stopped there; no login or replacement scope request was made. These are confirmed migration/access changes, not evidence of closed programs or newly verified scopes.

The unattended collector now distinguishes the exact same-program `/migrated` redirect category without following it. Other redirects remain blocked as before.

### Django

Django's [October 8 announcement](https://www.djangoproject.com/weblog/2026/oct/08/django-security-reporting-update/) says new security reports no longer go through HackerOne. Existing reports remain open, and new reports go to security@djangoproject.com under its [official security policy](https://docs.djangoproject.com/en/dev/internals/security/). The catalog now displays this dated transition. Historical HackerOne directory and bounty flags are preserved; the announcement alone does not establish present reward eligibility or a new asset table.

## Unresolved source limits

- The latest daily audit still records 34 redirects: three now-reviewed Bugcrowd migrations and 31 Intigriti redirects. The latter are observed preview/terms routes, not newly verified scopes.
- Five 404s and nine empty tables (six Bugcrowd, three HackerOne) do not prove closure or an empty authorized scope.
- Five excluded sources remain excluded. No override, alternate collector or access workaround was added.
- The 236 unsupported entries include 229 historical HackerOne non-bounty classifications that scope CSV alone cannot reverify.
- [Kong's official Trust Center](https://trust.konghq.com/) still links its HackerOne page; that page required sign-in/security verification during review. No replacement public scope evidence was recovered.
- Cisco's other named programs are not identity-equivalent substitutes for its failed responsible-disclosure source. The retained Cisco rows are explicitly redacted.

The coverage warning and failing completion check remain enabled. A correct collector must not report complete coverage merely because inaccessible, migrated or redacted sources have been labeled more precisely.
