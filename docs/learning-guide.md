# Defensive learning guide

Use the historical cases as architecture-review examples. The goal is to understand and verify security invariants in an owned or authorized environment, not to replay a public exploit against other systems.

## 1. Approval and concurrency integrity

**Case:** Cloud Build approval consistency (older reference)

Learn to distinguish mutable object names from immutable versions, document exactly what an approval authorizes, and model ordering assumptions. A useful review artifact is a state diagram with the approved version, executed version, and invalidation conditions. Local unit tests should demonstrate the invariant across ordinary state changes.

**Taxonomy:** `approval-state-integrity`, `concurrency-reasoning`, `integration-threat-modeling`

## 2. Cloud identities and integration permissions

**Case:** Meta service-identity and secret-access boundaries

Learn effective-permission review, service authentication, secret ownership, and least privilege across integrations. Produce an identity-to-resource access matrix and a justified minimum-permission design. Separate reported reach from actual data access; stop evidence collection once the approved review objective is met.

**Taxonomy:** `cloud-iam-review`, `machine-identity-governance`, `secrets-containment`

## 3. Build systems and dependency provenance

**Cases:** GitHub dependency-source trust; Angular build-cache and automation trust

Learn registry provenance, namespace governance, artifact integrity, cache separation, and bot authorization. Produce a trust-boundary diagram identifying who can create each input and which execution context consumes it. Review both direct privileges and shared state without assuming a read-only job is isolated.

**Taxonomy:** `pipeline-trust-modeling`, `dependency-provenance`, `cache-artifact-isolation`, `machine-identity-governance`

## 4. AI tools and persistent-state authorization

**Case:** Gemini Enterprise persistent-memory integrity

Learn data provenance and the difference between retrieved text and user authorization. Document which operations change persistent state, what independent checks authorize them, and how connector content is kept out of the authority path. Use synthetic content and a local mock integration for regression coverage.

**Taxonomy:** `ai-authority-boundaries`, `authorization-modeling`, `untrusted-input-handling`

## 5. Parser contracts and memory safety

**Case:** PostgreSQL CVE-2026-2006 (competition award)

Learn encoding validity, length accounting, extension contracts, and safe use of assumptions across components. Produce a contract map showing where validation occurs and which downstream routines depend on it. Follow vendor patch guidance; review safe unit-test coverage rather than developing an exploit.

**Taxonomy:** `secure-parser-review`, `encoding-invariant-review`, `memory-safety-review`, `patch-verification`

## Common reporting skill

For every review, distinguish the observed behavior, the intended invariant, the evidence supporting impact, and the limits of that evidence. Document remediation and residual uncertainty. A large historical award is neither a forecast of future earnings nor permission to test a target.
