# Authentication and identity

[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)

**Vulnerability family** · 16 reports · 40 related resources · 4 diagrams

Account lifecycle, session integrity, identity-provider trust.

Report membership uses the existing primary or secondary category authentication. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.

On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)

<a id="reports"></a>
## Reports

- [Facebook phone linking lacked account-specific authorization](<../reports/facebook-phone-linking-account-authorization-2013.md>) — Meta \(Facebook\); secondary category.
- [Facebook SDK message authentication relied on insecure randomness](<../reports/facebook-sdk-message-authentication-randomness-2023.md>) — Meta; primary category.
- [GitHub OAuth consent failed across request-method semantics](<../reports/github-oauth-method-semantics-2019.md>) — GitHub; secondary category.
- [GitLab recovery delivery lacked verified-address binding](<../reports/gitlab-recovery-address-binding-cve-2023-7028.md>) — GitLab; primary category.
- [Google device grants lost client and permission binding](<../reports/google-device-authorization-client-scope-binding-2026.md>) — Google; primary category.
- [Instagram mobile account recovery had inconsistent verification limits](<../reports/instagram-mobile-recovery-attempt-limits-2019.md>) — Facebook / Instagram; primary category.
- [Instagram recovery challenges were insufficiently bound to accounts](<../reports/instagram-recovery-challenge-account-binding-2019.md>) — Facebook / Instagram; primary category.
- [LiteSpeed Cache privileged user simulation relied on weak security tokens](<../reports/litespeed-cache-user-simulation-authentication-2024.md>) — LiteSpeed Technologies; primary category.
- [Meta account verification weakened linked SMS authentication state](<../reports/meta-account-verification-attempt-state-binding-2022.md>) — Meta; primary category.
- [Meta Accounts Center linking lost credential and identity confinement](<../reports/meta-accounts-center-linking-credential-confinement-2024.md>) — Meta; primary category.
- [Meta Pixel cross-window handling lost message and token authority](<../reports/meta-pixel-cross-window-authority-binding-2024.md>) — Meta; secondary category.
- [Meta Quest login migration lost OAuth credential confinement](<../reports/meta-quest-oauth-redirect-confidentiality-2022.md>) — Meta; primary category.
- [Meta service-identity exposure amplified by excessive secret access](<../reports/meta-service-identity-secrets-trust-boundary-2026.md>) — Meta; secondary category.
- [Microsoft account recovery lacked consistent attempt-limit enforcement](<../reports/microsoft-account-recovery-rate-limit-consistency-2021.md>) — Microsoft; primary category.
- [Pixel lock-screen completion lost security-state binding](<../reports/google-pixel-lock-screen-state-binding-2022.md>) — Google; primary category.
- [Shopify automatic account conversion lost merchant-consent binding](<../reports/shopify-collaborator-conversion-consent-2017.md>) — Shopify; secondary category.

<a id="related-learning"></a>
## Related learning

Included by the topic crosswalk or an explicit resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.

- [Adversarial passkeys: account recovery must close every continuing source of authority](<../resources/usenix-2026-passkey-remediation-authority-lifecycle.md>) — topic: Identity.
- [authentik: source-mapping edits carry identity-rebinding authority](<../resources/authentik-2026-source-mapping-mutation-authority.md>) — topic: Identity.
- [Authlib: error responses must preserve redirect-destination validation](<../resources/authlib-2026-error-path-redirect-authority.md>) — topic: Identity.
- [Authorization Cheat Sheet](<../resources/owasp-authorization-cheat-sheet.md>) — diagram: [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>).
- [AWS IAM security best practices for workload identities](<../resources/aws-iam-machine-identity-best-practices.md>) — topic: Identity; diagram: [Keep workload authority tenant-scoped](<../diagram-gallery.md#workload-identity-tenant-scope>).
- [Better Auth SCIM: absent ownership must not grant shared authority](<../resources/better-auth-2026-scim-ownerless-provider-authority.md>) — topic: Identity.
- [Better Auth: incoming identity proof does not validate existing credentials](<../resources/better-auth-2026-local-account-linking-verification.md>) — topic: Identity.
- [Better Auth: single-use authorization requires atomic state consumption](<../resources/better-auth-2026-authorization-code-consumption-integrity.md>) — topic: Identity.
- [Bugsink: time-unit consistency in account-access token expiry](<../resources/bugsink-2026-token-expiry-unit-integrity.md>) — topic: Identity.
- [Chrome bfcache: restored pages and session-state boundaries](<../resources/chrome-bfcache-restored-session-state.md>) — topic: Identity.
- [Cross-device authentication: bind informed consent to session authority](<../resources/ndss-2026-cross-device-consent-and-session-control.md>) — topic: Identity.
- [Dolibarr portal accounts: credential writes need object authorization](<../resources/dolibarr-2026-portal-object-authorization.md>) — topic: Identity.
- [FAPI 2\.0 Security Profile](<../resources/openid-fapi-2-api-authorization-profile.md>) — topic: Identity.
- [Grav API: account-disable enforcement across session authenticators](<../resources/grav-2026-session-account-state-revalidation.md>) — topic: Identity.
- [HotCRP: separate submission visibility from authorship authority](<../resources/hotcrp-2026-contact-authorship-permission-boundary.md>) — topic: Identity.
- [HTML5 Security Cheat Sheet: Web Messaging](<../resources/owasp-browser-message-trust-boundaries.md>) — diagram: [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>).
- [Langflow: project transport authorization must reach each resource read](<../resources/langflow-2026-mcp-resource-project-authorization.md>) — topic: Identity.
- [LibreChat: delegated credentials must remain bound to the initiating session](<../resources/librechat-2026-mcp-oauth-session-binding.md>) — topic: Identity.
- [MCP scope selection: progressive consent and accumulated authority](<../resources/mcp-progressive-scope-authority.md>) — topic: Identity.
- [n8n Dynamic Credentials: authorize credential lifecycle operations](<../resources/n8n-2026-dynamic-credential-object-authority.md>) — topic: Identity.
- [n8n: directory-attribute authority in durable account linking](<../resources/n8n-2026-ldap-account-linking-authority.md>) — topic: Identity.
- [n8n: refreshed authority must remain bound to the consented resource](<../resources/n8n-2026-refresh-grant-resource-binding.md>) — topic: Identity.
- [Nhost: provider adapters must preserve identity-claim evidence](<../resources/nhost-2026-provider-claim-verification-provenance.md>) — topic: Identity.
- [NIST SP 800-162: attribute authority and policy traceability](<../resources/nist-sp-800-162-attribute-authority-modeling.md>) — topic: Identity.
- [Obot: preserve delegated token audience and consent boundaries](<../resources/obot-2026-oauth-audience-and-consent-boundaries.md>) — topic: Identity.
- [Open WebUI: credentials must bind to their destination connection](<../resources/open-webui-2026-connection-credential-capture.md>) — topic: Identity.
- [Open WebUI: preserve role-policy meaning across identity flows](<../resources/open-webui-2026-role-claim-provenance-and-revocation.md>) — topic: Identity.
- [Open WebUI: revocation must cross HTTP and realtime boundaries](<../resources/open-webui-2026-realtime-revocation-consistency.md>) — topic: Identity.
- [Outline: integration authority must end with its owning account](<../resources/outline-2026-webhook-revocation-lifecycle.md>) — topic: Identity.
- [OWASP Forgot Password](<../resources/owasp-account-recovery-state-integrity.md>) — topic: Identity; diagram: [Recovery must preserve account ownership](<../diagram-gallery.md#account-recovery-challenge-lifecycle>).
- [pac4j JWT validation: confidentiality does not establish authenticity](<../resources/pac4j-2026-token-authenticity-enforcement.md>) — topic: Identity.
- [Prowler SAML: retain validated tenant authority](<../resources/prowler-2026-saml-tenant-issuance-binding.md>) — topic: Identity.
- [Pterodactyl: delegated tokens must preserve action-specific authority](<../resources/pterodactyl-2026-delegated-token-purpose-binding.md>) — topic: Identity.
- [RFC 10017: OAuth 2\.0 for Browser-Based Applications](<../resources/rfc-10017-browser-oauth-token-custody.md>) — topic: Identity.
- [RFC 9700: Best Current Practice for OAuth 2\.0 Security](<../resources/rfc-9700-oauth-security-best-current-practice.md>) — topic: Identity; diagram: [An identity claim must belong to the user](<../diagram-gallery.md#identity-claim-binding>).
- [Rocket\.Chat: authentication must await a completed verification decision](<../resources/rocketchat-2026-asynchronous-identity-verification.md>) — topic: Identity.
- [samlify: signing does not establish claim provenance](<../resources/samlify-2026-assertion-generation-claim-integrity.md>) — topic: Identity.
- [Sentry: resource ownership must match the authorized organization](<../resources/sentry-2026-organization-object-authorization.md>) — topic: Identity.
- [STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers using Session Tickets](<../resources/usenix-2025-tls-resumption-identity-isolation.md>) — topic: Identity.
- [Universal Cross-app Attacks: Exploiting and Securing OAuth 2\.0 in Integration Platforms](<../resources/usenix-2025-integration-platform-oauth-bindings.md>) — topic: Identity.

<a id="conceptual-diagrams"></a>
## Conceptual diagrams

Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.

- [An identity claim must belong to the user](<../diagram-gallery.md#identity-claim-binding>)
- [Browser messages need separate trust checks](<../diagram-gallery.md#browser-message-authority-boundaries>)
- [Keep workload authority tenant-scoped](<../diagram-gallery.md#workload-identity-tenant-scope>)
- [Recovery must preserve account ownership](<../diagram-gallery.md#account-recovery-challenge-lifecycle>)

---

Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).
