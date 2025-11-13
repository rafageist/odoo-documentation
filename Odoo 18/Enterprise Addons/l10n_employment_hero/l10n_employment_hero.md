<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Employment Hero Payroll

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_employment_hero
- Dependencies: [[Odoo 18/Enterprise Addons/account_accountant/account_accountant|account_accountant]]
## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountAccount`
- `AccountTax`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Employment Hero Payroll - Models and Relations
class AccountMove
class AccountAccount
class AccountTax
class ResCompany
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
