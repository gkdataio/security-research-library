# GitHub OAuth consent failed across request-method semantics

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** GitHub  
**Product:** GitHub OAuth authorization

## What the evidence establishes

Publication window: historical / outside the preferred window; reviewed as of 2026-10-02.

A USD 25,000 researcher-reported award illustrates how differing framework and controller assumptions can remove an OAuth consent boundary\.

### Root cause

The researcher compared the consent screen’s intended state change with routing and controller logic\. The framework accepted a wider set of request semantics than the controller expected\. Application logic treated the unexpected case as permission to grant access, even though the usual consent safeguards did not apply\. The failed invariant was that every new grant required the user’s explicit, validated approval\.

### Bounded impact

The researcher reports that a user visiting a malicious website could unintentionally grant an application access to read or modify private GitHub data\. This demonstrates unauthorized delegated access, rather than evidence that the attacker learned the account password or that all unrelated account controls failed\.

### Defensive lessons

- Require positive validation of the intended state-changing operation; reject unrecognized alternatives rather than defaulting to a privileged action\.
- Model framework routing, request interpretation and consent enforcement as separate layers whose assumptions must agree\.
- Verify that consent and request-integrity checks remain attached to every path that creates a grant\.
- The source dates the production fix and later Enterprise releases, but does not document the exact patch here; these lessons are defensive recommendations\.

## Award and evidence

**USD 25,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. Individual report; production fix date is for github\.com, with enterprise releases following June 26\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/github-oauth-method-semantics-2019.json>).

## Dates

- **published:** 2019-11-05; precision: day; basis: explicit
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported
- **reported:** 2019-06-19; precision: day; basis: explicit
- **awarded:** 2019-06-26; precision: day; basis: explicit
- **fixed:** 2019-06-20; precision: day; basis: explicit
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T19:39:00Z. Re-read the researcher’s intended-consent model, framework/controller distinction, impact and remediation timeline\. Expanded the original explanation while omitting the triggering request and reproduction details\.

- Researcher-reported award; cash settlement is not independently audited\.
- The reported impact requires user interaction\. Exact vendor patch implementation and evidence of real-world abuse are not supplied\.

## Related conceptual diagrams

- [An identity claim must belong to the user](<../diagram-gallery.md#identity-claim-binding>)

## Sources and attribution

- [Bypassing GitHub’s OAuth flow](<https://blog.teddykatz.com/2019/11/05/github-oauth-bypass.html>) — Teddy Katz; retrieved 2026-10-02T19:39:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
