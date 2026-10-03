# OWASP LLM08:2025: retrieval permissions and knowledge provenance

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/owasp-rag-retrieval-permission-boundaries.json>) · [Official resource](<https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/>)

**Publisher:** OWASP Gen AI Security Project  
**Authors:** Not identified in the reviewed record  
**Resource type:** Architecture Guide  
**Version:** LLM08:2025  
**Topics:** Ai Security; Authorization  
**Defensive skills:** Model access-control invariants; Review AI authority boundaries; Threat-model integrations

## Original summary

Examines security assumptions around retrieval-augmented generation, including access to embeddings, cross-context disclosure and integrity of imported knowledge\. Shared retrieval infrastructure must preserve the distinctions between users and data classifications\. Source validation and retrieval records help explain which knowledge entered a response and whether access was appropriate\.

## Defensive use

For an owned RAG design, document dataset partitions and permission-aware retrieval, preserve source classifications when combining knowledge, and review ingestion integrity\. Record retrieval events so confidentiality and provenance decisions remain reviewable\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Basic concepts of embeddings, vector stores and retrieval-augmented generation
- User, group and tenant access-control models

## Access and freshness

**Access cost at review:** free.

Official public guidance was readable without an account at review time\.

**Reviewed:** 2026-10-03T04:41:24Z  
**Review status:** primary source reviewed  
**Living resource:** Yes.

Reviewed the official page content\. The review date does not establish publication or an immutable revision\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- The 2025 designation is an edition identifier; publication and latest-update dates were not established\.
- This record focuses on permissions and provenance; it does not reproduce the source’s attack scenarios or quantify embedding reconstruction risk\.
- RAG grounding can improve relevance without establishing that retrieved content is authorized or trustworthy\.

## Sources and attribution

- [LLM08:2025 Vector and Embedding Weaknesses](<https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/>) — OWASP Gen AI Security Project; source ID: primary; provenance: official primary; retrieved 2026-10-03T04:40:03Z; supports: summary, version.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
