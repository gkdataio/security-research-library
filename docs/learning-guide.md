# Defensive learning guide

Use these historical cases to ask better questions about a system's design. Each topic names a security rule that should always hold, also called an invariant, and suggests a way to review it. The [methodology guide](research-methodology.md) covers hypotheses, code review and contained learning exercises for researchers and authorized offensive-security teams. Work only in an owned or authorized environment; these examples are not permission to replay a public exploit elsewhere.

## 1. Approval and concurrency integrity

**Case:** Cloud Build approval consistency (older reference)

Does the system execute the exact version a reviewer approved? A name can stay the same while its contents change. Draw the approved version, the executed version and the changes that would require a new approval. Use local unit tests to check that the rule holds as state changes.

The [Cloud Build record](../data/reports/google-cloud-build-approval-toctou-2025.json) distinguishes the observed revision mismatch from possible consequences under a pipeline’s privileges. Its fix-status confirmation is kept separate from an unknown deployment date.

**Taxonomy:** `approval-state-integrity`, `concurrency-reasoning`, `integration-threat-modeling`

**Reference:** [OWASP Transaction Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html)

## 2. Cloud identities and integration permissions

**Cases:** Meta service-identity and secret-access boundaries; Actifio driver and service-identity isolation; Apple PCC provisioning and mutable-configuration integrity

List each service identity, how it authenticates, which secrets it owns and which resources it can access through each integration. Compare those permissions with what the service actually needs. Keep possible access separate from data that was actually read, and stop collecting evidence once the approved review objective is met.

The [Instagram application-credential case](../data/reports/instagram-application-credential-client-containment-2022.json) shows why credential types matter: data delivered to a client should not carry server-level authority. The vendor confirmed the award, but the record still limits what can be claimed about downstream impact.

**Taxonomy:** `cloud-iam-review`, `machine-identity-governance`, `secrets-containment`

**Reference:** [AWS IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 3. Build systems and dependency provenance

Foundational reading: [Sigstore trust assumptions](resources/sigstore-security-model.md), [GitHub artifact attestation claims and consumer policy](resources/github-artifact-attestations.md), and [NIST SSDF component governance](resources/nist-ssdf-1-1-dependency-governance.md). Read provenance as evidence with explicit trust assumptions; a signature does not establish code quality.

**Cases:** GitHub dependency-source trust; Angular build-cache and automation trust

Trace where dependencies and build inputs come from, who controls their names and contents, and which jobs use them. Include shared caches, artifacts and bots in the diagram. A job's read-only permissions do not tell you whether its shared state is isolated from more privileged work.

**Taxonomy:** `pipeline-trust-modeling`, `dependency-provenance`, `cache-artifact-isolation`, `machine-identity-governance`

**Reference:** [SLSA v1.2](https://slsa.dev/spec/v1.2/)

## 4. AI tools and persistent-state authorization

**Case:** Gemini Enterprise persistent-memory integrity

Reading a document should not give that document permission to change saved state. List the operations that make lasting changes, the checks that authorize them and how the system keeps retrieved text from supplying that authorization. Use synthetic content and a local mock integration to check the distinction.

In the [Gemini memory record](../data/reports/google-gemini-enterprise-connected-content-memory-integrity-2026.json), the researcher observed deletion in a controlled account. Broader consequences were not demonstrated, and the vendor's exact fix remains unknown.

**Taxonomy:** `ai-authority-boundaries`, `authorization-modeling`, `untrusted-input-handling`

## 5. Parser contracts and memory safety

Foundational reading: [Rust ownership and borrowing](resources/rust-ownership-borrowing.md), [Rust slices and text boundaries](resources/rust-slices-parser-boundaries.md), and [C++ bounds and lifetime guidance](resources/cpp-core-guidelines-bounds-lifetime.md). Keep ownership, extent, lifetime, encoding and graceful error handling as distinct review questions.

**Cases:** PostgreSQL CVE-2026-2006 encoding contracts, CVE-2026-2005 buffer capacity and CVE-2026-2004 input-type validation (competition entries); MariaDB JSON normalization; Chrome V8 type consistency and initialization checks; Redis Lua object-lifetime integrity, deserialization ownership and replication-state lifetime

Which component checks an input's encoding, type and length, and which later routines rely on those checks? Map those dependencies, including extensions. Follow vendor patch guidance and review safe unit-test coverage rather than developing an exploit. The MariaDB case also shows a limit of demonstration evidence: code execution in a controlled setting does not establish the same reliability in every deployment.

**Taxonomy:** `secure-parser-review`, `encoding-invariant-review`, `memory-safety-review`, `patch-verification`

**Reference:** [Chromium Rule of Two](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/rule-of-2.md) · [Parsing and authority visual](visual-theory.md#separate-parsing-safety-from-action-authority)

## 6. Account recovery and identity binding

**Cases:** Microsoft account recovery; both Instagram recovery findings; Sign in with Apple; Google device-grant binding; Meta Quest login-migration credential confinement; Meta linked-account SMS verification; GitLab recovery-address binding; LiteSpeed Cache privileged user simulation

For each challenge or token, write down the account it belongs to, who may use it and when it expires. Check that attempt limits remain correct under concurrent use, challenges are unique and relying applications make compatible assumptions. A state diagram and local unit tests can make these rules easier to review.

The [Meta Quest migration case](../data/reports/meta-quest-oauth-redirect-confidentiality-2022.json) asks a useful question about upgrades: is an existing login destination still safe after the identity flow changes? Track who should receive each credential throughout the flow. A reported fix does not establish how every related component behaves.

The [GitLab recovery case](reports/gitlab-recovery-address-binding-cve-2023-7028.md) separates password-reset integrity from login protection. A second factor can preserve the login boundary while recovery remains flawed. Its documented remediation covers the complete reset flow, including address handling and generated email, rather than only a single input check.

**Taxonomy:** `identity-lifecycle-review`, `authorization-modeling`, `concurrency-reasoning`, `security-token-design`

**Reference:** [OWASP Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) · [Recovery-state visual](visual-theory.md#preserve-ownership-through-account-recovery)

## 7. Cross-API consistency and safe serialization

**Cases:** Google Support; YouTube creator privacy; YouTube/Pixel Recorder identity correlation; both GitHub fork-collaboration reports and cross-repository comparisons; HackerOne report serialization, private-program objects and support integration; Meta AI media ownership

Follow the same access rule through each API and framework layer. Check who owns an object, which fields a response may include and whether those limits survive creation, editing, serialization and use by another component. Test the privacy rules at each stage; an earlier check may no longer be sufficient.

**Taxonomy:** `authorization-modeling`, `secure-parser-review`, `untrusted-input-handling`, `patch-verification`

## 8. Browser permission and consent lifecycle

**Cases:** Both Ryan Pickren Apple research chains; GitHub OAuth consent; Google IDX worker isolation; Facebook SDK message authentication and Meta Pixel context binding; Chrome graphics input validation; Pixel authentication-state binding

Record what the user approved, which origin received permission, how long it lasts and which changes should invalidate it. Include request handling and the context that must remain unchanged. Check framework and OS defaults separately from the application's intended consent rules.

The [Facebook SDK record](../data/reports/facebook-sdk-message-authentication-randomness-2023.json) separates three questions: is the message authentic, is its content safe to render and is the page allowed to be embedded? Its reported mobile-browser impact does not establish the same effect in every deployment. The defensive advice is a set of recommendations, not a description of the vendor's undisclosed patch.

The Meta Pixel case adds another question: may the recipient receive the page data being sent? Knowing who sent the message does not answer it. [OWASP messaging guidance](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html) and the [message-boundary visual](visual-theory.md#keep-browser-message-identity-separate-from-authority) separate transport checks, permission to act and safe content handling.

**Taxonomy:** `browser-isolation-review`, `approval-state-integrity`, `identity-lifecycle-review`, `secure-parser-review`

## 9. HTTP message-boundary consistency

**Case:** ASP.NET Core Kestrel framing consistency

Compare how each proxy and application server decides where an HTTP message ends. The layers should agree and reject ambiguous input. Record assumptions that depend on the deployment, then check that both runtimes and self-contained applications have received the applicable updates. Link each component's parsing rules to the vendor's remediation evidence.

**Taxonomy:** `secure-parser-review`, `untrusted-input-handling`, `integration-threat-modeling`, `patch-verification`

## 10. Multi-app authorization context

**Resource:** [USENIX Security 2025 research on integration-platform OAuth bindings](https://www.usenix.org/conference/usenixsecurity25/presentation/luo-kaixuan)

Track the intended integration app and authorization issuer through every stage of account linking. Identify which component checks each identity and whether those checks survive compatibility changes. This research studies a different multi-app threat model from the Google device-grant case.

**Taxonomy:** `integration-threat-modeling`, `authorization-modeling`, `identity-lifecycle-review`

## 11. Coding-tool execution boundaries

**Cases:** Codex command-parser approval consistency, repository hook configuration, and metadata-helper configuration

Check background tool operations as well as the commands an agent shows the user. An approval must cover what the interpreter will actually execute. Repository-controlled configuration should not silently gain permission to run on the host. Keep filesystem restrictions independent of command approval, and distinguish ordinary repository files from local settings that can trigger execution.

**Taxonomy:** `ai-authority-boundaries`, `secure-parser-review`, `integration-threat-modeling`, `untrusted-input-handling`

## 12. Workload-to-host trust boundaries

**Cases:** NVIDIA container-initialization context (historical 2025 entry); Redis scripting isolation

Keep configuration supplied by a workload separate from privileged runtime startup. Identify where isolation depends on memory safety, containers, host identities or virtualization, and record the safeguards at each boundary. Check runtime-specific exceptions and corrected vendor release guidance. The effect on one deployment does not establish the same impact for every container or managed service.

**Taxonomy:** `integration-threat-modeling`, `untrusted-input-handling`, `memory-safety-review`, `patch-verification`

**Reference:** [NIST SP 800-190](https://csrc.nist.gov/pubs/sp/800/190/final) (historical 2017 guidance)

## 13. Failure-path privacy and authorization

**Cases:** Facebook error-response exposure; Instagram privileged embedding fallback (historical)

When an operation fails, its privacy and access rules still apply. Error responses should not leak data, and a fallback should stay within the original requester's permissions. Review shared error handlers and exceptional paths separately. Returning a generic error message does not, by itself, make the access decision safe.

**Taxonomy:** `error-response-design`, `authorization-modeling`, `secure-parser-review`

**Reference:** [OWASP Error Handling](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html) · [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

## Common reporting skill

Explain what happened, what should have happened and which evidence supports the claimed impact. Say what was fixed and what remains unknown. A large historical award does not predict future earnings or grant permission to test a target.
