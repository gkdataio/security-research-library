# Business logic and concurrency

[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)

**Vulnerability family** · 14 reports · 32 related resources · 3 diagrams

State transitions, approval integrity, and transactional invariants.

Report membership uses the existing primary or secondary category business-logic. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.

On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)

<a id="reports"></a>
## Reports

- [Cloud Build approval was not bound to immutable code](<../reports/google-cloud-build-approval-toctou-2025.md>) — Google; primary category.
- [GitHub Actions trust depended on invalid repository references](<../reports/github-actions-reference-validation-2021.md>) — GitHub; secondary category.
- [GitHub fork collaboration applied inconsistent authorization](<../reports/github-fork-collaboration-authorization-2021.md>) — GitHub; secondary category.
- [GitHub GraphQL collaboration changes lacked author consent](<../reports/github-fork-collaboration-consent-2021.md>) — GitHub; secondary category.
- [GitHub OAuth consent failed across request-method semantics](<../reports/github-oauth-method-semantics-2019.md>) — GitHub; secondary category.
- [iCloud sharing consent and Safari trust boundaries failed together](<../reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.md>) — Apple; secondary category.
- [Instagram embedding fallback changed the authorization context](<../reports/instagram-embedding-privileged-fallback-2023.md>) — Meta; secondary category.
- [Instagram mobile account recovery had inconsistent verification limits](<../reports/instagram-mobile-recovery-attempt-limits-2019.md>) — Facebook / Instagram; secondary category.
- [Instagram recovery challenges were insufficiently bound to accounts](<../reports/instagram-recovery-challenge-account-binding-2019.md>) — Facebook / Instagram; secondary category.
- [Meta account verification weakened linked SMS authentication state](<../reports/meta-account-verification-attempt-state-binding-2022.md>) — Meta; secondary category.
- [Microsoft account recovery lacked consistent attempt-limit enforcement](<../reports/microsoft-account-recovery-rate-limit-consistency-2021.md>) — Microsoft; secondary category.
- [Pixel lock-screen completion lost security-state binding](<../reports/google-pixel-lock-screen-state-binding-2022.md>) — Google; secondary category.
- [Redis replication state changes invalidated an active interpreter](<../reports/redis-replication-interpreter-lifetime-2026.md>) — Redis; secondary category.
- [Shopify automatic account conversion lost merchant-consent binding](<../reports/shopify-collaborator-conversion-consent-2017.md>) — Shopify; secondary category.

<a id="related-learning"></a>
## Related learning

Included by the topic crosswalk or an explicit resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.

- [Authorization Cheat Sheet](<../resources/owasp-authorization-cheat-sheet.md>) — diagram: [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>).
- [Better Auth: single-use authorization requires atomic state consumption](<../resources/better-auth-2026-authorization-code-consumption-integrity.md>) — topic: Business Logic and State Integrity.
- [Bugsink: time-unit consistency in account-access token expiry](<../resources/bugsink-2026-token-expiry-unit-integrity.md>) — topic: Business Logic and State Integrity.
- [Coder: privileged provisioning must preserve existing object ownership](<../resources/coder-2026-provisioned-object-ownership-integrity.md>) — topic: Business Logic and State Integrity.
- [Directus: denied mutations must leave dependent state unchanged](<../resources/directus-2026-preauthorization-side-effect-integrity.md>) — topic: Business Logic and State Integrity.
- [File Browser: existing shares must follow current owner permissions](<../resources/filebrowser-2026-share-owner-permission-lifecycle.md>) — topic: Business Logic and State Integrity.
- [Google API field masks: preserve server-owned and immutable state](<../resources/google-aip-161-update-field-authority.md>) — topic: Business Logic and State Integrity.
- [Google API request identity: bind retry semantics to the logical operation](<../resources/google-aip-155-request-identity-contract.md>) — topic: Business Logic and State Integrity.
- [Grav API: account-disable enforcement across session authenticators](<../resources/grav-2026-session-account-state-revalidation.md>) — topic: Business Logic and State Integrity.
- [HotCRP: separate submission visibility from authorship authority](<../resources/hotcrp-2026-contact-authorship-permission-boundary.md>) — topic: Business Logic and State Integrity.
- [Microsoft compensating transactions: recovery must preserve valid concurrent state](<../resources/microsoft-compensating-transaction-state-integrity.md>) — topic: Business Logic and State Integrity.
- [Microsoft Graph batching: preserve each member authorization outcome](<../resources/microsoft-graph-batch-member-authorization-outcomes.md>) — topic: Business Logic and State Integrity.
- [n8n: directory-attribute authority in durable account linking](<../resources/n8n-2026-ldap-account-linking-authority.md>) — topic: Business Logic and State Integrity.
- [n8n: refreshed authority must remain bound to the consented resource](<../resources/n8n-2026-refresh-grant-resource-binding.md>) — topic: Business Logic and State Integrity.
- [OpenFGA query consistency: authorization decisions need sufficiently fresh state](<../resources/openfga-authorization-query-freshness.md>) — topic: Business Logic and State Integrity.
- [OpenFGA: policy intersections must preserve explicit exclusions](<../resources/openfga-2026-composed-policy-exclusion-integrity.md>) — topic: Business Logic and State Integrity.
- [Outline: integration authority must end with its owning account](<../resources/outline-2026-webhook-revocation-lifecycle.md>) — topic: Business Logic and State Integrity.
- [OWASP Forgot Password](<../resources/owasp-account-recovery-state-integrity.md>) — topic: Business Logic and State Integrity; diagram: [Recovery must preserve account ownership](<../diagram-gallery.md#account-recovery-challenge-lifecycle>).
- [OWASP Secure Code Review: baseline and change-focused review](<../resources/owasp-secure-code-review-methodology.md>) — topic: Business Logic and State Integrity.
- [OWASP Threat Modeling: system assumptions and mitigation validation](<../resources/owasp-threat-modeling-assumptions-and-validation.md>) — topic: Business Logic and State Integrity.
- [OWASP Transaction Authorization](<../resources/owasp-transaction-authorization-state-integrity.md>) — topic: Business Logic and State Integrity; diagram: [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>).
- [Paymenter: refund entitlement and ledger changes need one atomic transition](<../resources/paymenter-2026-refund-transition-atomicity.md>) — topic: Business Logic and State Integrity.
- [PostgreSQL 18: Transaction Isolation and Business Invariants](<../resources/postgresql-transaction-isolation-business-invariants.md>) — topic: Business Logic and State Integrity.
- [Pterodactyl: delegated tokens must preserve action-specific authority](<../resources/pterodactyl-2026-delegated-token-purpose-binding.md>) — topic: Business Logic and State Integrity.
- [RFC 9700: Best Current Practice for OAuth 2\.0 Security](<../resources/rfc-9700-oauth-security-best-current-practice.md>) — diagram: [An identity claim must belong to the user](<../diagram-gallery.md#identity-claim-binding>).
- [Spree: cart association must retain guest-possession checks](<../resources/spree-2026-guest-cart-association-authority.md>) — topic: Business Logic and State Integrity.
- [Stripe webhooks: authentic delivery and business-state integrity](<../resources/stripe-webhook-delivery-state-integrity.md>) — topic: Business Logic and State Integrity.
- [Sylius: order ownership does not confer payment-operation authority](<../resources/sylius-2026-payment-action-authority.md>) — topic: Business Logic and State Integrity.
- [Sylius: promotion entitlement must be checked and consumed atomically](<../resources/sylius-2026-promotion-limit-atomicity.md>) — topic: Business Logic and State Integrity.
- [Vendure: payment child objects must inherit order channel authority](<../resources/vendure-2026-payment-child-object-channel-authority.md>) — topic: Business Logic and State Integrity.
- [Vikunja: saved favorites must recheck current project access](<../resources/vikunja-2026-favorites-current-access-revalidation.md>) — topic: Business Logic and State Integrity.
- [Vvveb: numeric input validity does not establish legitimate order state](<../resources/vvveb-2026-order-domain-invariant.md>) — topic: Business Logic and State Integrity.

<a id="conceptual-diagrams"></a>
## Conceptual diagrams

Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.

- [An identity claim must belong to the user](<../diagram-gallery.md#identity-claim-binding>)
- [Approval stays attached to the reviewed version](<../diagram-gallery.md#approval-version-integrity>)
- [Recovery must preserve account ownership](<../diagram-gallery.md#account-recovery-challenge-lifecycle>)

---

Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).
