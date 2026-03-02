<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Germany - Accounting Reports

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_de_reports
- Dependencies: [[Odoo 19/Community Addons/l10n_de/l10n_de|l10n_de]], [[Odoo 19/Enterprise Addons/account_reports/account_reports|account_reports]]

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Germany - Accounting Reports - Models and Relations
class AccountMove
class ResCompany
class ResPartner
class "account.account" as account_account
AccountMove --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


