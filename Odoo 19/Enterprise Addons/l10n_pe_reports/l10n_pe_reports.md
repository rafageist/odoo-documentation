<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Peru - Accounting Reports

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_pe_reports
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_pe_edi/l10n_pe_edi|l10n_pe_edi]], [[Odoo 19/Enterprise Addons/account_reports/account_reports|account_reports]]
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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
