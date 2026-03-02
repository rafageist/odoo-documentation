<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Timesheet and Planning

- Scope: Enterprise Addons
- Source: enterprise/project_timesheet_forecast
- Dependencies: [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]], [[docs/Enterprise Addons/project_forecast/project_forecast|project_forecast]]

## Summary

Compare timesheets and plannings

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 4
- Views: 12
- Actions: 8
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 2
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
title Timesheet and Planning - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n12 views\n4 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n1 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/project_timesheet_forecast/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/project_timesheet_forecast/Views|Views]] (4 files)
- Frontend: [[docs/Enterprise Addons/project_timesheet_forecast/Frontend|Frontend]] (1 files)

## Key models

- `ir.ui.menu`
- `planning.analysis.report`
- `planning.slot`
- `project.project`
- `project.timesheet.forecast.report.analysis`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




