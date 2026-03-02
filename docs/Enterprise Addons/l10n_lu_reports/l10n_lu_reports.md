<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Luxembourg - Accounting Reports

- Scope: Enterprise Addons
- Source: enterprise/l10n_lu_reports
- Dependencies: [[docs/Community Addons/l10n_lu/l10n_lu|l10n_lu]], [[docs/Enterprise Addons/account_asset/account_asset|account_asset]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]], [[docs/Enterprise Addons/account_saft/account_saft|account_saft]]

## Generated coverage

- Models: 23
- XML files with UI/data artifacts: 12
- Views: 8
- Actions: 5
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 9
- Controller units: 0
- Frontend asset files: 3

## Module map

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title Luxembourg - Accounting Reports - Generated Coverage
component "Module Overview" as overview
component "Models\n23" as models
component "Views / XML\n8 views\n12 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n1 rules\n9 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_lu_reports/Models|Models]] (23)
- Views and XML: [[docs/Enterprise Addons/l10n_lu_reports/Views|Views]] (12 files)
- Frontend: [[docs/Enterprise Addons/l10n_lu_reports/Frontend|Frontend]] (3 files)

## Key models

- `account.chart.template`
- `account.general.ledger.report.handler`
- `account.report`
- `account.return`
- `account.return.type`
- `ir.attachment`
- `l10n_lu.annual.tax.report.handler`
- `l10n_lu.appendix.a.tax.report.handler`
- `l10n_lu.appendix.opex.tax.report.handler`
- `l10n_lu.ec.sales.report.handler`
- `l10n_lu.generate.accounts.report`
- `l10n_lu.generate.asset.report`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




