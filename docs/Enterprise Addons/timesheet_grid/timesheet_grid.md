<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Timesheets

- Scope: Enterprise Addons
- Source: enterprise/timesheet_grid
- Dependencies: [[docs/Enterprise Addons/project_enterprise/project_enterprise|project_enterprise]], [[docs/Enterprise Addons/web_grid/web_grid|web_grid]], [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]], [[docs/Enterprise Addons/timer/timer|timer]], [[docs/Community Addons/hr_org_chart/hr_org_chart|hr_org_chart]]

## Summary

Track employee time on tasks

## Generated coverage

- Models: 13
- XML files with UI/data artifacts: 10
- Views: 33
- Actions: 26
- Menus: 3
- Rules (ir.rule): 2
- Access CSV entries: 2
- Controller units: 0
- Frontend asset files: 63

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
title Timesheets - Generated Coverage
component "Module Overview" as overview
component "Models\n13" as models
component "Views / XML\n33 views\n10 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n63 files" as frontend
component "Security / Data\n2 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/timesheet_grid/Models|Models]] (13)
- Views and XML: [[docs/Enterprise Addons/timesheet_grid/Views|Views]] (10 files)
- Frontend: [[docs/Enterprise Addons/timesheet_grid/Frontend|Frontend]] (63 files)

## Key models

- `account.analytic.line`
- `hr.employee`
- `hr.employee.public`
- `hr.timesheet.stop.timer.confirmation.wizard`
- `hr_timesheet.merge.wizard`
- `ir.module.module`
- `project.project`
- `project.task`
- `res.company`
- `res.config.settings`
- `res.users`
- `timesheet.grid.mixin`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





