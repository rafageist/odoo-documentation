<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Planning and Attendances

- Scope: Enterprise Addons
- Source: enterprise/planning_attendance
- Dependencies: [[docs/Enterprise Addons/planning/planning|planning]], [[docs/Community Addons/hr_attendance/hr_attendance|hr_attendance]]

## Summary

Compare plannings and attendances

## Generated coverage

- Models: 1
- XML files with UI/data artifacts: 3
- Views: 3
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
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
title Planning and Attendances - Generated Coverage
component "Module Overview" as overview
component "Models\n1" as models
component "Views / XML\n3 views\n3 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n1 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/planning_attendance/Models|Models]] (1)
- Views and XML: [[docs/Enterprise Addons/planning_attendance/Views|Views]] (3 files)

## Key models

- `planning.attendance.analysis.report`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




