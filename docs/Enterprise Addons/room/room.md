<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Meeting Rooms

- Scope: Enterprise Addons
- Source: enterprise/room
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Enterprise Addons/web_gantt/web_gantt|web_gantt]]

## Summary

Manage Meeting Rooms

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 5
- Views: 11
- Actions: 2
- Menus: 3
- Rules (ir.rule): 2
- Access CSV entries: 5
- Controller units: 1
- Frontend asset files: 8

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
title Meeting Rooms - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n11 views\n5 files" as views
component "Controllers\n6 routes" as controllers
component "Frontend\n8 files" as frontend
component "Security / Data\n2 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/room/Models|Models]] (4)
- Views and XML: [[docs/Enterprise Addons/room/Views|Views]] (5 files)
- Controllers: [[docs/Enterprise Addons/room/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/room/Frontend|Frontend]] (8 files)

## Key models

- `ir.http`
- `room.booking`
- `room.office`
- `room.room`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





