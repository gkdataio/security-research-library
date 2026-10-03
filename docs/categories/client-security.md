# Client and browser security

[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)

**Security theme / environment** · 20 reports · 4 related resources · 3 diagrams

Client-side isolation, memory safety, and security-sensitive state.

Report membership uses the existing primary or secondary category client-security. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.

On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)

<a id="reports"></a>
## Reports

- [Bard Workspace integration weakened output-data boundaries](<../reports/google-bard-workspace-output-boundary-2024.md>) — Google; secondary category.
- [Chrome graphics input validation weakened an isolation boundary](<../reports/google-chrome-angle-input-validation-2026.md>) — Google; primary category.
- [Codex automated Git operations trusted repository hook settings](<../reports/openai-codex-repository-hook-execution-trust-2026.md>) — OpenAI; secondary category.
- [Codex command approval relied on inconsistent parser semantics](<../reports/openai-codex-command-parser-approval-consistency-2026.md>) — OpenAI; secondary category.
- [Codex metadata collection trusted repository execution helpers](<../reports/openai-codex-repository-metadata-helper-trust-2026.md>) — OpenAI; secondary category.
- [Facebook SDK message authentication relied on insecure randomness](<../reports/facebook-sdk-message-authentication-randomness-2023.md>) — Meta; secondary category.
- [Gemini-to-Colab rendering boundary exposed Workspace data](<../reports/google-gemini-colab-rendering-boundary-2025.md>) — Google; secondary category.
- [Google IDX worker messaging crossed browser trust boundaries](<../reports/google-idx-worker-message-trust-2025.md>) — Google; primary category.
- [iCloud sharing consent and Safari trust boundaries failed together](<../reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.md>) — Apple; primary category.
- [Instagram client configuration exposed an application credential](<../reports/instagram-application-credential-client-containment-2022.md>) — Meta; secondary category.
- [macOS SMBFS error handling left inconsistent kernel parser state](<../reports/apple-smbfs-parser-state-consistency-2026.md>) — Apple; secondary category.
- [Meta Accounts Center linking lost credential and identity confinement](<../reports/meta-accounts-center-linking-credential-confinement-2024.md>) — Meta; secondary category.
- [Meta Conversions API Gateway mixed configuration data with executable output](<../reports/meta-conversions-gateway-generated-script-boundary-2025.md>) — Meta; secondary category.
- [Meta Conversions API Gateway trusted message origins as script authority](<../reports/meta-conversions-gateway-message-origin-boundary-2024.md>) — Meta; primary category.
- [Meta Pixel cross-window handling lost message and token authority](<../reports/meta-pixel-cross-window-authority-binding-2024.md>) — Meta; secondary category.
- [Meta Quest login migration lost OAuth credential confinement](<../reports/meta-quest-oauth-redirect-confidentiality-2022.md>) — Meta; secondary category.
- [Pixel lock-screen completion lost security-state binding](<../reports/google-pixel-lock-screen-state-binding-2022.md>) — Google; secondary category.
- [Safari origin confusion undermined stored media permissions](<../reports/apple-safari-media-permission-origin-confusion-2020.md>) — Apple; primary category.
- [V8 control-flow analysis omitted required initialization checks](<../reports/google-chrome-v8-initialization-checks-2025.md>) — Google; secondary category.
- [V8 optimized object handling retained invalid type assumptions](<../reports/google-chrome-v8-type-consistency-2025.md>) — Google; secondary category.

<a id="related-learning"></a>
## Related learning

Included by the topic crosswalk or an explicit resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.

- [Authorization Cheat Sheet](<../resources/owasp-authorization-cheat-sheet.md>) — diagram: [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>).
- [Chromium Rule of Two: input trust, memory safety and privilege](<../resources/chromium-rule-of-two-input-isolation.md>) — diagram: [Parsing safety and action authority](<../diagram-gallery.md#parsing-safety-action-authority>).
- [HTML5 Security Cheat Sheet: Web Messaging](<../resources/owasp-browser-message-trust-boundaries.md>) — diagram: [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>).
- [LLM Prompt Injection Prevention Cheat Sheet](<../resources/owasp-llm-prompt-injection-prevention.md>) — diagram: [Retrieved content is data, not authority](<../diagram-gallery.md#ai-content-authority-separation>).

<a id="conceptual-diagrams"></a>
## Conceptual diagrams

Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.

- [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>)
- [Parsing safety and action authority](<../diagram-gallery.md#parsing-safety-action-authority>)
- [Retrieved content is data, not authority](<../diagram-gallery.md#ai-content-authority-separation>)

---

Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).
