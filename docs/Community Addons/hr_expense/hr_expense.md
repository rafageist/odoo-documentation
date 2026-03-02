<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Expenses

- Scope: Community Addons
- Source: odoo/addons/hr_expense
- Dependencies: [[docs/Community Addons/account/account|account]], [[docs/Community Addons/web_tour/web_tour|web_tour]], [[docs/Community Addons/hr/hr|hr]]

## Summary

Submit, validate and reinvoice employee expenses

## Generated coverage

- Models: 21
- XML files with UI/data artifacts: 14
- Views: 32
- Actions: 21
- Menus: 11
- Rules (ir.rule): 12
- Access CSV entries: 14
- Controller units: 0
- Frontend asset files: 16

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
title Expenses - Generated Coverage
component "Module Overview" as overview
component "Models\n21" as models
component "Views / XML\n32 views\n14 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n16 files" as frontend
component "Security / Data\n12 rules\n14 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/hr_expense/Models|Models]] (21)
- Views and XML: [[docs/Community Addons/hr_expense/Views|Views]] (14 files)
- Frontend: [[docs/Community Addons/hr_expense/Frontend|Frontend]] (16 files)

## Key models

- `account.analytic.account`
- `account.analytic.applicability`
- `account.move`
- `account.move.line`
- `account.payment`
- `account.payment.register`
- `account.tax`
- `hr.department`
- `hr.employee`
- `hr.employee.public`
- `hr.expense`
- `hr.expense.approve.duplicate`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






