<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# IM Bus

- Scope: Community Addons
- Source: odoo/addons/bus
- Dependencies: base (not documented), [[docs/Community Addons/web/web|web]]

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 0
- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 2
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
title IM Bus - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n0 views\n0 files" as views
component "Controllers\n7 routes" as controllers
component "Frontend\n22 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/bus/Models|Models]] (10)
- Controllers: [[docs/Community Addons/bus/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/bus/Frontend|Frontend]] (22 files)

## Key models

- `bus.bus`
- `bus.listener.mixin`
- `ir.attachment`
- `ir.http`
- `ir.model`
- `ir.websocket`
- `res.groups`
- `res.partner`
- `res.users`
- `res.users.settings`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






