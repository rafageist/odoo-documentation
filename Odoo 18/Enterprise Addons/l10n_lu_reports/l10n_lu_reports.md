<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Luxembourg - Accounting Reports

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_lu_reports
- Dependencies: [[Odoo 18/Community Addons/l10n_lu/l10n_lu|l10n_lu]], [[Odoo 18/Enterprise Addons/account_asset/account_asset|account_asset]], [[Odoo 18/Enterprise Addons/account_reports/account_reports|account_reports]], [[Odoo 18/Enterprise Addons/account_saft/account_saft|account_saft]]
## XML Artifacts (detected)

- Views: 6
- Actions: 5
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 7

## Detected Models

- `AssetsReport`
- `l10n_lu.stored.intra.report`
- `IrAttachment`
- `l10n_lu_reports.report.appendix.expenditures`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Luxembourg - Accounting Reports - Models and Relations
class AssetsReport
class "l10n_lu.stored.intra.report" as l10n_lu_stored_intra_report
class IrAttachment
class "l10n_lu_reports.report.appendix.expenditures" as l10n_lu_reports_report_appendix_expenditures
class ResCompany
class ResPartner
class "ir.attachment" as ir_attachment
l10n_lu_stored_intra_report --> ir_attachment : many2one
class "res.company" as res_company
l10n_lu_stored_intra_report --> res_company : many2one
l10n_lu_reports_report_appendix_expenditures --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
