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

Prior scope and review dates were preserved for these sources.

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
- [Intigriti source](https://app.intigriti.com/programs/upcloud/upcloud): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/rpip/allekabels): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/leapsome/leapsome): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/farfetch/farfetchbugbounty): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/intigriti/captureourflag): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/doccle/doccle): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/liveperson/livepersonconversationalcloud): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/wl/wirelesslogic): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/telenet/telenetgroup): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/rampf/rampfbugbounty): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/uitgeverijdeviant/uitgeverijdeviant): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/aylo/mydirtyhobby-bbp): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/kahoot/kahoot): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/aylo/trafficjunky-bbp): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/aylo/probiller-bbp): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/colruyt/colruytgroupidcheck): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/belfius/belfius): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/aylo/nutaku-bbp): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/ideals/ideals): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/aylo/brazzers-bbp): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/sdworx/myworkandme): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/intertoys/intertoys): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/combell/webnode): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/coveo/coveopublicbugbounty): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/fortnox/fortnox): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/daytona/daytonabugbounty): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/ubisoft/ubisoftgamesecbbp): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/onetwobuild/12build): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/aylo/pornhub-bbp): HTTP Error 302: Found
- [Intigriti source](https://app.intigriti.com/programs/colruyt/newpharma): HTTP Error 302: Found
- [Intigriti source](None): HTTP Error 302: Found
- [Direct policy source](https://www.fastmail.com/bug-bounty/): HTTP 403 Forbidden on official policy page. No access workaround or retry attempted. Prior scope and dates preserved.
