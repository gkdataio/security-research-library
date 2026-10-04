# Authorization and tenant boundaries

[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)

**Vulnerability family** · 34 reports · 82 related resources · 10 diagrams

Object, role, account, and tenant access-control design.

Report membership uses the existing primary or secondary category authorization. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.

On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)

<a id="reports"></a>
## Reports

- [Actifio driver execution exposed excessive shared-service authority](<../reports/google-actifio-driver-service-identity-isolation-2025.md>) — Google; secondary category.
- [Angular automation trust and cache isolation weakness](<../reports/angular-ci-cache-trust-2026.md>) — Google; secondary category.
- [Cloud Build approval was not bound to immutable code](<../reports/google-cloud-build-approval-toctou-2025.md>) — Google; secondary category.
- [Facebook phone linking lacked account-specific authorization](<../reports/facebook-phone-linking-account-authorization-2013.md>) — Meta \(Facebook\); primary category.
- [Framework serialization change exposed private HackerOne user attributes](<../reports/hackerone-report-json-serialization-data-exposure-2025.md>) — HackerOne; secondary category.
- [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](<../reports/google-gemini-enterprise-connected-content-memory-integrity-2026.md>) — Google; secondary category.
- [GitHub Actions trust depended on invalid repository references](<../reports/github-actions-reference-validation-2021.md>) — GitHub; secondary category.
- [GitHub comparison output lacked source-repository authorization](<../reports/github-cross-repository-comparison-authorization-2025.md>) — GitHub; primary category.
- [GitHub fork collaboration applied inconsistent authorization](<../reports/github-fork-collaboration-authorization-2021.md>) — GitHub; primary category.
- [GitHub GraphQL collaboration changes lacked author consent](<../reports/github-fork-collaboration-consent-2021.md>) — GitHub; primary category.
- [GitHub OAuth consent failed across request-method semantics](<../reports/github-oauth-method-semantics-2019.md>) — GitHub; primary category.
- [GitHub runner-image builds shared persistent infrastructure with untrusted workflows](<../reports/github-runner-image-build-isolation-2023.md>) — GitHub; secondary category.
- [GitLab recovery delivery lacked verified-address binding](<../reports/gitlab-recovery-address-binding-cve-2023-7028.md>) — GitLab; secondary category.
- [Google Application Integration mixed resource and service authority](<../reports/google-application-integration-authorization-boundaries-2026.md>) — Google; primary category.
- [Google device grants lost client and permission binding](<../reports/google-device-authorization-client-scope-binding-2026.md>) — Google; secondary category.
- [Google Firefly confused worker authority and storage boundaries](<../reports/google-firefly-worker-authority-storage-boundary-2026.md>) — Google; primary category.
- [Google Mamba temporary outputs lacked access isolation](<../reports/google-mamba-temporary-output-isolation-2026.md>) — Google; primary category.
- [Google support API exposed customer and agent data](<../reports/google-support-api-authorization-2026.md>) — Google; primary category.
- [GraphQL object authorization exposed private-program metadata](<../reports/hackerone-private-program-graphql-object-authorization-2025.md>) — HackerOne; primary category.
- [HackerOne exports omitted internal-attachment authorization](<../reports/hackerone-export-attachment-authorization-2016.md>) — HackerOne; primary category.
- [Instagram client configuration exposed an application credential](<../reports/instagram-application-credential-client-containment-2022.md>) — Meta; secondary category.
- [Instagram embedding fallback changed the authorization context](<../reports/instagram-embedding-privileged-fallback-2023.md>) — Meta; primary category.
- [Kestrel HTTP framing differed across proxy and application boundaries](<../reports/microsoft-kestrel-http-framing-consistency-2025.md>) — Microsoft; secondary category.
- [LiteSpeed Cache privileged user simulation relied on weak security tokens](<../reports/litespeed-cache-user-simulation-authentication-2024.md>) — LiteSpeed Technologies; secondary category.
- [Meta Accounts Center linking lost credential and identity confinement](<../reports/meta-accounts-center-linking-credential-confinement-2024.md>) — Meta; secondary category.
- [Meta AI media access lacked object-ownership authorization](<../reports/meta-ai-media-object-authorization-2025.md>) — Meta; primary category.
- [Meta Pixel cross-window handling lost message and token authority](<../reports/meta-pixel-cross-window-authority-binding-2024.md>) — Meta; primary category.
- [Meta Quest login migration lost OAuth credential confinement](<../reports/meta-quest-oauth-redirect-confidentiality-2022.md>) — Meta; secondary category.
- [Meta service-identity exposure amplified by excessive secret access](<../reports/meta-service-identity-secrets-trust-boundary-2026.md>) — Meta; secondary category.
- [Shopify automatic account conversion lost merchant-consent binding](<../reports/shopify-collaborator-conversion-consent-2017.md>) — Shopify; primary category.
- [Sign in with Apple failed to bind identity claims to the authenticated user](<../reports/apple-sign-in-identity-claim-binding-2020.md>) — Apple; primary category.
- [Support integration exposed internal Confluence documentation](<../reports/hackerone-support-confluence-access-boundary-2025.md>) — HackerOne; primary category.
- [YouTube and Pixel Recorder exposed cross-product identity links](<../reports/youtube-pixel-recorder-identity-privacy-2025.md>) — Google; primary category.
- [YouTube creator metadata exposed private email addresses](<../reports/youtube-creator-email-authorization-2025.md>) — Google; primary category.

<a id="related-learning"></a>
## Related learning

Included by the topic crosswalk or an explicit resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.

- [Adversarial passkeys: account recovery must close every continuing source of authority](<../resources/usenix-2026-passkey-remediation-authority-lifecycle.md>) — topic: Authorization.
- [Apollo Federation: preserving the router-to-subgraph boundary](<../resources/apollo-2026-federation-router-subgraph-isolation.md>) — topic: Authorization.
- [Astro: routing and authorization must agree on resource identity](<../resources/astro-2026-route-normalization-authorization-consistency.md>) — topic: Authorization.
- [authentik: source-mapping edits carry identity-rebinding authority](<../resources/authentik-2026-source-mapping-mutation-authority.md>) — topic: Authorization.
- [Authlib: error responses must preserve redirect-destination validation](<../resources/authlib-2026-error-path-redirect-authority.md>) — topic: Authorization.
- [Authorization Cheat Sheet](<../resources/owasp-authorization-cheat-sheet.md>) — topic: Authorization; diagram: [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>), [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>), [Combined views preserve every source's access boundary](<../diagram-gallery.md#combined-view-source-authorization>), [Fallbacks must preserve the original caller's authority](<../diagram-gallery.md#fallback-requester-authorization>).
- [AWS IAM security best practices for workload identities](<../resources/aws-iam-machine-identity-best-practices.md>) — topic: Authorization; diagram: [Keep workload authority tenant-scoped](<../diagram-gallery.md#workload-identity-tenant-scope>).
- [Better Auth SCIM: absent ownership must not grant shared authority](<../resources/better-auth-2026-scim-ownerless-provider-authority.md>) — topic: Authorization.
- [Better Auth: incoming identity proof does not validate existing credentials](<../resources/better-auth-2026-local-account-linking-verification.md>) — topic: Authorization.
- [Better Auth: single-use authorization requires atomic state consumption](<../resources/better-auth-2026-authorization-code-consumption-integrity.md>) — topic: Authorization.
- [Bugsink: time-unit consistency in account-access token expiry](<../resources/bugsink-2026-token-expiry-unit-integrity.md>) — topic: Authorization.
- [Coder: privileged provisioning must preserve existing object ownership](<../resources/coder-2026-provisioned-object-ownership-integrity.md>) — topic: Authorization.
- [Cross-device authentication: bind informed consent to session authority](<../resources/ndss-2026-cross-device-consent-and-session-control.md>) — topic: Authorization.
- [Dify: telemetry destination changes carry tenant data-disclosure authority](<../resources/dify-2026-tracing-configuration-tenant-authority.md>) — topic: Authorization.
- [Directus: denied mutations must leave dependent state unchanged](<../resources/directus-2026-preauthorization-side-effect-integrity.md>) — topic: Authorization.
- [Dolibarr portal accounts: credential writes need object authorization](<../resources/dolibarr-2026-portal-object-authorization.md>) — topic: Authorization.
- [FAPI 2\.0 Security Profile](<../resources/openid-fapi-2-api-authorization-profile.md>) — topic: Authorization.
- [Fetch Metadata Request Headers](<../resources/w3c-fetch-metadata-request-context-boundaries.md>) — topic: Authorization.
- [File Browser: existing shares must follow current owner permissions](<../resources/filebrowser-2026-share-owner-permission-lifecycle.md>) — topic: Authorization.
- [Frappe: linked data must preserve document and field permissions](<../resources/frappe-2026-linked-document-response-authorization.md>) — topic: Authorization; diagram: [Combined views preserve every source's access boundary](<../diagram-gallery.md#combined-view-source-authorization>).
- [GitHub internal metadata: preserve the boundary between user data and service authority](<../resources/github-2026-internal-metadata-authority.md>) — topic: Authorization.
- [Google AIP-158: pagination continuation does not grant resource authority](<../resources/google-aip-158-pagination-authorization-boundary.md>) — topic: Authorization.
- [Google API field masks: preserve server-owned and immutable state](<../resources/google-aip-161-update-field-authority.md>) — topic: Authorization.
- [GraphQL-Ruby: authorization exceptions must stop execution](<../resources/graphql-ruby-2026-authorization-exception-integrity.md>) — topic: Authorization.
- [Grav API: account-disable enforcement across session authenticators](<../resources/grav-2026-session-account-state-revalidation.md>) — topic: Authorization.
- [HotCRP: separate submission visibility from authorship authority](<../resources/hotcrp-2026-contact-authorship-permission-boundary.md>) — topic: Authorization.
- [HTML COOP: opener separation and same-origin authority](<../resources/whatwg-coop-opener-and-origin-authority.md>) — topic: Authorization.
- [HTML5 Security Cheat Sheet: Web Messaging](<../resources/owasp-browser-message-trust-boundaries.md>) — topic: Authorization; diagram: [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>).
- [Langflow: project transport authorization must reach each resource read](<../resources/langflow-2026-mcp-resource-project-authorization.md>) — topic: Authorization.
- [LibreChat: agent edit authority must cover attached context](<../resources/librechat-2026-agent-context-mutation-authority.md>) — topic: Authorization.
- [LibreChat: delegated credentials must remain bound to the initiating session](<../resources/librechat-2026-mcp-oauth-session-binding.md>) — topic: Authorization.
- [LibreChat: viewing an integration must not reveal its service secrets](<../resources/librechat-2026-mcp-view-secret-projection.md>) — topic: Authorization.
- [LLM Prompt Injection Prevention Cheat Sheet](<../resources/owasp-llm-prompt-injection-prevention.md>) — diagram: [Retrieved content is data, not authority](<../diagram-gallery.md#ai-content-authority-separation>).
- [LobeHub: knowledge-base membership changes require ownership authorization](<../resources/lobehub-2026-knowledge-membership-mutation-authority.md>) — topic: Authorization.
- [MCP elicitation: consent, credential custody and completion](<../resources/mcp-elicitation-consent-credential-custody.md>) — topic: Authorization.
- [MCP scope selection: progressive consent and accumulated authority](<../resources/mcp-progressive-scope-authority.md>) — topic: Authorization.
- [Microsoft Graph batching: preserve each member authorization outcome](<../resources/microsoft-graph-batch-member-authorization-outcomes.md>) — topic: Authorization.
- [MLflow: authorization must survive alternate resource interfaces](<../resources/mlflow-2026-alternate-interface-authorization-consistency.md>) — topic: Authorization.
- [MythicalDash: payment evidence must establish credit entitlement](<../resources/mythicaldash-2026-payment-evidence-entitlement.md>) — topic: Authorization.
- [n8n Dynamic Credentials: authorize credential lifecycle operations](<../resources/n8n-2026-dynamic-credential-object-authority.md>) — topic: Authorization.
- [n8n: directory-attribute authority in durable account linking](<../resources/n8n-2026-ldap-account-linking-authority.md>) — topic: Authorization.
- [n8n: refreshed authority must remain bound to the consented resource](<../resources/n8n-2026-refresh-grant-resource-binding.md>) — topic: Authorization.
- [Next\.js data security: server authorization and client-visible data](<../resources/nextjs-server-client-data-security.md>) — topic: Authorization; diagram: [Server disclosure and browser interpretation](<../diagram-gallery.md#server-client-data-consumer-boundaries>).
- [Nhost: provider adapters must preserve identity-claim evidence](<../resources/nhost-2026-provider-claim-verification-provenance.md>) — topic: Authorization.
- [NIST SP 800-162: attribute authority and policy traceability](<../resources/nist-sp-800-162-attribute-authority-modeling.md>) — topic: Authorization.
- [Nuxt: rendered-data caches must preserve request authorization](<../resources/nuxt-2026-rendered-payload-cache-authorization.md>) — topic: Authorization.
- [OAuth2 Proxy: client-address provenance must precede authentication exemptions](<../resources/oauth2-proxy-2026-client-address-provenance-authority.md>) — topic: Authorization.
- [Obot: preserve delegated token audience and consent boundaries](<../resources/obot-2026-oauth-audience-and-consent-boundaries.md>) — topic: Authorization.
- [Open WebUI: credentials must bind to their destination connection](<../resources/open-webui-2026-connection-credential-capture.md>) — topic: Authorization.
- [Open WebUI: preserve role-policy meaning across identity flows](<../resources/open-webui-2026-role-claim-provenance-and-revocation.md>) — topic: Authorization.
- [Open WebUI: revocation must cross HTTP and realtime boundaries](<../resources/open-webui-2026-realtime-revocation-consistency.md>) — topic: Authorization.
- [OpenFGA query consistency: authorization decisions need sufficiently fresh state](<../resources/openfga-authorization-query-freshness.md>) — topic: Authorization.
- [OpenFGA: policy intersections must preserve explicit exclusions](<../resources/openfga-2026-composed-policy-exclusion-integrity.md>) — topic: Authorization.
- [Outline: integration authority must end with its owning account](<../resources/outline-2026-webhook-revocation-lifecycle.md>) — topic: Authorization.
- [OWASP Forgot Password](<../resources/owasp-account-recovery-state-integrity.md>) — diagram: [Recovery must preserve account ownership](<../diagram-gallery.md#account-recovery-challenge-lifecycle>).
- [OWASP LLM05:2025: generated-output consumer trust](<../resources/owasp-llm-output-consumer-trust.md>) — diagram: [Server disclosure and browser interpretation](<../diagram-gallery.md#server-client-data-consumer-boundaries>).
- [OWASP LLM08:2025: retrieval permissions and knowledge provenance](<../resources/owasp-rag-retrieval-permission-boundaries.md>) — topic: Authorization.
- [OWASP Session Management: privilege-transition integrity](<../resources/owasp-session-privilege-transition-integrity.md>) — topic: Authorization.
- [OWASP Transaction Authorization](<../resources/owasp-transaction-authorization-state-integrity.md>) — topic: Authorization; diagram: [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>).
- [pac4j JWT validation: confidentiality does not establish authenticity](<../resources/pac4j-2026-token-authenticity-enforcement.md>) — topic: Authorization.
- [Paymenter: refund entitlement and ledger changes need one atomic transition](<../resources/paymenter-2026-refund-transition-atomicity.md>) — topic: Authorization.
- [Permissions Policy: inherited browser-feature authority across embedded documents](<../resources/w3c-permissions-policy-embedded-feature-authority.md>) — topic: Authorization.
- [Prowler SAML: retain validated tenant authority](<../resources/prowler-2026-saml-tenant-issuance-binding.md>) — topic: Authorization.
- [Pterodactyl: delegated tokens must preserve action-specific authority](<../resources/pterodactyl-2026-delegated-token-purpose-binding.md>) — topic: Authorization.
- [RFC 10017: OAuth 2\.0 for Browser-Based Applications](<../resources/rfc-10017-browser-oauth-token-custody.md>) — topic: Authorization.
- [RFC 9700: Best Current Practice for OAuth 2\.0 Security](<../resources/rfc-9700-oauth-security-best-current-practice.md>) — diagram: [An identity claim must belong to the user](<../diagram-gallery.md#identity-claim-binding>).
- [samlify: signing does not establish claim provenance](<../resources/samlify-2026-assertion-generation-claim-integrity.md>) — topic: Authorization.
- [Sentry: resource ownership must match the authorized organization](<../resources/sentry-2026-organization-object-authorization.md>) — topic: Authorization.
- [SLSA v1\.2: supply-chain security and build provenance](<../resources/slsa-v1-2-supply-chain-build-provenance.md>) — diagram: [Build evidence must match the artifact and trusted builder](<../diagram-gallery.md#build-artifact-provenance-boundary>).
- [Spree: cart association must retain guest-possession checks](<../resources/spree-2026-guest-cart-association-authority.md>) — topic: Authorization.
- [Spree: guest ownership still requires an authorization proof](<../resources/spree-2026-guest-order-authorization-proof.md>) — topic: Authorization.
- [Steeltoe: diagnostic URI masking must cover the complete data contract](<../resources/steeltoe-2026-diagnostic-uri-data-minimization.md>) — topic: Authorization.
- [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](<../resources/usenix-2025-tls-resumption-identity-isolation.md>) — topic: Authorization.
- [Storage Access API: permission, document activation and cookie eligibility](<../resources/privacycg-storage-access-permission-activation-boundary.md>) — topic: Authorization.
- [Sylius: component integrity does not authorize referenced objects](<../resources/sylius-2026-component-argument-object-authorization.md>) — topic: Authorization.
- [Sylius: order ownership does not confer payment-operation authority](<../resources/sylius-2026-payment-action-authority.md>) — topic: Authorization.
- [Umbraco: editing an account does not authorize assigning every role](<../resources/umbraco-2026-group-assignment-authority.md>) — topic: Authorization.
- [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<../resources/usenix-2025-integration-platform-oauth-bindings.md>) — topic: Authorization.
- [Vendure: payment child objects must inherit order channel authority](<../resources/vendure-2026-payment-child-object-channel-authority.md>) — topic: Authorization.
- [Vercel React Router: session identity must not select unrestricted storage authority](<../resources/vercel-react-router-2026-session-storage-key-authority.md>) — topic: Authorization.
- [Vikunja: saved favorites must recheck current project access](<../resources/vikunja-2026-favorites-current-access-revalidation.md>) — topic: Authorization.
- [Zammad: overridden serialization must preserve group authorization](<../resources/zammad-2026-asset-serialization-group-authorization.md>) — topic: Authorization.

<a id="conceptual-diagrams"></a>
## Conceptual diagrams

Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.

- [An identity claim must belong to the user](<../diagram-gallery.md#identity-claim-binding>)
- [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>)
- [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>)
- [Build evidence must match the artifact and trusted builder](<../diagram-gallery.md#build-artifact-provenance-boundary>)
- [Combined views preserve every source's access boundary](<../diagram-gallery.md#combined-view-source-authorization>)
- [Fallbacks must preserve the original caller's authority](<../diagram-gallery.md#fallback-requester-authorization>)
- [Keep workload authority tenant-scoped](<../diagram-gallery.md#workload-identity-tenant-scope>)
- [Recovery must preserve account ownership](<../diagram-gallery.md#account-recovery-challenge-lifecycle>)
- [Retrieved content is data, not authority](<../diagram-gallery.md#ai-content-authority-separation>)
- [Server disclosure and browser interpretation](<../diagram-gallery.md#server-client-data-consumer-boundaries>)

---

Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).
