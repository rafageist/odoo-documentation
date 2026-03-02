<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Estonia - Accounting Reports

- Scope: Enterprise Addons
- Source: enterprise/l10n_ee_reports
- Dependencies: [[docs/Community Addons/l10n_ee/l10n_ee|l10n_ee]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 6
- Views: 5
- Actions: 0
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 3
- Controller units: 0
- Frontend asset files: 1

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
title Estonia - Accounting Reports - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n5 views\n6 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_ee_reports/Models|Models]] (8)
- Views and XML: [[docs/Enterprise Addons/l10n_ee_reports/Views|Views]] (6 files)
- Frontend: [[docs/Enterprise Addons/l10n_ee_reports/Frontend|Frontend]] (1 files)

## Key models

- `account.return`
- `l10n_ee.ec.sales.report.handler`
- `l10n_ee.kmd.inf.report.handler`
- `l10n_ee.tax.report.handler`
- `l10n_ee_reports.ec.sales.list.submission.wizard`
- `l10n_ee_reports.kmd.inf.return.submission.wizard`
- `l10n_ee_reports.tax.return.submission.wizard`
- `res.config.settings`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




