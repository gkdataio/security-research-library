# Information exposure and response privacy

[Browse all categories](../vulnerability-types.md) · [All reports](../reports.md) · [All resources](../resource-index.md) · [Library home](../../README.md)

**Vulnerability family** · 5 reports · 4 related resources · 2 diagrams

Unintended disclosure through error responses, diagnostics and output contracts.

Report membership uses the existing primary or secondary category information-exposure. Learning resources and diagrams are related context, not additional findings. Cross-links do not create duplicate records or testing authorization.

On this page: [Reports](#reports) · [Related learning](#related-learning) · [Conceptual diagrams](#conceptual-diagrams)

<a id="reports"></a>
## Reports

- [Facebook error responses exposed unintended application data](<../reports/facebook-error-response-data-isolation-2019.md>) — Meta \(Facebook\); primary category.
- [Framework serialization change exposed private HackerOne user attributes](<../reports/hackerone-report-json-serialization-data-exposure-2025.md>) — HackerOne; primary category.
- [GitHub unsafe reflection crossed method and credential boundaries](<../reports/github-reflection-method-authority-cve-2024-0200.md>) — GitHub; secondary category.
- [HackerOne exports omitted internal-attachment authorization](<../reports/hackerone-export-attachment-authorization-2016.md>) — HackerOne; secondary category.
- [Instagram client configuration exposed an application credential](<../reports/instagram-application-credential-client-containment-2022.md>) — Meta; primary category.

<a id="related-learning"></a>
## Related learning

Included by the topic crosswalk or an explicit resource link in a conceptual diagram below. Each entry states its relationship; this does not reclassify the resource.

- [Error Handling Cheat Sheet](<../resources/owasp-error-response-data-minimization.md>) — diagram: [Failures need separate public and diagnostic contracts](<../diagram-gallery.md#error-diagnostic-disclosure-boundary>).
- [Next\.js data security: server authorization and client-visible data](<../resources/nextjs-server-client-data-security.md>) — diagram: [Server disclosure and browser interpretation](<../diagram-gallery.md#server-client-data-consumer-boundaries>).
- [OWASP LLM05:2025: generated-output consumer trust](<../resources/owasp-llm-output-consumer-trust.md>) — diagram: [Server disclosure and browser interpretation](<../diagram-gallery.md#server-client-data-consumer-boundaries>).
- [OWASP Logging: trustworthy and minimal application evidence](<../resources/owasp-security-logging-evidence-quality.md>) — diagram: [Failures need separate public and diagnostic contracts](<../diagram-gallery.md#error-diagnostic-disclosure-boundary>).

<a id="conceptual-diagrams"></a>
## Conceptual diagrams

Included only when the canonical diagram links at least one report in this category. These are educational models, not vendor architecture claims.

- [Failures need separate public and diagnostic contracts](<../diagram-gallery.md#error-diagnostic-disclosure-boundary>)
- [Server disclosure and browser interpretation](<../diagram-gallery.md#server-client-data-consumer-boundaries>)

---

Generated offline from [canonical categories](../../data/taxonomy.json), the [navigation crosswalk](../../data/category-navigation.json) and existing report/resource/diagram records. Sources, classifications and review timestamps are unchanged. [Navigation maintenance](../category-navigation.md).
