<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Account Fiscal Report

- Scope: Enterprise Addons
- Source: enterprise/account_fiscal_categories
- Dependencies: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]

## Summary

Account Fiscal Report

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 4
- Views: 6
- Actions: 2
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 4
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
title Account Fiscal Report - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n6 views\n4 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n1 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_fiscal_categories/Models|Models]] (4)
- Views and XML: [[docs/Enterprise Addons/account_fiscal_categories/Views|Views]] (4 files)
- Frontend: [[docs/Enterprise Addons/account_fiscal_categories/Frontend|Frontend]] (1 files)

## Key models

- `account.account`
- `account.account.fiscal.rate`
- `account.fiscal.category`
- `account.fiscal.report.handler`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




