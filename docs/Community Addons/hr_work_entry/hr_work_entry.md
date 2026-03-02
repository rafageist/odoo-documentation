<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Work Entries

- Scope: Community Addons
- Source: odoo/addons/hr_work_entry
- Dependencies: [[docs/Community Addons/hr/hr|hr]]

## Summary

Manage work entries

## Generated coverage

- Models: 9
- XML files with UI/data artifacts: 6
- Views: 19
- Actions: 4
- Menus: 0
- Rules (ir.rule): 3
- Access CSV entries: 6
- Controller units: 0
- Frontend asset files: 22

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
title Work Entries - Generated Coverage
component "Module Overview" as overview
component "Models\n9" as models
component "Views / XML\n19 views\n6 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n22 files" as frontend
component "Security / Data\n3 rules\n6 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/hr_work_entry/Models|Models]] (9)
- Views and XML: [[docs/Community Addons/hr_work_entry/Views|Views]] (6 files)
- Frontend: [[docs/Community Addons/hr_work_entry/Frontend|Frontend]] (22 files)

## Key models

- `hr.employee`
- `hr.user.work.entry.employee`
- `hr.version`
- `hr.work.entry`
- `hr.work.entry.regeneration.wizard`
- `hr.work.entry.type`
- `resource.calendar`
- `resource.calendar.attendance`
- `resource.calendar.leaves`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






