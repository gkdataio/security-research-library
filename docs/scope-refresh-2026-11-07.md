# Scope refresh: November 7, 2026

This pass revisited existing public program scope sources. It did not test listed assets or infer scope from failed requests. Directory discovery and full policy review remain separate.

## Coverage

| Source | Program sources attempted | Sources freshly read | Preserved gaps |
|---|---:|---:|---:|
| Bugcrowd | 516 | 505 | 11 |
| HackerOne | 224 | 223 | 1 |
| Intigriti | 121 | 90 | 31 |
| Direct policy | 7 | 6 | 1 |

Updated **823 canonical scope records**, with asset-row changes in **105 records**. A program represented by both a catalog capture and a policy record can count twice in these record totals. Scope-source access counts above count program sources, not individual HTTP requests.

See the [machine-readable review](../exports/scope-refresh-2026-11-07.json) for every changed record and preserved gap, and the [retained change feed](program-changes.md) for before/after details. Version and provenance changes in the feed are not necessarily asset additions or removals.

## Limits

- Directory snapshot remains October 3, 2026; no discovery completeness claim is made by this refresh.
- Existing historical non-bounty HackerOne classification-only records with no captured scope are outside this catalog-scope pass.
- Scope rows and source observations do not establish current submission eligibility, bounty classification or permission to test.
- Failed, redirected or inaccessible sources retain their last verified scopes and timestamps.
- Current official policy controls. Platform scope tables do not capture every qualification or policy exclusion.
- The retained change feed also includes provenance/version changes; these are distinct from asset-row changes.

## Unavailable sources

Prior scope and review dates were preserved for these sources. The Intigriti explanations distinguish the November 7 redirect failures from the October 3 detailed gate reviews: 18 preview/login gates, 12 terms/login gates, and Adobe's redirect with no recorded destination. A historical gate classification is not a fresh policy or scope verification.

- [Bugcrowd source](https://eu.bugcrowd.net/engagements/eu-automation-test-regression-engagement1-b): HTTPError: HTTP Error 404: Not Found
- [Bugcrowd source](https://eu.bugcrowd.net/engagements/Demo-EU-admin-Test): HTTPError: HTTP Error 403: Forbidden
- [Bugcrowd source](https://eu.bugcrowd.net/engagements/eu-public-1): HTTPError: HTTP Error 404: Not Found
- [Bugcrowd source](https://eu.bugcrowd.net/engagements/demo-eu-admin-pentest-max-4): HTTPError: HTTP Error 403: Forbidden
- [Bugcrowd source](https://bugcrowd.com/engagements/fmshrc-vdp): ValueError: No current public brief version on page
- [Bugcrowd source](https://gov.bugcrowd.net/engagements/fmc-vdp): HTTPError: HTTP Error 404: Not Found
- [Bugcrowd source](https://bugcrowd.com/engagements/ciscosecurity): HTTPError: HTTP Error 404: Not Found
- [Bugcrowd source](https://bugcrowd.com/engagements/abmc-vdp): ValueError: No current public brief version on page
- [Bugcrowd source](https://eu.bugcrowd.net/engagements/eu-vdp-1): HTTPError: HTTP Error 404: Not Found
- [Bugcrowd source](https://bugcrowd.com/engagements/oshrc-vdp): ValueError: No current public brief version on page
- [Bugcrowd source](https://gov.bugcrowd.net/engagements/sec-vdp): HTTPError: HTTP Error 404: Not Found
- [HackerOne source](https://hackerone.com/kong?type=team): Official CSV returned HTTP 404. Normal public policy_scopes UI redirected to HackerOne sign-in; no sign-in attempted, prior scope and dates retained.
- [Intigriti source](https://app.intigriti.com/programs/upcloud/upcloud): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/rpip/allekabels): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/leapsome/leapsome): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/farfetch/farfetchbugbounty): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/intigriti/captureourflag): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/doccle/doccle): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/liveperson/livepersonconversationalcloud): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/wl/wirelesslogic): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/telenet/telenetgroup): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/rampf/rampfbugbounty): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/uitgeverijdeviant/uitgeverijdeviant): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/aylo/mydirtyhobby-bbp): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/kahoot/kahoot): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/aylo/trafficjunky-bbp): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/aylo/probiller-bbp): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/colruyt/colruytgroupidcheck): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/belfius/belfius): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/aylo/nutaku-bbp): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/ideals/ideals): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/aylo/brazzers-bbp): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/sdworx/myworkandme): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/intertoys/intertoys): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/combell/webnode): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/coveo/coveopublicbugbounty): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/fortnox/fortnox): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/daytona/daytonabugbounty): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/ubisoft/ubisoftgamesecbbp): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/onetwobuild/12build): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a preview/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/aylo/pornhub-bbp): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/colruyt/newpharma): HTTP 302 on 2026-11-07. The last detailed access review (2026-10-03) recorded a terms/login gate; no public asset rows were visible then. This refresh did not traverse the redirect or verify a scope table. Prior scope and verification date retained.
- [Intigriti source](https://app.intigriti.com/programs/adobe/adobepublic): HTTP 302 on 2026-11-07. Adobe Public Bug Bounty detail redirected; the destination was not recorded, so no gate classification is inferred. Prior scope and verification date retained.
- [Direct policy source](https://www.fastmail.com/bug-bounty/): HTTP 403 Forbidden on official policy page. No access workaround or retry attempted. Prior scope and dates preserved.

## Supplemental policy evidence reviewed November 7, 2026

These official policy sources provide context for existing gaps. They do not recover the missing platform tables, establish a recent scope change, or change the counts, scope rows, and verification timestamps above. Some policies have older publication dates. Current official terms still control.

- **ABMC:** The [agency policy](https://www.abmc.gov/about-us/reports-policy/vulnerability-disclosure-policy/) names www.abmc.gov, weremember.abmc.gov, and wwiiregistry.abmc.gov. It also excludes unlisted connected services and vendor systems. Keep those qualifications together; do not infer a wildcard or a newly expanded platform scope.
- **FMSHRC:** The [January 2024 policy PDF](https://fmshrc.gov/sites/default/files/Vulnerability%2520Disclosure%2520Policy_508.pdf), linked from the [agency policy page](https://fmshrc.gov/content/vulnerability-disclosure-policy), names fmshrc.gov and excludes unlisted connected and vendor services. Its submission link names fcc-vdp, a different agency; that link does not establish a replacement for the FMSHRC program.
- **FMC:** The [February 2021 policy PDF](https://www.fmc.gov/wp-content/uploads/2021/03/VulnerabilityDisclosurePolicy.pdf), still linked from the [agency's Open Government page](https://www.fmc.gov/open-government-at-the-fmc/), names *.fmc.gov with exclusions for unlisted connected and vendor services. This is separate policy evidence, not a recovered platform row; the retained platform row is redacted.
- **SEC:** The [agency policy](https://www.sec.gov/about/privacy-information/vulnerability-disclosure-policy) defines scope by SEC ownership and internet accessibility, with cloud-provider restrictions and exclusions for connected commercial, other-government, and vendor systems. Do not turn that prose into guessed asset hosts.
- **OSHRC:** The [agency policy](https://www.oshrc.gov/vulnerability-disclosure-policy/) states that no publicly accessible sites are in scope; its change history dates the scope removal to March 21, 2025. Both retained platform rows already have scope=out. One row's display group says “In Scope”; the structured scope value, not that label, controls its classification. No scope row was changed in this review.
