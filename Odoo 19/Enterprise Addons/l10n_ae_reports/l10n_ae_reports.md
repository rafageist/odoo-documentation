<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# United Arab Emirates - Accounting Reports

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_ae_reports
- Dependencies: [[Odoo 19/Community Addons/l10n_ae/l10n_ae|l10n_ae]], [[Odoo 19/Enterprise Addons/account_reports/account_reports|account_reports]], [[Odoo 19/Enterprise Addons/account_fiscal_categories/account_fiscal_categories|account_fiscal_categories]]
## XML Artifacts (detected)

- Views: 1
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountReport`
- `AccountReturn`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title United Arab Emirates - Accounting Reports - Models and Relations
class AccountReport
class AccountReturn
class ResCompany
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
