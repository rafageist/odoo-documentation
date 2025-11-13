<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Events Booths

- Version: v18
- Category: community
- Source: odoo/addons/event_booth
- Dependencies: [[Odoo 18/Community Addons/event/event|event]]

## Summary

Manage event booths

## XML Artifacts (detected)

- Views: 21
- Actions: 7
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 8

## Detected Models

- `event.booth`
- `event.booth.category`
- `Event`
- `EventType`
- `event.type.booth`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Events Booths - Models and Relations
class "event.booth" as event_booth
class "event.booth.category" as event_booth_category
class Event
class EventType
class "event.type.booth" as event_type_booth
class "event.event" as event_event
event_booth --> event_event : many2one
class "res.partner" as res_partner
event_booth --> res_partner : many2one
event_booth_category --|> event_booth : one2many
Event --|> event_booth : one2many
Event .. event_booth_category : many2many
Event .. event_booth_category : many2many
EventType --|> event_type_booth : one2many
class "event.type" as event_type
event_type_booth --> event_type : many2one
event_type_booth --> event_booth_category : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
