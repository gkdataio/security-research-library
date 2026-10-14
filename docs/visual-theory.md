# Visual theory: defensive trust boundaries

These are original conceptual models grounded in linked disclosures and official guidance. They explain security decisions, not the exact architecture of a vendor or an exploitation sequence. Each record links its evidence and supplies accessible alternate text.

## Bind approval to an immutable version

![Reviewed content and its immutable version are bound to approval. Execution checks that the version matches; mismatches require a new review.](../diagrams/approval-version-integrity.svg)

The system should execute exactly the content that was approved. Check the version when granting approval and again when the privileged component uses it.

[Evidence and metadata](../data/diagrams/approval-version-integrity.json) · [Mermaid source](../diagrams/approval-version-integrity.mmd)

## Separate AI content from action authority

![User intent and retrieved connector content enter separately. An independent policy gate authorizes each proposed state change. Unapproved changes are denied.](../diagrams/ai-content-authority-separation.svg)

Retrieved content can inform a response without gaining authority to change persistent state. The model's proposed action is a request to validate, not permission by itself.

[Evidence and metadata](../data/diagrams/ai-content-authority-separation.json) · [Mermaid source](../diagrams/ai-content-authority-separation.mmd)

## Preserve identity ownership across integrations

![Claims are bound to the authenticated subject. The relying application validates issuer, audience, signature, and ownership before mapping a local account.](../diagrams/identity-claim-binding.svg)

A valid signature is one check among several. The issued claims must still refer to the authenticated subject and the intended relying application.

[Evidence and metadata](../data/diagrams/identity-claim-binding.json) · [Mermaid source](../diagrams/identity-claim-binding.mmd)

## Keep workload authority tenant-scoped

![A verified workload identity and requested operation reach one policy decision. Role, action, resource and tenant must match; approved scope is allowed, other access is denied, and each decision is recorded.](../diagrams/workload-identity-tenant-scope.svg)

Authenticating a workload does not determine everything it may access. Bind authorization to the requested operation and tenant, keep credentials short-lived where supported, and review unused permissions separately. This connects the Meta and Actifio cases with AWS IAM guidance.

[Evidence and metadata](../data/diagrams/workload-identity-tenant-scope.json) · [Mermaid source](../diagrams/workload-identity-tenant-scope.mmd)

## Layer server-request destination controls

![Requests pass parsing, application destination policy and independent network egress checks. Any failure is rejected.](../diagrams/server-request-destination-policy.svg)

Combine application policy with an independent network boundary. Choose destination restrictions that fit the service’s documented purpose.

[Evidence and metadata](../data/diagrams/server-request-destination-policy.json) · [Mermaid source](../diagrams/server-request-destination-policy.mmd)

## Preserve ownership through account recovery

![An account-bound challenge is checked before changing a password. Invalid proof leaves account state unchanged; valid proof is consumed and followed by notification.](../diagrams/account-recovery-challenge-lifecycle.svg)

Check which account each challenge belongs to, how attempts are counted and what happens to sessions after a reset. Review these rules together. This conceptual model connects the GitLab, Microsoft and Instagram cases.

[Evidence and metadata](../data/diagrams/account-recovery-challenge-lifecycle.json) · [Mermaid source](../diagrams/account-recovery-challenge-lifecycle.mmd)

## Separate parsing safety from action authority

![Untrusted input is safely parsed into a bounded result. A separate meaning and authorization check controls the permitted operation; failed checks reject the request.](../diagrams/parsing-safety-action-authority.svg)

Memory safety and restricted privileges reduce parsing risk. Successfully parsing a request still does not give permission to carry it out. Keep that access decision independent of the parser.

[Evidence and metadata](../data/diagrams/parsing-safety-action-authority.json) · [Mermaid source](../diagrams/parsing-safety-action-authority.mmd)

## Keep browser message identity separate from authority

![A browser message passes origin, sender-context and format checks, then a separate operation and recipient decision. Failures reject without disclosure or state changes; approved content remains data.](../diagrams/browser-message-authority-boundaries.svg)

Knowing where a message came from does not settle what it may request or which data its recipient may receive. Keep those decisions explicit and prevent accepted content from becoming executable markup. This is a conceptual design model, not a description of Meta’s exact patch.

[Evidence and metadata](../data/diagrams/browser-message-authority-boundaries.json) · [Mermaid source](../diagrams/browser-message-authority-boundaries.mmd)

## Respect the server-to-client disclosure boundary

![A request enters a server-side caller, resource and operation authorization decision. Denial returns no protected data. Approval proceeds to explicit field selection before serialization. Only permitted, necessary fields cross into client-visible data. A separate consumer-context handling step keeps content, including generated text, from acquiring executable meaning before display. Browser rendering never supplies server authorization.](../diagrams/server-client-data-consumer-boundaries.svg)

Data is not safe to send to a browser just because it came from a server. Select only the fields the recipient may receive, then handle the content safely for the context where it will be used.

[Evidence and metadata](../data/diagrams/server-client-data-consumer-boundaries.json) · [Mermaid source](../diagrams/server-client-data-consumer-boundaries.mmd)

## Check build evidence at the artifact consumer

![Untrusted contributions remain separated from trusted build state. An artifact and its provenance reach a consumer policy gate. Only authenticated evidence matching the artifact and expected builder and inputs makes it eligible for release review; missing or mismatched evidence prevents promotion.](../diagrams/build-artifact-provenance-boundary.svg)

Keep untrusted contributions separate from trusted build state. Then, before using a build artifact, check that its authenticated provenance matches the artifact and the expected build. Passing that check still leaves the rest of the release review to do; provenance does not guarantee vulnerability-free software.

[Evidence and metadata](../data/diagrams/build-artifact-provenance-boundary.json) · [Mermaid source](../diagrams/build-artifact-provenance-boundary.mmd)

## Separate public errors from internal diagnostics

![A failure reaches a shared error handler. The public response contains minimal generic information. A separate diagnostic path selects useful context, removes secrets and unnecessary personal data, and stores it under access and retention controls. Raw exception details do not flow directly to the client.](../diagrams/error-diagnostic-disclosure-boundary.svg)

Decide what an error response may reveal and what belongs only in diagnostics. Give clients a minimal response. Collect only useful diagnostic details and protect them separately. Internal logs still need a legitimate purpose, restricted access and a retention policy.

[Evidence and metadata](../data/diagrams/error-diagnostic-disclosure-boundary.json) · [Mermaid source](../diagrams/error-diagnostic-disclosure-boundary.mmd)

## Preserve every source’s access boundary in a combined view

![A caller requests a combined view. Source A and source B each have an independent authorization decision. Either denial stops the combined view. An explicit AND gate requires both permissions before composition; field selection preserves each source’s field permissions before only permitted data is returned.](../diagrams/combined-view-source-authorization.svg)

Permission to read one source does not grant access to another. In this all-or-nothing model, both sources must permit the caller, and the combined response must retain each source's field restrictions. It connects GitHub's cross-repository comparison disclosure with Frappe's linked-document response disclosure and OWASP authorization guidance. Returning partial results needs a separate policy for omitting inaccessible data without revealing it. The model does not cover snapshot consistency, races with permission changes or information inferred from combined values.

[Evidence and metadata](../data/diagrams/combined-view-source-authorization.json) · [Mermaid source](../diagrams/combined-view-source-authorization.mmd) · [DOT source](../diagrams/combined-view-source-authorization.dot)

## Preserve the original caller's authority through fallbacks

![A failure retains the caller, action and resource. Explicit access denial stops without protected data. A known recoverable operational failure may propose a fallback, but execution identity adds no caller entitlement. Application policy must permit the fallback for the original caller before a scoped execution returns only caller-permitted data. Denied or indeterminate decisions stop.](../diagrams/fallback-requester-authorization.svg)

A fallback must stay within the original caller's permissions. An access denial ends this operation. A recoverable operational failure may justify considering a fallback, but application policy must still permit it for the original caller, regardless of which identity executes it. This editorial model connects the researcher's account of Instagram's privileged error handling with OWASP authorization guidance. It does not describe Instagram's architecture or patch. It also does not cover separately authorized background work, permission freshness, revocation or distributed consistency.

[Evidence and metadata](../data/diagrams/fallback-requester-authorization.json) · [Mermaid source](../diagrams/fallback-requester-authorization.mmd) · [DOT source](../diagrams/fallback-requester-authorization.dot)

## Keep delegated authority within the approved grant

![Approved grant context and a first-issuance or renewal request are both required. Resolve trusted context, then check the correct grant and client and whether requested authority stays within approval. Issue only bounded authority; mismatch or incomplete binding prevents issuance. Changing approved authority needs a separate authorization decision.](../diagrams/delegated-grant-authority-continuity.svg)

A grant authorizes a particular subject, client and set of permissions. Keep those limits through first issuance and renewal, even if the protocol steps differ. The user's wider access and the client's registration do not expand the grant. Issuing less authority, or adding authority with separate approval, still fits this model.

This editorial model connects the Google device-grant disclosure, n8n's refresh-resource advisory and RFC 9700 sections 2.3 and 4.14.2. It assumes that grant context is protected against tampering and that applicable client checks have been performed. It does not prescribe storage, describe vendor architecture or verify a deployed fix. Revocation, concurrency, replay protection and consent usability are outside its scope.

[Evidence and metadata](../data/diagrams/delegated-grant-authority-continuity.json) · [Mermaid source](../diagrams/delegated-grant-authority-continuity.mmd) · [DOT source](../diagrams/delegated-grant-authority-continuity.dot)

## Rendering and maintenance

The Mermaid and Graphviz sources are generated from the same canonical node/edge graph. The SVG companions were rendered offline with Graphviz and visually inspected. A Mermaid engine was not executed. To regenerate with an installed Graphviz version:

```sh
python3 scripts/render_diagrams.py
python3 scripts/render_diagrams.py --check
python3 scripts/validate_extra.py
```

After changing a graph, inspect the rendered SVG before marking visual QA passed. Resource and diagram metadata are included in the separate resources export.
