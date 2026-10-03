# Apple PCC startup archive processing lacked path confinement

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Apple  
**Product:** Private Cloud Compute server software

## What the evidence establishes

Publication window: within the preferred 12-month window; reviewed as of 2026-10-03.

Sentry documents a USD 150,000 award to Drinor Selmanaj for CVE-2026-20685\.

### Root cause

Privileged startup archive handling did not adequately confine output paths; mutable configuration could undermine runtime integrity assumptions\.

### Bounded impact

Researcher demonstrated configuration changes and telemetry disclosure in Apple’s virtual environment\. Apple confirms potential sensitive-information leakage from a privileged network position\.

### Defensive lessons

- Confine archive output and authenticate provisioning inputs\.
- Include security-relevant mutable configuration in integrity review\.
- Use the fixed PCC release and preserve the vendor’s impact prerequisites\.

## Award and evidence

**USD 150,000** — bug\_bounty; single\_vulnerability; status: awarded.

Evidence level: researcher\_reported\_with\_vendor\_quote. Individual CVE award attributed to Selmanaj\. Researcher-hosted Apple offer is not vendor-hosted payment confirmation\. USD follows official program context; cash settlement and award date are unverified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/apple-pcc-boot-archive-path-validation-2026.json>).

## Dates

- **published:** 2026-07-31; precision: day; basis: explicit. Sentry’s own article listing supplies the date\.
- **public disclosure:** 2026-05-18; precision: day; basis: explicit. CVE publication timestamp; detailed researcher article appeared later\.
- **reported:** Unknown; precision: unknown; basis: not\_reported
- **awarded:** Unknown; precision: unknown; basis: not\_reported
- **fixed:** Unknown; precision: unknown; basis: not\_reported. Apple identifies PCC Release 5E290\.3 as fixed; exact release/deployment date was not established\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-02T17:03:00Z. Read the researcher article, publication index, full Apple-authored CNA record and official currency context; reviewed the researcher-hosted offer graphic\.

- Research was demonstrated in Apple’s virtual environment; production was not tested by the researcher\.
- No confirmed production prompt-content leakage is claimed here\.
- Award attribution is researcher-hosted; vendor CNA evidence corroborates the vulnerability and fixed version, not payout\.
- No exact report, award, fix deployment or payment date was established\.

## Sources and attribution

- [Beyond Prompt Injection: Hacking Apple's Private Cloud Compute](<https://blog.sentry.security/beyond-prompt-injection-hacking-apples-private-cloud-compute/>) — Drinor Selmanaj / Sentry; retrieved 2026-10-02T17:03:00Z.
- [Sentry article listing](<https://blog.sentry.security/>) — Sentry; retrieved 2026-10-02T17:03:00Z.
- [Apple CNA record for CVE-2026-20685](<https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/20xxx/CVE-2026-20685.json>) — Apple CNA, distributed through the CVE Program; retrieved 2026-10-02T17:03:00Z.
- [Researcher-hosted Apple award-offer graphic](<https://storage.ghost.io/c/3c/85/3c852989-e4b5-4868-8226-9c9bebdfb8f2/content/images/2026/07/150k-post2.png>) — Sentry; retrieved 2026-10-02T17:03:00Z.
- [Apple Security Bounty US-dollar program context](<https://www.apple.com/nz/newsroom/2022/07/apple-expands-commitment-to-protect-users-from-mercenary-spyware/>) — Apple Newsroom; retrieved 2026-10-02T17:03:00Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
