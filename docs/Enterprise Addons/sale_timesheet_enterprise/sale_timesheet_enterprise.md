<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sales Timesheet: Invoicing

- Scope: Enterprise Addons
- Source: enterprise/sale_timesheet_enterprise
- Dependencies: [[docs/Community Addons/sale_timesheet/sale_timesheet|sale_timesheet]], [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]]

## Summary

Configure timesheet invoicing

## Generated coverage

- Models: 13
- XML files with UI/data artifacts: 12
- Views: 20
- Actions: 5
- Menus: 5
- Rules (ir.rule): 2
- Access CSV entries: 3
- Controller units: 0
- Frontend asset files: 19

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
title Sales Timesheet: Invoicing - Generated Coverage
component "Module Overview" as overview
component "Models\n13" as models
component "Views / XML\n20 views\n12 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n19 files" as frontend
component "Security / Data\n2 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/sale_timesheet_enterprise/Models|Models]] (13)
- Views and XML: [[docs/Enterprise Addons/sale_timesheet_enterprise/Views|Views]] (12 files)
- Frontend: [[docs/Enterprise Addons/sale_timesheet_enterprise/Frontend|Frontend]] (19 files)

## Key models

- `account.analytic.line`
- `account.move.line`
- `edit.billable.time.target`
- `hr.employee`
- `hr.employee.public`
- `hr.timesheet.tip`
- `ir.ui.menu`
- `project.project`
- `project.task`
- `res.company`
- `res.config.settings`
- `sale.advance.payment.inv`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





