<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Employee Presence Control

- Scope: Community Addons
- Source: odoo/addons/hr_presence
- Dependencies: [[docs/Community Addons/hr/hr|hr]], [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]], [[docs/Community Addons/sms/sms|sms]]

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 2
- Views: 1
- Actions: 5
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1
- Controller units: 0
- Frontend asset files: 7

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
title Employee Presence Control - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n1 views\n2 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n7 files" as frontend
component "Security / Data\n1 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/hr_presence/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/hr_presence/Views|Views]] (2 files)
- Frontend: [[docs/Community Addons/hr_presence/Frontend|Frontend]] (7 files)

## Key models

- `hr.employee`
- `hr.employee.public`
- `ir.websocket`
- `res.company`
- `res.config.settings`
- `res.users.log`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






