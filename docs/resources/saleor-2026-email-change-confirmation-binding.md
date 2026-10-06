# Saleor email changes: bind confirmation to account and state

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/saleor-2026-email-change-confirmation-binding.json>) · [Official resource](<https://github.com/saleor/saleor/security/advisories/GHSA-hwph-9537-mc3p>)

**Publisher:** Saleor maintainers  
**Authors:** Not identified in the reviewed record  
**Resource type:** Maintainer Advisory  
**Version:** Not established in the reviewed record  
**Topics:** Identity; Authorization; Business Logic and State Integrity  
**Defensive skills:** Model access-control invariants; Review security-token design; Review identity lifecycle; Verify remediation evidence

## Original summary

CVE-2026-35407 concerns email-change confirmation failing to bind a valid token to the authenticated account\. The stated scenario requires a valid confirmation token for one account and authenticated access to a second account\. Maintainers describe account-integrity loss and potential durable compromise; this is not an unauthenticated takeover claim\.

## Defensive use

Editorial lesson: a valid confirmation artifact should authorize one subject, one operation and an expected current state\. The linked patch adds subject and operation checks plus agreement with the account's prior email state\. Its confirmation tests cover cross-account rejection and changed-state handling\. Reading those checks and assertions does not establish a successful test run\. Review identity transitions as a complete authorization contract rather than treating token validity as sufficient permission\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Authenticated sessions, confirmation tokens and account lifecycle concepts
- Authorization invariants across business-state transitions

## Access and freshness

**Access cost at review:** free.

Public maintainer advisory, linked patch and associated test source\.

**Reviewed:** 2026-10-06T03:41:33Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Read the advisory, relevant patch changes and confirmation-test source\. Upstream code was not executed; no reproduction, target testing or independent patch verification performed\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-04-08; precision: day; basis: explicit; source: [Cross-Account Email Change via Unbound Confirmation Token](<https://github.com/saleor/saleor/security/advisories/GHSA-hwph-9537-mc3p>) (source ID: advisory). Original maintainer-advisory publication\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded. No separate educational-resource edition date established\.
- **source displayed:** 2026-04-08; precision: day; basis: explicit; source: [Cross-Account Email Change via Unbound Confirmation Token](<https://github.com/saleor/saleor/security/advisories/GHSA-hwph-9537-mc3p>) (source ID: advisory). Displayed primary publication date; no separate update date established\.

## Caveats

- The advisory lists branch fixes 3\.23\.0a3, 3\.22\.47, 3\.21\.54 and 3\.20\.118\. Its affected entries each start at 2\.10\.0 and end before the corresponding fix; retain these branch contexts rather than collapsing them into one interval\. 3\.23\.0a3 is a prerelease\.
- Maintainers list no known workaround\. Historical patched versions are not a guarantee of current security across all issues\.
- The reviewed sources do not establish a controlled independent demonstration or a production incident\. Durable account compromise remains maintainer-described potential impact, conditional on the stated authenticated-access prerequisite\.
- NyanKiyoshi published the advisory; ch1nhpd is credited as Reporter\. No narrative byline or qualifying individual award is established\.
- The linked commit bundles other security changes\. Only its email-confirmation binding and related tests support this case; unrelated changes are not attributed to CVE-2026-35407\. Commit and software-release dates were not established\.
- The confirmation operation's subject, purpose and current-state contract is distinct from the library's external-identity issuer and account-linking examples\. Learning prerequisites and generalized defensive guidance are editorial\.

## Sources and attribution

- [Cross-Account Email Change via Unbound Confirmation Token](<https://github.com/saleor/saleor/security/advisories/GHSA-hwph-9537-mc3p>) — Saleor maintainers; source ID: advisory; provenance: official primary; retrieved 2026-10-06T03:40:00Z; supports: summary, dates.
- [Saleor main-branch security patch containing email-confirmation checks](<https://github.com/saleor/saleor/commit/f0371bdd4cafcc841f1a9e7049cead6133bf7464>) — Saleor maintainers; source ID: patch; provenance: official primary; retrieved 2026-10-06T03:40:28Z; supports: summary.
- [Saleor email-confirmation tests at the linked fix commit](<https://github.com/saleor/saleor/blob/f0371bdd4cafcc841f1a9e7049cead6133bf7464/saleor/graphql/account/tests/mutations/account/test_confirm_email_change.py>) — Saleor maintainers; source ID: patch-tests; provenance: official primary; retrieved 2026-10-06T03:40:46Z; supports: summary.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
