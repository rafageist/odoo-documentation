<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk Timesheet

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_timesheet
- Dependencies: [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]], [[docs/Enterprise Addons/project_helpdesk/project_helpdesk|project_helpdesk]]

## Summary

Project, Tasks, Timesheet

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 9
- Views: 25
- Actions: 11
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 5
- Controller units: 0
- Frontend asset files: 6

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
title Helpdesk Timesheet - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n25 views\n9 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n6 files" as frontend
component "Security / Data\n2 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/helpdesk_timesheet/Models|Models]] (10)
- Views and XML: [[docs/Enterprise Addons/helpdesk_timesheet/Views|Views]] (9 files)
- Frontend: [[docs/Enterprise Addons/helpdesk_timesheet/Frontend|Frontend]] (6 files)

## Key models

- `account.analytic.line`
- `helpdesk.sla.report.analysis`
- `helpdesk.team`
- `helpdesk.ticket`
- `helpdesk.ticket.convert.wizard`
- `helpdesk.ticket.report.analysis`
- `hr_timesheet.merge.wizard`
- `project.project`
- `project.task.convert.wizard`
- `timesheets.analysis.report`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





