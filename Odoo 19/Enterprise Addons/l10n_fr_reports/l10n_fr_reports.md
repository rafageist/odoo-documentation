<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# France - Accounting Reports

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_fr_reports
- Dependencies: [[Odoo 19/Community Addons/l10n_fr_account/l10n_fr_account|l10n_fr_account]], [[Odoo 19/Enterprise Addons/account_reports/account_reports|account_reports]]

## XML Artifacts (detected)

- Views: 5
- Actions: 2
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 6

## Detected Models

- `account.report.async.document`
- `account.report.async.export`
- `AccountReturn`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title France - Accounting Reports - Models and Relations
class "account.report.async.document" as account_report_async_document
class "account.report.async.export" as account_report_async_export
class AccountReturn
class ResCompany
account_report_async_document --> account_report_async_export : many2one
class "account.report" as account_report
account_report_async_export --> account_report : many2one
account_report_async_export --|> account_report_async_document : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

