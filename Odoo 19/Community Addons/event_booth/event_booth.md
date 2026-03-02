<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Events Booths

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/event_booth
- Dependencies: [[Odoo 19/Community Addons/event/event|event]]

## Summary

Manage event booths

## XML Artifacts (detected)

- Views: 21
- Actions: 7
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 9

## Detected Models

- `event.booth`
- `event.booth.category`
- `EventEvent`
- `EventType`
- `event.type.booth`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Events Booths - Models and Relations
class "event.booth" as event_booth
class "event.booth.category" as event_booth_category
class EventEvent
class EventType
class "event.type.booth" as event_type_booth
class "event.event" as event_event
event_booth --> event_event : many2one
class "res.partner" as res_partner
event_booth --> res_partner : many2one
event_booth_category --|> event_booth : one2many
EventEvent --|> event_booth : one2many
EventEvent .. event_booth_category : many2many
EventEvent .. event_booth_category : many2many
EventType --|> event_type_booth : one2many
class "event.type" as event_type
event_type_booth --> event_type : many2one
event_type_booth --> event_booth_category : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


