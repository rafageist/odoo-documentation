<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Timesheet when on Time Off

- Scope: Community Addons
- Source: odoo/addons/project_timesheet_holidays
- Dependencies: [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]], [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

## Summary

Schedule timesheet when on time off

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 2
- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1
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
title Timesheet when on Time Off - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n2 views\n2 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/project_timesheet_holidays/Models|Models]] (7)
- Views and XML: [[docs/Community Addons/project_timesheet_holidays/Views|Views]] (2 files)

## Key models

- `account.analytic.line`
- `hr.employee`
- `hr.leave`
- `project.task`
- `res.company`
- `res.config.settings`
- `resource.calendar.leaves`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






