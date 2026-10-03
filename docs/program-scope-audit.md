# Program scope coverage audit

[Library home](../README.md) · [Bugcrowd catalog](bugcrowd-programs.md) · [Bounty catalog](public-bounties.md) · [Discovery queue](program-discovery.md)

Counts cover dated public directory snapshots and published scope rows. A visible listing or captured table is not a complete policy review or authorization to test. Empty exclusions do not mean unrestricted scope.

## Reconciled counts

| Measure | Count |
| --- | ---: |
| Separately reviewed policy records | 40 |
| Reviewed policy in-scope / out-of-scope rows | 470 / 194 |
| Discovery program-page listings | 1156 |
| Discovery listings linked to reviewed policies | 33 |
| Discovery listings with captured public scope tables | 785 |
| Raw bounty / VDP capture records | 833 / 223 |
| Bugcrowd public listings | 516 |
| Bugcrowd published scope captured | 507 |
| Bugcrowd scope gaps | 9 |
| Bugcrowd in-scope / out-of-scope rows | 5621 / 1394 |
| Cross-platform bounty candidates | 627 |
| Bounty published scope captured | 591 |
| Bounty scope gaps | 36 |
| Bounty in-scope / out-of-scope rows | 9098 / 3112 |
| Overlapping Bugcrowd bounty listings | 293 |
| Distinct programs across both catalogs | 850 |
| Distinct programs with captured scope rows | 808 |
| Distinct unresolved scope gaps | 42 |
| Distinct in-scope rows | 11758 |
| Distinct out-of-scope rows | 3414 |
| Repeated source rows collapsed | 77 |

The 293 overlapping Bugcrowd bounty pages are counted once in the distinct totals. The 40 separately reviewed policies include 23 bounty-catalog records; they are not added again. The October 3 Bugcrowd snapshot is paired with the earlier HackerOne and Intigriti directory observations.

## Unresolved gaps

Official pages showed 18 preview login gates, 12 terms login gates, 7 empty public tables, 3 JavaScript shells without an independently visible asset list, and 2 HTTP 403 responses.

| Program | Platform | Status | Official policy review |
| --- | --- | --- | --- |
| [Arlo Kudos Rewards](<bugcrowd-programs/vdp/bugcrowd-1ee3d56124cf736f.md>) | Bugcrowd | no published assets | [empty published table](<https://bugcrowd.com/engagements/arlokudos>) |
| [Demo-EU-admin-PenTest-Max-4](<public-bounties/bugcrowd/bugcrowd-eef3c6de790e5363.md>) | Bugcrowd | fetch failed | [http 403](<https://eu.bugcrowd.net/engagements/demo-eu-admin-pentest-max-4>) |
| [Demo-EU-admin-Test](<public-bounties/bugcrowd/bugcrowd-128c3420fe4d74c6.md>) | Bugcrowd | fetch failed | [http 403](<https://eu.bugcrowd.net/engagements/Demo-EU-admin-Test>) |
| [Dyson Demo VDP Engagement](<bugcrowd-programs/vdp/bugcrowd-2ba4f933d6de7ca7.md>) | Bugcrowd | no published assets | [empty published table](<https://bugcrowd.com/engagements/dyson-demo-vdp-engagement>) |
| [EU-Automation-Test-Regression-Engagement1-B](<public-bounties/bugcrowd/bugcrowd-0deaf756ac57137f.md>) | Bugcrowd | no published assets | [empty published table](<https://eu.bugcrowd.net/engagements/eu-automation-test-regression-engagement1-b>) |
| [Office of Personnel Management - Vulnerability Disclosure Program](<bugcrowd-programs/vdp/bugcrowd-ff6465c6cc35cf62.md>) | Bugcrowd | no published assets | [empty published table](<https://bugcrowd.com/engagements/opm-vdp>) |
| [Progress Software – Progress Data Cloud](<bugcrowd-programs/vdp/bugcrowd-ee194a4857e12397.md>) | Bugcrowd | no published assets | [empty published table](<https://bugcrowd.com/engagements/progressdatacloud-vdp-pro>) |
| [Stickman 2](<bugcrowd-programs/vdp/bugcrowd-3c7ab64d8b64c31f.md>) | Bugcrowd | no published assets | [empty published table](<https://bugcrowd.com/engagements/stickman2>) |
| [test engagement](<bugcrowd-programs/vdp/bugcrowd-6df51f6ee18c7b08.md>) | Bugcrowd | no published assets | [empty published table](<https://bugcrowd.com/engagements/testing-vdp-pro>) |
| [CoinMate\.io](<public-bounties/hackerone/hackerone-506fc9236b351984.md>) | HackerOne | no published assets | [javascript required](<https://hackerone.com/coinmate/policy_scopes>) |
| [Django](<public-bounties/hackerone/hackerone-be10e8ab9c7750da.md>) | HackerOne | no published assets | [javascript required](<https://hackerone.com/django/policy_scopes>) |
| [Phabricator](<public-bounties/hackerone/hackerone-0402fac19fe5f16c.md>) | HackerOne | no published assets | [javascript required](<https://hackerone.com/phabricator/policy_scopes>) |
| [12Build Bug Bounty Program](<public-bounties/intigriti/intigriti-f80b2fe8a24e9060.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/onetwobuild/12build/preview/detail>) |
| [Allekabels](<public-bounties/intigriti/intigriti-0c5bec9f65e46eb9.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/rpip/allekabels/preview/detail>) |
| [Belfius](<public-bounties/intigriti/intigriti-aa34891c6a4d965a.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/belfius/belfius/tac/detail>) |
| [Brazzers Bug Bounty Program](<public-bounties/intigriti/intigriti-b89f92cb496b8747.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/aylo/brazzers-bbp/tac/detail>) |
| [Capture Our Flag](<public-bounties/intigriti/intigriti-2310f52431fb92bd.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/intigriti/captureourflag/preview/detail>) |
| [Colruyt Group](<public-bounties/intigriti/intigriti-a36852fc9ef38048.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/colruyt/colruytgroupidcheck/tac/detail>) |
| [Coveo Public Bug Bounty](<public-bounties/intigriti/intigriti-e01da94530cd8bf0.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/coveo/coveopublicbugbounty/preview/detail>) |
| [Daytona Bug Bounty](<public-bounties/intigriti/intigriti-e4396437b33f824f.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/daytona/daytonabugbounty/preview/detail>) |
| [Doccle Bug Bounty program](<public-bounties/intigriti/intigriti-247b5b0bf0908a57.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/doccle/doccle/preview/detail>) |
| [Farfetch Bug Bounty](<public-bounties/intigriti/intigriti-1c92df8e83902323.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/farfetch/farfetchbugbounty/preview/detail>) |
| [Fortnox Bug Bounty Program](<public-bounties/intigriti/intigriti-e2f3e3ddec74de2c.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/fortnox/fortnox/preview/detail>) |
| [Ideals Bug Bounty Program](<public-bounties/intigriti/intigriti-b179780cc1d1f514.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/ideals/ideals/preview/detail>) |
| [Intertoys](<public-bounties/intigriti/intigriti-c2b0db1b0d386293.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/intertoys/intertoys/preview/detail>) |
| [Kahoot Bug Bounty Program](<public-bounties/intigriti/intigriti-75e73143438d2023.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/kahoot/kahoot/preview/detail>) |
| [Leapsome](<public-bounties/intigriti/intigriti-11ea6c34a5fc8e32.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/leapsome/leapsome/preview/detail>) |
| [Liveperson Conversational Cloud](<public-bounties/intigriti/intigriti-3b4650952b890d2a.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/liveperson/livepersonconversationalcloud/tac/detail>) |
| [My\.sdworx\.com](<public-bounties/intigriti/intigriti-c1e7680283f3b791.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/sdworx/myworkandme/tac/detail>) |
| [MyDirtyHobby Bug Bounty Program](<public-bounties/intigriti/intigriti-6c718f89002da960.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/aylo/mydirtyhobby-bbp/tac/detail>) |
| [Newpharma](<public-bounties/intigriti/intigriti-faccd7a67d359b6c.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/colruyt/newpharma/tac/detail>) |
| [Nutaku Bug Bounty Program](<public-bounties/intigriti/intigriti-ae62addf0fe136d2.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/aylo/nutaku-bbp/tac/detail>) |
| [Pornhub Bug Bounty Program](<public-bounties/intigriti/intigriti-fa268c09399b222d.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/aylo/pornhub-bbp/tac/detail>) |
| [Probiller Bug Bounty Program](<public-bounties/intigriti/intigriti-9b1c87de2b2d754c.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/aylo/probiller-bbp/tac/detail>) |
| [RAMPF Bug Bounty](<public-bounties/intigriti/intigriti-50368e0e356572c8.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/rampf/rampfbugbounty/preview/detail>) |
| [Telenet - Base - Wyre - Tadaam](<public-bounties/intigriti/intigriti-4f3851c94514719c.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/telenet/telenetgroup/tac/detail>) |
| [TrafficJunky Bug Bounty Program](<public-bounties/intigriti/intigriti-8307183f06cec029.md>) | Intigriti | terms only | [terms login gate](<https://app.intigriti.com/programs/aylo/trafficjunky-bbp/tac/detail>) |
| [Ubisoft Game Security BBP](<public-bounties/intigriti/intigriti-e80762bd94c58a62.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/ubisoft/ubisoftgamesecbbp/preview/detail>) |
| [Uitgeverij Deviant Bug Bounty](<public-bounties/intigriti/intigriti-545a9316e98fac09.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/uitgeverijdeviant/uitgeverijdeviant/preview/detail>) |
| [UpCloud Bug Bounty](<public-bounties/intigriti/intigriti-069d131a65f4f903.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/upcloud/upcloud/preview/detail>) |
| [Webnode](<public-bounties/intigriti/intigriti-c2c21827100d7db4.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/combell/webnode/preview/detail>) |
| [Wireless Logic](<public-bounties/intigriti/intigriti-43c2b66cd2246ab7.md>) | Intigriti | preview only | [preview login gate](<https://app.intigriti.com/programs/wl/wirelesslogic/preview/detail>) |

Each gap page states the observed access or asset-list limitation. The [JSON audit](../exports/program-scope-audit.json) retains the exact review note and timestamp.
