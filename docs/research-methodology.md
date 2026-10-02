# Research methodology and evidence

[Library home](../README.md) · [Readable reports](reports.md) · [Program policies](programs.md) · [Learning guide](learning-guide.md)

This guide is for security researchers, bug hunters, authorized offensive-security teams and people building research catalogs with agents or APIs. The methods below are editorial learning guidance. A linked disclosure supports its own recorded observations, not a claim that its researcher followed every method here.

## Form a precise hypothesis

State the security property before choosing a technique: which identity owns the data, what an approval covers, which state a completion event belongs to, or which assumptions a parser guarantees. Distinguish an architectural hypothesis from a demonstrated defect. Record what evidence would disprove the hypothesis.

The [GitLab recovery case](reports/gitlab-recovery-address-binding-cve-2023-7028.md) illustrates why recovery integrity and login protection need separate claims. The [Cloud Build case](reports/google-cloud-build-approval-toctou-2025.md) separates the identity of reviewed content from its later version. These are reasoning examples, not instructions to repeat the incidents.

Relevant machine-readable skill tags: `identity-lifecycle-review`, `authorization-modeling`, `approval-state-integrity`, `concurrency-reasoning`.

## Read code across a trust boundary

In code you are permitted to review, document where untrusted values enter, where identity or ownership is established, and which component enforces the final decision. Compare the stated contract with the consumer's assumptions. Include error paths and feature transitions; a validation function's presence does not establish that all callers use it consistently.

Prerequisites include understanding the language's data types, the application's identity model and the relevant framework's documented behavior. Keep source-backed descriptions of a real fix distinct from your proposed design improvement.

Relevant tags: `secure-parser-review`, `untrusted-input-handling`, `integration-threat-modeling`, `error-response-design`.

## Use contained exercises to test an invariant

Use deliberately vulnerable training material or a synthetic local model with fictitious identities and data. Express the intended property as a unit-test assertion or state diagram. Compare ordinary valid transitions with invalid states and verify that a rejected transition preserves the protected state. Keep network access and real credentials out of a self-contained learning exercise.

Prerequisites are a documented exercise boundary, reversible fixtures and a known expected result. The artifact should explain the invariant and test result; it should not become a live-system reproduction sequence. The [diagram gallery](diagram-gallery.md) supplies conceptual models, and the [resource catalog](resources.md) links official guidance.

## Collect the minimum evidence for the claim

Separate observation, inference and uncertainty. Document the environment and version represented by the evidence, without turning identifiers into a target inventory. Use synthetic or redacted examples; discovering another person's data is a reason to stop and follow the governing reporting process.

Describe demonstrated impact before hypothetical reach. A failed security assumption does not, by itself, prove reliable account takeover or arbitrary execution in every deployment. Preserve attribution when a vendor response is reproduced by a researcher rather than independently published by the vendor.

Relevant tags: `defensive-evidence-writing`, `patch-verification`.

## Use the JSON as a research interface

Canonical records and deterministic exports support indexing, retrieval, comparison and agent-assisted study. They are ordinary data files, not a hosted ingestion API or an authorization feed.

- Resolve stable IDs before joining reports, diagrams, resources and taxonomy.
- Preserve the source links and distinguish source-explicit facts from editorial classifications.
- Treat unknown dates, amounts and status as unknown, rather than as zero, false or permission.
- Keep program reward advertisements separate from documented report awards.
- Preserve publication, reporting, award and fix dates as different events.
- Use verification timestamps to decide what needs rechecking; they do not certify that a historical issue remains present.

See the [schemas and exports](../README.md#use-the-json). Program summaries omit asset inventories and do not authorize testing; consult current official terms and your actual authorization. This collection supplies no exploit recipes, live-target chains or autonomous targeting workflow.
