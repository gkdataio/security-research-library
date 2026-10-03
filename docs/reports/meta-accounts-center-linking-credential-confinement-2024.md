# Meta Accounts Center linking lost credential and identity confinement

[Report index](../reports.md) · [Diagram gallery](../diagram-gallery.md) · [Library home](../../README.md)

**Organization:** Meta  
**Product:** Accounts Center Facebook–Instagram account linking

## What the evidence establishes

Publication window: uncertain original publication date; reviewed as of 2026-10-03.

A researcher-reported USD 30,000 award documents a cross-product account-linking trust failure\.

### Root cause

SSO destination validation and browser-message confidentiality did not preserve account-linking credential confinement\. Session identity could also differ from the person authorizing the connection, allowing linking authority to cross account boundaries\.

### Bounded impact

The researcher reports unauthorized Facebook linking and persistent account control\. Prerequisites included an attacker-controlled Instagram account, account-specific authorization material, an authenticated Facebook user visiting attacker-controlled content, and user confirmation\. Mobile sign-in is described as potential; no widespread exploitation is established\.

### Defensive lessons

- Bind linking approval to both intended account identities, the initiating session, and the exact operation\.
- Constrain credential delivery end to end, including browser-message recipients and final redirect destinations\.
- Make identity changes visible and require fresh authorization when a sensitive linking flow changes account context\.
- Treat these as defensive design recommendations rather than a reconstruction of the undisclosed vendor patch\.

## Award and evidence

**USD 30,000** — bug\_bounty; single\_report; status: awarded.

Evidence level: researcher\_reported. The article assigns one award to the reported finding\. It uses $; USD is inferred from official February 2020 program-wide reporting, roughly five years before this award\. That contextual source does not verify the individual denomination or settlement\. No conflicting currency was identified\.

Exact source quotation and location remain in the [canonical record](<../../data/reports/meta-accounts-center-linking-credential-confinement-2024.json>).

## Dates

- **published:** Unknown; precision: unknown; basis: not\_reported. Current article and archive index display January 15, 2026; original publication versus migration/republication is unverified\. This header is not used to assert recent research\.
- **public disclosure:** Unknown; precision: unknown; basis: not\_reported. Earliest public disclosure was not established\.
- **reported:** 2024-10-16; precision: day; basis: explicit
- **awarded:** 2024-11-27; precision: day; basis: explicit
- **fixed:** 2024-11-05; precision: day; basis: explicit. Overall researcher timeline label; component-level remediation and patch details are not independently verified\.
- **paid:** Unknown; precision: unknown; basis: not\_reported
- **award announced:** Unknown; precision: unknown; basis: not\_reported
- **mitigated:** Unknown; precision: unknown; basis: not\_reported

## Verification limits

Reviewed: 2026-10-03T10:10:05\.389636Z. Read the primary article and dated individual award, checked the researcher archive and official denomination context, and compared report identities with existing Meta records\. Retained only conceptual defensive content\.

- The award and overall fix are researcher-reported; vendor confirmation and cash settlement are unverified\.
- Original publication is unknown, so no preferred-window inclusion is claimed\.
- USD relies on earlier program-wide context rather than report-specific currency evidence\.
- The source inconsistently names the final return host; no exact route or operational sequence is inferred\.
- This account-linking report is counted once, not as separate records for its constituent weaknesses\.

## Sources and attribution

- [Two-click Facebook account takeover via FXAuth token and blob theft](<https://ysamm.com/uncategorized/2026/01/15/steal-fxauth-leads-instagram-ato.html>) — Youssef Sammouda; retrieved 2026-10-03T10:10:05\.389636Z.
- [Una mirada retrospectiva a los aspectos más destacados de Bug Bounty 2019](<https://about.fb.com/ltam/news/2020/02/una-mirada-retrospectiva-a-los-aspectos-mas-destacados-de-bug-bounty-2019/>) — Dan Gurfinkel / Facebook; retrieved 2026-10-03T10:10:05\.389636Z.

Original summary: Security Research Library contributors, CC BY 4.0. Linked sources retain their own rights. [License scope](../../LICENSE.md).
