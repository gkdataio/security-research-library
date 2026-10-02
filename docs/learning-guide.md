# Defensive learning guide

Use the historical cases as architecture-review examples. The goal is to understand and verify security invariants in an owned or authorized environment, not to replay a public exploit against other systems.

## 1. Approval and concurrency integrity

**Case:** Cloud Build approval consistency (older reference)

Learn to distinguish mutable object names from immutable versions, document exactly what an approval authorizes, and model ordering assumptions. A useful review artifact is a state diagram with the approved version, executed version, and invalidation conditions. Local unit tests should demonstrate the invariant across ordinary state changes.

**Taxonomy:** `approval-state-integrity`, `concurrency-reasoning`, `integration-threat-modeling`

**Reference:** [OWASP Transaction Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html)

## 2. Cloud identities and integration permissions

**Cases:** Meta service-identity and secret-access boundaries; Actifio driver and service-identity isolation; Apple PCC provisioning and mutable-configuration integrity

Learn effective-permission review, service authentication, secret ownership, and least privilege across integrations. Produce an identity-to-resource access matrix and a justified minimum-permission design. Separate reported reach from actual data access; stop evidence collection once the approved review objective is met.

**Taxonomy:** `cloud-iam-review`, `machine-identity-governance`, `secrets-containment`

**Reference:** [AWS IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 3. Build systems and dependency provenance

**Cases:** GitHub dependency-source trust; Angular build-cache and automation trust

Learn registry provenance, namespace governance, artifact integrity, cache separation, and bot authorization. Produce a trust-boundary diagram identifying who can create each input and which execution context consumes it. Review both direct privileges and shared state without assuming a read-only job is isolated.

**Taxonomy:** `pipeline-trust-modeling`, `dependency-provenance`, `cache-artifact-isolation`, `machine-identity-governance`

**Reference:** [SLSA v1.2](https://slsa.dev/spec/v1.2/)

## 4. AI tools and persistent-state authorization

**Case:** Gemini Enterprise persistent-memory integrity

Learn data provenance and the difference between retrieved text and user authorization. Document which operations change persistent state, what independent checks authorize them, and how connector content is kept out of the authority path. Use synthetic content and a local mock integration for regression coverage.

**Taxonomy:** `ai-authority-boundaries`, `authorization-modeling`, `untrusted-input-handling`

## 5. Parser contracts and memory safety

**Cases:** PostgreSQL CVE-2026-2006 encoding contracts, CVE-2026-2005 buffer capacity and CVE-2026-2004 input-type validation (competition entries); MariaDB JSON normalization; Chrome V8 type consistency and initialization checks; Redis Lua object-lifetime integrity and deserialization ownership

Learn encoding validity, length accounting, extension contracts, and safe use of assumptions across components. Produce a contract map showing where validation occurs and which downstream routines depend on it. Follow vendor patch guidance; review safe unit-test coverage rather than developing an exploit. The MariaDB example also teaches evidence calibration: a controlled code-execution demonstration does not establish the same reliability in every deployment.

**Taxonomy:** `secure-parser-review`, `encoding-invariant-review`, `memory-safety-review`, `patch-verification`

**Reference:** [Chromium Rule of Two](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/rule-of-2.md) · [Parsing and authority visual](visual-theory.md#separate-parsing-safety-from-action-authority)

## 6. Account recovery and identity binding

**Cases:** Microsoft account recovery; both Instagram recovery findings; Sign in with Apple; Google device-grant binding; Meta Quest login-migration credential confinement; Meta linked-account SMS verification; GitLab recovery-address binding; LiteSpeed Cache privileged user simulation

Learn to express which account a verification challenge or token represents, which actor may use it, and when it expires. Review atomic attempt accounting, challenge uniqueness, and relying-party assumptions. A useful deliverable is an identity-state model with local unit tests for its invariants.

The [Meta Quest migration case](../data/reports/meta-quest-oauth-redirect-confidentiality-2022.json) highlights a change-management question: does an existing login destination still preserve the same security guarantees after the identity flow changes? Document the intended recipient of a credential throughout its lifecycle and distinguish the reported fix from assumptions about every related component.

**Taxonomy:** `identity-lifecycle-review`, `authorization-modeling`, `concurrency-reasoning`, `security-token-design`

**Reference:** [OWASP Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) · [Recovery-state visual](visual-theory.md#preserve-ownership-through-account-recovery)

## 7. Cross-API consistency and safe serialization

**Cases:** Google Support; YouTube creator privacy; YouTube/Pixel Recorder identity correlation; both GitHub fork-collaboration reports and cross-repository comparisons; HackerOne report serialization, private-program objects and support integration; Meta AI media ownership

Learn how the same entitlement can be represented across API surfaces and framework layers. Define response allowlists, ownership checks, and privacy-contract tests. Compare the intended policies at creation, editing, serialization, and consumption rather than assuming an earlier check remains sufficient.

**Taxonomy:** `authorization-modeling`, `secure-parser-review`, `untrusted-input-handling`, `patch-verification`

## 8. Browser permission and consent lifecycle

**Cases:** Both Ryan Pickren Apple research chains; GitHub OAuth consent; Google IDX worker isolation; Facebook SDK message authentication and Meta Pixel context binding; Chrome graphics input validation; Pixel authentication-state binding

Learn origin identity, permission persistence, request semantics, and consent invalidation when a resource changes. Produce a consent-lifecycle map identifying what was approved, by whom, and under which immutable context. Keep approved application behavior separate from assumptions about framework or OS defaults.

The [Facebook SDK record](../data/reports/facebook-sdk-message-authentication-randomness-2023.json) gives a concrete reasoning example: examine what grants a message authority, then assess how accepted content is consumed. Authentication, rendering safety and embedding permissions are separate invariants. The record distinguishes reported mobile-browser impact from broader effects that depend on deployment, and labels remediation guidance as recommendations rather than an undocumented vendor patch.

**Taxonomy:** `browser-isolation-review`, `approval-state-integrity`, `identity-lifecycle-review`, `secure-parser-review`

## 9. HTTP message-boundary consistency

**Case:** ASP.NET Core Kestrel framing consistency

Review the documented parsing contract across proxies and application servers. Each layer should agree on message boundaries and reject ambiguous input. Record deployment-specific assumptions and check that updated runtimes and self-contained applications are actually deployed. A useful artifact is a parser-contract matrix linked to vendor remediation evidence.

**Taxonomy:** `secure-parser-review`, `untrusted-input-handling`, `integration-threat-modeling`, `patch-verification`

## 10. Multi-app authorization context

**Resource:** [USENIX Security 2025 research on integration-platform OAuth bindings](https://www.usenix.org/conference/usenixsecurity25/presentation/luo-kaixuan)

Keep the intended integration app and authorization issuer consistent throughout account linking. Model which component owns each identity check and how compatibility transitions preserve it. This research considers a different multi-app threat model from the Google device-grant case.

**Taxonomy:** `integration-threat-modeling`, `authorization-modeling`, `identity-lifecycle-review`

## 11. Coding-tool execution boundaries

**Cases:** Codex command-parser approval consistency, repository hook configuration, and metadata-helper configuration

Review both explicit agent actions and background tool operations. Security decisions must describe the operation the interpreter will execute, while repository-controlled configuration must not silently gain host authority. Preserve independent filesystem controls and distinguish ordinary repository content from local execution settings.

**Taxonomy:** `ai-authority-boundaries`, `secure-parser-review`, `integration-threat-modeling`, `untrusted-input-handling`

## 12. Workload-to-host trust boundaries

**Cases:** NVIDIA container-initialization context (historical 2025 entry); Redis scripting isolation

Separate workload-controlled configuration from privileged runtime initialization. Document where isolation relies on language memory safety, container boundaries, host identities, or virtualization. Check runtime-specific exceptions and corrected vendor release information. An architecture-review deliverable should identify each boundary and its independent safeguards, without assuming that all containers or all managed services share the same impact.

**Taxonomy:** `integration-threat-modeling`, `untrusted-input-handling`, `memory-safety-review`, `patch-verification`

**Reference:** [NIST SP 800-190](https://csrc.nist.gov/pubs/sp/800/190/final) (historical 2017 guidance)

## 13. Failure-path privacy and authorization

**Cases:** Facebook error-response exposure; Instagram privileged embedding fallback (historical)

Treat failure handling as part of the security contract. Error responses should avoid returning unintended data, while alternate execution paths should retain the requester’s original authority. Review common handlers and exceptional paths separately: a generic error message alone does not ensure a safe authorization decision.

**Taxonomy:** `error-response-design`, `authorization-modeling`, `secure-parser-review`

**Reference:** [OWASP Error Handling](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

## Common reporting skill

For every review, distinguish the observed behavior, the intended invariant, the evidence supporting impact, and the limits of that evidence. Document remediation and residual uncertainty. A large historical award is neither a forecast of future earnings nor permission to test a target.
