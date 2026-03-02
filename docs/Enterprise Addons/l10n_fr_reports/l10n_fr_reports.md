<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# France - Accounting Reports

- Scope: Enterprise Addons
- Source: enterprise/l10n_fr_reports
- Dependencies: [[docs/Community Addons/l10n_fr_account/l10n_fr_account|l10n_fr_account]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



