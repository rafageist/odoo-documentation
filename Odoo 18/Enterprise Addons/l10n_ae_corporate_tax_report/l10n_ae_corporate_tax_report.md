<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# United Arab Emirates - Corporate Tax Report

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_ae_corporate_tax_report
- Dependencies: [[Odoo 18/Community Addons/l10n_ae/l10n_ae|l10n_ae]], [[Odoo 18/Enterprise Addons/account_reports/account_reports|account_reports]]
## XML Artifacts (detected)

- Views: 1
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title United Arab Emirates - Corporate Tax Report - Models and Relations
class ResCompany
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
