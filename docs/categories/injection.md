# Injection and untrusted input

[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)

**Vulnerability family** · 12 reports · 11 related resources · 3 diagrams

Separation between untrusted data and executable interpretation.

Report membership uses the existing primary or secondary category injection. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.

On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)

<a id="reports"></a>
## Reports

- [Angular automation trust and cache isolation weakness](<../reports/angular-ci-cache-trust-2026.md>) — Google; secondary category.
- [Bard Workspace integration weakened output-data boundaries](<../reports/google-bard-workspace-output-boundary-2024.md>) — Google; secondary category.
- [Codex command approval relied on inconsistent parser semantics](<../reports/openai-codex-command-parser-approval-consistency-2026.md>) — OpenAI; primary category.
- [Facebook SDK message authentication relied on insecure randomness](<../reports/facebook-sdk-message-authentication-randomness-2023.md>) — Meta; secondary category.
- [Gemini-to-Colab rendering boundary exposed Workspace data](<../reports/google-gemini-colab-rendering-boundary-2025.md>) — Google; secondary category.
- [GitHub package-source trust allowed dependency confusion](<../reports/github-ruby-dependency-confusion-2025.md>) — GitHub; secondary category.
- [Google IDX worker messaging crossed browser trust boundaries](<../reports/google-idx-worker-message-trust-2025.md>) — Google; secondary category.
- [Kestrel HTTP framing differed across proxy and application boundaries](<../reports/microsoft-kestrel-http-framing-consistency-2025.md>) — Microsoft; primary category.
- [Meta Conversions API Gateway mixed configuration data with executable output](<../reports/meta-conversions-gateway-generated-script-boundary-2025.md>) — Meta; primary category.
- [Meta Conversions API Gateway trusted message origins as script authority](<../reports/meta-conversions-gateway-message-origin-boundary-2024.md>) — Meta; secondary category.
- [NVIDIA container initialization inherited untrusted execution context](<../reports/nvidia-container-runtime-environment-trust-2025.md>) — NVIDIA; secondary category.
- [PostgreSQL text-encoding invariant failure caused memory corruption](<../reports/postgresql-multibyte-validation-cve-2026-2006.md>) — PostgreSQL; secondary category.

<a id="related-learning"></a>
## Related learning

Included by the topic crosswalk or an explicit resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.

- [Authorization Cheat Sheet](<../resources/owasp-authorization-cheat-sheet.md>) — diagram: [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>).
- [Django: ORM alias metadata must not acquire query authority](<../resources/django-2026-query-alias-structure-boundary.md>) — topic: Interpreter Boundaries.
- [DOMPurify: accepted DOM realms must retain complete sanitization](<../resources/dompurify-2026-cross-realm-sanitization-consistency.md>) — topic: Interpreter Boundaries.
- [HTML5 Security Cheat Sheet: Web Messaging](<../resources/owasp-browser-message-trust-boundaries.md>) — diagram: [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>).
- [LLM Prompt Injection Prevention Cheat Sheet](<../resources/owasp-llm-prompt-injection-prevention.md>) — diagram: [Retrieved content is data, not authority](<../diagram-gallery.md#ai-content-authority-separation>).
- [Next\.js: response metadata must preserve representation boundaries](<../resources/nextjs-2026-response-metadata-representation-boundary.md>) — topic: Interpreter Boundaries.
- [Python subprocess: executable, argument, and interpreter boundaries](<../resources/python-subprocess-interpreter-boundaries.md>) — topic: Interpreter Boundaries.
- [SearchLeak: streamed output needs policy enforcement before browser activation](<../resources/microsoft-copilot-2026-streaming-output-activation-boundary.md>) — topic: Interpreter Boundaries.
- [Serialize JavaScript: every serialized field must retain data semantics](<../resources/serialize-javascript-2026-output-code-boundary.md>) — topic: Interpreter Boundaries.
- [SLSA v1\.2: supply-chain security and build provenance](<../resources/slsa-v1-2-supply-chain-build-provenance.md>) — diagram: [Build evidence must match the artifact and trusted builder](<../diagram-gallery.md#build-artifact-provenance-boundary>).
- [TanStack Start: preserve server-owned response authority through errors](<../resources/tanstack-2026-server-function-response-authority.md>) — topic: Interpreter Boundaries.

<a id="conceptual-diagrams"></a>
## Conceptual diagrams

Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.

- [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>)
- [Build evidence must match the artifact and trusted builder](<../diagram-gallery.md#build-artifact-provenance-boundary>)
- [Retrieved content is data, not authority](<../diagram-gallery.md#ai-content-authority-separation>)

---

Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).
