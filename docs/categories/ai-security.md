# AI integration boundaries

[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)

**Security theme / environment** · 7 reports · 15 related resources · 1 diagram

Authority boundaries around model input, tools, and downstream actions.

Report membership uses the existing primary or secondary category ai-security. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.

On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)

<a id="reports"></a>
## Reports

- [Apple PCC startup archive processing lacked path confinement](<../reports/apple-pcc-boot-archive-path-validation-2026.md>) — Apple; secondary category.
- [Bard Workspace integration weakened output-data boundaries](<../reports/google-bard-workspace-output-boundary-2024.md>) — Google; primary category.
- [Codex automated Git operations trusted repository hook settings](<../reports/openai-codex-repository-hook-execution-trust-2026.md>) — OpenAI; primary category.
- [Codex metadata collection trusted repository execution helpers](<../reports/openai-codex-repository-metadata-helper-trust-2026.md>) — OpenAI; primary category.
- [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](<../reports/google-gemini-enterprise-connected-content-memory-integrity-2026.md>) — Google; primary category.
- [Gemini-to-Colab rendering boundary exposed Workspace data](<../reports/google-gemini-colab-rendering-boundary-2025.md>) — Google; primary category.
- [Meta AI media access lacked object-ownership authorization](<../reports/meta-ai-media-object-authorization-2025.md>) — Meta; secondary category.

<a id="related-learning"></a>
## Related learning

Included by the topic crosswalk or an explicit resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.

- [Claude Cowork: approved destinations need account and operation binding](<../resources/anthropic-2026-egress-capability-identity-binding.md>) — topic: Ai Security.
- [Dify: telemetry destination changes carry tenant data-disclosure authority](<../resources/dify-2026-tracing-configuration-tenant-authority.md>) — topic: Ai Security.
- [Langflow: project transport authorization must reach each resource read](<../resources/langflow-2026-mcp-resource-project-authorization.md>) — topic: Ai Security.
- [LibreChat: agent edit authority must cover attached context](<../resources/librechat-2026-agent-context-mutation-authority.md>) — topic: Ai Security.
- [LibreChat: delegated credentials must remain bound to the initiating session](<../resources/librechat-2026-mcp-oauth-session-binding.md>) — topic: Ai Security.
- [LibreChat: viewing an integration must not reveal its service secrets](<../resources/librechat-2026-mcp-view-secret-projection.md>) — topic: Ai Security.
- [LLM Prompt Injection Prevention Cheat Sheet](<../resources/owasp-llm-prompt-injection-prevention.md>) — topic: Ai Security; diagram: [Retrieved content is data, not authority](<../diagram-gallery.md#ai-content-authority-separation>).
- [LobeHub: knowledge-base membership changes require ownership authorization](<../resources/lobehub-2026-knowledge-membership-mutation-authority.md>) — topic: Ai Security.
- [MCP elicitation: consent, credential custody and completion](<../resources/mcp-elicitation-consent-credential-custody.md>) — topic: Ai Security.
- [MCP scope selection: progressive consent and accumulated authority](<../resources/mcp-progressive-scope-authority.md>) — topic: Ai Security.
- [Open WebUI: credentials must bind to their destination connection](<../resources/open-webui-2026-connection-credential-capture.md>) — topic: Ai Security.
- [OWASP LLM05:2025: generated-output consumer trust](<../resources/owasp-llm-output-consumer-trust.md>) — topic: Ai Security.
- [OWASP LLM08:2025: retrieval permissions and knowledge provenance](<../resources/owasp-rag-retrieval-permission-boundaries.md>) — topic: Ai Security.
- [SearchLeak: streamed output needs policy enforcement before browser activation](<../resources/microsoft-copilot-2026-streaming-output-activation-boundary.md>) — topic: Ai Security.
- [ServiceNow: agent discovery expands the delegated authority boundary](<../resources/servicenow-2025-agent-discovery-delegation-authority.md>) — topic: Ai Security.

<a id="conceptual-diagrams"></a>
## Conceptual diagrams

Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.

- [Retrieved content is data, not authority](<../diagram-gallery.md#ai-content-authority-separation>)

---

Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).
