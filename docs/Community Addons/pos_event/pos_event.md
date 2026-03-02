<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# POS - Event

- Scope: Community Addons
- Source: odoo/addons/pos_event
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Community Addons/event_product/event_product|event_product]]

## Summary

Link module between Point of Sale and Event

## Generated coverage

- Models: 11
- XML files with UI/data artifacts: 3
- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3
- Controller units: 0
- Frontend asset files: 17

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
title POS - Event - Generated Coverage
component "Module Overview" as overview
component "Models\n11" as models
component "Views / XML\n3 views\n3 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n17 files" as frontend
component "Security / Data\n0 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/pos_event/Models|Models]] (11)
- Views and XML: [[docs/Community Addons/pos_event/Views|Views]] (3 files)
- Frontend: [[docs/Community Addons/pos_event/Frontend|Frontend]] (17 files)

## Key models

- `event.event`
- `event.event.ticket`
- `event.question`
- `event.question.answer`
- `event.registration`
- `event.registration.answer`
- `event.slot`
- `pos.config`
- `pos.order`
- `pos.order.line`
- `pos.session`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






