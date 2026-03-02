<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Peru - Accounting Reports

- Scope: Enterprise Addons
- Source: enterprise/l10n_pe_reports
- Dependencies: [[docs/Enterprise Addons/l10n_pe_edi/l10n_pe_edi|l10n_pe_edi]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `AccountReport`
- `l10n_pe.ple.usage`
- `ResCompany`
- `ResCountry`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Peru - Accounting Reports - Models and Relations
class AccountMove
class AccountReport
class "l10n_pe.ple.usage" as l10n_pe_ple_usage
class ResCompany
class ResCountry
class "account.move" as account_move
AccountMove --> account_move : many2one
AccountMove --> l10n_pe_ple_usage : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



