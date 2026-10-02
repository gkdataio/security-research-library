# Defensive learning guide

Use the historical cases as architecture-review examples. The goal is to understand and verify security invariants in an owned or authorized environment, not to replay a public exploit against other systems.

## 1. Approval and concurrency integrity

**Case:** Cloud Build approval consistency (older reference)

Learn to distinguish mutable object names from immutable versions, document exactly what an approval authorizes, and model ordering assumptions. A useful review artifact is a state diagram with the approved version, executed version, and invalidation conditions. Local unit tests should demonstrate the invariant across ordinary state changes.

**Taxonomy:** `approval-state-integrity`, `concurrency-reasoning`, `integration-threat-modeling`

**Reference:** [OWASP Transaction Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html)

## 2. Cloud identities and integration permissions

**Cases:** Meta service-identity and secret-access boundaries; Actifio driver and service-identity isolation

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

**Cases:** PostgreSQL CVE-2026-2006 (competition award); Chrome V8 type consistency and initialization checks

Learn encoding validity, length accounting, extension contracts, and safe use of assumptions across components. Produce a contract map showing where validation occurs and which downstream routines depend on it. Follow vendor patch guidance; review safe unit-test coverage rather than developing an exploit.

**Taxonomy:** `secure-parser-review`, `encoding-invariant-review`, `memory-safety-review`, `patch-verification`

## 6. Account recovery and identity binding

**Cases:** Microsoft account recovery; both Instagram recovery findings; Sign in with Apple; GitLab recovery-address binding; LiteSpeed Cache privileged user simulation

Learn to express which account a verification challenge or token represents, which actor may use it, and when it expires. Review atomic attempt accounting, challenge uniqueness, and relying-party assumptions. A useful deliverable is an identity-state model with local unit tests for its invariants.

**Taxonomy:** `identity-lifecycle-review`, `authorization-modeling`, `concurrency-reasoning`, `security-token-design`

## 7. Cross-API consistency and safe serialization

**Cases:** Google Support; YouTube creator privacy; YouTube/Pixel Recorder identity correlation; both GitHub fork-collaboration reports and cross-repository comparisons; HackerOne report serialization, private-program objects and support integration; Meta AI media ownership

Learn how the same entitlement can be represented across API surfaces and framework layers. Define response allowlists, ownership checks, and privacy-contract tests. Compare the intended policies at creation, editing, serialization, and consumption rather than assuming an earlier check remains sufficient.

**Taxonomy:** `authorization-modeling`, `secure-parser-review`, `untrusted-input-handling`, `patch-verification`

## 8. Browser permission and consent lifecycle

**Cases:** Both Ryan Pickren Apple research chains; GitHub OAuth consent; Google IDX worker isolation; Chrome graphics input validation

Learn origin identity, permission persistence, request semantics, and consent invalidation when a resource changes. Produce a consent-lifecycle map identifying what was approved, by whom, and under which immutable context. Keep approved application behavior separate from assumptions about framework or OS defaults.

**Taxonomy:** `browser-isolation-review`, `approval-state-integrity`, `identity-lifecycle-review`, `secure-parser-review`

## 9. HTTP message-boundary consistency

**Case:** ASP.NET Core Kestrel framing consistency

Review the documented parsing contract across proxies and application servers. Each layer should agree on message boundaries and reject ambiguous input. Record deployment-specific assumptions and check that updated runtimes and self-contained applications are actually deployed. A useful artifact is a parser-contract matrix linked to vendor remediation evidence.

**Taxonomy:** `secure-parser-review`, `untrusted-input-handling`, `integration-threat-modeling`, `patch-verification`

## Common reporting skill

For every review, distinguish the observed behavior, the intended invariant, the evidence supporting impact, and the limits of that evidence. Document remediation and residual uncertainty. A large historical award is neither a forecast of future earnings nor permission to test a target.
