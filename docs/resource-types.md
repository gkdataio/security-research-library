# Learning resources by type

[Resource index](resource-index.md) · [Topics](resource-topics.md) · [Defensive skills](skillsets.md) · [Publication years](publication-years.md) · [Library home](../README.md)

155 distinct educational resources across 8 publication types. Each resource has exactly one canonical type; empty types remain visible.

Types describe the primary publication, not its supporting sources, quality, current applicability or award eligibility. Maintainer advisories remain separate from researcher articles; controlled training remains a learning format. Regeneration does not reverify sources.

## Browse types

- [Architecture Guide](<#type-architecture-guide>) — 15 resources.
- [Implementation Guide](<#type-implementation-guide>) — 26 resources.
- [Maintainer Advisory](<#type-maintainer-advisory>) — 69 resources.
- [Reporting Guide](<#type-reporting-guide>) — 2 resources.
- [Research Paper](<#type-research-paper>) — 26 resources.
- [Security Standard](<#type-security-standard>) — 2 resources.
- [Technical Standard](<#type-technical-standard>) — 9 resources.
- [Training Lab](<#type-training-lab>) — 6 resources.

<a id="type-architecture-guide"></a>
## Architecture Guide

15 resources.

- [Apollo Federation: preserving the router-to-subgraph boundary](<resources/apollo-2026-federation-router-subgraph-isolation.md>) — Apollo GraphQL.
- [Chrome Local Network Access: separate browser reachability from site authority](<resources/chrome-local-network-permission-boundaries.md>) — Google Chrome for Developers.
- [Chromium Rule of Two: input trust, memory safety and privilege](<resources/chromium-rule-of-two-input-isolation.md>) — Chromium Project.
- [Document Isolation Policy: process separation and residual authority](<resources/chrome-document-isolation-policy-boundaries.md>) — Google Chrome for Developers.
- [GitHub Artifact Attestations: Provenance and Consumer Policy](<resources/github-artifact-attestations.md>) — GitHub.
- [LLM Prompt Injection Prevention Cheat Sheet](<resources/owasp-llm-prompt-injection-prevention.md>) — OWASP Cheat Sheet Series.
- [MCP scope selection: progressive consent and accumulated authority](<resources/mcp-progressive-scope-authority.md>) — Model Context Protocol.
- [Microsoft compensating transactions: recovery must preserve valid concurrent state](<resources/microsoft-compensating-transaction-state-integrity.md>) — Microsoft Azure Architecture Center.
- [NIST SP 800-162: attribute authority and policy traceability](<resources/nist-sp-800-162-attribute-authority-modeling.md>) — National Institute of Standards and Technology.
- [NIST SP 800-190: Application Container Security Guide](<resources/nist-sp-800-190-container-isolation-guide.md>) — National Institute of Standards and Technology.
- [OWASP LLM08:2025: retrieval permissions and knowledge provenance](<resources/owasp-rag-retrieval-permission-boundaries.md>) — OWASP Gen AI Security Project.
- [OWASP LLM09:2026: embedding confidentiality and storage lifecycle](<resources/owasp-2026-embedding-confidentiality-lifecycle.md>) — OWASP Gen AI Security Project.
- [OWASP Threat Modeling: system assumptions and mitigation validation](<resources/owasp-threat-modeling-assumptions-and-validation.md>) — OWASP Cheat Sheet Series.
- [React2Shell response: parser consistency and layered remediation](<resources/vercel-react2shell-parser-normalization-defense.md>) — Vercel.
- [Sigstore Security Model](<resources/sigstore-security-model.md>) — Sigstore.

<a id="type-implementation-guide"></a>
## Implementation Guide

26 resources.

- [Authorization Cheat Sheet](<resources/owasp-authorization-cheat-sheet.md>) — OWASP Cheat Sheet Series.
- [AWS IAM security best practices for workload identities](<resources/aws-iam-machine-identity-best-practices.md>) — Amazon Web Services.
- [C\+\+ Core Guidelines: Bounds and Lifetime Safety](<resources/cpp-core-guidelines-bounds-lifetime.md>) — C\+\+ Core Guidelines project.
- [Chrome bfcache: restored pages and session-state boundaries](<resources/chrome-bfcache-restored-session-state.md>) — Google Chrome for Developers.
- [Error Handling Cheat Sheet](<resources/owasp-error-response-data-minimization.md>) — OWASP Cheat Sheet Series.
- [Google AIP-158: pagination continuation does not grant resource authority](<resources/google-aip-158-pagination-authorization-boundary.md>) — Google.
- [Google API field masks: preserve server-owned and immutable state](<resources/google-aip-161-update-field-authority.md>) — Google.
- [Google API request identity: bind retry semantics to the logical operation](<resources/google-aip-155-request-identity-contract.md>) — Google.
- [Google long-running operations: cancellation requests and completion evidence](<resources/google-aip-151-operation-completion-integrity.md>) — Google.
- [HTML5 Security Cheat Sheet: Web Messaging](<resources/owasp-browser-message-trust-boundaries.md>) — OWASP Cheat Sheet Series.
- [Microsoft Graph batching: preserve each member authorization outcome](<resources/microsoft-graph-batch-member-authorization-outcomes.md>) — Microsoft.
- [Next\.js data security: server authorization and client-visible data](<resources/nextjs-server-client-data-security.md>) — Next\.js / Vercel.
- [NIST SSDF 1\.1: Component Governance and Release Provenance](<resources/nist-ssdf-1-1-dependency-governance.md>) — NIST.
- [OpenFGA query consistency: authorization decisions need sufficiently fresh state](<resources/openfga-authorization-query-freshness.md>) — OpenFGA.
- [OWASP Forgot Password](<resources/owasp-account-recovery-state-integrity.md>) — OWASP Cheat Sheet Series.
- [OWASP LLM05:2025: generated-output consumer trust](<resources/owasp-llm-output-consumer-trust.md>) — OWASP Gen AI Security Project.
- [OWASP Logging: trustworthy and minimal application evidence](<resources/owasp-security-logging-evidence-quality.md>) — OWASP Cheat Sheet Series.
- [OWASP Secure Code Review: baseline and change-focused review](<resources/owasp-secure-code-review-methodology.md>) — OWASP Cheat Sheet Series.
- [OWASP Server-Side Request Forgery Prevention](<resources/owasp-server-request-destination-boundaries.md>) — OWASP Cheat Sheet Series.
- [OWASP Session Management: privilege-transition integrity](<resources/owasp-session-privilege-transition-integrity.md>) — OWASP Cheat Sheet Series.
- [OWASP Transaction Authorization](<resources/owasp-transaction-authorization-state-integrity.md>) — OWASP Cheat Sheet Series.
- [PostgreSQL 18: Transaction Isolation and Business Invariants](<resources/postgresql-transaction-isolation-business-invariants.md>) — PostgreSQL Global Development Group.
- [Python subprocess: executable, argument, and interpreter boundaries](<resources/python-subprocess-interpreter-boundaries.md>) — Python Software Foundation.
- [Rust Ownership and Borrowing: Lifetime Contracts](<resources/rust-ownership-borrowing.md>) — The Rust Project.
- [Rust Slices: Bounds, Borrowing, and Text Boundaries](<resources/rust-slices-parser-boundaries.md>) — The Rust Project.
- [Stripe webhooks: authentic delivery and business-state integrity](<resources/stripe-webhook-delivery-state-integrity.md>) — Stripe.

<a id="type-maintainer-advisory"></a>
## Maintainer Advisory

69 resources.

- [Angular host bindings: bind sanitization to the concrete output element](<resources/angular-2026-host-binding-context-authority.md>) — Angular.
- [Angular hydration: verify the source of restored state](<resources/angular-2026-hydration-state-source-authenticity.md>) — Angular maintainers.
- [Angular SSR: preserve output context through serialization and post-processing](<resources/angular-2026-raw-content-serialization-context.md>) — Angular.
- [Astro: composable dispatch must preserve mandatory origin checks](<resources/astro-2026-composable-dispatch-origin-enforcement.md>) — Astro.
- [Astro: routing and authorization must agree on resource identity](<resources/astro-2026-route-normalization-authorization-consistency.md>) — Astro.
- [authentik: source-mapping edits carry identity-rebinding authority](<resources/authentik-2026-source-mapping-mutation-authority.md>) — authentik.
- [Authlib: error responses must preserve redirect-destination validation](<resources/authlib-2026-error-path-redirect-authority.md>) — Authlib.
- [Axios: enforce upload budgets across transport implementations](<resources/axios-2026-streamed-upload-budget-enforcement.md>) — Axios.
- [Axios: URL construction does not establish destination authority](<resources/axios-2025-base-url-destination-authority.md>) — Axios.
- [Better Auth SCIM: absent ownership must not grant shared authority](<resources/better-auth-2026-scim-ownerless-provider-authority.md>) — Better Auth.
- [Better Auth: incoming identity proof does not validate existing credentials](<resources/better-auth-2026-local-account-linking-verification.md>) — Better Auth.
- [Better Auth: single-use authorization requires atomic state consumption](<resources/better-auth-2026-authorization-code-consumption-integrity.md>) — Better Auth.
- [Bugsink: time-unit consistency in account-access token expiry](<resources/bugsink-2026-token-expiry-unit-integrity.md>) — Bugsink.
- [CI4MS: keep stored diagnostic content inert in administrative log views](<resources/ci4ms-2026-log-viewer-stored-blind-xss-boundary.md>) — CI4MS maintainers.
- [Coder: privileged provisioning must preserve existing object ownership](<resources/coder-2026-provisioned-object-ownership-integrity.md>) — Coder.
- [Directus: denied mutations must leave dependent state unchanged](<resources/directus-2026-preauthorization-side-effect-integrity.md>) — Directus.
- [Django: ORM alias metadata must not acquire query authority](<resources/django-2026-query-alias-structure-boundary.md>) — Django Software Foundation.
- [DOMPurify: accepted DOM realms must retain complete sanitization](<resources/dompurify-2026-cross-realm-sanitization-consistency.md>) — DOMPurify / Cure53.
- [File Browser: existing shares must follow current owner permissions](<resources/filebrowser-2026-share-owner-permission-lifecycle.md>) — File Browser.
- [Formie: integration settings need operation and attribute authority](<resources/formie-2026-integration-settings-credential-authority.md>) — Verbb / Formie.
- [Grav API: account-disable enforcement across session authenticators](<resources/grav-2026-session-account-state-revalidation.md>) — Grav.
- [HotCRP: separate submission visibility from authorship authority](<resources/hotcrp-2026-contact-authorship-permission-boundary.md>) — HotCRP.
- [Jupyter Enterprise Gateway: keep kernel configuration outside template authority](<resources/jupyter-enterprise-gateway-2026-kernel-configuration-template-boundary.md>) — Jupyter Enterprise Gateway maintainers.
- [Langflow: project transport authorization must reach each resource read](<resources/langflow-2026-mcp-resource-project-authorization.md>) — Langflow.
- [LibreChat: agent edit authority must cover attached context](<resources/librechat-2026-agent-context-mutation-authority.md>) — LibreChat.
- [LibreChat: delegated credentials must remain bound to the initiating session](<resources/librechat-2026-mcp-oauth-session-binding.md>) — LibreChat.
- [LibreChat: viewing an integration must not reveal its service secrets](<resources/librechat-2026-mcp-view-secret-projection.md>) — LibreChat.
- [LobeHub: knowledge-base membership changes require ownership authorization](<resources/lobehub-2026-knowledge-membership-mutation-authority.md>) — LobeHub.
- [mailcow: stored configuration retains its original trust level](<resources/mailcow-2026-persisted-data-query-boundary.md>) — mailcow.
- [MLflow: destination validation must remain bound to the actual connection](<resources/mlflow-2026-webhook-connection-destination-integrity.md>) — MLflow.
- [MythicalDash: payment evidence must establish credit entitlement](<resources/mythicaldash-2026-payment-evidence-entitlement.md>) — MythicalDash.
- [n8n Dynamic Credentials: authorize credential lifecycle operations](<resources/n8n-2026-dynamic-credential-object-authority.md>) — n8n.
- [n8n token exchange: preserve the issuer namespace](<resources/n8n-2026-external-identity-issuer-binding.md>) — n8n.
- [n8n: directory-attribute authority in durable account linking](<resources/n8n-2026-ldap-account-linking-authority.md>) — n8n.
- [n8n: refreshed authority must remain bound to the consented resource](<resources/n8n-2026-refresh-grant-resource-binding.md>) — n8n.
- [Nhost: provider adapters must preserve identity-claim evidence](<resources/nhost-2026-provider-claim-verification-provenance.md>) — Nhost.
- [Nuxt: island data must not acquire component-selection authority](<resources/nuxt-2026-island-component-selection-authority.md>) — Nuxt.
- [Nuxt: rendered-data caches must preserve request authorization](<resources/nuxt-2026-rendered-payload-cache-authorization.md>) — Nuxt.
- [OAuth2 Proxy: client-address provenance must precede authentication exemptions](<resources/oauth2-proxy-2026-client-address-provenance-authority.md>) — OAuth2 Proxy.
- [Obot: preserve delegated token audience and consent boundaries](<resources/obot-2026-oauth-audience-and-consent-boundaries.md>) — Obot.
- [Open WebUI: credentials must bind to their destination connection](<resources/open-webui-2026-connection-credential-capture.md>) — Open WebUI.
- [Open WebUI: preserve role-policy meaning across identity flows](<resources/open-webui-2026-role-claim-provenance-and-revocation.md>) — Open WebUI.
- [Open WebUI: revocation must cross HTTP and realtime boundaries](<resources/open-webui-2026-realtime-revocation-consistency.md>) — Open WebUI.
- [OpenFGA: policy intersections must preserve explicit exclusions](<resources/openfga-2026-composed-policy-exclusion-integrity.md>) — OpenFGA.
- [Outline: integration authority must end with its owning account](<resources/outline-2026-webhook-revocation-lifecycle.md>) — Outline.
- [Parse Server: preserve safe file interpretation across storage and browsers](<resources/parse-server-2026-upload-metadata-consumer-boundary.md>) — Parse Community.
- [Payload: request adapters must retain caller-level authorization](<resources/payload-2026-local-api-caller-authority.md>) — jhb-software / Payload plugins.
- [Paymenter: refund entitlement and ledger changes need one atomic transition](<resources/paymenter-2026-refund-transition-atomicity.md>) — Paymenter.
- [Prowler SAML: retain validated tenant authority](<resources/prowler-2026-saml-tenant-issuance-binding.md>) — Prowler.
- [Pterodactyl: delegated tokens must preserve action-specific authority](<resources/pterodactyl-2026-delegated-token-purpose-binding.md>) — Pterodactyl.
- [pypdf: bound repeated work when reading embedded attachments](<resources/pypdf-2026-attachment-processing-cost-boundary.md>) — py-pdf / pypdf.
- [Qwik: resumability metadata must preserve HTML serialization boundaries](<resources/qwik-2026-resumability-comment-serialization-boundary.md>) — QwikDev.
- [React Router: hydrated error metadata must not select client behavior](<resources/react-router-2026-hydration-error-constructor-boundary.md>) — React Router / Remix.
- [Saleor email changes: bind confirmation to account and state](<resources/saleor-2026-email-change-confirmation-binding.md>) — Saleor maintainers.
- [samlify: signing does not establish claim provenance](<resources/samlify-2026-assertion-generation-claim-integrity.md>) — samlify.
- [Serialize JavaScript: every serialized field must retain data semantics](<resources/serialize-javascript-2026-output-code-boundary.md>) — Yahoo serialize-javascript.
- [Spree: cart association must retain guest-possession checks](<resources/spree-2026-guest-cart-association-authority.md>) — Spree.
- [Steeltoe: diagnostic URI masking must cover the complete data contract](<resources/steeltoe-2026-diagnostic-uri-data-minimization.md>) — Steeltoe.
- [Sylius: order ownership does not confer payment-operation authority](<resources/sylius-2026-payment-action-authority.md>) — Sylius.
- [Sylius: promotion entitlement must be checked and consumed atomically](<resources/sylius-2026-promotion-limit-atomicity.md>) — Sylius.
- [TanStack Start: preserve server-owned response authority through errors](<resources/tanstack-2026-server-function-response-authority.md>) — TanStack.
- [Trix: validate stored attachment data before link interpretation](<resources/trix-2025-attachment-link-interpretation-boundary.md>) — Trix maintainers.
- [TYPO3: configured upload policy must reach the runtime validator](<resources/typo3-2026-upload-validator-lifecycle-boundary.md>) — TYPO3.
- [Uptime Kuma: separate notification-template authority from server files](<resources/uptime-kuma-2025-notification-template-file-boundary.md>) — Uptime Kuma maintainers.
- [Vendure: payment child objects must inherit order channel authority](<resources/vendure-2026-payment-child-object-channel-authority.md>) — Vendure.
- [Vercel React Router: session identity must not select unrestricted storage authority](<resources/vercel-react-router-2026-session-storage-key-authority.md>) — Vercel.
- [Vikunja: saved favorites must recheck current project access](<resources/vikunja-2026-favorites-current-access-revalidation.md>) — Vikunja.
- [Vite: local reachability does not establish browser-origin authority](<resources/vite-2025-development-server-origin-authority.md>) — Vite.
- [Vvveb: numeric input validity does not establish legitimate order state](<resources/vvveb-2026-order-domain-invariant.md>) — Vvveb.

<a id="type-reporting-guide"></a>
## Reporting Guide

2 resources.

- [Quality Reports](<resources/hackerone-quality-vulnerability-reports.md>) — HackerOne Help Center.
- [What is a security vulnerability?](<resources/google-understanding-security-vulnerability-reports.md>) — Google Bug Hunters.

<a id="type-research-paper"></a>
## Research Paper

26 resources.

- [Adversarial passkeys: account recovery must close every continuing source of authority](<resources/usenix-2026-passkey-remediation-authority-lifecycle.md>) — USENIX Association.
- [Claude Cowork: approved destinations need account and operation binding](<resources/anthropic-2026-egress-capability-identity-binding.md>) — Anthropic.
- [Cross-device authentication: bind informed consent to session authority](<resources/ndss-2026-cross-device-consent-and-session-control.md>) — Internet Society / NDSS Symposium.
- [Dify: telemetry destination changes carry tenant data-disclosure authority](<resources/dify-2026-tracing-configuration-tenant-authority.md>) — Zafran Labs.
- [Dolibarr portal accounts: credential writes need object authorization](<resources/dolibarr-2026-portal-object-authorization.md>) — CodeAnt AI.
- [Frappe: linked data must preserve document and field permissions](<resources/frappe-2026-linked-document-response-authorization.md>) — GitHub Security Lab.
- [GitHub internal metadata: preserve the boundary between user data and service authority](<resources/github-2026-internal-metadata-authority.md>) — Wiz Research.
- [GraphQL-Ruby: authorization exceptions must stop execution](<resources/graphql-ruby-2026-authorization-exception-integrity.md>) — GitHub Security Lab.
- [Laravel: preserve output encoding in debug diagnostics](<resources/laravel-2025-debug-diagnostic-output-encoding.md>) — SBA Research.
- [MLflow: authorization must survive alternate resource interfaces](<resources/mlflow-2026-alternate-interface-authorization-consistency.md>) — Tachyon.
- [Next\.js: response metadata must preserve representation boundaries](<resources/nextjs-2026-response-metadata-representation-boundary.md>) — zhero\_web\_security.
- [pac4j JWT validation: confidentiality does not establish authenticity](<resources/pac4j-2026-token-authenticity-enforcement.md>) — CodeAnt AI.
- [Rocket\.Chat: authentication must await a completed verification decision](<resources/rocketchat-2026-asynchronous-identity-verification.md>) — GitHub Security Lab.
- [SearchLeak: streamed output needs policy enforcement before browser activation](<resources/microsoft-copilot-2026-streaming-output-activation-boundary.md>) — Varonis Threat Labs.
- [Sentry: resource ownership must match the authorized organization](<resources/sentry-2026-organization-object-authorization.md>) — GitHub Security Lab.
- [ServiceNow: agent discovery expands the delegated authority boundary](<resources/servicenow-2025-agent-discovery-delegation-authority.md>) — AppOmni AO Labs.
- [Spree: guest ownership still requires an authorization proof](<resources/spree-2026-guest-order-authorization-proof.md>) — GitHub Security Lab.
- [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](<resources/usenix-2025-tls-resumption-identity-isolation.md>) — USENIX Association.
- [Svelte hydration: serialization must preserve the enclosing output context](<resources/svelte-2026-hydration-output-context-boundary.md>) — Camilo Vera.
- [SvelteKit: origin construction and routing must preserve server request authority](<resources/sveltekit-2026-origin-routing-trust-boundary.md>) — zhero\_web\_security.
- [Sylius: component integrity does not authorize referenced objects](<resources/sylius-2026-component-argument-object-authorization.md>) — GitHub Security Lab.
- [Umbraco: editing an account does not authorize assigning every role](<resources/umbraco-2026-group-assignment-authority.md>) — GitHub Security Lab.
- [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<resources/usenix-2025-integration-platform-oauth-bindings.md>) — USENIX Association.
- [Upstream HTTP framing and parser-consistency boundaries](<resources/portswigger-2025-upstream-http-framing-boundaries.md>) — PortSwigger.
- [Web cache key precision and capacity isolation](<resources/arxiv-2026-cache-key-precision-and-capacity.md>) — arXiv.
- [Zammad: overridden serialization must preserve group authorization](<resources/zammad-2026-asset-serialization-group-authorization.md>) — GitHub Security Lab.

<a id="type-security-standard"></a>
## Security Standard

2 resources.

- [OWASP Application Security Verification Standard \(ASVS\)](<resources/owasp-asvs-5-security-verification-standard.md>) — OWASP Foundation.
- [SLSA v1\.2: supply-chain security and build provenance](<resources/slsa-v1-2-supply-chain-build-provenance.md>) — SLSA Community.

<a id="type-technical-standard"></a>
## Technical Standard

9 resources.

- [FAPI 2\.0 Security Profile](<resources/openid-fapi-2-api-authorization-profile.md>) — OpenID Foundation.
- [Fetch Metadata Request Headers](<resources/w3c-fetch-metadata-request-context-boundaries.md>) — World Wide Web Consortium.
- [HTML COOP: opener separation and same-origin authority](<resources/whatwg-coop-opener-and-origin-authority.md>) — WHATWG.
- [MCP elicitation: consent, credential custody and completion](<resources/mcp-elicitation-consent-credential-custody.md>) — Model Context Protocol.
- [Permissions Policy: inherited browser-feature authority across embedded documents](<resources/w3c-permissions-policy-embedded-feature-authority.md>) — World Wide Web Consortium.
- [RFC 10017: OAuth 2\.0 for Browser-Based Applications](<resources/rfc-10017-browser-oauth-token-custody.md>) — Internet Engineering Task Force / RFC Editor.
- [RFC 9700: Best Current Practice for OAuth 2\.0 Security](<resources/rfc-9700-oauth-security-best-current-practice.md>) — Internet Engineering Task Force / RFC Editor.
- [Storage Access API: permission, document activation and cookie eligibility](<resources/privacycg-storage-access-permission-activation-boundary.md>) — Privacy Community Group.
- [Trusted Types: typed sinks depend on trustworthy policy creation](<resources/w3c-2026-trusted-types-policy-authority.md>) — World Wide Web Consortium.

<a id="type-training-lab"></a>
## Training Lab

6 resources.

- [CyLab Security Academy: Self-Paced CTF Learning](<resources/cylab-security-academy-ctf-practice.md>) — Carnegie Mellon University.
- [OverTheWire Bandit: Unix/Linux Foundations](<resources/overthewire-bandit-unix-foundations.md>) — OverTheWire.
- [OverTheWire Natas: Server-Side Web Security Practice](<resources/overthewire-natas-web-security-practice.md>) — OverTheWire.
- [OWASP Juice Shop: Controlled Web-Security Training](<resources/owasp-juice-shop-controlled-training.md>) — OWASP Foundation.
- [OWASP WebGoat: Web-Application Security Lessons](<resources/owasp-webgoat-controlled-training.md>) — OWASP Foundation.
- [Web Security Academy: Free Online Training from PortSwigger](<resources/portswigger-web-security-academy-controlled-training.md>) — PortSwigger.
