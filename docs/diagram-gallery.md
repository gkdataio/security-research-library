# Diagram gallery

[Library home](../README.md) · [Report index](reports.md) · [Visual learning guide](visual-theory.md)

Original conceptual defensive models. Images are local, inert SVGs; no script, embeds, external dependencies or interactive links. These are not vendor architecture diagrams or operational sequences.

<a id="account-recovery-challenge-lifecycle"></a>
## Recovery must preserve account ownership

![A limited recovery request creates an account-bound challenge\. Only valid, unexpired, unused proof permits a reset\. Failure preserves account state; success consumes the challenge and notifies the owner\.](../diagrams/account-recovery-challenge-lifecycle.svg)

Editorial conceptual model derived from the linked cases and official guidance; not a vendor architecture diagram or an exploitation sequence\.

**Related reports**

- [GitLab recovery delivery lacked verified-address binding](<reports/gitlab-recovery-address-binding-cve-2023-7028.md>)
- [Microsoft account recovery lacked consistent attempt-limit enforcement](<reports/microsoft-account-recovery-rate-limit-consistency-2021.md>)
- [Instagram recovery challenges were insufficiently bound to accounts](<reports/instagram-recovery-challenge-account-binding-2019.md>)

[Canonical graph and provenance](<../data/diagrams/account-recovery-challenge-lifecycle.json>) · [Mermaid source](<../diagrams/account-recovery-challenge-lifecycle.mmd>) · [DOT source](<../diagrams/account-recovery-challenge-lifecycle.dot>)

<a id="ai-content-authority-separation"></a>
## Retrieved content is data, not authority

![User intent and untrusted connector content enter the AI workflow separately\. A proposed action reaches an independent policy decision\. Only an authorized state change proceeds; otherwise state remains unchanged\.](../diagrams/ai-content-authority-separation.svg)

Editorial conceptual model derived from the linked cases and official guidance; not a vendor architecture diagram or an exploitation sequence\.

**Related reports**

- [Gemini Enterprise connected-content trust failure allowed persistent-memory modification](<reports/google-gemini-enterprise-connected-content-memory-integrity-2026.md>)
- [Gemini-to-Colab rendering boundary exposed Workspace data](<reports/google-gemini-colab-rendering-boundary-2025.md>)

[Canonical graph and provenance](<../data/diagrams/ai-content-authority-separation.json>) · [Mermaid source](<../diagrams/ai-content-authority-separation.mmd>) · [DOT source](<../diagrams/ai-content-authority-separation.dot>)

<a id="approval-version-integrity"></a>
## Approval stays attached to the reviewed version

![Reviewed content and its immutable version are bound to an approval\. Execution independently checks that the version still matches\. Matching requests proceed with least privilege; mismatches require a new review\.](../diagrams/approval-version-integrity.svg)

Editorial conceptual model derived from the linked cases and official guidance; not a vendor architecture diagram or an exploitation sequence\.

**Related reports**

- [Cloud Build approval was not bound to immutable code](<reports/google-cloud-build-approval-toctou-2025.md>)
- [GitHub Actions trust depended on invalid repository references](<reports/github-actions-reference-validation-2021.md>)

[Canonical graph and provenance](<../data/diagrams/approval-version-integrity.json>) · [Mermaid source](<../diagrams/approval-version-integrity.mmd>) · [DOT source](<../diagrams/approval-version-integrity.dot>)

<a id="browser-message-authority-boundaries"></a>
## Browser messages need separate trust checks

![An incoming browser message first passes origin, sender-context and format validation\. A separate decision checks the operation and recipient\. Failed checks reject the message without disclosure or state change\. Approved content remains data and only the permitted action is performed\.](../diagrams/browser-message-authority-boundaries.svg)

Original defensive model combining OWASP messaging and authorization guidance with the linked historical cases\. These are independent design checks, not a vendor patch diagram or an operational reproduction\.

**Related reports**

- [Facebook SDK message authentication relied on insecure randomness](<reports/facebook-sdk-message-authentication-randomness-2023.md>)
- [Meta Pixel cross-window handling lost message and token authority](<reports/meta-pixel-cross-window-authority-binding-2024.md>)

[Canonical graph and provenance](<../data/diagrams/browser-message-authority-boundaries.json>) · [Mermaid source](<../diagrams/browser-message-authority-boundaries.mmd>) · [DOT source](<../diagrams/browser-message-authority-boundaries.dot>)

<a id="build-artifact-provenance-boundary"></a>
## Build evidence must match the artifact and trusted builder

![Untrusted contributions remain separated from trusted build state\. An artifact and its provenance reach a consumer policy gate\. Only authenticated evidence matching the artifact and expected builder and inputs makes it eligible for release review; missing or mismatched evidence prevents promotion\.](../diagrams/build-artifact-provenance-boundary.svg)

Editorial conceptual model combining the Angular case with SLSA build guidance\. The case supports separating automation trust and shared build state; the consumer verification gate is a general design synthesis, not a reconstruction of Angular remediation\. Assumes a defined trust policy for builders and provenance\. Provenance presence alone does not establish authenticity, and passing these checks does not prove the software is free of vulnerabilities\.

**Related reports**

- [Angular automation trust and cache isolation weakness](<reports/angular-ci-cache-trust-2026.md>)

[Canonical graph and provenance](<../data/diagrams/build-artifact-provenance-boundary.json>) · [Mermaid source](<../diagrams/build-artifact-provenance-boundary.mmd>) · [DOT source](<../diagrams/build-artifact-provenance-boundary.dot>)

<a id="error-diagnostic-disclosure-boundary"></a>
## Failures need separate public and diagnostic contracts

![A failure reaches a shared error handler\. The public response contains minimal generic information\. A separate diagnostic path selects useful context, removes secrets and unnecessary personal data, and stores it under access and retention controls\. Raw exception details do not flow directly to the client\.](../diagrams/error-diagnostic-disclosure-boundary.svg)

Editorial conceptual model derived from the Facebook error-response case and OWASP error-handling and logging guidance\. The case establishes unintended response disclosure and broader framework remediation; diagnostic minimization and retention are general guidance, not claims about the vendor patch\. Assumes an application-defined public error contract and an authorized diagnostic purpose\. This model does not establish preserved authorization in fallback behavior or independent proof from logs\.

**Related reports**

- [Facebook error responses exposed unintended application data](<reports/facebook-error-response-data-isolation-2019.md>)

[Canonical graph and provenance](<../data/diagrams/error-diagnostic-disclosure-boundary.json>) · [Mermaid source](<../diagrams/error-diagnostic-disclosure-boundary.mmd>) · [DOT source](<../diagrams/error-diagnostic-disclosure-boundary.dot>)

<a id="identity-claim-binding"></a>
## An identity claim must belong to the user

![The identity provider authenticates a subject and binds issued claims to it\. The relying application validates the issuer, audience, signature, and ownership binding before mapping to a local account\. Failed validation is rejected\.](../diagrams/identity-claim-binding.svg)

Editorial conceptual model derived from the linked cases and official guidance; not a vendor architecture diagram or an exploitation sequence\.

**Related reports**

- [Sign in with Apple failed to bind identity claims to the authenticated user](<reports/apple-sign-in-identity-claim-binding-2020.md>)
- [GitHub OAuth consent failed across request-method semantics](<reports/github-oauth-method-semantics-2019.md>)

[Canonical graph and provenance](<../data/diagrams/identity-claim-binding.json>) · [Mermaid source](<../diagrams/identity-claim-binding.mmd>) · [DOT source](<../diagrams/identity-claim-binding.dot>)

<a id="parsing-safety-action-authority"></a>
## Parsing safety and action authority

![Untrusted input is parsed with memory safety and limited privileges\. A bounded typed result still requires an independent meaning and authorization check before any scoped operation; failed checks reject the request\.](../diagrams/parsing-safety-action-authority.svg)

Editorial conceptual model derived from the linked cases and official guidance; not a vendor architecture diagram or an exploitation sequence\.

**Related reports**

- [V8 optimized object handling retained invalid type assumptions](<reports/google-chrome-v8-type-consistency-2025.md>)
- [Redis Lua object lifetime failure crossed the scripting boundary](<reports/redis-lua-object-lifetime-isolation-2025.md>)

[Canonical graph and provenance](<../data/diagrams/parsing-safety-action-authority.json>) · [Mermaid source](<../diagrams/parsing-safety-action-authority.mmd>) · [DOT source](<../diagrams/parsing-safety-action-authority.dot>)

<a id="server-client-data-consumer-boundaries"></a>
## Server disclosure and browser interpretation

![A request enters a server-side caller, resource and operation authorization decision\. Denial returns no protected data\. Approval proceeds to explicit field selection before serialization\. Only permitted, necessary fields cross into client-visible data\. A separate consumer-context handling step keeps content, including generated text, from acquiring executable meaning before display\. Browser rendering never supplies server authorization\.](../diagrams/server-client-data-consumer-boundaries.svg)

Editorial conceptual model: assumes an application with server-side privileged data and a browser consumer\. Next\.js guidance supports server authorization and minimal client-visible contracts; OWASP LLM05 supports treating generated text as untrusted at each consumer\. The linked HackerOne Rails case illustrates why serialization needs an explicit disclosure boundary; it is not evidence of Next\.js or an LLM integration\. The arrows show defensive responsibilities, not a framework execution trace\. Context-aware encoding or sanitization belongs where the output context is known, including server rendering; the lower steps do not imply exclusively client-side execution\. Rendering safety cannot replace permission checks, and authorized disclosure does not make content safe to interpret\.

**Related reports**

- [Framework serialization change exposed private HackerOne user attributes](<reports/hackerone-report-json-serialization-data-exposure-2025.md>)

[Canonical graph and provenance](<../data/diagrams/server-client-data-consumer-boundaries.json>) · [Mermaid source](<../diagrams/server-client-data-consumer-boundaries.mmd>) · [DOT source](<../diagrams/server-client-data-consumer-boundaries.dot>)

<a id="server-request-destination-policy"></a>
## Layer server-request destination controls

![A requested destination passes consistent parsing, application policy and independent network egress checks\. Invalid input or either policy failure is rejected\. Only an approved destination is requested\.](../diagrams/server-request-destination-policy.svg)

Original conceptual defense-in-depth model linked to the historical Shopify Exchange case and OWASP guidance\. It is not a vendor architecture diagram\. Policy must fit the service’s destination requirements\.

**Related reports**

- [Shopify Exchange screenshot service crossed internal boundaries](<reports/shopify-exchange-request-isolation-2019.md>)

[Canonical graph and provenance](<../data/diagrams/server-request-destination-policy.json>) · [Mermaid source](<../diagrams/server-request-destination-policy.mmd>) · [DOT source](<../diagrams/server-request-destination-policy.dot>)

<a id="workload-identity-tenant-scope"></a>
## Keep workload authority tenant-scoped

![A verified workload identity and a requested operation enter an independent authorization decision\. Policy checks the role, action, resource and tenant together\. Only the approved resource scope is allowed; other requests are denied\. Both decisions produce an audit record\.](../diagrams/workload-identity-tenant-scope.svg)

Editorial conceptual model derived from the linked cases and official guidance; not a vendor architecture diagram or an exploitation sequence\.

**Related reports**

- [Meta service-identity exposure amplified by excessive secret access](<reports/meta-service-identity-secrets-trust-boundary-2026.md>)
- [Actifio driver execution exposed excessive shared-service authority](<reports/google-actifio-driver-service-identity-isolation-2025.md>)

[Canonical graph and provenance](<../data/diagrams/workload-identity-tenant-scope.json>) · [Mermaid source](<../diagrams/workload-identity-tenant-scope.mmd>) · [DOT source](<../diagrams/workload-identity-tenant-scope.dot>)

Original diagrams: Security Research Library contributors, CC BY 4.0. [License scope](../LICENSE.md).
