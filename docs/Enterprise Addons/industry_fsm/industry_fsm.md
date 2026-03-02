<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Field Service

- Scope: Enterprise Addons
- Source: enterprise/industry_fsm
- Dependencies: [[docs/Enterprise Addons/project_enterprise/project_enterprise|project_enterprise]], [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]], [[docs/Community Addons/base_geolocalize/base_geolocalize|base_geolocalize]]

## Summary

Schedule and track onsite operations, time and material

## Generated coverage

- Models: 17
- XML files with UI/data artifacts: 12
- Views: 55
- Actions: 150
- Menus: 21
- Rules (ir.rule): 2
- Access CSV entries: 4
- Controller units: 1
- Frontend asset files: 31

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
title Field Service - Generated Coverage
component "Module Overview" as overview
component "Models\n17" as models
component "Views / XML\n55 views\n12 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n31 files" as frontend
component "Security / Data\n2 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/industry_fsm/Models|Models]] (17)
- Views and XML: [[docs/Enterprise Addons/industry_fsm/Views|Views]] (12 files)
- Controllers: [[docs/Enterprise Addons/industry_fsm/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/industry_fsm/Frontend|Frontend]] (31 files)

## Key models

- `account.analytic.line`
- `base.document.layout`
- `hr.timesheet.stop.timer.confirmation.wizard`
- `ir.actions.report`
- `ir.ui.menu`
- `project.project`
- `project.task`
- `project.task.recurrence`
- `project.task.stop.timers.wizard`
- `project.task.stop.timers.wizard.line`
- `project.task.type`
- `rating.rating`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




