# Award-backed reports by topic

[Report index](reports.md) · [Library home](../README.md)

Generated offline from canonical primary and secondary category IDs and the report taxonomy. These historical disclosures are separate from educational resources and grant no testing authorization.

61 distinct award-backed reports across 11 taxonomy categories. A report can appear under several categories; overlapping memberships do not increase the distinct report count. Category counts must not be added to count reports.

Each entry labels its primary or secondary category membership. Categories and reports are ordered alphabetically by title, with stable IDs breaking ties. Empty taxonomy categories are shown explicitly. Regeneration does not reverify sources or advance review timestamps.

## Browse topics

- [AI integration boundaries](<#category-ai-security>) — 7 distinct reports.
- [Authentication and identity](<#category-authentication>) — 15 distinct reports.
- [Authorization and tenant boundaries](<#category-authorization>) — 30 distinct reports.
- [Business logic and concurrency](<#category-business-logic>) — 14 distinct reports.
- [Client and browser security](<#category-client-security>) — 19 distinct reports.
- [Cloud permissions and isolation](<#category-cloud-security>) — 13 distinct reports.
- [Information exposure and response privacy](<#category-information-exposure>) — 3 distinct reports.
- [Injection and untrusted input](<#category-injection>) — 11 distinct reports.
- [Memory safety and parser contracts](<#category-memory-safety>) — 10 distinct reports.
- [Server-side request trust](<#category-server-request-trust>) — 1 distinct report.
- [Software supply-chain security](<#category-supply-chain>) — 6 distinct reports.

<a id="category-ai-security"></a>
## AI integration boundaries

7 distinct reports.

- [Apple PCC startup archive processing lacked path confinement](<reports/apple-pcc-boot-archive-path-validation-2026.md>) — Apple; secondary category.
- [Bard Workspace integration weakened output-data boundaries](<reports/google-bard-workspace-output-boundary-2024.md>) — Google; primary category.
- [Codex automated Git operations trusted repository hook settings](<reports/openai-codex-repository-hook-execution-trust-2026.md>) — OpenAI; primary category.
- [Codex metadata collection trusted repository execution helpers](<reports/openai-codex-repository-metadata-helper-trust-2026.md>) — OpenAI; primary category.
- [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](<reports/google-gemini-enterprise-connected-content-memory-integrity-2026.md>) — Google; primary category.
- [Gemini-to-Colab rendering boundary exposed Workspace data](<reports/google-gemini-colab-rendering-boundary-2025.md>) — Google; primary category.
- [Meta AI media access lacked object-ownership authorization](<reports/meta-ai-media-object-authorization-2025.md>) — Meta; secondary category.

<a id="category-authentication"></a>
## Authentication and identity

15 distinct reports.

- [Facebook SDK message authentication relied on insecure randomness](<reports/facebook-sdk-message-authentication-randomness-2023.md>) — Meta; primary category.
- [GitHub OAuth consent failed across request-method semantics](<reports/github-oauth-method-semantics-2019.md>) — GitHub; secondary category.
- [GitLab recovery delivery lacked verified-address binding](<reports/gitlab-recovery-address-binding-cve-2023-7028.md>) — GitLab; primary category.
- [Google device grants lost client and permission binding](<reports/google-device-authorization-client-scope-binding-2026.md>) — Google; primary category.
- [Instagram mobile account recovery had inconsistent verification limits](<reports/instagram-mobile-recovery-attempt-limits-2019.md>) — Facebook / Instagram; primary category.
- [Instagram recovery challenges were insufficiently bound to accounts](<reports/instagram-recovery-challenge-account-binding-2019.md>) — Facebook / Instagram; primary category.
- [LiteSpeed Cache privileged user simulation relied on weak security tokens](<reports/litespeed-cache-user-simulation-authentication-2024.md>) — LiteSpeed Technologies; primary category.
- [Meta account verification weakened linked SMS authentication state](<reports/meta-account-verification-attempt-state-binding-2022.md>) — Meta; primary category.
- [Meta Accounts Center linking lost credential and identity confinement](<reports/meta-accounts-center-linking-credential-confinement-2024.md>) — Meta; primary category.
- [Meta Pixel cross-window handling lost message and token authority](<reports/meta-pixel-cross-window-authority-binding-2024.md>) — Meta; secondary category.
- [Meta Quest login migration lost OAuth credential confinement](<reports/meta-quest-oauth-redirect-confidentiality-2022.md>) — Meta; primary category.
- [Meta service-identity exposure amplified by excessive secret access](<reports/meta-service-identity-secrets-trust-boundary-2026.md>) — Meta; secondary category.
- [Microsoft account recovery lacked consistent attempt-limit enforcement](<reports/microsoft-account-recovery-rate-limit-consistency-2021.md>) — Microsoft; primary category.
- [Pixel lock-screen completion lost security-state binding](<reports/google-pixel-lock-screen-state-binding-2022.md>) — Google; primary category.
- [Shopify automatic account conversion lost merchant-consent binding](<reports/shopify-collaborator-conversion-consent-2017.md>) — Shopify; secondary category.

<a id="category-authorization"></a>
## Authorization and tenant boundaries

30 distinct reports.

- [Actifio driver execution exposed excessive shared-service authority](<reports/google-actifio-driver-service-identity-isolation-2025.md>) — Google; secondary category.
- [Angular automation trust and cache isolation weakness](<reports/angular-ci-cache-trust-2026.md>) — Google; secondary category.
- [Cloud Build approval was not bound to immutable code](<reports/google-cloud-build-approval-toctou-2025.md>) — Google; secondary category.
- [Framework serialization change exposed private HackerOne user attributes](<reports/hackerone-report-json-serialization-data-exposure-2025.md>) — HackerOne; secondary category.
- [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](<reports/google-gemini-enterprise-connected-content-memory-integrity-2026.md>) — Google; secondary category.
- [GitHub Actions trust depended on invalid repository references](<reports/github-actions-reference-validation-2021.md>) — GitHub; secondary category.
- [GitHub comparison output lacked source-repository authorization](<reports/github-cross-repository-comparison-authorization-2025.md>) — GitHub; primary category.
- [GitHub fork collaboration applied inconsistent authorization](<reports/github-fork-collaboration-authorization-2021.md>) — GitHub; primary category.
- [GitHub GraphQL collaboration changes lacked author consent](<reports/github-fork-collaboration-consent-2021.md>) — GitHub; primary category.
- [GitHub OAuth consent failed across request-method semantics](<reports/github-oauth-method-semantics-2019.md>) — GitHub; primary category.
- [GitHub runner-image builds shared persistent infrastructure with untrusted workflows](<reports/github-runner-image-build-isolation-2023.md>) — GitHub; secondary category.
- [GitLab recovery delivery lacked verified-address binding](<reports/gitlab-recovery-address-binding-cve-2023-7028.md>) — GitLab; secondary category.
- [Google Application Integration mixed resource and service authority](<reports/google-application-integration-authorization-boundaries-2026.md>) — Google; primary category.
- [Google device grants lost client and permission binding](<reports/google-device-authorization-client-scope-binding-2026.md>) — Google; secondary category.
- [Google support API exposed customer and agent data](<reports/google-support-api-authorization-2026.md>) — Google; primary category.
- [GraphQL object authorization exposed private-program metadata](<reports/hackerone-private-program-graphql-object-authorization-2025.md>) — HackerOne; primary category.
- [Instagram client configuration exposed an application credential](<reports/instagram-application-credential-client-containment-2022.md>) — Meta; secondary category.
- [Instagram embedding fallback changed the authorization context](<reports/instagram-embedding-privileged-fallback-2023.md>) — Meta; primary category.
- [Kestrel HTTP framing differed across proxy and application boundaries](<reports/microsoft-kestrel-http-framing-consistency-2025.md>) — Microsoft; secondary category.
- [LiteSpeed Cache privileged user simulation relied on weak security tokens](<reports/litespeed-cache-user-simulation-authentication-2024.md>) — LiteSpeed Technologies; secondary category.
- [Meta Accounts Center linking lost credential and identity confinement](<reports/meta-accounts-center-linking-credential-confinement-2024.md>) — Meta; secondary category.
- [Meta AI media access lacked object-ownership authorization](<reports/meta-ai-media-object-authorization-2025.md>) — Meta; primary category.
- [Meta Pixel cross-window handling lost message and token authority](<reports/meta-pixel-cross-window-authority-binding-2024.md>) — Meta; primary category.
- [Meta Quest login migration lost OAuth credential confinement](<reports/meta-quest-oauth-redirect-confidentiality-2022.md>) — Meta; secondary category.
- [Meta service-identity exposure amplified by excessive secret access](<reports/meta-service-identity-secrets-trust-boundary-2026.md>) — Meta; secondary category.
- [Shopify automatic account conversion lost merchant-consent binding](<reports/shopify-collaborator-conversion-consent-2017.md>) — Shopify; primary category.
- [Sign in with Apple failed to bind identity claims to the authenticated user](<reports/apple-sign-in-identity-claim-binding-2020.md>) — Apple; primary category.
- [Support integration exposed internal Confluence documentation](<reports/hackerone-support-confluence-access-boundary-2025.md>) — HackerOne; primary category.
- [YouTube and Pixel Recorder exposed cross-product identity links](<reports/youtube-pixel-recorder-identity-privacy-2025.md>) — Google; primary category.
- [YouTube creator metadata exposed private email addresses](<reports/youtube-creator-email-authorization-2025.md>) — Google; primary category.

<a id="category-business-logic"></a>
## Business logic and concurrency

14 distinct reports.

- [Cloud Build approval was not bound to immutable code](<reports/google-cloud-build-approval-toctou-2025.md>) — Google; primary category.
- [GitHub Actions trust depended on invalid repository references](<reports/github-actions-reference-validation-2021.md>) — GitHub; secondary category.
- [GitHub fork collaboration applied inconsistent authorization](<reports/github-fork-collaboration-authorization-2021.md>) — GitHub; secondary category.
- [GitHub GraphQL collaboration changes lacked author consent](<reports/github-fork-collaboration-consent-2021.md>) — GitHub; secondary category.
- [GitHub OAuth consent failed across request-method semantics](<reports/github-oauth-method-semantics-2019.md>) — GitHub; secondary category.
- [iCloud sharing consent and Safari trust boundaries failed together](<reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.md>) — Apple; secondary category.
- [Instagram embedding fallback changed the authorization context](<reports/instagram-embedding-privileged-fallback-2023.md>) — Meta; secondary category.
- [Instagram mobile account recovery had inconsistent verification limits](<reports/instagram-mobile-recovery-attempt-limits-2019.md>) — Facebook / Instagram; secondary category.
- [Instagram recovery challenges were insufficiently bound to accounts](<reports/instagram-recovery-challenge-account-binding-2019.md>) — Facebook / Instagram; secondary category.
- [Meta account verification weakened linked SMS authentication state](<reports/meta-account-verification-attempt-state-binding-2022.md>) — Meta; secondary category.
- [Microsoft account recovery lacked consistent attempt-limit enforcement](<reports/microsoft-account-recovery-rate-limit-consistency-2021.md>) — Microsoft; secondary category.
- [Pixel lock-screen completion lost security-state binding](<reports/google-pixel-lock-screen-state-binding-2022.md>) — Google; secondary category.
- [Redis replication state changes invalidated an active interpreter](<reports/redis-replication-interpreter-lifetime-2026.md>) — Redis; secondary category.
- [Shopify automatic account conversion lost merchant-consent binding](<reports/shopify-collaborator-conversion-consent-2017.md>) — Shopify; secondary category.

<a id="category-client-security"></a>
## Client and browser security

19 distinct reports.

- [Bard Workspace integration weakened output-data boundaries](<reports/google-bard-workspace-output-boundary-2024.md>) — Google; secondary category.
- [Chrome graphics input validation weakened an isolation boundary](<reports/google-chrome-angle-input-validation-2026.md>) — Google; primary category.
- [Codex automated Git operations trusted repository hook settings](<reports/openai-codex-repository-hook-execution-trust-2026.md>) — OpenAI; secondary category.
- [Codex command approval relied on inconsistent parser semantics](<reports/openai-codex-command-parser-approval-consistency-2026.md>) — OpenAI; secondary category.
- [Codex metadata collection trusted repository execution helpers](<reports/openai-codex-repository-metadata-helper-trust-2026.md>) — OpenAI; secondary category.
- [Facebook SDK message authentication relied on insecure randomness](<reports/facebook-sdk-message-authentication-randomness-2023.md>) — Meta; secondary category.
- [Gemini-to-Colab rendering boundary exposed Workspace data](<reports/google-gemini-colab-rendering-boundary-2025.md>) — Google; secondary category.
- [Google IDX worker messaging crossed browser trust boundaries](<reports/google-idx-worker-message-trust-2025.md>) — Google; primary category.
- [iCloud sharing consent and Safari trust boundaries failed together](<reports/apple-icloud-sharing-consent-safari-origin-boundary-2022.md>) — Apple; primary category.
- [Instagram client configuration exposed an application credential](<reports/instagram-application-credential-client-containment-2022.md>) — Meta; secondary category.
- [macOS SMBFS error handling left inconsistent kernel parser state](<reports/apple-smbfs-parser-state-consistency-2026.md>) — Apple; secondary category.
- [Meta Accounts Center linking lost credential and identity confinement](<reports/meta-accounts-center-linking-credential-confinement-2024.md>) — Meta; secondary category.
- [Meta Conversions API Gateway mixed configuration data with executable output](<reports/meta-conversions-gateway-generated-script-boundary-2025.md>) — Meta; secondary category.
- [Meta Pixel cross-window handling lost message and token authority](<reports/meta-pixel-cross-window-authority-binding-2024.md>) — Meta; secondary category.
- [Meta Quest login migration lost OAuth credential confinement](<reports/meta-quest-oauth-redirect-confidentiality-2022.md>) — Meta; secondary category.
- [Pixel lock-screen completion lost security-state binding](<reports/google-pixel-lock-screen-state-binding-2022.md>) — Google; secondary category.
- [Safari origin confusion undermined stored media permissions](<reports/apple-safari-media-permission-origin-confusion-2020.md>) — Apple; primary category.
- [V8 control-flow analysis omitted required initialization checks](<reports/google-chrome-v8-initialization-checks-2025.md>) — Google; secondary category.
- [V8 optimized object handling retained invalid type assumptions](<reports/google-chrome-v8-type-consistency-2025.md>) — Google; secondary category.

<a id="category-cloud-security"></a>
## Cloud permissions and isolation

13 distinct reports.

- [Actifio driver execution exposed excessive shared-service authority](<reports/google-actifio-driver-service-identity-isolation-2025.md>) — Google; primary category.
- [Apple PCC startup archive processing lacked path confinement](<reports/apple-pcc-boot-archive-path-validation-2026.md>) — Apple; primary category.
- [Cloud Build approval was not bound to immutable code](<reports/google-cloud-build-approval-toctou-2025.md>) — Google; secondary category.
- [Google Application Integration mixed resource and service authority](<reports/google-application-integration-authorization-boundaries-2026.md>) — Google; secondary category.
- [MariaDB JSON normalization exceeded allocated buffer capacity](<reports/mariadb-json-normalization-buffer-capacity-2026.md>) — MariaDB; secondary category.
- [Meta service-identity exposure amplified by excessive secret access](<reports/meta-service-identity-secrets-trust-boundary-2026.md>) — Meta; primary category.
- [NVIDIA container initialization inherited untrusted execution context](<reports/nvidia-container-runtime-environment-trust-2025.md>) — NVIDIA; primary category.
- [PostgreSQL cryptographic parsing omitted a buffer-capacity check](<reports/postgresql-pgcrypto-buffer-capacity-validation-2026.md>) — PostgreSQL; secondary category.
- [PostgreSQL extension estimator trusted an unchecked input type](<reports/postgresql-extension-input-type-validation-2026.md>) — PostgreSQL; secondary category.
- [Redis deserialization cleanup violated object-ownership invariants](<reports/redis-deserialization-object-ownership-2026.md>) — Redis; secondary category.
- [Redis Lua object lifetime failure crossed the scripting boundary](<reports/redis-lua-object-lifetime-isolation-2025.md>) — Redis; secondary category.
- [Redis replication state changes invalidated an active interpreter](<reports/redis-replication-interpreter-lifetime-2026.md>) — Redis; secondary category.
- [Shopify Exchange screenshot service crossed internal boundaries](<reports/shopify-exchange-request-isolation-2019.md>) — Shopify; secondary category.

<a id="category-information-exposure"></a>
## Information exposure and response privacy

3 distinct reports.

- [Facebook error responses exposed unintended application data](<reports/facebook-error-response-data-isolation-2019.md>) — Meta \(Facebook\); primary category.
- [Framework serialization change exposed private HackerOne user attributes](<reports/hackerone-report-json-serialization-data-exposure-2025.md>) — HackerOne; primary category.
- [Instagram client configuration exposed an application credential](<reports/instagram-application-credential-client-containment-2022.md>) — Meta; primary category.

<a id="category-injection"></a>
## Injection and untrusted input

11 distinct reports.

- [Angular automation trust and cache isolation weakness](<reports/angular-ci-cache-trust-2026.md>) — Google; secondary category.
- [Bard Workspace integration weakened output-data boundaries](<reports/google-bard-workspace-output-boundary-2024.md>) — Google; secondary category.
- [Codex command approval relied on inconsistent parser semantics](<reports/openai-codex-command-parser-approval-consistency-2026.md>) — OpenAI; primary category.
- [Facebook SDK message authentication relied on insecure randomness](<reports/facebook-sdk-message-authentication-randomness-2023.md>) — Meta; secondary category.
- [Gemini-to-Colab rendering boundary exposed Workspace data](<reports/google-gemini-colab-rendering-boundary-2025.md>) — Google; secondary category.
- [GitHub package-source trust allowed dependency confusion](<reports/github-ruby-dependency-confusion-2025.md>) — GitHub; secondary category.
- [Google IDX worker messaging crossed browser trust boundaries](<reports/google-idx-worker-message-trust-2025.md>) — Google; secondary category.
- [Kestrel HTTP framing differed across proxy and application boundaries](<reports/microsoft-kestrel-http-framing-consistency-2025.md>) — Microsoft; primary category.
- [Meta Conversions API Gateway mixed configuration data with executable output](<reports/meta-conversions-gateway-generated-script-boundary-2025.md>) — Meta; primary category.
- [NVIDIA container initialization inherited untrusted execution context](<reports/nvidia-container-runtime-environment-trust-2025.md>) — NVIDIA; secondary category.
- [PostgreSQL text-encoding invariant failure caused memory corruption](<reports/postgresql-multibyte-validation-cve-2026-2006.md>) — PostgreSQL; secondary category.

<a id="category-memory-safety"></a>
## Memory safety and parser contracts

10 distinct reports.

- [macOS SMBFS error handling left inconsistent kernel parser state](<reports/apple-smbfs-parser-state-consistency-2026.md>) — Apple; primary category.
- [MariaDB JSON normalization exceeded allocated buffer capacity](<reports/mariadb-json-normalization-buffer-capacity-2026.md>) — MariaDB; primary category.
- [PostgreSQL cryptographic parsing omitted a buffer-capacity check](<reports/postgresql-pgcrypto-buffer-capacity-validation-2026.md>) — PostgreSQL; primary category.
- [PostgreSQL extension estimator trusted an unchecked input type](<reports/postgresql-extension-input-type-validation-2026.md>) — PostgreSQL; primary category.
- [PostgreSQL text-encoding invariant failure caused memory corruption](<reports/postgresql-multibyte-validation-cve-2026-2006.md>) — PostgreSQL; primary category.
- [Redis deserialization cleanup violated object-ownership invariants](<reports/redis-deserialization-object-ownership-2026.md>) — Redis; primary category.
- [Redis Lua object lifetime failure crossed the scripting boundary](<reports/redis-lua-object-lifetime-isolation-2025.md>) — Redis; primary category.
- [Redis replication state changes invalidated an active interpreter](<reports/redis-replication-interpreter-lifetime-2026.md>) — Redis; primary category.
- [V8 control-flow analysis omitted required initialization checks](<reports/google-chrome-v8-initialization-checks-2025.md>) — Google; primary category.
- [V8 optimized object handling retained invalid type assumptions](<reports/google-chrome-v8-type-consistency-2025.md>) — Google; primary category.

<a id="category-server-request-trust"></a>
## Server-side request trust

1 distinct report.

- [Shopify Exchange screenshot service crossed internal boundaries](<reports/shopify-exchange-request-isolation-2019.md>) — Shopify; primary category.

<a id="category-supply-chain"></a>
## Software supply-chain security

6 distinct reports.

- [Angular automation trust and cache isolation weakness](<reports/angular-ci-cache-trust-2026.md>) — Google; primary category.
- [Cloud Build approval was not bound to immutable code](<reports/google-cloud-build-approval-toctou-2025.md>) — Google; secondary category.
- [GitHub Actions trust depended on invalid repository references](<reports/github-actions-reference-validation-2021.md>) — GitHub; primary category.
- [GitHub package-source trust allowed dependency confusion](<reports/github-ruby-dependency-confusion-2025.md>) — GitHub; primary category.
- [GitHub runner-image builds shared persistent infrastructure with untrusted workflows](<reports/github-runner-image-build-isolation-2023.md>) — GitHub; primary category.
- [Meta Conversions API Gateway mixed configuration data with executable output](<reports/meta-conversions-gateway-generated-script-boundary-2025.md>) — Meta; secondary category.
