<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Germany - Accounting Reports

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_de_reports
- Dependencies: [[Odoo 18/Community Addons/l10n_de/l10n_de|l10n_de]], [[Odoo 18/Enterprise Addons/account_reports/account_reports|account_reports]]
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
