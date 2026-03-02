
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Belgium - Payroll with Accounting

- Scope: Enterprise Addons
- Source: enterprise/l10n_be_hr_payroll_account
- Dependencies: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]], [[docs/Enterprise Addons/hr_payroll_account/hr_payroll_account|hr_payroll_account]], [[docs/Community Addons/l10n_be/l10n_be|l10n_be]]

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `l10n_be.274_xx`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Belgium - Payroll with Accounting - Models and Relations
class "l10n_be.274_xx" as l10n_be_274_xx
class ResCompany
class "account.move" as account_move
l10n_be_274_xx --> account_move : many2one
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


