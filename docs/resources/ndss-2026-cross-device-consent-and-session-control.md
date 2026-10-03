# Cross-device authentication: bind informed consent to session authority

[Resource index](../resource-index.md) · [Curated resource guide](../resources.md) · [Library home](../../README.md)

[Canonical JSON](<../../data/resources/ndss-2026-cross-device-consent-and-session-control.json>) · [Official resource](<https://www.ndss-symposium.org/ndss-paper/anchors-of-trust-a-usability-study-on-user-awareness-consent-and-control-in-cross-device-authentication/>)

**Publisher:** Internet Society / NDSS Symposium  
**Authors:** Xin Zhang; Xiaohan Zhang; Huijun Zhou; Bo Zhao  
**Resource type:** Research Paper  
**Version:** NDSS 2026 proceedings; DOI 10\.14722/ndss\.2026\.240656  
**Topics:** Identity; Authorization; Web Foundations  
**Defensive skills:** Review identity lifecycle; Review approval-state integrity; Write bounded security evidence

## Original summary

An evaluation of 27 services and a 100-participant user study examines missing context, explicit consent and post-login control in cross-device authentication\. Conceptual boundary: an already trusted device may approve access on another device, but possession of that trusted session alone does not establish the user’s informed intent for the new session\.

## Defensive use

For an owned design, connect the approving interface to meaningful target-device and request context, a deliberate consent decision, and accessible session review and revocation\. Verify that a revocation decision reaches the actual authorization checks\. UI confirmation alone cannot establish backend enforcement\.

Educational reference only; linked material does not authorize testing unrelated systems.

## Prerequisites

**Basis:** editorial guidance.

- Cross-device login approval and session lifecycle
- Difference between interface consent and server-side authorization

## Access and freshness

**Access cost at review:** free.

Publisher page and full paper were publicly readable at review\.

**Reviewed:** 2026-10-03T06:50:31Z  
**Review status:** primary source reviewed  
**Living resource:** No.

Reviewed publisher metadata and paper findings, discussion and limitations\. Proceedings edition identified; no separate revision date established\.

Review and retrieval timestamps are distinct from publication and version dates. Regeneration does not reverify sources.

## Dates and provenance

- **published:** 2026-02; precision: month; basis: explicit; source: [Publisher-hosted proceedings paper](<https://www.ndss-symposium.org/wp-content/uploads/2026-f656-paper.pdf>) (source ID: paper). Proceedings identifies the February 23–27, 2026 symposium; month describes that edition, not an established first online publication date\.
- **version released:** Unknown; precision: unknown; basis: not reported; source: Not recorded.
- **source displayed:** Unknown; precision: unknown; basis: not reported; source: Not recorded.

## Caveats

- The study documents implementation and user-expectation gaps, including six services without revocation controls\. These are historical observations, not a present-day exposure inventory\.
- The paper reports continued chat-history access in one revoked-session case; broad account-compromise risk is a consequence discussed by the authors, not a measured compromise rate across all 27 services\.
- The main user study used videos and screenshots and primarily U\.S\. participants; a separate ten-person interactive study is supportive but small\. Self-report and sampling limitations remain\.
- Developer acknowledgments and roadmap commitments do not establish completed remediation\. Context-specific interface patterns and broader validation remain future work\.
- Published in NDSS 2026 proceedings; the paper acknowledges anonymous reviewers\. This is not a protocol-wide proof or a claim that all cross-device authentication is insecure\.

## Sources and attribution

- [Anchors of Trust: A Usability Study on User Awareness, Consent, and Control in Cross-Device Authentication](<https://www.ndss-symposium.org/ndss-paper/anchors-of-trust-a-usability-study-on-user-awareness-consent-and-control-in-cross-device-authentication/>) — Internet Society / NDSS Symposium; source ID: primary; provenance: official primary; retrieved 2026-10-03T06:50:31Z; supports: summary, version, dates.
- [Publisher-hosted proceedings paper](<https://www.ndss-symposium.org/wp-content/uploads/2026-f656-paper.pdf>) — Internet Society / NDSS Symposium; source ID: paper; provenance: official primary; retrieved 2026-10-03T06:50:31Z; supports: summary, version, dates.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
