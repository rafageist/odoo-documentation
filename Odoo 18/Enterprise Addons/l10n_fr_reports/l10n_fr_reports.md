<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# France - Accounting Reports

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_fr_reports
- Dependencies: [[Odoo 18/Community Addons/l10n_fr_account/l10n_fr_account|l10n_fr_account]], [[Odoo 18/Enterprise Addons/account_reports/account_reports|account_reports]]
## XML Artifacts (detected)

- Views: 5
- Actions: 3
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `AccountMove`
- `account.report.async.export`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title France - Accounting Reports - Models and Relations
class AccountMove
class "account.report.async.export" as account_report_async_export
class ResCompany
class "account.report" as account_report
account_report_async_export --> account_report : many2one
class "ir.attachment" as ir_attachment
account_report_async_export .. ir_attachment : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
