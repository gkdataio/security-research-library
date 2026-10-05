# Cloud permissions and isolation

[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)

**Security theme / environment** · 15 reports · 10 related resources · 4 diagrams

Service identities, IAM boundaries, tenant isolation, and delegated authority.

Report membership uses the existing primary or secondary category cloud-security. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.

On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)

<a id="reports"></a>
## Reports

- [Actifio driver execution exposed excessive shared-service authority](<../reports/google-actifio-driver-service-identity-isolation-2025.md>) — Google; primary category.
- [Apple PCC startup archive processing lacked path confinement](<../reports/apple-pcc-boot-archive-path-validation-2026.md>) — Apple; primary category.
- [Cloud Build approval was not bound to immutable code](<../reports/google-cloud-build-approval-toctou-2025.md>) — Google; secondary category.
- [Google Application Integration mixed resource and service authority](<../reports/google-application-integration-authorization-boundaries-2026.md>) — Google; secondary category.
- [Google Firefly confused worker authority and storage boundaries](<../reports/google-firefly-worker-authority-storage-boundary-2026.md>) — Google; secondary category.
- [Google Mamba temporary outputs lacked access isolation](<../reports/google-mamba-temporary-output-isolation-2026.md>) — Google; secondary category.
- [MariaDB JSON normalization exceeded allocated buffer capacity](<../reports/mariadb-json-normalization-buffer-capacity-2026.md>) — MariaDB; secondary category.
- [Meta service-identity exposure amplified by excessive secret access](<../reports/meta-service-identity-secrets-trust-boundary-2026.md>) — Meta; primary category.
- [NVIDIA container initialization inherited untrusted execution context](<../reports/nvidia-container-runtime-environment-trust-2025.md>) — NVIDIA; primary category.
- [PostgreSQL cryptographic parsing omitted a buffer-capacity check](<../reports/postgresql-pgcrypto-buffer-capacity-validation-2026.md>) — PostgreSQL; secondary category.
- [PostgreSQL extension estimator trusted an unchecked input type](<../reports/postgresql-extension-input-type-validation-2026.md>) — PostgreSQL; secondary category.
- [Redis deserialization cleanup violated object-ownership invariants](<../reports/redis-deserialization-object-ownership-2026.md>) — Redis; secondary category.
- [Redis Lua object lifetime failure crossed the scripting boundary](<../reports/redis-lua-object-lifetime-isolation-2025.md>) — Redis; secondary category.
- [Redis replication state changes invalidated an active interpreter](<../reports/redis-replication-interpreter-lifetime-2026.md>) — Redis; secondary category.
- [Shopify Exchange screenshot service crossed internal boundaries](<../reports/shopify-exchange-request-isolation-2019.md>) — Shopify; secondary category.

<a id="related-learning"></a>
## Related learning

Included by the topic crosswalk or an explicit resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.

- [Authorization Cheat Sheet](<../resources/owasp-authorization-cheat-sheet.md>) — diagram: [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>).
- [AWS IAM security best practices for workload identities](<../resources/aws-iam-machine-identity-best-practices.md>) — topic: Cloud Security; diagram: [Keep workload authority tenant-scoped](<../diagram-gallery.md#workload-identity-tenant-scope>).
- [Chromium Rule of Two: input trust, memory safety and privilege](<../resources/chromium-rule-of-two-input-isolation.md>) — diagram: [Parsing safety and action authority](<../diagram-gallery.md#parsing-safety-action-authority>).
- [GitHub internal metadata: preserve the boundary between user data and service authority](<../resources/github-2026-internal-metadata-authority.md>) — topic: Cloud Security.
- [Jupyter Enterprise Gateway: keep kernel configuration outside template authority](<../resources/jupyter-enterprise-gateway-2026-kernel-configuration-template-boundary.md>) — topic: Cloud Security.
- [NIST SP 800-190: Application Container Security Guide](<../resources/nist-sp-800-190-container-isolation-guide.md>) — topic: Cloud Security.
- [OWASP Server-Side Request Forgery Prevention](<../resources/owasp-server-request-destination-boundaries.md>) — topic: Cloud Security; diagram: [Layer server-request destination controls](<../diagram-gallery.md#server-request-destination-policy>).
- [OWASP Transaction Authorization](<../resources/owasp-transaction-authorization-state-integrity.md>) — diagram: [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>).
- [React2Shell response: parser consistency and layered remediation](<../resources/vercel-react2shell-parser-normalization-defense.md>) — topic: Cloud Security.
- [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<../resources/usenix-2025-integration-platform-oauth-bindings.md>) — topic: Cloud Security.

<a id="conceptual-diagrams"></a>
## Conceptual diagrams

Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.

- [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>)
- [Keep workload authority tenant-scoped](<../diagram-gallery.md#workload-identity-tenant-scope>)
- [Layer server-request destination controls](<../diagram-gallery.md#server-request-destination-policy>)
- [Parsing safety and action authority](<../diagram-gallery.md#parsing-safety-action-authority>)

---

Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).
