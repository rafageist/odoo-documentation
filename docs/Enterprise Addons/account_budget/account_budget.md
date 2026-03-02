<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Budget Management

- Scope: Enterprise Addons
- Source: enterprise/account_budget
- Dependencies: [[docs/Enterprise Addons/accountant/accountant|accountant]]

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 6
- Views: 15
- Actions: 4
- Menus: 2
- Rules (ir.rule): 3
- Access CSV entries: 7
- Controller units: 0
- Frontend asset files: 0

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
title Budget Management - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n15 views\n6 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n3 rules\n7 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_budget/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/account_budget/Views|Views]] (6 files)

## Key models

- `account.analytic.account`
- `budget.analytic`
- `budget.line`
- `budget.report`
- `budget.split.wizard`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




