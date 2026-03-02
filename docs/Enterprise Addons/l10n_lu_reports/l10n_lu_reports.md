<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Luxembourg - Accounting Reports

- Scope: Enterprise Addons
- Source: enterprise/l10n_lu_reports
- Dependencies: [[docs/Community Addons/l10n_lu/l10n_lu|l10n_lu]], [[docs/Enterprise Addons/account_asset/account_asset|account_asset]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]], [[docs/Enterprise Addons/account_saft/account_saft|account_saft]]

## XML Artifacts (detected)

- Views: 8
- Actions: 5
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 9

## Detected Models

- `AccountReport`
- `AccountReturn`
- `account.return.type`
- `l10n_lu.stored.intra.report`
- `IrAttachment`
- `l10n_lu_reports.report.appendix.expenditures`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Luxembourg - Accounting Reports - Models and Relations
class AccountReport
class AccountReturn
class "account.return.type" as account_return_type
class "l10n_lu.stored.intra.report" as l10n_lu_stored_intra_report
class IrAttachment
class "l10n_lu_reports.report.appendix.expenditures" as l10n_lu_reports_report_appendix_expenditures
class ResCompany
class ResPartner
class "res.company" as res_company
l10n_lu_stored_intra_report --> res_company : many2one
l10n_lu_reports_report_appendix_expenditures --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



