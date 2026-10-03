# Software supply-chain security

[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)

**Security theme / environment** · 6 reports · 4 related resources · 2 diagrams

Build systems, package provenance, release integrity, and automation trust.

Report membership uses the existing primary or secondary category supply-chain. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.

On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)

<a id="reports"></a>
## Reports

- [Angular automation trust and cache isolation weakness](<../reports/angular-ci-cache-trust-2026.md>) — Google; primary category.
- [Cloud Build approval was not bound to immutable code](<../reports/google-cloud-build-approval-toctou-2025.md>) — Google; secondary category.
- [GitHub Actions trust depended on invalid repository references](<../reports/github-actions-reference-validation-2021.md>) — GitHub; primary category.
- [GitHub package-source trust allowed dependency confusion](<../reports/github-ruby-dependency-confusion-2025.md>) — GitHub; primary category.
- [GitHub runner-image builds shared persistent infrastructure with untrusted workflows](<../reports/github-runner-image-build-isolation-2023.md>) — GitHub; primary category.
- [Meta Conversions API Gateway mixed configuration data with executable output](<../reports/meta-conversions-gateway-generated-script-boundary-2025.md>) — Meta; secondary category.

<a id="related-learning"></a>
## Related learning

Included by the topic crosswalk or an explicit resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.

- [Authorization Cheat Sheet](<../resources/owasp-authorization-cheat-sheet.md>) — diagram: [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>).
- [NIST SP 800-190: Application Container Security Guide](<../resources/nist-sp-800-190-container-isolation-guide.md>) — topic: Software Supply Chain.
- [OWASP Transaction Authorization](<../resources/owasp-transaction-authorization-state-integrity.md>) — diagram: [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>).
- [SLSA v1\.2: supply-chain security and build provenance](<../resources/slsa-v1-2-supply-chain-build-provenance.md>) — topic: Software Supply Chain; diagram: [Build evidence must match the artifact and trusted builder](<../diagram-gallery.md#build-artifact-provenance-boundary>).

<a id="conceptual-diagrams"></a>
## Conceptual diagrams

Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.

- [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>)
- [Build evidence must match the artifact and trusted builder](<../diagram-gallery.md#build-artifact-provenance-boundary>)

---

Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).
