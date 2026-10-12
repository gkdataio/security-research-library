# Browse by defensive skill

[Reports](reports.md) · [Learning resources](resource-index.md) · [Resource types](resource-types.md) · [Publication years](publication-years.md) · [Library home](../README.md)

67 distinct award-backed reports and 155 distinct educational resources across 22 defensive skills. A record can appear under several skills; overlapping memberships must not be added to count records.

Skills are editorial learning objectives from the existing taxonomy, not certifications, new vulnerability classifications or permission to test. Reports and learning references remain separate. Empty skill groups remain visible; regeneration preserves review timestamps.

## Browse skills

- [Learn through controlled practice](<#skill-controlled-practice>) — 0 reports; 6 resources.
- [Model access-control invariants](<#skill-authorization-modeling>) — 31 reports; 70 resources.
- [Model build and release trust](<#skill-pipeline-trust-modeling>) — 5 reports; 4 resources.
- [Reason about concurrent state](<#skill-concurrency-reasoning>) — 6 reports; 14 resources.
- [Review AI authority boundaries](<#skill-ai-authority-boundaries>) — 6 reports; 15 resources.
- [Review approval-state integrity](<#skill-approval-state-integrity>) — 8 reports; 11 resources.
- [Review artifact isolation](<#skill-cache-artifact-isolation>) — 1 reports; 5 resources.
- [Review client isolation](<#skill-browser-isolation-review>) — 11 reports; 15 resources.
- [Review cloud IAM boundaries](<#skill-cloud-iam-review>) — 6 reports; 3 resources.
- [Review dependency provenance](<#skill-dependency-provenance>) — 1 reports; 4 resources.
- [Review identity lifecycle](<#skill-identity-lifecycle-review>) — 17 reports; 36 resources.
- [Review input trust boundaries](<#skill-untrusted-input-handling>) — 20 reports; 45 resources.
- [Review machine identities](<#skill-machine-identity-governance>) — 4 reports; 2 resources.
- [Review memory-safety assumptions](<#skill-memory-safety-review>) — 10 reports; 4 resources.
- [Review parsing and serialization](<#skill-secure-parser-review>) — 17 reports; 28 resources.
- [Review secrets containment](<#skill-secrets-containment>) — 10 reports; 13 resources.
- [Review secure error behavior](<#skill-error-response-design>) — 2 reports; 8 resources.
- [Review security-token design](<#skill-security-token-design>) — 6 reports; 15 resources.
- [Review text-encoding invariants](<#skill-encoding-invariant-review>) — 1 reports; 3 resources.
- [Threat-model integrations](<#skill-integration-threat-modeling>) — 36 reports; 62 resources.
- [Verify remediation evidence](<#skill-patch-verification>) — 26 reports; 77 resources.
- [Write bounded security evidence](<#skill-defensive-evidence-writing>) — 37 reports; 18 resources.

<a id="skill-controlled-practice"></a>
## Learn through controlled practice

Plan and document exercises in provider-designated or isolated learning environments, then explain the security boundary and defensive lesson without extending activity to unrelated systems.

### Award-backed reports

0 records.

No records currently assigned.

### Educational resources

6 records.

- [CyLab Security Academy: Self-Paced CTF Learning](<resources/cylab-security-academy-ctf-practice.md>)
- [OverTheWire Bandit: Unix/Linux Foundations](<resources/overthewire-bandit-unix-foundations.md>)
- [OverTheWire Natas: Server-Side Web Security Practice](<resources/overthewire-natas-web-security-practice.md>)
- [OWASP Juice Shop: Controlled Web-Security Training](<resources/owasp-juice-shop-controlled-training.md>)
- [OWASP WebGoat: Web-Application Security Lessons](<resources/owasp-webgoat-controlled-training.md>)
- [Web Security Academy: Free Online Training from PortSwigger](<resources/portswigger-web-security-academy-controlled-training.md>)

<a id="skill-authorization-modeling"></a>
## Model access-control invariants

Document expected actor, action, resource, and tenant relationships in an authorized design review.

### Award-backed reports

31 records.

- [Facebook phone linking lacked account-specific authorization](<reports/facebook-phone-linking-account-authorization-2013.md>)
- [Framework serialization change exposed private HackerOne user attributes](<reports/hackerone-report-json-serialization-data-exposure-2025.md>)
- [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](<reports/google-gemini-enterprise-connected-content-memory-integrity-2026.md>)
- [GitHub Actions trust depended on invalid repository references](<reports/github-actions-reference-validation-2021.md>)
- [GitHub comparison output lacked source-repository authorization](<reports/github-cross-repository-comparison-authorization-2025.md>)
- [GitHub fork collaboration applied inconsistent authorization](<reports/github-fork-collaboration-authorization-2021.md>)
- [GitHub GraphQL collaboration changes lacked author consent](<reports/github-fork-collaboration-consent-2021.md>)
- [GitHub OAuth consent failed across request-method semantics](<reports/github-oauth-method-semantics-2019.md>)
- [GitLab recovery delivery lacked verified-address binding](<reports/gitlab-recovery-address-binding-cve-2023-7028.md>)
- [Google Application Integration mixed resource and service authority](<reports/google-application-integration-authorization-boundaries-2026.md>)
- [Google device grants lost client and permission binding](<reports/google-device-authorization-client-scope-binding-2026.md>)
- [Google Firefly confused worker authority and storage boundaries](<reports/google-firefly-worker-authority-storage-boundary-2026.md>)
- [Google Mamba temporary outputs lacked access isolation](<reports/google-mamba-temporary-output-isolation-2026.md>)
- [Google support API exposed customer and agent data](<reports/google-support-api-authorization-2026.md>)
- [GraphQL object authorization exposed private-program metadata](<reports/hackerone-private-program-graphql-object-authorization-2025.md>)
- [HackerOne exports omitted internal-attachment authorization](<reports/hackerone-export-attachment-authorization-2016.md>)
- [Instagram client configuration exposed an application credential](<reports/instagram-application-credential-client-containment-2022.md>)
- [Instagram embedding fallback changed the authorization context](<reports/instagram-embedding-privileged-fallback-2023.md>)
- [Instagram mobile account recovery had inconsistent verification limits](<reports/instagram-mobile-recovery-attempt-limits-2019.md>)
- [Instagram recovery challenges were insufficiently bound to accounts](<reports/instagram-recovery-challenge-account-binding-2019.md>)
- [LiteSpeed Cache privileged user simulation relied on weak security tokens](<reports/litespeed-cache-user-simulation-authentication-2024.md>)
- [Meta account verification weakened linked SMS authentication state](<reports/meta-account-verification-attempt-state-binding-2022.md>)
- [Meta AI media access lacked object-ownership authorization](<reports/meta-ai-media-object-authorization-2025.md>)
- [Meta Pixel cross-window handling lost message and token authority](<reports/meta-pixel-cross-window-authority-binding-2024.md>)
- [Microsoft account recovery lacked consistent attempt-limit enforcement](<reports/microsoft-account-recovery-rate-limit-consistency-2021.md>)
- [Redis Lua object lifetime failure crossed the scripting boundary](<reports/redis-lua-object-lifetime-isolation-2025.md>)
- [Shopify automatic account conversion lost merchant-consent binding](<reports/shopify-collaborator-conversion-consent-2017.md>)
- [Sign in with Apple failed to bind identity claims to the authenticated user](<reports/apple-sign-in-identity-claim-binding-2020.md>)
- [Support integration exposed internal Confluence documentation](<reports/hackerone-support-confluence-access-boundary-2025.md>)
- [YouTube and Pixel Recorder exposed cross-product identity links](<reports/youtube-pixel-recorder-identity-privacy-2025.md>)
- [YouTube creator metadata exposed private email addresses](<reports/youtube-creator-email-authorization-2025.md>)

### Educational resources

70 records.

- [Apollo Federation: preserving the router-to-subgraph boundary](<resources/apollo-2026-federation-router-subgraph-isolation.md>)
- [Astro: composable dispatch must preserve mandatory origin checks](<resources/astro-2026-composable-dispatch-origin-enforcement.md>)
- [Astro: routing and authorization must agree on resource identity](<resources/astro-2026-route-normalization-authorization-consistency.md>)
- [authentik: source-mapping edits carry identity-rebinding authority](<resources/authentik-2026-source-mapping-mutation-authority.md>)
- [Authlib: error responses must preserve redirect-destination validation](<resources/authlib-2026-error-path-redirect-authority.md>)
- [Authorization Cheat Sheet](<resources/owasp-authorization-cheat-sheet.md>)
- [Better Auth SCIM: absent ownership must not grant shared authority](<resources/better-auth-2026-scim-ownerless-provider-authority.md>)
- [Chrome Local Network Access: separate browser reachability from site authority](<resources/chrome-local-network-permission-boundaries.md>)
- [Claude Cowork: approved destinations need account and operation binding](<resources/anthropic-2026-egress-capability-identity-binding.md>)
- [Coder: privileged provisioning must preserve existing object ownership](<resources/coder-2026-provisioned-object-ownership-integrity.md>)
- [Dify: telemetry destination changes carry tenant data-disclosure authority](<resources/dify-2026-tracing-configuration-tenant-authority.md>)
- [Directus: denied mutations must leave dependent state unchanged](<resources/directus-2026-preauthorization-side-effect-integrity.md>)
- [Dolibarr portal accounts: credential writes need object authorization](<resources/dolibarr-2026-portal-object-authorization.md>)
- [FAPI 2\.0 Security Profile](<resources/openid-fapi-2-api-authorization-profile.md>)
- [File Browser: existing shares must follow current owner permissions](<resources/filebrowser-2026-share-owner-permission-lifecycle.md>)
- [Formie: integration settings need operation and attribute authority](<resources/formie-2026-integration-settings-credential-authority.md>)
- [Frappe: linked data must preserve document and field permissions](<resources/frappe-2026-linked-document-response-authorization.md>)
- [Google AIP-158: pagination continuation does not grant resource authority](<resources/google-aip-158-pagination-authorization-boundary.md>)
- [Google API field masks: preserve server-owned and immutable state](<resources/google-aip-161-update-field-authority.md>)
- [GraphQL-Ruby: authorization exceptions must stop execution](<resources/graphql-ruby-2026-authorization-exception-integrity.md>)
- [Grav API: account-disable enforcement across session authenticators](<resources/grav-2026-session-account-state-revalidation.md>)
- [HotCRP: separate submission visibility from authorship authority](<resources/hotcrp-2026-contact-authorship-permission-boundary.md>)
- [HTML5 Security Cheat Sheet: Web Messaging](<resources/owasp-browser-message-trust-boundaries.md>)
- [Langflow: project transport authorization must reach each resource read](<resources/langflow-2026-mcp-resource-project-authorization.md>)
- [LibreChat: agent edit authority must cover attached context](<resources/librechat-2026-agent-context-mutation-authority.md>)
- [LibreChat: delegated credentials must remain bound to the initiating session](<resources/librechat-2026-mcp-oauth-session-binding.md>)
- [LibreChat: viewing an integration must not reveal its service secrets](<resources/librechat-2026-mcp-view-secret-projection.md>)
- [LobeHub: knowledge-base membership changes require ownership authorization](<resources/lobehub-2026-knowledge-membership-mutation-authority.md>)
- [MCP scope selection: progressive consent and accumulated authority](<resources/mcp-progressive-scope-authority.md>)
- [Microsoft Graph batching: preserve each member authorization outcome](<resources/microsoft-graph-batch-member-authorization-outcomes.md>)
- [MLflow: authorization must survive alternate resource interfaces](<resources/mlflow-2026-alternate-interface-authorization-consistency.md>)
- [n8n Dynamic Credentials: authorize credential lifecycle operations](<resources/n8n-2026-dynamic-credential-object-authority.md>)
- [n8n token exchange: preserve the issuer namespace](<resources/n8n-2026-external-identity-issuer-binding.md>)
- [n8n: directory-attribute authority in durable account linking](<resources/n8n-2026-ldap-account-linking-authority.md>)
- [n8n: refreshed authority must remain bound to the consented resource](<resources/n8n-2026-refresh-grant-resource-binding.md>)
- [Next\.js data security: server authorization and client-visible data](<resources/nextjs-server-client-data-security.md>)
- [NIST SP 800-162: attribute authority and policy traceability](<resources/nist-sp-800-162-attribute-authority-modeling.md>)
- [Nuxt: island data must not acquire component-selection authority](<resources/nuxt-2026-island-component-selection-authority.md>)
- [Nuxt: rendered-data caches must preserve request authorization](<resources/nuxt-2026-rendered-payload-cache-authorization.md>)
- [OAuth2 Proxy: client-address provenance must precede authentication exemptions](<resources/oauth2-proxy-2026-client-address-provenance-authority.md>)
- [Obot: preserve delegated token audience and consent boundaries](<resources/obot-2026-oauth-audience-and-consent-boundaries.md>)
- [Open WebUI: preserve role-policy meaning across identity flows](<resources/open-webui-2026-role-claim-provenance-and-revocation.md>)
- [OpenFGA query consistency: authorization decisions need sufficiently fresh state](<resources/openfga-authorization-query-freshness.md>)
- [OpenFGA: policy intersections must preserve explicit exclusions](<resources/openfga-2026-composed-policy-exclusion-integrity.md>)
- [Outline: integration authority must end with its owning account](<resources/outline-2026-webhook-revocation-lifecycle.md>)
- [OWASP Application Security Verification Standard \(ASVS\)](<resources/owasp-asvs-5-security-verification-standard.md>)
- [OWASP Juice Shop: Controlled Web-Security Training](<resources/owasp-juice-shop-controlled-training.md>)
- [OWASP LLM08:2025: retrieval permissions and knowledge provenance](<resources/owasp-rag-retrieval-permission-boundaries.md>)
- [OWASP Secure Code Review: baseline and change-focused review](<resources/owasp-secure-code-review-methodology.md>)
- [OWASP Session Management: privilege-transition integrity](<resources/owasp-session-privilege-transition-integrity.md>)
- [OWASP Threat Modeling: system assumptions and mitigation validation](<resources/owasp-threat-modeling-assumptions-and-validation.md>)
- [OWASP Transaction Authorization](<resources/owasp-transaction-authorization-state-integrity.md>)
- [Payload: request adapters must retain caller-level authorization](<resources/payload-2026-local-api-caller-authority.md>)
- [Prowler SAML: retain validated tenant authority](<resources/prowler-2026-saml-tenant-issuance-binding.md>)
- [Pterodactyl: delegated tokens must preserve action-specific authority](<resources/pterodactyl-2026-delegated-token-purpose-binding.md>)
- [RFC 9700: Best Current Practice for OAuth 2\.0 Security](<resources/rfc-9700-oauth-security-best-current-practice.md>)
- [Saleor email changes: bind confirmation to account and state](<resources/saleor-2026-email-change-confirmation-binding.md>)
- [Sentry: resource ownership must match the authorized organization](<resources/sentry-2026-organization-object-authorization.md>)
- [ServiceNow: agent discovery expands the delegated authority boundary](<resources/servicenow-2025-agent-discovery-delegation-authority.md>)
- [Spree: cart association must retain guest-possession checks](<resources/spree-2026-guest-cart-association-authority.md>)
- [Spree: guest ownership still requires an authorization proof](<resources/spree-2026-guest-order-authorization-proof.md>)
- [Sylius: component integrity does not authorize referenced objects](<resources/sylius-2026-component-argument-object-authorization.md>)
- [Sylius: order ownership does not confer payment-operation authority](<resources/sylius-2026-payment-action-authority.md>)
- [Umbraco: editing an account does not authorize assigning every role](<resources/umbraco-2026-group-assignment-authority.md>)
- [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<resources/usenix-2025-integration-platform-oauth-bindings.md>)
- [Vendure: payment child objects must inherit order channel authority](<resources/vendure-2026-payment-child-object-channel-authority.md>)
- [Vercel React Router: session identity must not select unrestricted storage authority](<resources/vercel-react-router-2026-session-storage-key-authority.md>)
- [Vikunja: saved favorites must recheck current project access](<resources/vikunja-2026-favorites-current-access-revalidation.md>)
- [Web Security Academy: Free Online Training from PortSwigger](<resources/portswigger-web-security-academy-controlled-training.md>)
- [Zammad: overridden serialization must preserve group authorization](<resources/zammad-2026-asset-serialization-group-authorization.md>)

<a id="skill-pipeline-trust-modeling"></a>
## Model build and release trust

Map trusted and untrusted inputs, artifacts, jobs, and identity boundaries in approved architecture diagrams.

### Award-backed reports

5 records.

- [Angular automation trust and cache isolation weakness](<reports/angular-ci-cache-trust-2026.md>)
- [Cloud Build approval was not bound to immutable code](<reports/google-cloud-build-approval-toctou-2025.md>)
- [GitHub Actions trust depended on invalid repository references](<reports/github-actions-reference-validation-2021.md>)
- [GitHub package-source trust allowed dependency confusion](<reports/github-ruby-dependency-confusion-2025.md>)
- [GitHub runner-image builds shared persistent infrastructure with untrusted workflows](<reports/github-runner-image-build-isolation-2023.md>)

### Educational resources

4 records.

- [GitHub Artifact Attestations: Provenance and Consumer Policy](<resources/github-artifact-attestations.md>)
- [NIST SSDF 1\.1: Component Governance and Release Provenance](<resources/nist-ssdf-1-1-dependency-governance.md>)
- [Sigstore Security Model](<resources/sigstore-security-model.md>)
- [SLSA v1\.2: supply-chain security and build provenance](<resources/slsa-v1-2-supply-chain-build-provenance.md>)

<a id="skill-concurrency-reasoning"></a>
## Reason about concurrent state

Model ordering assumptions and prove security invariants with local state-machine or unit tests.

### Award-backed reports

6 records.

- [Cloud Build approval was not bound to immutable code](<reports/google-cloud-build-approval-toctou-2025.md>)
- [Instagram mobile account recovery had inconsistent verification limits](<reports/instagram-mobile-recovery-attempt-limits-2019.md>)
- [Instagram recovery challenges were insufficiently bound to accounts](<reports/instagram-recovery-challenge-account-binding-2019.md>)
- [Microsoft account recovery lacked consistent attempt-limit enforcement](<reports/microsoft-account-recovery-rate-limit-consistency-2021.md>)
- [Pixel lock-screen completion lost security-state binding](<reports/google-pixel-lock-screen-state-binding-2022.md>)
- [Redis replication state changes invalidated an active interpreter](<reports/redis-replication-interpreter-lifetime-2026.md>)

### Educational resources

14 records.

- [Better Auth: single-use authorization requires atomic state consumption](<resources/better-auth-2026-authorization-code-consumption-integrity.md>)
- [Google API request identity: bind retry semantics to the logical operation](<resources/google-aip-155-request-identity-contract.md>)
- [Google long-running operations: cancellation requests and completion evidence](<resources/google-aip-151-operation-completion-integrity.md>)
- [Microsoft compensating transactions: recovery must preserve valid concurrent state](<resources/microsoft-compensating-transaction-state-integrity.md>)
- [OpenFGA query consistency: authorization decisions need sufficiently fresh state](<resources/openfga-authorization-query-freshness.md>)
- [OWASP Forgot Password](<resources/owasp-account-recovery-state-integrity.md>)
- [OWASP Transaction Authorization](<resources/owasp-transaction-authorization-state-integrity.md>)
- [Paymenter: refund entitlement and ledger changes need one atomic transition](<resources/paymenter-2026-refund-transition-atomicity.md>)
- [PostgreSQL 18: Transaction Isolation and Business Invariants](<resources/postgresql-transaction-isolation-business-invariants.md>)
- [Rocket\.Chat: authentication must await a completed verification decision](<resources/rocketchat-2026-asynchronous-identity-verification.md>)
- [SearchLeak: streamed output needs policy enforcement before browser activation](<resources/microsoft-copilot-2026-streaming-output-activation-boundary.md>)
- [Stripe webhooks: authentic delivery and business-state integrity](<resources/stripe-webhook-delivery-state-integrity.md>)
- [Sylius: promotion entitlement must be checked and consumed atomically](<resources/sylius-2026-promotion-limit-atomicity.md>)
- [Web Security Academy: Free Online Training from PortSwigger](<resources/portswigger-web-security-academy-controlled-training.md>)

<a id="skill-ai-authority-boundaries"></a>
## Review AI authority boundaries

Assess least privilege and independent validation at tool execution and data disclosure boundaries.

### Award-backed reports

6 records.

- [Bard Workspace integration weakened output-data boundaries](<reports/google-bard-workspace-output-boundary-2024.md>)
- [Codex automated Git operations trusted repository hook settings](<reports/openai-codex-repository-hook-execution-trust-2026.md>)
- [Codex command approval relied on inconsistent parser semantics](<reports/openai-codex-command-parser-approval-consistency-2026.md>)
- [Codex metadata collection trusted repository execution helpers](<reports/openai-codex-repository-metadata-helper-trust-2026.md>)
- [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](<reports/google-gemini-enterprise-connected-content-memory-integrity-2026.md>)
- [Gemini-to-Colab rendering boundary exposed Workspace data](<reports/google-gemini-colab-rendering-boundary-2025.md>)

### Educational resources

15 records.

- [Claude Cowork: approved destinations need account and operation binding](<resources/anthropic-2026-egress-capability-identity-binding.md>)
- [Dify: telemetry destination changes carry tenant data-disclosure authority](<resources/dify-2026-tracing-configuration-tenant-authority.md>)
- [Langflow: project transport authorization must reach each resource read](<resources/langflow-2026-mcp-resource-project-authorization.md>)
- [LibreChat: agent edit authority must cover attached context](<resources/librechat-2026-agent-context-mutation-authority.md>)
- [LibreChat: delegated credentials must remain bound to the initiating session](<resources/librechat-2026-mcp-oauth-session-binding.md>)
- [LibreChat: viewing an integration must not reveal its service secrets](<resources/librechat-2026-mcp-view-secret-projection.md>)
- [LLM Prompt Injection Prevention Cheat Sheet](<resources/owasp-llm-prompt-injection-prevention.md>)
- [LobeHub: knowledge-base membership changes require ownership authorization](<resources/lobehub-2026-knowledge-membership-mutation-authority.md>)
- [MCP elicitation: consent, credential custody and completion](<resources/mcp-elicitation-consent-credential-custody.md>)
- [MCP scope selection: progressive consent and accumulated authority](<resources/mcp-progressive-scope-authority.md>)
- [OWASP LLM05:2025: generated-output consumer trust](<resources/owasp-llm-output-consumer-trust.md>)
- [OWASP LLM08:2025: retrieval permissions and knowledge provenance](<resources/owasp-rag-retrieval-permission-boundaries.md>)
- [OWASP LLM09:2026: embedding confidentiality and storage lifecycle](<resources/owasp-2026-embedding-confidentiality-lifecycle.md>)
- [SearchLeak: streamed output needs policy enforcement before browser activation](<resources/microsoft-copilot-2026-streaming-output-activation-boundary.md>)
- [ServiceNow: agent discovery expands the delegated authority boundary](<resources/servicenow-2025-agent-discovery-delegation-authority.md>)

<a id="skill-approval-state-integrity"></a>
## Review approval-state integrity

Check that approval records bind to immutable content and survive state changes safely.

### Award-backed reports

8 records.

- [Angular automation trust and cache isolation weakness](<reports/angular-ci-cache-trust-2026.md>)
- [Cloud Build approval was not bound to immutable code](<reports/google-cloud-build-approval-toctou-2025.md>)
- [GitHub fork collaboration applied inconsistent authorization](<reports/github-fork-collaboration-authorization-2021.md>)
- [GitHub GraphQL collaboration changes lacked author consent](<reports/github-fork-collaboration-consent-2021.md>)
- [GitHub OAuth consent failed across request-method semantics](<reports/github-oauth-method-semantics-2019.md>)
- [GitHub runner-image builds shared persistent infrastructure with untrusted workflows](<reports/github-runner-image-build-isolation-2023.md>)
- [iCloud sharing consent and Safari trust boundaries failed together](<reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.md>)
- [Pixel lock-screen completion lost security-state binding](<reports/google-pixel-lock-screen-state-binding-2022.md>)

### Educational resources

11 records.

- [Adversarial passkeys: account recovery must close every continuing source of authority](<resources/usenix-2026-passkey-remediation-authority-lifecycle.md>)
- [Better Auth: single-use authorization requires atomic state consumption](<resources/better-auth-2026-authorization-code-consumption-integrity.md>)
- [Cross-device authentication: bind informed consent to session authority](<resources/ndss-2026-cross-device-consent-and-session-control.md>)
- [Directus: denied mutations must leave dependent state unchanged](<resources/directus-2026-preauthorization-side-effect-integrity.md>)
- [MythicalDash: payment evidence must establish credit entitlement](<resources/mythicaldash-2026-payment-evidence-entitlement.md>)
- [OWASP Transaction Authorization](<resources/owasp-transaction-authorization-state-integrity.md>)
- [Paymenter: refund entitlement and ledger changes need one atomic transition](<resources/paymenter-2026-refund-transition-atomicity.md>)
- [PostgreSQL 18: Transaction Isolation and Business Invariants](<resources/postgresql-transaction-isolation-business-invariants.md>)
- [Sylius: order ownership does not confer payment-operation authority](<resources/sylius-2026-payment-action-authority.md>)
- [Sylius: promotion entitlement must be checked and consumed atomically](<resources/sylius-2026-promotion-limit-atomicity.md>)
- [Vvveb: numeric input validity does not establish legitimate order state](<resources/vvveb-2026-order-domain-invariant.md>)

<a id="skill-cache-artifact-isolation"></a>
## Review artifact isolation

Assess separation of caches and artifacts by trust level, and define integrity controls.

### Award-backed reports

1 records.

- [Angular automation trust and cache isolation weakness](<reports/angular-ci-cache-trust-2026.md>)

### Educational resources

5 records.

- [Angular hydration: verify the source of restored state](<resources/angular-2026-hydration-state-source-authenticity.md>)
- [Next\.js: response metadata must preserve representation boundaries](<resources/nextjs-2026-response-metadata-representation-boundary.md>)
- [Nuxt: rendered-data caches must preserve request authorization](<resources/nuxt-2026-rendered-payload-cache-authorization.md>)
- [SLSA v1\.2: supply-chain security and build provenance](<resources/slsa-v1-2-supply-chain-build-provenance.md>)
- [Web cache key precision and capacity isolation](<resources/arxiv-2026-cache-key-precision-and-capacity.md>)

<a id="skill-browser-isolation-review"></a>
## Review client isolation

Study process, origin, memory-safety, and permission boundaries in patched historical cases.

### Award-backed reports

11 records.

- [Chrome graphics input validation weakened an isolation boundary](<reports/google-chrome-angle-input-validation-2026.md>)
- [Facebook SDK message authentication relied on insecure randomness](<reports/facebook-sdk-message-authentication-randomness-2023.md>)
- [Google IDX worker messaging crossed browser trust boundaries](<reports/google-idx-worker-message-trust-2025.md>)
- [iCloud sharing consent and Safari trust boundaries failed together](<reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.md>)
- [Meta Accounts Center linking lost credential and identity confinement](<reports/meta-accounts-center-linking-credential-confinement-2024.md>)
- [Meta Conversions API Gateway trusted message origins as script authority](<reports/meta-conversions-gateway-message-origin-boundary-2024.md>)
- [Meta Pixel cross-window handling lost message and token authority](<reports/meta-pixel-cross-window-authority-binding-2024.md>)
- [Meta Quest login migration lost OAuth credential confinement](<reports/meta-quest-oauth-redirect-confidentiality-2022.md>)
- [Safari origin confusion undermined stored media permissions](<reports/apple-safari-media-permission-origin-confusion-2020.md>)
- [V8 control-flow analysis omitted required initialization checks](<reports/google-chrome-v8-initialization-checks-2025.md>)
- [V8 optimized object handling retained invalid type assumptions](<reports/google-chrome-v8-type-consistency-2025.md>)

### Educational resources

15 records.

- [Chrome bfcache: restored pages and session-state boundaries](<resources/chrome-bfcache-restored-session-state.md>)
- [Chrome Local Network Access: separate browser reachability from site authority](<resources/chrome-local-network-permission-boundaries.md>)
- [Chromium Rule of Two: input trust, memory safety and privilege](<resources/chromium-rule-of-two-input-isolation.md>)
- [CI4MS: keep stored diagnostic content inert in administrative log views](<resources/ci4ms-2026-log-viewer-stored-blind-xss-boundary.md>)
- [Document Isolation Policy: process separation and residual authority](<resources/chrome-document-isolation-policy-boundaries.md>)
- [Fetch Metadata Request Headers](<resources/w3c-fetch-metadata-request-context-boundaries.md>)
- [HTML COOP: opener separation and same-origin authority](<resources/whatwg-coop-opener-and-origin-authority.md>)
- [HTML5 Security Cheat Sheet: Web Messaging](<resources/owasp-browser-message-trust-boundaries.md>)
- [Permissions Policy: inherited browser-feature authority across embedded documents](<resources/w3c-permissions-policy-embedded-feature-authority.md>)
- [Qwik: resumability metadata must preserve HTML serialization boundaries](<resources/qwik-2026-resumability-comment-serialization-boundary.md>)
- [RFC 10017: OAuth 2\.0 for Browser-Based Applications](<resources/rfc-10017-browser-oauth-token-custody.md>)
- [Storage Access API: permission, document activation and cookie eligibility](<resources/privacycg-storage-access-permission-activation-boundary.md>)
- [Trix: validate stored attachment data before link interpretation](<resources/trix-2025-attachment-link-interpretation-boundary.md>)
- [Trusted Types: typed sinks depend on trustworthy policy creation](<resources/w3c-2026-trusted-types-policy-authority.md>)
- [Vite: local reachability does not establish browser-origin authority](<resources/vite-2025-development-server-origin-authority.md>)

<a id="skill-cloud-iam-review"></a>
## Review cloud IAM boundaries

Compare intended service authority with documented effective permissions and least-privilege requirements.

### Award-backed reports

6 records.

- [Actifio driver execution exposed excessive shared-service authority](<reports/google-actifio-driver-service-identity-isolation-2025.md>)
- [Google Application Integration mixed resource and service authority](<reports/google-application-integration-authorization-boundaries-2026.md>)
- [Google Firefly confused worker authority and storage boundaries](<reports/google-firefly-worker-authority-storage-boundary-2026.md>)
- [Google Mamba temporary outputs lacked access isolation](<reports/google-mamba-temporary-output-isolation-2026.md>)
- [Meta service-identity exposure amplified by excessive secret access](<reports/meta-service-identity-secrets-trust-boundary-2026.md>)
- [Shopify Exchange screenshot service crossed internal boundaries](<reports/shopify-exchange-request-isolation-2019.md>)

### Educational resources

3 records.

- [Authorization Cheat Sheet](<resources/owasp-authorization-cheat-sheet.md>)
- [AWS IAM security best practices for workload identities](<resources/aws-iam-machine-identity-best-practices.md>)
- [Jupyter Enterprise Gateway: keep kernel configuration outside template authority](<resources/jupyter-enterprise-gateway-2026-kernel-configuration-template-boundary.md>)

<a id="skill-dependency-provenance"></a>
## Review dependency provenance

Check explicit registries, namespace ownership, lockfiles, source pinning, and package-origin policy.

### Award-backed reports

1 records.

- [GitHub package-source trust allowed dependency confusion](<reports/github-ruby-dependency-confusion-2025.md>)

### Educational resources

4 records.

- [GitHub Artifact Attestations: Provenance and Consumer Policy](<resources/github-artifact-attestations.md>)
- [NIST SP 800-190: Application Container Security Guide](<resources/nist-sp-800-190-container-isolation-guide.md>)
- [NIST SSDF 1\.1: Component Governance and Release Provenance](<resources/nist-ssdf-1-1-dependency-governance.md>)
- [SLSA v1\.2: supply-chain security and build provenance](<resources/slsa-v1-2-supply-chain-build-provenance.md>)

<a id="skill-identity-lifecycle-review"></a>
## Review identity lifecycle

Assess binding, verification, recovery, linking, and revocation requirements using approved test accounts.

### Award-backed reports

17 records.

- [Facebook phone linking lacked account-specific authorization](<reports/facebook-phone-linking-account-authorization-2013.md>)
- [GitHub OAuth consent failed across request-method semantics](<reports/github-oauth-method-semantics-2019.md>)
- [GitLab recovery delivery lacked verified-address binding](<reports/gitlab-recovery-address-binding-cve-2023-7028.md>)
- [Google device grants lost client and permission binding](<reports/google-device-authorization-client-scope-binding-2026.md>)
- [iCloud sharing consent and Safari trust boundaries failed together](<reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.md>)
- [Instagram mobile account recovery had inconsistent verification limits](<reports/instagram-mobile-recovery-attempt-limits-2019.md>)
- [Instagram recovery challenges were insufficiently bound to accounts](<reports/instagram-recovery-challenge-account-binding-2019.md>)
- [LiteSpeed Cache privileged user simulation relied on weak security tokens](<reports/litespeed-cache-user-simulation-authentication-2024.md>)
- [Meta account verification weakened linked SMS authentication state](<reports/meta-account-verification-attempt-state-binding-2022.md>)
- [Meta Accounts Center linking lost credential and identity confinement](<reports/meta-accounts-center-linking-credential-confinement-2024.md>)
- [Meta Pixel cross-window handling lost message and token authority](<reports/meta-pixel-cross-window-authority-binding-2024.md>)
- [Meta Quest login migration lost OAuth credential confinement](<reports/meta-quest-oauth-redirect-confidentiality-2022.md>)
- [Microsoft account recovery lacked consistent attempt-limit enforcement](<reports/microsoft-account-recovery-rate-limit-consistency-2021.md>)
- [Pixel lock-screen completion lost security-state binding](<reports/google-pixel-lock-screen-state-binding-2022.md>)
- [Safari origin confusion undermined stored media permissions](<reports/apple-safari-media-permission-origin-confusion-2020.md>)
- [Shopify automatic account conversion lost merchant-consent binding](<reports/shopify-collaborator-conversion-consent-2017.md>)
- [Sign in with Apple failed to bind identity claims to the authenticated user](<reports/apple-sign-in-identity-claim-binding-2020.md>)

### Educational resources

36 records.

- [Adversarial passkeys: account recovery must close every continuing source of authority](<resources/usenix-2026-passkey-remediation-authority-lifecycle.md>)
- [authentik: source-mapping edits carry identity-rebinding authority](<resources/authentik-2026-source-mapping-mutation-authority.md>)
- [Authlib: error responses must preserve redirect-destination validation](<resources/authlib-2026-error-path-redirect-authority.md>)
- [AWS IAM security best practices for workload identities](<resources/aws-iam-machine-identity-best-practices.md>)
- [Better Auth SCIM: absent ownership must not grant shared authority](<resources/better-auth-2026-scim-ownerless-provider-authority.md>)
- [Better Auth: incoming identity proof does not validate existing credentials](<resources/better-auth-2026-local-account-linking-verification.md>)
- [Bugsink: time-unit consistency in account-access token expiry](<resources/bugsink-2026-token-expiry-unit-integrity.md>)
- [Chrome bfcache: restored pages and session-state boundaries](<resources/chrome-bfcache-restored-session-state.md>)
- [Cross-device authentication: bind informed consent to session authority](<resources/ndss-2026-cross-device-consent-and-session-control.md>)
- [Dolibarr portal accounts: credential writes need object authorization](<resources/dolibarr-2026-portal-object-authorization.md>)
- [File Browser: existing shares must follow current owner permissions](<resources/filebrowser-2026-share-owner-permission-lifecycle.md>)
- [Grav API: account-disable enforcement across session authenticators](<resources/grav-2026-session-account-state-revalidation.md>)
- [HotCRP: separate submission visibility from authorship authority](<resources/hotcrp-2026-contact-authorship-permission-boundary.md>)
- [n8n Dynamic Credentials: authorize credential lifecycle operations](<resources/n8n-2026-dynamic-credential-object-authority.md>)
- [n8n token exchange: preserve the issuer namespace](<resources/n8n-2026-external-identity-issuer-binding.md>)
- [n8n: directory-attribute authority in durable account linking](<resources/n8n-2026-ldap-account-linking-authority.md>)
- [Nhost: provider adapters must preserve identity-claim evidence](<resources/nhost-2026-provider-claim-verification-provenance.md>)
- [NIST SP 800-162: attribute authority and policy traceability](<resources/nist-sp-800-162-attribute-authority-modeling.md>)
- [Obot: preserve delegated token audience and consent boundaries](<resources/obot-2026-oauth-audience-and-consent-boundaries.md>)
- [Open WebUI: preserve role-policy meaning across identity flows](<resources/open-webui-2026-role-claim-provenance-and-revocation.md>)
- [Open WebUI: revocation must cross HTTP and realtime boundaries](<resources/open-webui-2026-realtime-revocation-consistency.md>)
- [Outline: integration authority must end with its owning account](<resources/outline-2026-webhook-revocation-lifecycle.md>)
- [OWASP Forgot Password](<resources/owasp-account-recovery-state-integrity.md>)
- [OWASP Juice Shop: Controlled Web-Security Training](<resources/owasp-juice-shop-controlled-training.md>)
- [OWASP Session Management: privilege-transition integrity](<resources/owasp-session-privilege-transition-integrity.md>)
- [pac4j JWT validation: confidentiality does not establish authenticity](<resources/pac4j-2026-token-authenticity-enforcement.md>)
- [Prowler SAML: retain validated tenant authority](<resources/prowler-2026-saml-tenant-issuance-binding.md>)
- [RFC 10017: OAuth 2\.0 for Browser-Based Applications](<resources/rfc-10017-browser-oauth-token-custody.md>)
- [RFC 9700: Best Current Practice for OAuth 2\.0 Security](<resources/rfc-9700-oauth-security-best-current-practice.md>)
- [Rocket\.Chat: authentication must await a completed verification decision](<resources/rocketchat-2026-asynchronous-identity-verification.md>)
- [Saleor email changes: bind confirmation to account and state](<resources/saleor-2026-email-change-confirmation-binding.md>)
- [samlify: signing does not establish claim provenance](<resources/samlify-2026-assertion-generation-claim-integrity.md>)
- [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](<resources/usenix-2025-tls-resumption-identity-isolation.md>)
- [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<resources/usenix-2025-integration-platform-oauth-bindings.md>)
- [Vikunja: saved favorites must recheck current project access](<resources/vikunja-2026-favorites-current-access-revalidation.md>)
- [Web Security Academy: Free Online Training from PortSwigger](<resources/portswigger-web-security-academy-controlled-training.md>)

<a id="skill-untrusted-input-handling"></a>
## Review input trust boundaries

Assess validation and data/code separation without collecting offensive payloads.

### Award-backed reports

20 records.

- [Apple PCC startup archive processing lacked path confinement](<reports/apple-pcc-boot-archive-path-validation-2026.md>)
- [Bard Workspace integration weakened output-data boundaries](<reports/google-bard-workspace-output-boundary-2024.md>)
- [Chrome graphics input validation weakened an isolation boundary](<reports/google-chrome-angle-input-validation-2026.md>)
- [Codex automated Git operations trusted repository hook settings](<reports/openai-codex-repository-hook-execution-trust-2026.md>)
- [Codex command approval relied on inconsistent parser semantics](<reports/openai-codex-command-parser-approval-consistency-2026.md>)
- [Codex metadata collection trusted repository execution helpers](<reports/openai-codex-repository-metadata-helper-trust-2026.md>)
- [Facebook SDK message authentication relied on insecure randomness](<reports/facebook-sdk-message-authentication-randomness-2023.md>)
- [Framework serialization change exposed private HackerOne user attributes](<reports/hackerone-report-json-serialization-data-exposure-2025.md>)
- [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](<reports/google-gemini-enterprise-connected-content-memory-integrity-2026.md>)
- [Gemini-to-Colab rendering boundary exposed Workspace data](<reports/google-gemini-colab-rendering-boundary-2025.md>)
- [GitHub unsafe reflection crossed method and credential boundaries](<reports/github-reflection-method-authority-cve-2024-0200.md>)
- [Google IDX worker messaging crossed browser trust boundaries](<reports/google-idx-worker-message-trust-2025.md>)
- [Kestrel HTTP framing differed across proxy and application boundaries](<reports/microsoft-kestrel-http-framing-consistency-2025.md>)
- [MariaDB JSON normalization exceeded allocated buffer capacity](<reports/mariadb-json-normalization-buffer-capacity-2026.md>)
- [Meta Conversions API Gateway mixed configuration data with executable output](<reports/meta-conversions-gateway-generated-script-boundary-2025.md>)
- [Meta Conversions API Gateway trusted message origins as script authority](<reports/meta-conversions-gateway-message-origin-boundary-2024.md>)
- [NVIDIA container initialization inherited untrusted execution context](<reports/nvidia-container-runtime-environment-trust-2025.md>)
- [PostgreSQL cryptographic parsing omitted a buffer-capacity check](<reports/postgresql-pgcrypto-buffer-capacity-validation-2026.md>)
- [PostgreSQL extension estimator trusted an unchecked input type](<reports/postgresql-extension-input-type-validation-2026.md>)
- [Redis deserialization cleanup violated object-ownership invariants](<reports/redis-deserialization-object-ownership-2026.md>)

### Educational resources

45 records.

- [Angular host bindings: bind sanitization to the concrete output element](<resources/angular-2026-host-binding-context-authority.md>)
- [Angular hydration: verify the source of restored state](<resources/angular-2026-hydration-state-source-authenticity.md>)
- [Axios: enforce upload budgets across transport implementations](<resources/axios-2026-streamed-upload-budget-enforcement.md>)
- [Axios: URL construction does not establish destination authority](<resources/axios-2025-base-url-destination-authority.md>)
- [Chromium Rule of Two: input trust, memory safety and privilege](<resources/chromium-rule-of-two-input-isolation.md>)
- [CI4MS: keep stored diagnostic content inert in administrative log views](<resources/ci4ms-2026-log-viewer-stored-blind-xss-boundary.md>)
- [CyLab Security Academy: Self-Paced CTF Learning](<resources/cylab-security-academy-ctf-practice.md>)
- [Django: ORM alias metadata must not acquire query authority](<resources/django-2026-query-alias-structure-boundary.md>)
- [DOMPurify: accepted DOM realms must retain complete sanitization](<resources/dompurify-2026-cross-realm-sanitization-consistency.md>)
- [GitHub internal metadata: preserve the boundary between user data and service authority](<resources/github-2026-internal-metadata-authority.md>)
- [Google API field masks: preserve server-owned and immutable state](<resources/google-aip-161-update-field-authority.md>)
- [HTML5 Security Cheat Sheet: Web Messaging](<resources/owasp-browser-message-trust-boundaries.md>)
- [Jupyter Enterprise Gateway: keep kernel configuration outside template authority](<resources/jupyter-enterprise-gateway-2026-kernel-configuration-template-boundary.md>)
- [Laravel: preserve output encoding in debug diagnostics](<resources/laravel-2025-debug-diagnostic-output-encoding.md>)
- [LLM Prompt Injection Prevention Cheat Sheet](<resources/owasp-llm-prompt-injection-prevention.md>)
- [mailcow: stored configuration retains its original trust level](<resources/mailcow-2026-persisted-data-query-boundary.md>)
- [MLflow: destination validation must remain bound to the actual connection](<resources/mlflow-2026-webhook-connection-destination-integrity.md>)
- [Next\.js data security: server authorization and client-visible data](<resources/nextjs-server-client-data-security.md>)
- [Next\.js: response metadata must preserve representation boundaries](<resources/nextjs-2026-response-metadata-representation-boundary.md>)
- [Nuxt: island data must not acquire component-selection authority](<resources/nuxt-2026-island-component-selection-authority.md>)
- [OAuth2 Proxy: client-address provenance must precede authentication exemptions](<resources/oauth2-proxy-2026-client-address-provenance-authority.md>)
- [OWASP Juice Shop: Controlled Web-Security Training](<resources/owasp-juice-shop-controlled-training.md>)
- [OWASP LLM05:2025: generated-output consumer trust](<resources/owasp-llm-output-consumer-trust.md>)
- [OWASP Logging: trustworthy and minimal application evidence](<resources/owasp-security-logging-evidence-quality.md>)
- [OWASP Secure Code Review: baseline and change-focused review](<resources/owasp-secure-code-review-methodology.md>)
- [OWASP Server-Side Request Forgery Prevention](<resources/owasp-server-request-destination-boundaries.md>)
- [OWASP WebGoat: Web-Application Security Lessons](<resources/owasp-webgoat-controlled-training.md>)
- [Parse Server: preserve safe file interpretation across storage and browsers](<resources/parse-server-2026-upload-metadata-consumer-boundary.md>)
- [pypdf: bound repeated work when reading embedded attachments](<resources/pypdf-2026-attachment-processing-cost-boundary.md>)
- [Python subprocess: executable, argument, and interpreter boundaries](<resources/python-subprocess-interpreter-boundaries.md>)
- [Qwik: resumability metadata must preserve HTML serialization boundaries](<resources/qwik-2026-resumability-comment-serialization-boundary.md>)
- [React Router: hydrated error metadata must not select client behavior](<resources/react-router-2026-hydration-error-constructor-boundary.md>)
- [React2Shell response: parser consistency and layered remediation](<resources/vercel-react2shell-parser-normalization-defense.md>)
- [SearchLeak: streamed output needs policy enforcement before browser activation](<resources/microsoft-copilot-2026-streaming-output-activation-boundary.md>)
- [Serialize JavaScript: every serialized field must retain data semantics](<resources/serialize-javascript-2026-output-code-boundary.md>)
- [Svelte hydration: serialization must preserve the enclosing output context](<resources/svelte-2026-hydration-output-context-boundary.md>)
- [SvelteKit: origin construction and routing must preserve server request authority](<resources/sveltekit-2026-origin-routing-trust-boundary.md>)
- [TanStack Start: preserve server-owned response authority through errors](<resources/tanstack-2026-server-function-response-authority.md>)
- [Trix: validate stored attachment data before link interpretation](<resources/trix-2025-attachment-link-interpretation-boundary.md>)
- [Trusted Types: typed sinks depend on trustworthy policy creation](<resources/w3c-2026-trusted-types-policy-authority.md>)
- [TYPO3: configured upload policy must reach the runtime validator](<resources/typo3-2026-upload-validator-lifecycle-boundary.md>)
- [Upstream HTTP framing and parser-consistency boundaries](<resources/portswigger-2025-upstream-http-framing-boundaries.md>)
- [Uptime Kuma: separate notification-template authority from server files](<resources/uptime-kuma-2025-notification-template-file-boundary.md>)
- [Vercel React Router: session identity must not select unrestricted storage authority](<resources/vercel-react-router-2026-session-storage-key-authority.md>)
- [Vvveb: numeric input validity does not establish legitimate order state](<resources/vvveb-2026-order-domain-invariant.md>)

<a id="skill-machine-identity-governance"></a>
## Review machine identities

Document bot and service identity privileges, rotation, approvals, and separation of duties.

### Award-backed reports

4 records.

- [Actifio driver execution exposed excessive shared-service authority](<reports/google-actifio-driver-service-identity-isolation-2025.md>)
- [Angular automation trust and cache isolation weakness](<reports/angular-ci-cache-trust-2026.md>)
- [Instagram client configuration exposed an application credential](<reports/instagram-application-credential-client-containment-2022.md>)
- [Meta service-identity exposure amplified by excessive secret access](<reports/meta-service-identity-secrets-trust-boundary-2026.md>)

### Educational resources

2 records.

- [AWS IAM security best practices for workload identities](<resources/aws-iam-machine-identity-best-practices.md>)
- [Sigstore Security Model](<resources/sigstore-security-model.md>)

<a id="skill-memory-safety-review"></a>
## Review memory-safety assumptions

Assess length, bounds, allocation, and lifetime assumptions in owned source code and vendor patches.

### Award-backed reports

10 records.

- [macOS SMBFS error handling left inconsistent kernel parser state](<reports/apple-smbfs-parser-state-consistency-2026.md>)
- [MariaDB JSON normalization exceeded allocated buffer capacity](<reports/mariadb-json-normalization-buffer-capacity-2026.md>)
- [PostgreSQL cryptographic parsing omitted a buffer-capacity check](<reports/postgresql-pgcrypto-buffer-capacity-validation-2026.md>)
- [PostgreSQL extension estimator trusted an unchecked input type](<reports/postgresql-extension-input-type-validation-2026.md>)
- [PostgreSQL text-encoding invariant failure caused memory corruption](<reports/postgresql-multibyte-validation-cve-2026-2006.md>)
- [Redis deserialization cleanup violated object-ownership invariants](<reports/redis-deserialization-object-ownership-2026.md>)
- [Redis Lua object lifetime failure crossed the scripting boundary](<reports/redis-lua-object-lifetime-isolation-2025.md>)
- [Redis replication state changes invalidated an active interpreter](<reports/redis-replication-interpreter-lifetime-2026.md>)
- [V8 control-flow analysis omitted required initialization checks](<reports/google-chrome-v8-initialization-checks-2025.md>)
- [V8 optimized object handling retained invalid type assumptions](<reports/google-chrome-v8-type-consistency-2025.md>)

### Educational resources

4 records.

- [C\+\+ Core Guidelines: Bounds and Lifetime Safety](<resources/cpp-core-guidelines-bounds-lifetime.md>)
- [Chromium Rule of Two: input trust, memory safety and privilege](<resources/chromium-rule-of-two-input-isolation.md>)
- [Rust Ownership and Borrowing: Lifetime Contracts](<resources/rust-ownership-borrowing.md>)
- [Rust Slices: Bounds, Borrowing, and Text Boundaries](<resources/rust-slices-parser-boundaries.md>)

<a id="skill-secure-parser-review"></a>
## Review parsing and serialization

Reason about parser consistency, validation, and safe serialization contracts.

### Award-backed reports

17 records.

- [Apple PCC startup archive processing lacked path confinement](<reports/apple-pcc-boot-archive-path-validation-2026.md>)
- [Codex command approval relied on inconsistent parser semantics](<reports/openai-codex-command-parser-approval-consistency-2026.md>)
- [Facebook error responses exposed unintended application data](<reports/facebook-error-response-data-isolation-2019.md>)
- [Framework serialization change exposed private HackerOne user attributes](<reports/hackerone-report-json-serialization-data-exposure-2025.md>)
- [Gemini-to-Colab rendering boundary exposed Workspace data](<reports/google-gemini-colab-rendering-boundary-2025.md>)
- [GitHub OAuth consent failed across request-method semantics](<reports/github-oauth-method-semantics-2019.md>)
- [GitLab recovery delivery lacked verified-address binding](<reports/gitlab-recovery-address-binding-cve-2023-7028.md>)
- [HackerOne exports omitted internal-attachment authorization](<reports/hackerone-export-attachment-authorization-2016.md>)
- [Kestrel HTTP framing differed across proxy and application boundaries](<reports/microsoft-kestrel-http-framing-consistency-2025.md>)
- [macOS SMBFS error handling left inconsistent kernel parser state](<reports/apple-smbfs-parser-state-consistency-2026.md>)
- [MariaDB JSON normalization exceeded allocated buffer capacity](<reports/mariadb-json-normalization-buffer-capacity-2026.md>)
- [Meta Conversions API Gateway mixed configuration data with executable output](<reports/meta-conversions-gateway-generated-script-boundary-2025.md>)
- [PostgreSQL cryptographic parsing omitted a buffer-capacity check](<reports/postgresql-pgcrypto-buffer-capacity-validation-2026.md>)
- [PostgreSQL extension estimator trusted an unchecked input type](<reports/postgresql-extension-input-type-validation-2026.md>)
- [PostgreSQL text-encoding invariant failure caused memory corruption](<reports/postgresql-multibyte-validation-cve-2026-2006.md>)
- [Redis deserialization cleanup violated object-ownership invariants](<reports/redis-deserialization-object-ownership-2026.md>)
- [Safari origin confusion undermined stored media permissions](<reports/apple-safari-media-permission-origin-confusion-2020.md>)

### Educational resources

28 records.

- [Angular SSR: preserve output context through serialization and post-processing](<resources/angular-2026-raw-content-serialization-context.md>)
- [Astro: routing and authorization must agree on resource identity](<resources/astro-2026-route-normalization-authorization-consistency.md>)
- [C\+\+ Core Guidelines: Bounds and Lifetime Safety](<resources/cpp-core-guidelines-bounds-lifetime.md>)
- [Chromium Rule of Two: input trust, memory safety and privilege](<resources/chromium-rule-of-two-input-isolation.md>)
- [Django: ORM alias metadata must not acquire query authority](<resources/django-2026-query-alias-structure-boundary.md>)
- [DOMPurify: accepted DOM realms must retain complete sanitization](<resources/dompurify-2026-cross-realm-sanitization-consistency.md>)
- [Error Handling Cheat Sheet](<resources/owasp-error-response-data-minimization.md>)
- [Frappe: linked data must preserve document and field permissions](<resources/frappe-2026-linked-document-response-authorization.md>)
- [GitHub internal metadata: preserve the boundary between user data and service authority](<resources/github-2026-internal-metadata-authority.md>)
- [LibreChat: viewing an integration must not reveal its service secrets](<resources/librechat-2026-mcp-view-secret-projection.md>)
- [mailcow: stored configuration retains its original trust level](<resources/mailcow-2026-persisted-data-query-boundary.md>)
- [Next\.js data security: server authorization and client-visible data](<resources/nextjs-server-client-data-security.md>)
- [Next\.js: response metadata must preserve representation boundaries](<resources/nextjs-2026-response-metadata-representation-boundary.md>)
- [OWASP Server-Side Request Forgery Prevention](<resources/owasp-server-request-destination-boundaries.md>)
- [Parse Server: preserve safe file interpretation across storage and browsers](<resources/parse-server-2026-upload-metadata-consumer-boundary.md>)
- [pypdf: bound repeated work when reading embedded attachments](<resources/pypdf-2026-attachment-processing-cost-boundary.md>)
- [Python subprocess: executable, argument, and interpreter boundaries](<resources/python-subprocess-interpreter-boundaries.md>)
- [Qwik: resumability metadata must preserve HTML serialization boundaries](<resources/qwik-2026-resumability-comment-serialization-boundary.md>)
- [React Router: hydrated error metadata must not select client behavior](<resources/react-router-2026-hydration-error-constructor-boundary.md>)
- [React2Shell response: parser consistency and layered remediation](<resources/vercel-react2shell-parser-normalization-defense.md>)
- [Rust Slices: Bounds, Borrowing, and Text Boundaries](<resources/rust-slices-parser-boundaries.md>)
- [samlify: signing does not establish claim provenance](<resources/samlify-2026-assertion-generation-claim-integrity.md>)
- [Serialize JavaScript: every serialized field must retain data semantics](<resources/serialize-javascript-2026-output-code-boundary.md>)
- [Steeltoe: diagnostic URI masking must cover the complete data contract](<resources/steeltoe-2026-diagnostic-uri-data-minimization.md>)
- [Svelte hydration: serialization must preserve the enclosing output context](<resources/svelte-2026-hydration-output-context-boundary.md>)
- [Trusted Types: typed sinks depend on trustworthy policy creation](<resources/w3c-2026-trusted-types-policy-authority.md>)
- [TYPO3: configured upload policy must reach the runtime validator](<resources/typo3-2026-upload-validator-lifecycle-boundary.md>)
- [Upstream HTTP framing and parser-consistency boundaries](<resources/portswigger-2025-upstream-http-framing-boundaries.md>)

<a id="skill-secrets-containment"></a>
## Review secrets containment

Assess whether secrets are limited to the minimum necessary trusted execution contexts.

### Award-backed reports

10 records.

- [Actifio driver execution exposed excessive shared-service authority](<reports/google-actifio-driver-service-identity-isolation-2025.md>)
- [Angular automation trust and cache isolation weakness](<reports/angular-ci-cache-trust-2026.md>)
- [Cloud Build approval was not bound to immutable code](<reports/google-cloud-build-approval-toctou-2025.md>)
- [GitHub Actions trust depended on invalid repository references](<reports/github-actions-reference-validation-2021.md>)
- [GitHub package-source trust allowed dependency confusion](<reports/github-ruby-dependency-confusion-2025.md>)
- [GitHub runner-image builds shared persistent infrastructure with untrusted workflows](<reports/github-runner-image-build-isolation-2023.md>)
- [GitHub unsafe reflection crossed method and credential boundaries](<reports/github-reflection-method-authority-cve-2024-0200.md>)
- [Instagram client configuration exposed an application credential](<reports/instagram-application-credential-client-containment-2022.md>)
- [Meta service-identity exposure amplified by excessive secret access](<reports/meta-service-identity-secrets-trust-boundary-2026.md>)
- [Shopify Exchange screenshot service crossed internal boundaries](<reports/shopify-exchange-request-isolation-2019.md>)

### Educational resources

13 records.

- [AWS IAM security best practices for workload identities](<resources/aws-iam-machine-identity-best-practices.md>)
- [Axios: URL construction does not establish destination authority](<resources/axios-2025-base-url-destination-authority.md>)
- [Document Isolation Policy: process separation and residual authority](<resources/chrome-document-isolation-policy-boundaries.md>)
- [Formie: integration settings need operation and attribute authority](<resources/formie-2026-integration-settings-credential-authority.md>)
- [LibreChat: viewing an integration must not reveal its service secrets](<resources/librechat-2026-mcp-view-secret-projection.md>)
- [MCP elicitation: consent, credential custody and completion](<resources/mcp-elicitation-consent-credential-custody.md>)
- [Next\.js data security: server authorization and client-visible data](<resources/nextjs-server-client-data-security.md>)
- [Open WebUI: credentials must bind to their destination connection](<resources/open-webui-2026-connection-credential-capture.md>)
- [OWASP LLM09:2026: embedding confidentiality and storage lifecycle](<resources/owasp-2026-embedding-confidentiality-lifecycle.md>)
- [OWASP Logging: trustworthy and minimal application evidence](<resources/owasp-security-logging-evidence-quality.md>)
- [OWASP Server-Side Request Forgery Prevention](<resources/owasp-server-request-destination-boundaries.md>)
- [Steeltoe: diagnostic URI masking must cover the complete data contract](<resources/steeltoe-2026-diagnostic-uri-data-minimization.md>)
- [Uptime Kuma: separate notification-template authority from server files](<resources/uptime-kuma-2025-notification-template-file-boundary.md>)

<a id="skill-error-response-design"></a>
## Review secure error behavior

Verify that failure responses minimize disclosure and that fallback paths preserve the original authorization context.

### Award-backed reports

2 records.

- [Facebook error responses exposed unintended application data](<reports/facebook-error-response-data-isolation-2019.md>)
- [Instagram embedding fallback changed the authorization context](<reports/instagram-embedding-privileged-fallback-2023.md>)

### Educational resources

8 records.

- [Error Handling Cheat Sheet](<resources/owasp-error-response-data-minimization.md>)
- [Google long-running operations: cancellation requests and completion evidence](<resources/google-aip-151-operation-completion-integrity.md>)
- [GraphQL-Ruby: authorization exceptions must stop execution](<resources/graphql-ruby-2026-authorization-exception-integrity.md>)
- [Laravel: preserve output encoding in debug diagnostics](<resources/laravel-2025-debug-diagnostic-output-encoding.md>)
- [Microsoft Graph batching: preserve each member authorization outcome](<resources/microsoft-graph-batch-member-authorization-outcomes.md>)
- [React Router: hydrated error metadata must not select client behavior](<resources/react-router-2026-hydration-error-constructor-boundary.md>)
- [SvelteKit: origin construction and routing must preserve server request authority](<resources/sveltekit-2026-origin-routing-trust-boundary.md>)
- [TanStack Start: preserve server-owned response authority through errors](<resources/tanstack-2026-server-function-response-authority.md>)

<a id="skill-security-token-design"></a>
## Review security-token design

Assess unpredictable generation, subject and operation binding, limited lifetime, single-use semantics and safe validation of security-sensitive tokens.

### Award-backed reports

6 records.

- [Facebook SDK message authentication relied on insecure randomness](<reports/facebook-sdk-message-authentication-randomness-2023.md>)
- [Google device grants lost client and permission binding](<reports/google-device-authorization-client-scope-binding-2026.md>)
- [LiteSpeed Cache privileged user simulation relied on weak security tokens](<reports/litespeed-cache-user-simulation-authentication-2024.md>)
- [Meta account verification weakened linked SMS authentication state](<reports/meta-account-verification-attempt-state-binding-2022.md>)
- [Meta Accounts Center linking lost credential and identity confinement](<reports/meta-accounts-center-linking-credential-confinement-2024.md>)
- [Meta Quest login migration lost OAuth credential confinement](<reports/meta-quest-oauth-redirect-confidentiality-2022.md>)

### Educational resources

15 records.

- [Better Auth: single-use authorization requires atomic state consumption](<resources/better-auth-2026-authorization-code-consumption-integrity.md>)
- [Bugsink: time-unit consistency in account-access token expiry](<resources/bugsink-2026-token-expiry-unit-integrity.md>)
- [FAPI 2\.0 Security Profile](<resources/openid-fapi-2-api-authorization-profile.md>)
- [n8n token exchange: preserve the issuer namespace](<resources/n8n-2026-external-identity-issuer-binding.md>)
- [n8n: refreshed authority must remain bound to the consented resource](<resources/n8n-2026-refresh-grant-resource-binding.md>)
- [Open WebUI: revocation must cross HTTP and realtime boundaries](<resources/open-webui-2026-realtime-revocation-consistency.md>)
- [OWASP Forgot Password](<resources/owasp-account-recovery-state-integrity.md>)
- [OWASP Session Management: privilege-transition integrity](<resources/owasp-session-privilege-transition-integrity.md>)
- [OWASP Transaction Authorization](<resources/owasp-transaction-authorization-state-integrity.md>)
- [pac4j JWT validation: confidentiality does not establish authenticity](<resources/pac4j-2026-token-authenticity-enforcement.md>)
- [Prowler SAML: retain validated tenant authority](<resources/prowler-2026-saml-tenant-issuance-binding.md>)
- [Pterodactyl: delegated tokens must preserve action-specific authority](<resources/pterodactyl-2026-delegated-token-purpose-binding.md>)
- [Saleor email changes: bind confirmation to account and state](<resources/saleor-2026-email-change-confirmation-binding.md>)
- [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](<resources/usenix-2025-tls-resumption-identity-isolation.md>)
- [Vercel React Router: session identity must not select unrestricted storage authority](<resources/vercel-react-router-2026-session-storage-key-authority.md>)

<a id="skill-encoding-invariant-review"></a>
## Review text-encoding invariants

Identify and document validation contracts at extension and parser boundaries, then verify them with safe unit tests.

### Award-backed reports

1 records.

- [PostgreSQL text-encoding invariant failure caused memory corruption](<reports/postgresql-multibyte-validation-cve-2026-2006.md>)

### Educational resources

3 records.

- [Angular host bindings: bind sanitization to the concrete output element](<resources/angular-2026-host-binding-context-authority.md>)
- [Angular SSR: preserve output context through serialization and post-processing](<resources/angular-2026-raw-content-serialization-context.md>)
- [Rust Slices: Bounds, Borrowing, and Text Boundaries](<resources/rust-slices-parser-boundaries.md>)

<a id="skill-integration-threat-modeling"></a>
## Threat-model integrations

Trace documented trust assumptions between services and identify where authorization responsibility changes.

### Award-backed reports

36 records.

- [Actifio driver execution exposed excessive shared-service authority](<reports/google-actifio-driver-service-identity-isolation-2025.md>)
- [Apple PCC startup archive processing lacked path confinement](<reports/apple-pcc-boot-archive-path-validation-2026.md>)
- [Bard Workspace integration weakened output-data boundaries](<reports/google-bard-workspace-output-boundary-2024.md>)
- [Cloud Build approval was not bound to immutable code](<reports/google-cloud-build-approval-toctou-2025.md>)
- [Codex automated Git operations trusted repository hook settings](<reports/openai-codex-repository-hook-execution-trust-2026.md>)
- [Codex metadata collection trusted repository execution helpers](<reports/openai-codex-repository-metadata-helper-trust-2026.md>)
- [Facebook SDK message authentication relied on insecure randomness](<reports/facebook-sdk-message-authentication-randomness-2023.md>)
- [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](<reports/google-gemini-enterprise-connected-content-memory-integrity-2026.md>)
- [Gemini-to-Colab rendering boundary exposed Workspace data](<reports/google-gemini-colab-rendering-boundary-2025.md>)
- [GitHub comparison output lacked source-repository authorization](<reports/github-cross-repository-comparison-authorization-2025.md>)
- [Google Application Integration mixed resource and service authority](<reports/google-application-integration-authorization-boundaries-2026.md>)
- [Google device grants lost client and permission binding](<reports/google-device-authorization-client-scope-binding-2026.md>)
- [Google Firefly confused worker authority and storage boundaries](<reports/google-firefly-worker-authority-storage-boundary-2026.md>)
- [Google IDX worker messaging crossed browser trust boundaries](<reports/google-idx-worker-message-trust-2025.md>)
- [Google Mamba temporary outputs lacked access isolation](<reports/google-mamba-temporary-output-isolation-2026.md>)
- [Google support API exposed customer and agent data](<reports/google-support-api-authorization-2026.md>)
- [GraphQL object authorization exposed private-program metadata](<reports/hackerone-private-program-graphql-object-authorization-2025.md>)
- [iCloud sharing consent and Safari trust boundaries failed together](<reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.md>)
- [Instagram embedding fallback changed the authorization context](<reports/instagram-embedding-privileged-fallback-2023.md>)
- [Kestrel HTTP framing differed across proxy and application boundaries](<reports/microsoft-kestrel-http-framing-consistency-2025.md>)
- [Meta account verification weakened linked SMS authentication state](<reports/meta-account-verification-attempt-state-binding-2022.md>)
- [Meta Accounts Center linking lost credential and identity confinement](<reports/meta-accounts-center-linking-credential-confinement-2024.md>)
- [Meta AI media access lacked object-ownership authorization](<reports/meta-ai-media-object-authorization-2025.md>)
- [Meta Conversions API Gateway mixed configuration data with executable output](<reports/meta-conversions-gateway-generated-script-boundary-2025.md>)
- [Meta Conversions API Gateway trusted message origins as script authority](<reports/meta-conversions-gateway-message-origin-boundary-2024.md>)
- [Meta Pixel cross-window handling lost message and token authority](<reports/meta-pixel-cross-window-authority-binding-2024.md>)
- [Meta Quest login migration lost OAuth credential confinement](<reports/meta-quest-oauth-redirect-confidentiality-2022.md>)
- [Meta service-identity exposure amplified by excessive secret access](<reports/meta-service-identity-secrets-trust-boundary-2026.md>)
- [NVIDIA container initialization inherited untrusted execution context](<reports/nvidia-container-runtime-environment-trust-2025.md>)
- [PostgreSQL text-encoding invariant failure caused memory corruption](<reports/postgresql-multibyte-validation-cve-2026-2006.md>)
- [Redis Lua object lifetime failure crossed the scripting boundary](<reports/redis-lua-object-lifetime-isolation-2025.md>)
- [Redis replication state changes invalidated an active interpreter](<reports/redis-replication-interpreter-lifetime-2026.md>)
- [Shopify Exchange screenshot service crossed internal boundaries](<reports/shopify-exchange-request-isolation-2019.md>)
- [Support integration exposed internal Confluence documentation](<reports/hackerone-support-confluence-access-boundary-2025.md>)
- [YouTube and Pixel Recorder exposed cross-product identity links](<reports/youtube-pixel-recorder-identity-privacy-2025.md>)
- [YouTube creator metadata exposed private email addresses](<reports/youtube-creator-email-authorization-2025.md>)

### Educational resources

62 records.

- [Apollo Federation: preserving the router-to-subgraph boundary](<resources/apollo-2026-federation-router-subgraph-isolation.md>)
- [Astro: composable dispatch must preserve mandatory origin checks](<resources/astro-2026-composable-dispatch-origin-enforcement.md>)
- [Axios: URL construction does not establish destination authority](<resources/axios-2025-base-url-destination-authority.md>)
- [Better Auth: incoming identity proof does not validate existing credentials](<resources/better-auth-2026-local-account-linking-verification.md>)
- [Chrome Local Network Access: separate browser reachability from site authority](<resources/chrome-local-network-permission-boundaries.md>)
- [Claude Cowork: approved destinations need account and operation binding](<resources/anthropic-2026-egress-capability-identity-binding.md>)
- [Dify: telemetry destination changes carry tenant data-disclosure authority](<resources/dify-2026-tracing-configuration-tenant-authority.md>)
- [Document Isolation Policy: process separation and residual authority](<resources/chrome-document-isolation-policy-boundaries.md>)
- [FAPI 2\.0 Security Profile](<resources/openid-fapi-2-api-authorization-profile.md>)
- [Fetch Metadata Request Headers](<resources/w3c-fetch-metadata-request-context-boundaries.md>)
- [Formie: integration settings need operation and attribute authority](<resources/formie-2026-integration-settings-credential-authority.md>)
- [GitHub internal metadata: preserve the boundary between user data and service authority](<resources/github-2026-internal-metadata-authority.md>)
- [Google AIP-158: pagination continuation does not grant resource authority](<resources/google-aip-158-pagination-authorization-boundary.md>)
- [Google API request identity: bind retry semantics to the logical operation](<resources/google-aip-155-request-identity-contract.md>)
- [Google long-running operations: cancellation requests and completion evidence](<resources/google-aip-151-operation-completion-integrity.md>)
- [HTML COOP: opener separation and same-origin authority](<resources/whatwg-coop-opener-and-origin-authority.md>)
- [HTML5 Security Cheat Sheet: Web Messaging](<resources/owasp-browser-message-trust-boundaries.md>)
- [Langflow: project transport authorization must reach each resource read](<resources/langflow-2026-mcp-resource-project-authorization.md>)
- [LibreChat: delegated credentials must remain bound to the initiating session](<resources/librechat-2026-mcp-oauth-session-binding.md>)
- [LLM Prompt Injection Prevention Cheat Sheet](<resources/owasp-llm-prompt-injection-prevention.md>)
- [MCP elicitation: consent, credential custody and completion](<resources/mcp-elicitation-consent-credential-custody.md>)
- [MCP scope selection: progressive consent and accumulated authority](<resources/mcp-progressive-scope-authority.md>)
- [Microsoft compensating transactions: recovery must preserve valid concurrent state](<resources/microsoft-compensating-transaction-state-integrity.md>)
- [Microsoft Graph batching: preserve each member authorization outcome](<resources/microsoft-graph-batch-member-authorization-outcomes.md>)
- [MLflow: authorization must survive alternate resource interfaces](<resources/mlflow-2026-alternate-interface-authorization-consistency.md>)
- [MLflow: destination validation must remain bound to the actual connection](<resources/mlflow-2026-webhook-connection-destination-integrity.md>)
- [MythicalDash: payment evidence must establish credit entitlement](<resources/mythicaldash-2026-payment-evidence-entitlement.md>)
- [n8n Dynamic Credentials: authorize credential lifecycle operations](<resources/n8n-2026-dynamic-credential-object-authority.md>)
- [n8n: refreshed authority must remain bound to the consented resource](<resources/n8n-2026-refresh-grant-resource-binding.md>)
- [Nhost: provider adapters must preserve identity-claim evidence](<resources/nhost-2026-provider-claim-verification-provenance.md>)
- [NIST SP 800-162: attribute authority and policy traceability](<resources/nist-sp-800-162-attribute-authority-modeling.md>)
- [NIST SP 800-190: Application Container Security Guide](<resources/nist-sp-800-190-container-isolation-guide.md>)
- [Nuxt: island data must not acquire component-selection authority](<resources/nuxt-2026-island-component-selection-authority.md>)
- [OAuth2 Proxy: client-address provenance must precede authentication exemptions](<resources/oauth2-proxy-2026-client-address-provenance-authority.md>)
- [Obot: preserve delegated token audience and consent boundaries](<resources/obot-2026-oauth-audience-and-consent-boundaries.md>)
- [Open WebUI: credentials must bind to their destination connection](<resources/open-webui-2026-connection-credential-capture.md>)
- [Open WebUI: preserve role-policy meaning across identity flows](<resources/open-webui-2026-role-claim-provenance-and-revocation.md>)
- [Open WebUI: revocation must cross HTTP and realtime boundaries](<resources/open-webui-2026-realtime-revocation-consistency.md>)
- [Outline: integration authority must end with its owning account](<resources/outline-2026-webhook-revocation-lifecycle.md>)
- [OWASP LLM05:2025: generated-output consumer trust](<resources/owasp-llm-output-consumer-trust.md>)
- [OWASP LLM08:2025: retrieval permissions and knowledge provenance](<resources/owasp-rag-retrieval-permission-boundaries.md>)
- [OWASP LLM09:2026: embedding confidentiality and storage lifecycle](<resources/owasp-2026-embedding-confidentiality-lifecycle.md>)
- [OWASP Server-Side Request Forgery Prevention](<resources/owasp-server-request-destination-boundaries.md>)
- [OWASP Threat Modeling: system assumptions and mitigation validation](<resources/owasp-threat-modeling-assumptions-and-validation.md>)
- [Payload: request adapters must retain caller-level authorization](<resources/payload-2026-local-api-caller-authority.md>)
- [Permissions Policy: inherited browser-feature authority across embedded documents](<resources/w3c-permissions-policy-embedded-feature-authority.md>)
- [Pterodactyl: delegated tokens must preserve action-specific authority](<resources/pterodactyl-2026-delegated-token-purpose-binding.md>)
- [React2Shell response: parser consistency and layered remediation](<resources/vercel-react2shell-parser-normalization-defense.md>)
- [RFC 10017: OAuth 2\.0 for Browser-Based Applications](<resources/rfc-10017-browser-oauth-token-custody.md>)
- [RFC 9700: Best Current Practice for OAuth 2\.0 Security](<resources/rfc-9700-oauth-security-best-current-practice.md>)
- [ServiceNow: agent discovery expands the delegated authority boundary](<resources/servicenow-2025-agent-discovery-delegation-authority.md>)
- [Steeltoe: diagnostic URI masking must cover the complete data contract](<resources/steeltoe-2026-diagnostic-uri-data-minimization.md>)
- [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](<resources/usenix-2025-tls-resumption-identity-isolation.md>)
- [Storage Access API: permission, document activation and cookie eligibility](<resources/privacycg-storage-access-permission-activation-boundary.md>)
- [Stripe webhooks: authentic delivery and business-state integrity](<resources/stripe-webhook-delivery-state-integrity.md>)
- [SvelteKit: origin construction and routing must preserve server request authority](<resources/sveltekit-2026-origin-routing-trust-boundary.md>)
- [Sylius: order ownership does not confer payment-operation authority](<resources/sylius-2026-payment-action-authority.md>)
- [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<resources/usenix-2025-integration-platform-oauth-bindings.md>)
- [Upstream HTTP framing and parser-consistency boundaries](<resources/portswigger-2025-upstream-http-framing-boundaries.md>)
- [Vendure: payment child objects must inherit order channel authority](<resources/vendure-2026-payment-child-object-channel-authority.md>)
- [Vite: local reachability does not establish browser-origin authority](<resources/vite-2025-development-server-origin-authority.md>)
- [Web cache key precision and capacity isolation](<resources/arxiv-2026-cache-key-precision-and-capacity.md>)

<a id="skill-patch-verification"></a>
## Verify remediation evidence

Compare vendor advisories, affected versions, fixes, and regression coverage without reproducing an exploit.

### Award-backed reports

26 records.

- [Apple PCC startup archive processing lacked path confinement](<reports/apple-pcc-boot-archive-path-validation-2026.md>)
- [Chrome graphics input validation weakened an isolation boundary](<reports/google-chrome-angle-input-validation-2026.md>)
- [Codex automated Git operations trusted repository hook settings](<reports/openai-codex-repository-hook-execution-trust-2026.md>)
- [Codex command approval relied on inconsistent parser semantics](<reports/openai-codex-command-parser-approval-consistency-2026.md>)
- [Codex metadata collection trusted repository execution helpers](<reports/openai-codex-repository-metadata-helper-trust-2026.md>)
- [Facebook error responses exposed unintended application data](<reports/facebook-error-response-data-isolation-2019.md>)
- [Framework serialization change exposed private HackerOne user attributes](<reports/hackerone-report-json-serialization-data-exposure-2025.md>)
- [GitHub comparison output lacked source-repository authorization](<reports/github-cross-repository-comparison-authorization-2025.md>)
- [GitHub unsafe reflection crossed method and credential boundaries](<reports/github-reflection-method-authority-cve-2024-0200.md>)
- [GitLab recovery delivery lacked verified-address binding](<reports/gitlab-recovery-address-binding-cve-2023-7028.md>)
- [Kestrel HTTP framing differed across proxy and application boundaries](<reports/microsoft-kestrel-http-framing-consistency-2025.md>)
- [LiteSpeed Cache privileged user simulation relied on weak security tokens](<reports/litespeed-cache-user-simulation-authentication-2024.md>)
- [macOS SMBFS error handling left inconsistent kernel parser state](<reports/apple-smbfs-parser-state-consistency-2026.md>)
- [MariaDB JSON normalization exceeded allocated buffer capacity](<reports/mariadb-json-normalization-buffer-capacity-2026.md>)
- [Meta AI media access lacked object-ownership authorization](<reports/meta-ai-media-object-authorization-2025.md>)
- [NVIDIA container initialization inherited untrusted execution context](<reports/nvidia-container-runtime-environment-trust-2025.md>)
- [Pixel lock-screen completion lost security-state binding](<reports/google-pixel-lock-screen-state-binding-2022.md>)
- [PostgreSQL cryptographic parsing omitted a buffer-capacity check](<reports/postgresql-pgcrypto-buffer-capacity-validation-2026.md>)
- [PostgreSQL extension estimator trusted an unchecked input type](<reports/postgresql-extension-input-type-validation-2026.md>)
- [PostgreSQL text-encoding invariant failure caused memory corruption](<reports/postgresql-multibyte-validation-cve-2026-2006.md>)
- [Redis deserialization cleanup violated object-ownership invariants](<reports/redis-deserialization-object-ownership-2026.md>)
- [Redis Lua object lifetime failure crossed the scripting boundary](<reports/redis-lua-object-lifetime-isolation-2025.md>)
- [Redis replication state changes invalidated an active interpreter](<reports/redis-replication-interpreter-lifetime-2026.md>)
- [Safari origin confusion undermined stored media permissions](<reports/apple-safari-media-permission-origin-confusion-2020.md>)
- [V8 control-flow analysis omitted required initialization checks](<reports/google-chrome-v8-initialization-checks-2025.md>)
- [V8 optimized object handling retained invalid type assumptions](<reports/google-chrome-v8-type-consistency-2025.md>)

### Educational resources

77 records.

- [Angular host bindings: bind sanitization to the concrete output element](<resources/angular-2026-host-binding-context-authority.md>)
- [Angular hydration: verify the source of restored state](<resources/angular-2026-hydration-state-source-authenticity.md>)
- [Angular SSR: preserve output context through serialization and post-processing](<resources/angular-2026-raw-content-serialization-context.md>)
- [Astro: composable dispatch must preserve mandatory origin checks](<resources/astro-2026-composable-dispatch-origin-enforcement.md>)
- [Astro: routing and authorization must agree on resource identity](<resources/astro-2026-route-normalization-authorization-consistency.md>)
- [authentik: source-mapping edits carry identity-rebinding authority](<resources/authentik-2026-source-mapping-mutation-authority.md>)
- [Authlib: error responses must preserve redirect-destination validation](<resources/authlib-2026-error-path-redirect-authority.md>)
- [Axios: enforce upload budgets across transport implementations](<resources/axios-2026-streamed-upload-budget-enforcement.md>)
- [Axios: URL construction does not establish destination authority](<resources/axios-2025-base-url-destination-authority.md>)
- [Better Auth SCIM: absent ownership must not grant shared authority](<resources/better-auth-2026-scim-ownerless-provider-authority.md>)
- [Better Auth: incoming identity proof does not validate existing credentials](<resources/better-auth-2026-local-account-linking-verification.md>)
- [Better Auth: single-use authorization requires atomic state consumption](<resources/better-auth-2026-authorization-code-consumption-integrity.md>)
- [Bugsink: time-unit consistency in account-access token expiry](<resources/bugsink-2026-token-expiry-unit-integrity.md>)
- [CI4MS: keep stored diagnostic content inert in administrative log views](<resources/ci4ms-2026-log-viewer-stored-blind-xss-boundary.md>)
- [Coder: privileged provisioning must preserve existing object ownership](<resources/coder-2026-provisioned-object-ownership-integrity.md>)
- [Dify: telemetry destination changes carry tenant data-disclosure authority](<resources/dify-2026-tracing-configuration-tenant-authority.md>)
- [Directus: denied mutations must leave dependent state unchanged](<resources/directus-2026-preauthorization-side-effect-integrity.md>)
- [Django: ORM alias metadata must not acquire query authority](<resources/django-2026-query-alias-structure-boundary.md>)
- [Dolibarr portal accounts: credential writes need object authorization](<resources/dolibarr-2026-portal-object-authorization.md>)
- [DOMPurify: accepted DOM realms must retain complete sanitization](<resources/dompurify-2026-cross-realm-sanitization-consistency.md>)
- [File Browser: existing shares must follow current owner permissions](<resources/filebrowser-2026-share-owner-permission-lifecycle.md>)
- [Formie: integration settings need operation and attribute authority](<resources/formie-2026-integration-settings-credential-authority.md>)
- [Frappe: linked data must preserve document and field permissions](<resources/frappe-2026-linked-document-response-authorization.md>)
- [GitHub internal metadata: preserve the boundary between user data and service authority](<resources/github-2026-internal-metadata-authority.md>)
- [GraphQL-Ruby: authorization exceptions must stop execution](<resources/graphql-ruby-2026-authorization-exception-integrity.md>)
- [Grav API: account-disable enforcement across session authenticators](<resources/grav-2026-session-account-state-revalidation.md>)
- [HotCRP: separate submission visibility from authorship authority](<resources/hotcrp-2026-contact-authorship-permission-boundary.md>)
- [Jupyter Enterprise Gateway: keep kernel configuration outside template authority](<resources/jupyter-enterprise-gateway-2026-kernel-configuration-template-boundary.md>)
- [Langflow: project transport authorization must reach each resource read](<resources/langflow-2026-mcp-resource-project-authorization.md>)
- [Laravel: preserve output encoding in debug diagnostics](<resources/laravel-2025-debug-diagnostic-output-encoding.md>)
- [LibreChat: agent edit authority must cover attached context](<resources/librechat-2026-agent-context-mutation-authority.md>)
- [LibreChat: delegated credentials must remain bound to the initiating session](<resources/librechat-2026-mcp-oauth-session-binding.md>)
- [LobeHub: knowledge-base membership changes require ownership authorization](<resources/lobehub-2026-knowledge-membership-mutation-authority.md>)
- [mailcow: stored configuration retains its original trust level](<resources/mailcow-2026-persisted-data-query-boundary.md>)
- [MLflow: authorization must survive alternate resource interfaces](<resources/mlflow-2026-alternate-interface-authorization-consistency.md>)
- [MLflow: destination validation must remain bound to the actual connection](<resources/mlflow-2026-webhook-connection-destination-integrity.md>)
- [n8n: directory-attribute authority in durable account linking](<resources/n8n-2026-ldap-account-linking-authority.md>)
- [Nhost: provider adapters must preserve identity-claim evidence](<resources/nhost-2026-provider-claim-verification-provenance.md>)
- [NIST SP 800-190: Application Container Security Guide](<resources/nist-sp-800-190-container-isolation-guide.md>)
- [Nuxt: rendered-data caches must preserve request authorization](<resources/nuxt-2026-rendered-payload-cache-authorization.md>)
- [OAuth2 Proxy: client-address provenance must precede authentication exemptions](<resources/oauth2-proxy-2026-client-address-provenance-authority.md>)
- [Obot: preserve delegated token audience and consent boundaries](<resources/obot-2026-oauth-audience-and-consent-boundaries.md>)
- [Open WebUI: credentials must bind to their destination connection](<resources/open-webui-2026-connection-credential-capture.md>)
- [Open WebUI: preserve role-policy meaning across identity flows](<resources/open-webui-2026-role-claim-provenance-and-revocation.md>)
- [Open WebUI: revocation must cross HTTP and realtime boundaries](<resources/open-webui-2026-realtime-revocation-consistency.md>)
- [OpenFGA: policy intersections must preserve explicit exclusions](<resources/openfga-2026-composed-policy-exclusion-integrity.md>)
- [OWASP Application Security Verification Standard \(ASVS\)](<resources/owasp-asvs-5-security-verification-standard.md>)
- [pac4j JWT validation: confidentiality does not establish authenticity](<resources/pac4j-2026-token-authenticity-enforcement.md>)
- [Parse Server: preserve safe file interpretation across storage and browsers](<resources/parse-server-2026-upload-metadata-consumer-boundary.md>)
- [Payload: request adapters must retain caller-level authorization](<resources/payload-2026-local-api-caller-authority.md>)
- [Paymenter: refund entitlement and ledger changes need one atomic transition](<resources/paymenter-2026-refund-transition-atomicity.md>)
- [Pterodactyl: delegated tokens must preserve action-specific authority](<resources/pterodactyl-2026-delegated-token-purpose-binding.md>)
- [pypdf: bound repeated work when reading embedded attachments](<resources/pypdf-2026-attachment-processing-cost-boundary.md>)
- [React2Shell response: parser consistency and layered remediation](<resources/vercel-react2shell-parser-normalization-defense.md>)
- [Rocket\.Chat: authentication must await a completed verification decision](<resources/rocketchat-2026-asynchronous-identity-verification.md>)
- [Saleor email changes: bind confirmation to account and state](<resources/saleor-2026-email-change-confirmation-binding.md>)
- [samlify: signing does not establish claim provenance](<resources/samlify-2026-assertion-generation-claim-integrity.md>)
- [Sentry: resource ownership must match the authorized organization](<resources/sentry-2026-organization-object-authorization.md>)
- [Serialize JavaScript: every serialized field must retain data semantics](<resources/serialize-javascript-2026-output-code-boundary.md>)
- [Spree: cart association must retain guest-possession checks](<resources/spree-2026-guest-cart-association-authority.md>)
- [Spree: guest ownership still requires an authorization proof](<resources/spree-2026-guest-order-authorization-proof.md>)
- [Steeltoe: diagnostic URI masking must cover the complete data contract](<resources/steeltoe-2026-diagnostic-uri-data-minimization.md>)
- [Svelte hydration: serialization must preserve the enclosing output context](<resources/svelte-2026-hydration-output-context-boundary.md>)
- [SvelteKit: origin construction and routing must preserve server request authority](<resources/sveltekit-2026-origin-routing-trust-boundary.md>)
- [Sylius: component integrity does not authorize referenced objects](<resources/sylius-2026-component-argument-object-authorization.md>)
- [Sylius: promotion entitlement must be checked and consumed atomically](<resources/sylius-2026-promotion-limit-atomicity.md>)
- [TanStack Start: preserve server-owned response authority through errors](<resources/tanstack-2026-server-function-response-authority.md>)
- [Trix: validate stored attachment data before link interpretation](<resources/trix-2025-attachment-link-interpretation-boundary.md>)
- [TYPO3: configured upload policy must reach the runtime validator](<resources/typo3-2026-upload-validator-lifecycle-boundary.md>)
- [Umbraco: editing an account does not authorize assigning every role](<resources/umbraco-2026-group-assignment-authority.md>)
- [Upstream HTTP framing and parser-consistency boundaries](<resources/portswigger-2025-upstream-http-framing-boundaries.md>)
- [Uptime Kuma: separate notification-template authority from server files](<resources/uptime-kuma-2025-notification-template-file-boundary.md>)
- [Vendure: payment child objects must inherit order channel authority](<resources/vendure-2026-payment-child-object-channel-authority.md>)
- [Vercel React Router: session identity must not select unrestricted storage authority](<resources/vercel-react-router-2026-session-storage-key-authority.md>)
- [Vikunja: saved favorites must recheck current project access](<resources/vikunja-2026-favorites-current-access-revalidation.md>)
- [Vite: local reachability does not establish browser-origin authority](<resources/vite-2025-development-server-origin-authority.md>)
- [Zammad: overridden serialization must preserve group authorization](<resources/zammad-2026-asset-serialization-group-authorization.md>)

<a id="skill-defensive-evidence-writing"></a>
## Write bounded security evidence

Separate demonstrated impact, modeled impact, remediation, and source uncertainty in review findings.

### Award-backed reports

37 records.

- [Actifio driver execution exposed excessive shared-service authority](<reports/google-actifio-driver-service-identity-isolation-2025.md>)
- [Angular automation trust and cache isolation weakness](<reports/angular-ci-cache-trust-2026.md>)
- [Chrome graphics input validation weakened an isolation boundary](<reports/google-chrome-angle-input-validation-2026.md>)
- [Facebook error responses exposed unintended application data](<reports/facebook-error-response-data-isolation-2019.md>)
- [Facebook phone linking lacked account-specific authorization](<reports/facebook-phone-linking-account-authorization-2013.md>)
- [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](<reports/google-gemini-enterprise-connected-content-memory-integrity-2026.md>)
- [GitHub Actions trust depended on invalid repository references](<reports/github-actions-reference-validation-2021.md>)
- [GitHub comparison output lacked source-repository authorization](<reports/github-cross-repository-comparison-authorization-2025.md>)
- [GitHub fork collaboration applied inconsistent authorization](<reports/github-fork-collaboration-authorization-2021.md>)
- [GitHub GraphQL collaboration changes lacked author consent](<reports/github-fork-collaboration-consent-2021.md>)
- [GitHub package-source trust allowed dependency confusion](<reports/github-ruby-dependency-confusion-2025.md>)
- [GitHub runner-image builds shared persistent infrastructure with untrusted workflows](<reports/github-runner-image-build-isolation-2023.md>)
- [GitHub unsafe reflection crossed method and credential boundaries](<reports/github-reflection-method-authority-cve-2024-0200.md>)
- [GitLab recovery delivery lacked verified-address binding](<reports/gitlab-recovery-address-binding-cve-2023-7028.md>)
- [Google Application Integration mixed resource and service authority](<reports/google-application-integration-authorization-boundaries-2026.md>)
- [Google Firefly confused worker authority and storage boundaries](<reports/google-firefly-worker-authority-storage-boundary-2026.md>)
- [Google IDX worker messaging crossed browser trust boundaries](<reports/google-idx-worker-message-trust-2025.md>)
- [Google Mamba temporary outputs lacked access isolation](<reports/google-mamba-temporary-output-isolation-2026.md>)
- [Google support API exposed customer and agent data](<reports/google-support-api-authorization-2026.md>)
- [GraphQL object authorization exposed private-program metadata](<reports/hackerone-private-program-graphql-object-authorization-2025.md>)
- [HackerOne exports omitted internal-attachment authorization](<reports/hackerone-export-attachment-authorization-2016.md>)
- [Instagram client configuration exposed an application credential](<reports/instagram-application-credential-client-containment-2022.md>)
- [Instagram embedding fallback changed the authorization context](<reports/instagram-embedding-privileged-fallback-2023.md>)
- [Kestrel HTTP framing differed across proxy and application boundaries](<reports/microsoft-kestrel-http-framing-consistency-2025.md>)
- [macOS SMBFS error handling left inconsistent kernel parser state](<reports/apple-smbfs-parser-state-consistency-2026.md>)
- [Meta AI media access lacked object-ownership authorization](<reports/meta-ai-media-object-authorization-2025.md>)
- [Meta Conversions API Gateway mixed configuration data with executable output](<reports/meta-conversions-gateway-generated-script-boundary-2025.md>)
- [Meta Conversions API Gateway trusted message origins as script authority](<reports/meta-conversions-gateway-message-origin-boundary-2024.md>)
- [Meta service-identity exposure amplified by excessive secret access](<reports/meta-service-identity-secrets-trust-boundary-2026.md>)
- [Shopify automatic account conversion lost merchant-consent binding](<reports/shopify-collaborator-conversion-consent-2017.md>)
- [Shopify Exchange screenshot service crossed internal boundaries](<reports/shopify-exchange-request-isolation-2019.md>)
- [Sign in with Apple failed to bind identity claims to the authenticated user](<reports/apple-sign-in-identity-claim-binding-2020.md>)
- [Support integration exposed internal Confluence documentation](<reports/hackerone-support-confluence-access-boundary-2025.md>)
- [V8 control-flow analysis omitted required initialization checks](<reports/google-chrome-v8-initialization-checks-2025.md>)
- [V8 optimized object handling retained invalid type assumptions](<reports/google-chrome-v8-type-consistency-2025.md>)
- [YouTube and Pixel Recorder exposed cross-product identity links](<reports/youtube-pixel-recorder-identity-privacy-2025.md>)
- [YouTube creator metadata exposed private email addresses](<reports/youtube-creator-email-authorization-2025.md>)

### Educational resources

18 records.

- [Adversarial passkeys: account recovery must close every continuing source of authority](<resources/usenix-2026-passkey-remediation-authority-lifecycle.md>)
- [Axios: enforce upload budgets across transport implementations](<resources/axios-2026-streamed-upload-budget-enforcement.md>)
- [Cross-device authentication: bind informed consent to session authority](<resources/ndss-2026-cross-device-consent-and-session-control.md>)
- [CyLab Security Academy: Self-Paced CTF Learning](<resources/cylab-security-academy-ctf-practice.md>)
- [GitHub internal metadata: preserve the boundary between user data and service authority](<resources/github-2026-internal-metadata-authority.md>)
- [MLflow: authorization must survive alternate resource interfaces](<resources/mlflow-2026-alternate-interface-authorization-consistency.md>)
- [MLflow: destination validation must remain bound to the actual connection](<resources/mlflow-2026-webhook-connection-destination-integrity.md>)
- [MythicalDash: payment evidence must establish credit entitlement](<resources/mythicaldash-2026-payment-evidence-entitlement.md>)
- [OWASP Application Security Verification Standard \(ASVS\)](<resources/owasp-asvs-5-security-verification-standard.md>)
- [OWASP Logging: trustworthy and minimal application evidence](<resources/owasp-security-logging-evidence-quality.md>)
- [OWASP Secure Code Review: baseline and change-focused review](<resources/owasp-secure-code-review-methodology.md>)
- [OWASP Threat Modeling: system assumptions and mitigation validation](<resources/owasp-threat-modeling-assumptions-and-validation.md>)
- [Quality Reports](<resources/hackerone-quality-vulnerability-reports.md>)
- [React2Shell response: parser consistency and layered remediation](<resources/vercel-react2shell-parser-normalization-defense.md>)
- [SLSA v1\.2: supply-chain security and build provenance](<resources/slsa-v1-2-supply-chain-build-provenance.md>)
- [Vvveb: numeric input validity does not establish legitimate order state](<resources/vvveb-2026-order-domain-invariant.md>)
- [Web cache key precision and capacity isolation](<resources/arxiv-2026-cache-key-precision-and-capacity.md>)
- [What is a security vulnerability?](<resources/google-understanding-security-vulnerability-reports.md>)
