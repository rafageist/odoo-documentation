<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Belgium - Payroll with Accounting

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_be_hr_payroll_account
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]], [[Odoo 18/Enterprise Addons/hr_payroll_account/hr_payroll_account|hr_payroll_account]], [[Odoo 18/Community Addons/l10n_be/l10n_be|l10n_be]]
## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `L10nBe274XX`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll with Accounting - Models and Relations
class L10nBe274XX
class ResCompany
class "account.move" as account_move
L10nBe274XX --> account_move : many2one
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
