<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Planning Time Off

- Scope: Enterprise Addons
- Source: enterprise/planning_holidays
- Dependencies: [[docs/Enterprise Addons/planning/planning|planning]], [[docs/Enterprise Addons/hr_holidays_gantt/hr_holidays_gantt|hr_holidays_gantt]]

## Summary

Planning integration with holidays

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 2
- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
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
title Planning Time Off - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n5 views\n2 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/planning_holidays/Models|Models]] (3)
- Views and XML: [[docs/Enterprise Addons/planning_holidays/Views|Views]] (2 files)

## Key models

- `planning.slot`
- `resource.calendar`
- `resource.calendar.leaves`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





