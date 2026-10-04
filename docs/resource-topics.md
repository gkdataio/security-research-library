# Learning resources by topic

[Alphabetical resource index](resource-index.md) · [Curated resource guide](resources.md) · [Library home](../README.md) · [Browse by vulnerability type](vulnerability-types.md)

Generated offline from canonical resource topic IDs and the resource taxonomy. These educational references are separate from award-backed reports and grant no testing authorization.

117 distinct resources across 11 taxonomy topics. A resource can appear under several topics; overlapping memberships do not increase the distinct resource count. Topic counts must not be added to count resources.

Topics and resources are ordered alphabetically by title, with stable IDs breaking ties. Empty taxonomy topics are shown explicitly. Regeneration does not reverify sources or advance review timestamps.

## Browse topics

- [Ai Security](<#topic-ai-security>) — 11 resources.
- [Authorization](<#topic-authorization>) — 72 resources.
- [Business Logic and State Integrity](<#topic-business-logic>) — 30 resources.
- [Cloud Security](<#topic-cloud-security>) — 6 resources.
- [Identity](<#topic-identity>) — 39 resources.
- [Interpreter Boundaries](<#topic-interpreter-boundaries>) — 3 resources.
- [Memory Safety and Process Isolation](<#topic-memory-safety>) — 2 resources.
- [Reporting](<#topic-reporting>) — 2 resources.
- [Software Supply Chain](<#topic-supply-chain>) — 2 resources.
- [Verification](<#topic-verification>) — 23 resources.
- [Web Foundations](<#topic-web-foundations>) — 53 resources.

<a id="topic-ai-security"></a>
## Ai Security

11 resources.

- [Dify: telemetry destination changes carry tenant data-disclosure authority](<resources/dify-2026-tracing-configuration-tenant-authority.md>) — Zafran Labs.
- [Langflow: project transport authorization must reach each resource read](<resources/langflow-2026-mcp-resource-project-authorization.md>) — Langflow.
- [LibreChat: agent edit authority must cover attached context](<resources/librechat-2026-agent-context-mutation-authority.md>) — LibreChat.
- [LibreChat: delegated credentials must remain bound to the initiating session](<resources/librechat-2026-mcp-oauth-session-binding.md>) — LibreChat.
- [LibreChat: viewing an integration must not reveal its service secrets](<resources/librechat-2026-mcp-view-secret-projection.md>) — LibreChat.
- [LLM Prompt Injection Prevention Cheat Sheet](<resources/owasp-llm-prompt-injection-prevention.md>) — OWASP Cheat Sheet Series.
- [LobeHub: knowledge-base membership changes require ownership authorization](<resources/lobehub-2026-knowledge-membership-mutation-authority.md>) — LobeHub.
- [MCP scope selection: progressive consent and accumulated authority](<resources/mcp-progressive-scope-authority.md>) — Model Context Protocol.
- [Open WebUI: credentials must bind to their destination connection](<resources/open-webui-2026-connection-credential-capture.md>) — Open WebUI.
- [OWASP LLM05:2025: generated-output consumer trust](<resources/owasp-llm-output-consumer-trust.md>) — OWASP Gen AI Security Project.
- [OWASP LLM08:2025: retrieval permissions and knowledge provenance](<resources/owasp-rag-retrieval-permission-boundaries.md>) — OWASP Gen AI Security Project.

<a id="topic-authorization"></a>
## Authorization

72 resources.

- [Adversarial passkeys: account recovery must close every continuing source of authority](<resources/usenix-2026-passkey-remediation-authority-lifecycle.md>) — USENIX Association.
- [Apollo Federation: preserving the router-to-subgraph boundary](<resources/apollo-2026-federation-router-subgraph-isolation.md>) — Apollo GraphQL.
- [Astro: routing and authorization must agree on resource identity](<resources/astro-2026-route-normalization-authorization-consistency.md>) — Astro.
- [authentik: source-mapping edits carry identity-rebinding authority](<resources/authentik-2026-source-mapping-mutation-authority.md>) — authentik.
- [Authlib: error responses must preserve redirect-destination validation](<resources/authlib-2026-error-path-redirect-authority.md>) — Authlib.
- [Authorization Cheat Sheet](<resources/owasp-authorization-cheat-sheet.md>) — OWASP Cheat Sheet Series.
- [AWS IAM security best practices for workload identities](<resources/aws-iam-machine-identity-best-practices.md>) — Amazon Web Services.
- [Better Auth SCIM: absent ownership must not grant shared authority](<resources/better-auth-2026-scim-ownerless-provider-authority.md>) — Better Auth.
- [Better Auth: incoming identity proof does not validate existing credentials](<resources/better-auth-2026-local-account-linking-verification.md>) — Better Auth.
- [Better Auth: single-use authorization requires atomic state consumption](<resources/better-auth-2026-authorization-code-consumption-integrity.md>) — Better Auth.
- [Bugsink: time-unit consistency in account-access token expiry](<resources/bugsink-2026-token-expiry-unit-integrity.md>) — Bugsink.
- [Coder: privileged provisioning must preserve existing object ownership](<resources/coder-2026-provisioned-object-ownership-integrity.md>) — Coder.
- [Cross-device authentication: bind informed consent to session authority](<resources/ndss-2026-cross-device-consent-and-session-control.md>) — Internet Society / NDSS Symposium.
- [Dify: telemetry destination changes carry tenant data-disclosure authority](<resources/dify-2026-tracing-configuration-tenant-authority.md>) — Zafran Labs.
- [Directus: denied mutations must leave dependent state unchanged](<resources/directus-2026-preauthorization-side-effect-integrity.md>) — Directus.
- [Dolibarr portal accounts: credential writes need object authorization](<resources/dolibarr-2026-portal-object-authorization.md>) — CodeAnt AI.
- [FAPI 2\.0 Security Profile](<resources/openid-fapi-2-api-authorization-profile.md>) — OpenID Foundation.
- [Fetch Metadata Request Headers](<resources/w3c-fetch-metadata-request-context-boundaries.md>) — World Wide Web Consortium.
- [File Browser: existing shares must follow current owner permissions](<resources/filebrowser-2026-share-owner-permission-lifecycle.md>) — File Browser.
- [Frappe: linked data must preserve document and field permissions](<resources/frappe-2026-linked-document-response-authorization.md>) — GitHub Security Lab.
- [GitHub internal metadata: preserve the boundary between user data and service authority](<resources/github-2026-internal-metadata-authority.md>) — Wiz Research.
- [Google AIP-158: pagination continuation does not grant resource authority](<resources/google-aip-158-pagination-authorization-boundary.md>) — Google.
- [Google API field masks: preserve server-owned and immutable state](<resources/google-aip-161-update-field-authority.md>) — Google.
- [GraphQL-Ruby: authorization exceptions must stop execution](<resources/graphql-ruby-2026-authorization-exception-integrity.md>) — GitHub Security Lab.
- [Grav API: account-disable enforcement across session authenticators](<resources/grav-2026-session-account-state-revalidation.md>) — Grav.
- [HotCRP: separate submission visibility from authorship authority](<resources/hotcrp-2026-contact-authorship-permission-boundary.md>) — HotCRP.
- [HTML COOP: opener separation and same-origin authority](<resources/whatwg-coop-opener-and-origin-authority.md>) — WHATWG.
- [HTML5 Security Cheat Sheet: Web Messaging](<resources/owasp-browser-message-trust-boundaries.md>) — OWASP Cheat Sheet Series.
- [Langflow: project transport authorization must reach each resource read](<resources/langflow-2026-mcp-resource-project-authorization.md>) — Langflow.
- [LibreChat: agent edit authority must cover attached context](<resources/librechat-2026-agent-context-mutation-authority.md>) — LibreChat.
- [LibreChat: delegated credentials must remain bound to the initiating session](<resources/librechat-2026-mcp-oauth-session-binding.md>) — LibreChat.
- [LibreChat: viewing an integration must not reveal its service secrets](<resources/librechat-2026-mcp-view-secret-projection.md>) — LibreChat.
- [LobeHub: knowledge-base membership changes require ownership authorization](<resources/lobehub-2026-knowledge-membership-mutation-authority.md>) — LobeHub.
- [MCP scope selection: progressive consent and accumulated authority](<resources/mcp-progressive-scope-authority.md>) — Model Context Protocol.
- [Microsoft Graph batching: preserve each member authorization outcome](<resources/microsoft-graph-batch-member-authorization-outcomes.md>) — Microsoft.
- [MLflow: authorization must survive alternate resource interfaces](<resources/mlflow-2026-alternate-interface-authorization-consistency.md>) — Tachyon.
- [n8n Dynamic Credentials: authorize credential lifecycle operations](<resources/n8n-2026-dynamic-credential-object-authority.md>) — n8n.
- [n8n: directory-attribute authority in durable account linking](<resources/n8n-2026-ldap-account-linking-authority.md>) — n8n.
- [n8n: refreshed authority must remain bound to the consented resource](<resources/n8n-2026-refresh-grant-resource-binding.md>) — n8n.
- [Next\.js data security: server authorization and client-visible data](<resources/nextjs-server-client-data-security.md>) — Next\.js / Vercel.
- [Nhost: provider adapters must preserve identity-claim evidence](<resources/nhost-2026-provider-claim-verification-provenance.md>) — Nhost.
- [NIST SP 800-162: attribute authority and policy traceability](<resources/nist-sp-800-162-attribute-authority-modeling.md>) — National Institute of Standards and Technology.
- [Nuxt: rendered-data caches must preserve request authorization](<resources/nuxt-2026-rendered-payload-cache-authorization.md>) — Nuxt.
- [Obot: preserve delegated token audience and consent boundaries](<resources/obot-2026-oauth-audience-and-consent-boundaries.md>) — Obot.
- [Open WebUI: credentials must bind to their destination connection](<resources/open-webui-2026-connection-credential-capture.md>) — Open WebUI.
- [Open WebUI: preserve role-policy meaning across identity flows](<resources/open-webui-2026-role-claim-provenance-and-revocation.md>) — Open WebUI.
- [Open WebUI: revocation must cross HTTP and realtime boundaries](<resources/open-webui-2026-realtime-revocation-consistency.md>) — Open WebUI.
- [OpenFGA query consistency: authorization decisions need sufficiently fresh state](<resources/openfga-authorization-query-freshness.md>) — OpenFGA.
- [OpenFGA: policy intersections must preserve explicit exclusions](<resources/openfga-2026-composed-policy-exclusion-integrity.md>) — OpenFGA.
- [Outline: integration authority must end with its owning account](<resources/outline-2026-webhook-revocation-lifecycle.md>) — Outline.
- [OWASP LLM08:2025: retrieval permissions and knowledge provenance](<resources/owasp-rag-retrieval-permission-boundaries.md>) — OWASP Gen AI Security Project.
- [OWASP Session Management: privilege-transition integrity](<resources/owasp-session-privilege-transition-integrity.md>) — OWASP Cheat Sheet Series.
- [OWASP Transaction Authorization](<resources/owasp-transaction-authorization-state-integrity.md>) — OWASP Cheat Sheet Series.
- [pac4j JWT validation: confidentiality does not establish authenticity](<resources/pac4j-2026-token-authenticity-enforcement.md>) — CodeAnt AI.
- [Paymenter: refund entitlement and ledger changes need one atomic transition](<resources/paymenter-2026-refund-transition-atomicity.md>) — Paymenter.
- [Permissions Policy: inherited browser-feature authority across embedded documents](<resources/w3c-permissions-policy-embedded-feature-authority.md>) — World Wide Web Consortium.
- [Prowler SAML: retain validated tenant authority](<resources/prowler-2026-saml-tenant-issuance-binding.md>) — Prowler.
- [Pterodactyl: delegated tokens must preserve action-specific authority](<resources/pterodactyl-2026-delegated-token-purpose-binding.md>) — Pterodactyl.
- [RFC 10017: OAuth 2\.0 for Browser-Based Applications](<resources/rfc-10017-browser-oauth-token-custody.md>) — Internet Engineering Task Force / RFC Editor.
- [samlify: signing does not establish claim provenance](<resources/samlify-2026-assertion-generation-claim-integrity.md>) — samlify.
- [Sentry: resource ownership must match the authorized organization](<resources/sentry-2026-organization-object-authorization.md>) — GitHub Security Lab.
- [Spree: cart association must retain guest-possession checks](<resources/spree-2026-guest-cart-association-authority.md>) — Spree.
- [Spree: guest ownership still requires an authorization proof](<resources/spree-2026-guest-order-authorization-proof.md>) — GitHub Security Lab.
- [Steeltoe: diagnostic URI masking must cover the complete data contract](<resources/steeltoe-2026-diagnostic-uri-data-minimization.md>) — Steeltoe.
- [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](<resources/usenix-2025-tls-resumption-identity-isolation.md>) — USENIX Association.
- [Sylius: component integrity does not authorize referenced objects](<resources/sylius-2026-component-argument-object-authorization.md>) — GitHub Security Lab.
- [Sylius: order ownership does not confer payment-operation authority](<resources/sylius-2026-payment-action-authority.md>) — Sylius.
- [Umbraco: editing an account does not authorize assigning every role](<resources/umbraco-2026-group-assignment-authority.md>) — GitHub Security Lab.
- [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<resources/usenix-2025-integration-platform-oauth-bindings.md>) — USENIX Association.
- [Vendure: payment child objects must inherit order channel authority](<resources/vendure-2026-payment-child-object-channel-authority.md>) — Vendure.
- [Vikunja: saved favorites must recheck current project access](<resources/vikunja-2026-favorites-current-access-revalidation.md>) — Vikunja.
- [Zammad: overridden serialization must preserve group authorization](<resources/zammad-2026-asset-serialization-group-authorization.md>) — GitHub Security Lab.

<a id="topic-business-logic"></a>
## Business Logic and State Integrity

30 resources.

- [Better Auth: single-use authorization requires atomic state consumption](<resources/better-auth-2026-authorization-code-consumption-integrity.md>) — Better Auth.
- [Bugsink: time-unit consistency in account-access token expiry](<resources/bugsink-2026-token-expiry-unit-integrity.md>) — Bugsink.
- [Coder: privileged provisioning must preserve existing object ownership](<resources/coder-2026-provisioned-object-ownership-integrity.md>) — Coder.
- [Directus: denied mutations must leave dependent state unchanged](<resources/directus-2026-preauthorization-side-effect-integrity.md>) — Directus.
- [File Browser: existing shares must follow current owner permissions](<resources/filebrowser-2026-share-owner-permission-lifecycle.md>) — File Browser.
- [Google API field masks: preserve server-owned and immutable state](<resources/google-aip-161-update-field-authority.md>) — Google.
- [Google API request identity: bind retry semantics to the logical operation](<resources/google-aip-155-request-identity-contract.md>) — Google.
- [Grav API: account-disable enforcement across session authenticators](<resources/grav-2026-session-account-state-revalidation.md>) — Grav.
- [HotCRP: separate submission visibility from authorship authority](<resources/hotcrp-2026-contact-authorship-permission-boundary.md>) — HotCRP.
- [Microsoft compensating transactions: recovery must preserve valid concurrent state](<resources/microsoft-compensating-transaction-state-integrity.md>) — Microsoft Azure Architecture Center.
- [Microsoft Graph batching: preserve each member authorization outcome](<resources/microsoft-graph-batch-member-authorization-outcomes.md>) — Microsoft.
- [n8n: directory-attribute authority in durable account linking](<resources/n8n-2026-ldap-account-linking-authority.md>) — n8n.
- [n8n: refreshed authority must remain bound to the consented resource](<resources/n8n-2026-refresh-grant-resource-binding.md>) — n8n.
- [OpenFGA query consistency: authorization decisions need sufficiently fresh state](<resources/openfga-authorization-query-freshness.md>) — OpenFGA.
- [OpenFGA: policy intersections must preserve explicit exclusions](<resources/openfga-2026-composed-policy-exclusion-integrity.md>) — OpenFGA.
- [Outline: integration authority must end with its owning account](<resources/outline-2026-webhook-revocation-lifecycle.md>) — Outline.
- [OWASP Forgot Password](<resources/owasp-account-recovery-state-integrity.md>) — OWASP Cheat Sheet Series.
- [OWASP Secure Code Review: baseline and change-focused review](<resources/owasp-secure-code-review-methodology.md>) — OWASP Cheat Sheet Series.
- [OWASP Threat Modeling: system assumptions and mitigation validation](<resources/owasp-threat-modeling-assumptions-and-validation.md>) — OWASP Cheat Sheet Series.
- [OWASP Transaction Authorization](<resources/owasp-transaction-authorization-state-integrity.md>) — OWASP Cheat Sheet Series.
- [Paymenter: refund entitlement and ledger changes need one atomic transition](<resources/paymenter-2026-refund-transition-atomicity.md>) — Paymenter.
- [PostgreSQL 18: Transaction Isolation and Business Invariants](<resources/postgresql-transaction-isolation-business-invariants.md>) — PostgreSQL Global Development Group.
- [Pterodactyl: delegated tokens must preserve action-specific authority](<resources/pterodactyl-2026-delegated-token-purpose-binding.md>) — Pterodactyl.
- [Spree: cart association must retain guest-possession checks](<resources/spree-2026-guest-cart-association-authority.md>) — Spree.
- [Stripe webhooks: authentic delivery and business-state integrity](<resources/stripe-webhook-delivery-state-integrity.md>) — Stripe.
- [Sylius: order ownership does not confer payment-operation authority](<resources/sylius-2026-payment-action-authority.md>) — Sylius.
- [Sylius: promotion entitlement must be checked and consumed atomically](<resources/sylius-2026-promotion-limit-atomicity.md>) — Sylius.
- [Vendure: payment child objects must inherit order channel authority](<resources/vendure-2026-payment-child-object-channel-authority.md>) — Vendure.
- [Vikunja: saved favorites must recheck current project access](<resources/vikunja-2026-favorites-current-access-revalidation.md>) — Vikunja.
- [Vvveb: numeric input validity does not establish legitimate order state](<resources/vvveb-2026-order-domain-invariant.md>) — Vvveb.

<a id="topic-cloud-security"></a>
## Cloud Security

6 resources.

- [AWS IAM security best practices for workload identities](<resources/aws-iam-machine-identity-best-practices.md>) — Amazon Web Services.
- [GitHub internal metadata: preserve the boundary between user data and service authority](<resources/github-2026-internal-metadata-authority.md>) — Wiz Research.
- [NIST SP 800-190: Application Container Security Guide](<resources/nist-sp-800-190-container-isolation-guide.md>) — National Institute of Standards and Technology.
- [OWASP Server-Side Request Forgery Prevention](<resources/owasp-server-request-destination-boundaries.md>) — OWASP Cheat Sheet Series.
- [React2Shell response: parser consistency and layered remediation](<resources/vercel-react2shell-parser-normalization-defense.md>) — Vercel.
- [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<resources/usenix-2025-integration-platform-oauth-bindings.md>) — USENIX Association.

<a id="topic-identity"></a>
## Identity

39 resources.

- [Adversarial passkeys: account recovery must close every continuing source of authority](<resources/usenix-2026-passkey-remediation-authority-lifecycle.md>) — USENIX Association.
- [authentik: source-mapping edits carry identity-rebinding authority](<resources/authentik-2026-source-mapping-mutation-authority.md>) — authentik.
- [Authlib: error responses must preserve redirect-destination validation](<resources/authlib-2026-error-path-redirect-authority.md>) — Authlib.
- [AWS IAM security best practices for workload identities](<resources/aws-iam-machine-identity-best-practices.md>) — Amazon Web Services.
- [Better Auth SCIM: absent ownership must not grant shared authority](<resources/better-auth-2026-scim-ownerless-provider-authority.md>) — Better Auth.
- [Better Auth: incoming identity proof does not validate existing credentials](<resources/better-auth-2026-local-account-linking-verification.md>) — Better Auth.
- [Better Auth: single-use authorization requires atomic state consumption](<resources/better-auth-2026-authorization-code-consumption-integrity.md>) — Better Auth.
- [Bugsink: time-unit consistency in account-access token expiry](<resources/bugsink-2026-token-expiry-unit-integrity.md>) — Bugsink.
- [Chrome bfcache: restored pages and session-state boundaries](<resources/chrome-bfcache-restored-session-state.md>) — Google Chrome for Developers.
- [Cross-device authentication: bind informed consent to session authority](<resources/ndss-2026-cross-device-consent-and-session-control.md>) — Internet Society / NDSS Symposium.
- [Dolibarr portal accounts: credential writes need object authorization](<resources/dolibarr-2026-portal-object-authorization.md>) — CodeAnt AI.
- [FAPI 2\.0 Security Profile](<resources/openid-fapi-2-api-authorization-profile.md>) — OpenID Foundation.
- [Grav API: account-disable enforcement across session authenticators](<resources/grav-2026-session-account-state-revalidation.md>) — Grav.
- [HotCRP: separate submission visibility from authorship authority](<resources/hotcrp-2026-contact-authorship-permission-boundary.md>) — HotCRP.
- [Langflow: project transport authorization must reach each resource read](<resources/langflow-2026-mcp-resource-project-authorization.md>) — Langflow.
- [LibreChat: delegated credentials must remain bound to the initiating session](<resources/librechat-2026-mcp-oauth-session-binding.md>) — LibreChat.
- [MCP scope selection: progressive consent and accumulated authority](<resources/mcp-progressive-scope-authority.md>) — Model Context Protocol.
- [n8n Dynamic Credentials: authorize credential lifecycle operations](<resources/n8n-2026-dynamic-credential-object-authority.md>) — n8n.
- [n8n: directory-attribute authority in durable account linking](<resources/n8n-2026-ldap-account-linking-authority.md>) — n8n.
- [n8n: refreshed authority must remain bound to the consented resource](<resources/n8n-2026-refresh-grant-resource-binding.md>) — n8n.
- [Nhost: provider adapters must preserve identity-claim evidence](<resources/nhost-2026-provider-claim-verification-provenance.md>) — Nhost.
- [NIST SP 800-162: attribute authority and policy traceability](<resources/nist-sp-800-162-attribute-authority-modeling.md>) — National Institute of Standards and Technology.
- [Obot: preserve delegated token audience and consent boundaries](<resources/obot-2026-oauth-audience-and-consent-boundaries.md>) — Obot.
- [Open WebUI: credentials must bind to their destination connection](<resources/open-webui-2026-connection-credential-capture.md>) — Open WebUI.
- [Open WebUI: preserve role-policy meaning across identity flows](<resources/open-webui-2026-role-claim-provenance-and-revocation.md>) — Open WebUI.
- [Open WebUI: revocation must cross HTTP and realtime boundaries](<resources/open-webui-2026-realtime-revocation-consistency.md>) — Open WebUI.
- [Outline: integration authority must end with its owning account](<resources/outline-2026-webhook-revocation-lifecycle.md>) — Outline.
- [OWASP Forgot Password](<resources/owasp-account-recovery-state-integrity.md>) — OWASP Cheat Sheet Series.
- [OWASP Session Management: privilege-transition integrity](<resources/owasp-session-privilege-transition-integrity.md>) — OWASP Cheat Sheet Series.
- [pac4j JWT validation: confidentiality does not establish authenticity](<resources/pac4j-2026-token-authenticity-enforcement.md>) — CodeAnt AI.
- [Prowler SAML: retain validated tenant authority](<resources/prowler-2026-saml-tenant-issuance-binding.md>) — Prowler.
- [Pterodactyl: delegated tokens must preserve action-specific authority](<resources/pterodactyl-2026-delegated-token-purpose-binding.md>) — Pterodactyl.
- [RFC 10017: OAuth 2\.0 for Browser-Based Applications](<resources/rfc-10017-browser-oauth-token-custody.md>) — Internet Engineering Task Force / RFC Editor.
- [RFC 9700: Best Current Practice for OAuth 2\.0 Security](<resources/rfc-9700-oauth-security-best-current-practice.md>) — Internet Engineering Task Force / RFC Editor.
- [Rocket\.Chat: authentication must await a completed verification decision](<resources/rocketchat-2026-asynchronous-identity-verification.md>) — GitHub Security Lab.
- [samlify: signing does not establish claim provenance](<resources/samlify-2026-assertion-generation-claim-integrity.md>) — samlify.
- [Sentry: resource ownership must match the authorized organization](<resources/sentry-2026-organization-object-authorization.md>) — GitHub Security Lab.
- [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](<resources/usenix-2025-tls-resumption-identity-isolation.md>) — USENIX Association.
- [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<resources/usenix-2025-integration-platform-oauth-bindings.md>) — USENIX Association.

<a id="topic-interpreter-boundaries"></a>
## Interpreter Boundaries

3 resources.

- [Django: ORM alias metadata must not acquire query authority](<resources/django-2026-query-alias-structure-boundary.md>) — Django Software Foundation.
- [Python subprocess: executable, argument, and interpreter boundaries](<resources/python-subprocess-interpreter-boundaries.md>) — Python Software Foundation.
- [Serialize JavaScript: every serialized field must retain data semantics](<resources/serialize-javascript-2026-output-code-boundary.md>) — Yahoo serialize-javascript.

<a id="topic-memory-safety"></a>
## Memory Safety and Process Isolation

2 resources.

- [Chromium Rule of Two: input trust, memory safety and privilege](<resources/chromium-rule-of-two-input-isolation.md>) — Chromium Project.
- [Document Isolation Policy: process separation and residual authority](<resources/chrome-document-isolation-policy-boundaries.md>) — Google Chrome for Developers.

<a id="topic-reporting"></a>
## Reporting

2 resources.

- [OWASP Logging: trustworthy and minimal application evidence](<resources/owasp-security-logging-evidence-quality.md>) — OWASP Cheat Sheet Series.
- [Quality Reports](<resources/hackerone-quality-vulnerability-reports.md>) — HackerOne Help Center.

<a id="topic-supply-chain"></a>
## Software Supply Chain

2 resources.

- [NIST SP 800-190: Application Container Security Guide](<resources/nist-sp-800-190-container-isolation-guide.md>) — National Institute of Standards and Technology.
- [SLSA v1\.2: supply-chain security and build provenance](<resources/slsa-v1-2-supply-chain-build-provenance.md>) — SLSA Community.

<a id="topic-verification"></a>
## Verification

23 resources.

- [Astro: composable dispatch must preserve mandatory origin checks](<resources/astro-2026-composable-dispatch-origin-enforcement.md>) — Astro.
- [Axios: enforce upload budgets across transport implementations](<resources/axios-2026-streamed-upload-budget-enforcement.md>) — Axios.
- [Chromium Rule of Two: input trust, memory safety and privilege](<resources/chromium-rule-of-two-input-isolation.md>) — Chromium Project.
- [Django: ORM alias metadata must not acquire query authority](<resources/django-2026-query-alias-structure-boundary.md>) — Django Software Foundation.
- [Error Handling Cheat Sheet](<resources/owasp-error-response-data-minimization.md>) — OWASP Cheat Sheet Series.
- [mailcow: stored configuration retains its original trust level](<resources/mailcow-2026-persisted-data-query-boundary.md>) — mailcow.
- [Nuxt: island data must not acquire component-selection authority](<resources/nuxt-2026-island-component-selection-authority.md>) — Nuxt.
- [Nuxt: rendered-data caches must preserve request authorization](<resources/nuxt-2026-rendered-payload-cache-authorization.md>) — Nuxt.
- [OWASP Application Security Verification Standard \(ASVS\)](<resources/owasp-asvs-5-security-verification-standard.md>) — OWASP Foundation.
- [OWASP Logging: trustworthy and minimal application evidence](<resources/owasp-security-logging-evidence-quality.md>) — OWASP Cheat Sheet Series.
- [OWASP Secure Code Review: baseline and change-focused review](<resources/owasp-secure-code-review-methodology.md>) — OWASP Cheat Sheet Series.
- [OWASP Threat Modeling: system assumptions and mitigation validation](<resources/owasp-threat-modeling-assumptions-and-validation.md>) — OWASP Cheat Sheet Series.
- [Parse Server: preserve safe file interpretation across storage and browsers](<resources/parse-server-2026-upload-metadata-consumer-boundary.md>) — Parse Community.
- [pypdf: bound repeated work when reading embedded attachments](<resources/pypdf-2026-attachment-processing-cost-boundary.md>) — py-pdf / pypdf.
- [Qwik: resumability metadata must preserve HTML serialization boundaries](<resources/qwik-2026-resumability-comment-serialization-boundary.md>) — QwikDev.
- [React Router: hydrated error metadata must not select client behavior](<resources/react-router-2026-hydration-error-constructor-boundary.md>) — React Router / Remix.
- [React2Shell response: parser consistency and layered remediation](<resources/vercel-react2shell-parser-normalization-defense.md>) — Vercel.
- [Serialize JavaScript: every serialized field must retain data semantics](<resources/serialize-javascript-2026-output-code-boundary.md>) — Yahoo serialize-javascript.
- [SLSA v1\.2: supply-chain security and build provenance](<resources/slsa-v1-2-supply-chain-build-provenance.md>) — SLSA Community.
- [TYPO3: configured upload policy must reach the runtime validator](<resources/typo3-2026-upload-validator-lifecycle-boundary.md>) — TYPO3.
- [Upstream HTTP framing and parser-consistency boundaries](<resources/portswigger-2025-upstream-http-framing-boundaries.md>) — PortSwigger.
- [Vvveb: numeric input validity does not establish legitimate order state](<resources/vvveb-2026-order-domain-invariant.md>) — Vvveb.
- [Web cache key precision and capacity isolation](<resources/arxiv-2026-cache-key-precision-and-capacity.md>) — arXiv.

<a id="topic-web-foundations"></a>
## Web Foundations

53 resources.

- [Adversarial passkeys: account recovery must close every continuing source of authority](<resources/usenix-2026-passkey-remediation-authority-lifecycle.md>) — USENIX Association.
- [Angular host bindings: bind sanitization to the concrete output element](<resources/angular-2026-host-binding-context-authority.md>) — Angular.
- [Angular SSR: preserve output context through serialization and post-processing](<resources/angular-2026-raw-content-serialization-context.md>) — Angular.
- [Apollo Federation: preserving the router-to-subgraph boundary](<resources/apollo-2026-federation-router-subgraph-isolation.md>) — Apollo GraphQL.
- [Astro: composable dispatch must preserve mandatory origin checks](<resources/astro-2026-composable-dispatch-origin-enforcement.md>) — Astro.
- [Astro: routing and authorization must agree on resource identity](<resources/astro-2026-route-normalization-authorization-consistency.md>) — Astro.
- [Axios: enforce upload budgets across transport implementations](<resources/axios-2026-streamed-upload-budget-enforcement.md>) — Axios.
- [Chrome bfcache: restored pages and session-state boundaries](<resources/chrome-bfcache-restored-session-state.md>) — Google Chrome for Developers.
- [Chrome Local Network Access: separate browser reachability from site authority](<resources/chrome-local-network-permission-boundaries.md>) — Google Chrome for Developers.
- [Cross-device authentication: bind informed consent to session authority](<resources/ndss-2026-cross-device-consent-and-session-control.md>) — Internet Society / NDSS Symposium.
- [Django: ORM alias metadata must not acquire query authority](<resources/django-2026-query-alias-structure-boundary.md>) — Django Software Foundation.
- [Document Isolation Policy: process separation and residual authority](<resources/chrome-document-isolation-policy-boundaries.md>) — Google Chrome for Developers.
- [Error Handling Cheat Sheet](<resources/owasp-error-response-data-minimization.md>) — OWASP Cheat Sheet Series.
- [Fetch Metadata Request Headers](<resources/w3c-fetch-metadata-request-context-boundaries.md>) — World Wide Web Consortium.
- [Frappe: linked data must preserve document and field permissions](<resources/frappe-2026-linked-document-response-authorization.md>) — GitHub Security Lab.
- [GitHub internal metadata: preserve the boundary between user data and service authority](<resources/github-2026-internal-metadata-authority.md>) — Wiz Research.
- [Google AIP-158: pagination continuation does not grant resource authority](<resources/google-aip-158-pagination-authorization-boundary.md>) — Google.
- [Google API field masks: preserve server-owned and immutable state](<resources/google-aip-161-update-field-authority.md>) — Google.
- [Google API request identity: bind retry semantics to the logical operation](<resources/google-aip-155-request-identity-contract.md>) — Google.
- [GraphQL-Ruby: authorization exceptions must stop execution](<resources/graphql-ruby-2026-authorization-exception-integrity.md>) — GitHub Security Lab.
- [HTML COOP: opener separation and same-origin authority](<resources/whatwg-coop-opener-and-origin-authority.md>) — WHATWG.
- [HTML5 Security Cheat Sheet: Web Messaging](<resources/owasp-browser-message-trust-boundaries.md>) — OWASP Cheat Sheet Series.
- [mailcow: stored configuration retains its original trust level](<resources/mailcow-2026-persisted-data-query-boundary.md>) — mailcow.
- [MLflow: authorization must survive alternate resource interfaces](<resources/mlflow-2026-alternate-interface-authorization-consistency.md>) — Tachyon.
- [Next\.js data security: server authorization and client-visible data](<resources/nextjs-server-client-data-security.md>) — Next\.js / Vercel.
- [Nuxt: island data must not acquire component-selection authority](<resources/nuxt-2026-island-component-selection-authority.md>) — Nuxt.
- [Nuxt: rendered-data caches must preserve request authorization](<resources/nuxt-2026-rendered-payload-cache-authorization.md>) — Nuxt.
- [Open WebUI: revocation must cross HTTP and realtime boundaries](<resources/open-webui-2026-realtime-revocation-consistency.md>) — Open WebUI.
- [OWASP LLM05:2025: generated-output consumer trust](<resources/owasp-llm-output-consumer-trust.md>) — OWASP Gen AI Security Project.
- [OWASP Server-Side Request Forgery Prevention](<resources/owasp-server-request-destination-boundaries.md>) — OWASP Cheat Sheet Series.
- [OWASP Session Management: privilege-transition integrity](<resources/owasp-session-privilege-transition-integrity.md>) — OWASP Cheat Sheet Series.
- [Parse Server: preserve safe file interpretation across storage and browsers](<resources/parse-server-2026-upload-metadata-consumer-boundary.md>) — Parse Community.
- [Permissions Policy: inherited browser-feature authority across embedded documents](<resources/w3c-permissions-policy-embedded-feature-authority.md>) — World Wide Web Consortium.
- [pypdf: bound repeated work when reading embedded attachments](<resources/pypdf-2026-attachment-processing-cost-boundary.md>) — py-pdf / pypdf.
- [Qwik: resumability metadata must preserve HTML serialization boundaries](<resources/qwik-2026-resumability-comment-serialization-boundary.md>) — QwikDev.
- [React Router: hydrated error metadata must not select client behavior](<resources/react-router-2026-hydration-error-constructor-boundary.md>) — React Router / Remix.
- [React2Shell response: parser consistency and layered remediation](<resources/vercel-react2shell-parser-normalization-defense.md>) — Vercel.
- [RFC 10017: OAuth 2\.0 for Browser-Based Applications](<resources/rfc-10017-browser-oauth-token-custody.md>) — Internet Engineering Task Force / RFC Editor.
- [Rocket\.Chat: authentication must await a completed verification decision](<resources/rocketchat-2026-asynchronous-identity-verification.md>) — GitHub Security Lab.
- [Serialize JavaScript: every serialized field must retain data semantics](<resources/serialize-javascript-2026-output-code-boundary.md>) — Yahoo serialize-javascript.
- [Spree: guest ownership still requires an authorization proof](<resources/spree-2026-guest-order-authorization-proof.md>) — GitHub Security Lab.
- [Steeltoe: diagnostic URI masking must cover the complete data contract](<resources/steeltoe-2026-diagnostic-uri-data-minimization.md>) — Steeltoe.
- [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](<resources/usenix-2025-tls-resumption-identity-isolation.md>) — USENIX Association.
- [Svelte hydration: serialization must preserve the enclosing output context](<resources/svelte-2026-hydration-output-context-boundary.md>) — Camilo Vera.
- [SvelteKit: origin construction and routing must preserve server request authority](<resources/sveltekit-2026-origin-routing-trust-boundary.md>) — zhero\_web\_security.
- [Sylius: component integrity does not authorize referenced objects](<resources/sylius-2026-component-argument-object-authorization.md>) — GitHub Security Lab.
- [Trusted Types: typed sinks depend on trustworthy policy creation](<resources/w3c-2026-trusted-types-policy-authority.md>) — World Wide Web Consortium.
- [TYPO3: configured upload policy must reach the runtime validator](<resources/typo3-2026-upload-validator-lifecycle-boundary.md>) — TYPO3.
- [Umbraco: editing an account does not authorize assigning every role](<resources/umbraco-2026-group-assignment-authority.md>) — GitHub Security Lab.
- [Upstream HTTP framing and parser-consistency boundaries](<resources/portswigger-2025-upstream-http-framing-boundaries.md>) — PortSwigger.
- [Web cache key precision and capacity isolation](<resources/arxiv-2026-cache-key-precision-and-capacity.md>) — arXiv.
- [Web Security Academy: Free Online Training from PortSwigger](<resources/portswigger-web-security-academy-controlled-training.md>) — PortSwigger.
- [Zammad: overridden serialization must preserve group authorization](<resources/zammad-2026-asset-serialization-group-authorization.md>) — GitHub Security Lab.
