<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Task Logs

- Scope: Community Addons
- Source: odoo/addons/hr_timesheet
- Dependencies: [[docs/Community Addons/hr/hr|hr]], [[docs/Community Addons/hr_hourly_cost/hr_hourly_cost|hr_hourly_cost]], [[docs/Community Addons/analytic/analytic|analytic]], [[docs/Community Addons/project/project|project]], [[docs/Community Addons/uom/uom|uom]]

## Summary

Track employee time on tasks

## Generated coverage

- Models: 17
- XML files with UI/data artifacts: 15
- Views: 54
- Actions: 44
- Menus: 11
- Rules (ir.rule): 9
- Access CSV entries: 7
- Controller units: 1
- Frontend asset files: 18

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
title Task Logs - Generated Coverage
component "Module Overview" as overview
component "Models\n17" as models
component "Views / XML\n54 views\n15 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n18 files" as frontend
component "Security / Data\n9 rules\n7 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/hr_timesheet/Models|Models]] (17)
- Views and XML: [[docs/Community Addons/hr_timesheet/Views|Views]] (15 files)
- Controllers: [[docs/Community Addons/hr_timesheet/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/hr_timesheet/Frontend|Frontend]] (18 files)

## Key models

- `account.analytic.applicability`
- `account.analytic.line`
- `account.analytic.line.calendar.employee`
- `hr.employee`
- `hr.employee.delete.wizard`
- `hr.employee.public`
- `ir.http`
- `ir.ui.menu`
- `project.collaborator`
- `project.project`
- `project.task`
- `project.update`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






