# Memory safety and parser contracts

[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)

**Vulnerability family** · 10 reports · 2 related resources · 1 diagram

Safe length, lifetime, encoding, and component-boundary assumptions.

Report membership uses the existing primary or secondary category memory-safety. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.

On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)

<a id="reports"></a>
## Reports

- [macOS SMBFS error handling left inconsistent kernel parser state](<../reports/apple-smbfs-parser-state-consistency-2026.md>) — Apple; primary category.
- [MariaDB JSON normalization exceeded allocated buffer capacity](<../reports/mariadb-json-normalization-buffer-capacity-2026.md>) — MariaDB; primary category.
- [PostgreSQL cryptographic parsing omitted a buffer-capacity check](<../reports/postgresql-pgcrypto-buffer-capacity-validation-2026.md>) — PostgreSQL; primary category.
- [PostgreSQL extension estimator trusted an unchecked input type](<../reports/postgresql-extension-input-type-validation-2026.md>) — PostgreSQL; primary category.
- [PostgreSQL text-encoding invariant failure caused memory corruption](<../reports/postgresql-multibyte-validation-cve-2026-2006.md>) — PostgreSQL; primary category.
- [Redis deserialization cleanup violated object-ownership invariants](<../reports/redis-deserialization-object-ownership-2026.md>) — Redis; primary category.
- [Redis Lua object lifetime failure crossed the scripting boundary](<../reports/redis-lua-object-lifetime-isolation-2025.md>) — Redis; primary category.
- [Redis replication state changes invalidated an active interpreter](<../reports/redis-replication-interpreter-lifetime-2026.md>) — Redis; primary category.
- [V8 control-flow analysis omitted required initialization checks](<../reports/google-chrome-v8-initialization-checks-2025.md>) — Google; primary category.
- [V8 optimized object handling retained invalid type assumptions](<../reports/google-chrome-v8-type-consistency-2025.md>) — Google; primary category.

<a id="related-learning"></a>
## Related learning

Included by the topic crosswalk or an explicit resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.

- [Chromium Rule of Two: input trust, memory safety and privilege](<../resources/chromium-rule-of-two-input-isolation.md>) — topic: Memory Safety and Process Isolation; diagram: [Parsing safety and action authority](<../diagram-gallery.md#parsing-safety-action-authority>).
- [Document Isolation Policy: process separation and residual authority](<../resources/chrome-document-isolation-policy-boundaries.md>) — topic: Memory Safety and Process Isolation.

<a id="conceptual-diagrams"></a>
## Conceptual diagrams

Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.

- [Parsing safety and action authority](<../diagram-gallery.md#parsing-safety-action-authority>)

---

Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).
