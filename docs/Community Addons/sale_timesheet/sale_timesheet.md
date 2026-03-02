<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sales Timesheet

- Scope: Community Addons
- Source: odoo/addons/sale_timesheet
- Dependencies: [[docs/Community Addons/sale_project/sale_project|sale_project]], [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]

## Summary

Sell based on timesheets

## Generated coverage

- Models: 15
- XML files with UI/data artifacts: 12
- Views: 37
- Actions: 24
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 2
- Controller units: 2
- Frontend asset files: 2

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
title Sales Timesheet - Generated Coverage
component "Module Overview" as overview
component "Models\n15" as models
component "Views / XML\n37 views\n12 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n2 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/sale_timesheet/Models|Models]] (15)
- Views and XML: [[docs/Community Addons/sale_timesheet/Views|Views]] (12 files)
- Controllers: [[docs/Community Addons/sale_timesheet/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/sale_timesheet/Frontend|Frontend]] (2 files)

## Key models

- `account.analytic.line`
- `account.move`
- `account.move.line`
- `hr.employee`
- `product.product`
- `product.template`
- `project.project`
- `project.sale.line.employee.map`
- `project.task`
- `report.project.task.user`
- `res.config.settings`
- `sale.advance.payment.inv`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





