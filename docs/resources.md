# Official learning resources

This collection is separate from paid-award reports. It contains official educational references, with original summaries, source review dates, version information where known, and clearly marked editorial prerequisites.

- [OWASP ASVS 5.0.0](https://owasp.org/projects/asvs): turn security goals into versioned verification requirements
- [OAuth security best practice, RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html): review identity integration assumptions and token protections
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html): make authorization consistent, explicit, and testable
- [OWASP LLM Prompt Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html): reason about untrusted content, tool permissions, and defense in depth
- [HackerOne Quality Reports](https://docs.hackerone.com/en/articles/8475116-quality-reports): communicate evidence-backed impact, scope, and remediation clearly
- [PortSwigger Web Security Academy](https://portswigger.net/web-security): study fundamentals in provider-controlled training environments

- [SLSA v1.2](https://slsa.dev/spec/v1.2/): review build provenance, artifact integrity, and distinct assurance levels
- [AWS IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html): assess workload identities, short-lived credentials, permission scope, and access lifecycle

- [OWASP SSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html): combine destination policy with independent network isolation

- [OWASP Transaction Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html): bind approval to significant data and validate state transitions

- [OWASP Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html): preserve account binding through recovery and reset

- [USENIX Security 2025: Cross-app OAuth bindings](https://www.usenix.org/conference/usenixsecurity25/presentation/luo-kaixuan): study app-specific authorization context in integration platforms

- [Chromium Rule of Two](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/rule-of-2.md): separate input trust, memory safety and process privilege
- [NIST SP 800-190](https://csrc.nist.gov/pubs/sp/800/190/final): study container/runtime/host boundaries using explicitly historical 2017 guidance

- [OWASP Error Handling](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html): minimize client-visible failure data while retaining appropriate internal diagnostics

- [OWASP HTML5 Web Messaging](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html): distinguish message origin, data validity and safe consumption from application authorization

- [NIST SP 800-162: attribute authority and policy traceability](https://csrc.nist.gov/pubs/sp/800/162/upd2/final): Defines authorization in terms of subject, object, operation and environmental attributes evaluated against policy. Enterprise considerations connect business rules to machine-enforced decisions, attribute authorities and consistent meanings across organizations. Attribute maintenance, provenance and integrity are part of the authorization model rather than incidental metadata. [Structured record](../data/resources/nist-sp-800-162-attribute-authority-modeling.json)
- [OWASP Secure Code Review: baseline and change-focused review](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html): Explains how whole-codebase reviews and change-focused reviews answer different assurance questions. Connects architecture, business requirements and existing findings to manual examination of data movement, control placement and workflow state. Review documentation records the inspected version, coverage and remediation decisions. [Structured record](../data/resources/owasp-secure-code-review-methodology.json)
- [OWASP Logging: trustworthy and minimal application evidence](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html): Explains how application events support investigation through consistent context, interaction identifiers, outcomes and confidence information. Distinguishes event occurrence from recording time and treats cross-boundary event data as untrusted. Evidence quality also depends on data minimization, access restrictions, integrity protection and reliable logging behavior. [Structured record](../data/resources/owasp-security-logging-evidence-quality.json)
- [OWASP Threat Modeling: system assumptions and mitigation validation](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html): Presents an iterative design-review process linking a system model to potential threats, agreed responses and validation. Data-flow diagrams expose trust boundaries and dependencies; structured prompts help identify missing assumptions. Mitigations become measurable requirements, and accepted residual risks remain documented as the system changes. [Structured record](../data/resources/owasp-threat-modeling-assumptions-and-validation.json)

The collection links these resources without copying exercises, payloads, or operational techniques. Training access does not authorize testing unrelated systems. Living documents may change; the JSON records say when they were reviewed. Suggested prerequisites are editorial guidance unless explicitly marked otherwise.

[Machine-readable export](../exports/resources.json) · [Resource taxonomy](../data/resource-taxonomy.json) · [Conceptual visual guide](visual-theory.md)
