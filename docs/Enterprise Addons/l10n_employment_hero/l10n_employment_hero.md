<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Employment Hero Payroll

- Scope: Enterprise Addons
- Source: enterprise/l10n_employment_hero
- Dependencies: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



