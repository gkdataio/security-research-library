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

## Rendering and maintenance

The Mermaid and Graphviz sources are generated from the same canonical node/edge graph. The SVG companions were rendered offline with Graphviz and visually inspected. A Mermaid engine was not executed. To regenerate with an installed Graphviz version:

```sh
python3 scripts/render_diagrams.py
python3 scripts/render_diagrams.py --check
python3 scripts/validate_extra.py
```

After changing a graph, inspect the rendered SVG before marking visual QA passed. Resource and diagram metadata are included in the separate resources export.
