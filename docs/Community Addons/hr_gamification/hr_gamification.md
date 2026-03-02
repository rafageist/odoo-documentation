<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# HR Gamification

- Scope: Community Addons
- Source: odoo/addons/hr_gamification
- Dependencies: [[docs/Community Addons/gamification/gamification|gamification]], [[docs/Community Addons/hr/hr|hr]]

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 4
- Views: 6
- Actions: 5
- Menus: 4
- Rules (ir.rule): 4
- Access CSV entries: 5
- Controller units: 0
- Frontend asset files: 2

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
title HR Gamification - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n6 views\n4 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n4 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/hr_gamification/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/hr_gamification/Views|Views]] (4 files)
- Frontend: [[docs/Community Addons/hr_gamification/Frontend|Frontend]] (2 files)

## Key models

- `gamification.badge`
- `gamification.badge.user`
- `gamification.badge.user.wizard`
- `hr.employee`
- `hr.employee.public`
- `res.users`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






