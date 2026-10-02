# Visual theory: defensive trust boundaries

These are original conceptual models grounded in linked disclosures and official guidance. They explain security decisions, not the exact architecture of a vendor or an exploitation sequence. Each record links its evidence and supplies accessible alternate text.

## Bind approval to an immutable version

![Reviewed content and its immutable version are bound to approval. Execution checks that the version matches; mismatches require a new review.](../diagrams/approval-version-integrity.svg)

The key invariant is that the content executed is the content approved. Validation belongs at both the decision and the privileged consumer.

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

Review challenge binding, consistent attempt accounting and post-reset session policy together. This conceptual model connects the GitLab, Microsoft and Instagram cases.

[Evidence and metadata](../data/diagrams/account-recovery-challenge-lifecycle.json) · [Mermaid source](../diagrams/account-recovery-challenge-lifecycle.mmd)

## Separate parsing safety from action authority

![Untrusted input is safely parsed into a bounded result. A separate meaning and authorization check controls the permitted operation; failed checks reject the request.](../diagrams/parsing-safety-action-authority.svg)

Memory safety and restricted privileges reduce parsing risk. They do not authorize the meaning of parsed data. Keep the final policy decision independent of the parser.

[Evidence and metadata](../data/diagrams/parsing-safety-action-authority.json) · [Mermaid source](../diagrams/parsing-safety-action-authority.mmd)

## Rendering and maintenance

The Mermaid and Graphviz sources are generated from the same canonical node/edge graph. The SVG companions were rendered offline with Graphviz and visually inspected. A Mermaid engine was not executed. To regenerate with an installed Graphviz version:

```sh
python3 scripts/render_diagrams.py
python3 scripts/render_diagrams.py --check
python3 scripts/validate_extra.py
```

After changing a graph, inspect the rendered SVG before marking visual QA passed. Resource and diagram metadata are included in the separate resources export.
