# Server-side request trust

[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)

**Vulnerability family** · 1 report · 5 related resources · 1 diagram

Destination validation and boundaries in server-initiated requests.

Report membership uses the existing primary or secondary category server-request-trust. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.

## Specific vulnerability types

These narrower pages use separate source-backed memberships and publication-year groups. Their placement here is navigation, not an additional classification of every record in this family.

- [Server-side request forgery \(SSRF\)](<../vulnerabilities/ssrf.md>) — 1 award-backed report · 4 educational case studies · 1 learning reference

On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)

<a id="reports"></a>
## Reports

- [Shopify Exchange screenshot service crossed internal boundaries](<../reports/shopify-exchange-request-isolation-2019.md>) — Shopify; primary category.

<a id="related-learning"></a>
## Related learning

Included by the topic crosswalk, an explicit related-learning selection, or a resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.

- [Axios: URL construction does not establish destination authority](<../resources/axios-2025-base-url-destination-authority.md>) — explicit related-learning selection.
- [Formie: integration settings need operation and attribute authority](<../resources/formie-2026-integration-settings-credential-authority.md>) — explicit related-learning selection.
- [MLflow: destination validation must remain bound to the actual connection](<../resources/mlflow-2026-webhook-connection-destination-integrity.md>) — explicit related-learning selection.
- [OWASP Server-Side Request Forgery Prevention](<../resources/owasp-server-request-destination-boundaries.md>) — explicit related-learning selection; diagram: [Layer server-request destination controls](<../diagram-gallery.md#server-request-destination-policy>).
- [SvelteKit: origin construction and routing must preserve server request authority](<../resources/sveltekit-2026-origin-routing-trust-boundary.md>) — explicit related-learning selection.

<a id="conceptual-diagrams"></a>
## Conceptual diagrams

Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.

- [Layer server-request destination controls](<../diagram-gallery.md#server-request-destination-policy>)

---

Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).
