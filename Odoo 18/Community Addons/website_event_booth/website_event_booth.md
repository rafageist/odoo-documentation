<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Online Event Booths

- Version: v18
- Category: community
- Source: odoo/addons/website_event_booth
- Dependencies: [[Odoo 18/Community Addons/website_event/website_event|website_event]], [[Odoo 18/Community Addons/event_booth/event_booth|event_booth]]

## Summary

Events, display your booths on your website

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `Event`
- `EventType`
- `EventMenu`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Online Event Booths - Models and Relations
class Event
class EventType
class EventMenu
class "website.event.menu" as website_event_menu
Event --|> website_event_menu : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
