<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Online Event Booths

- Version: v19
- Category: community
- Source: odoo19/addons/website_event_booth
- Dependencies: [[Odoo 19/Community Addons/website_event/website_event|website_event]], [[Odoo 19/Community Addons/event_booth/event_booth|event_booth]]

## Summary

Events, display your booths on your website

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `EventEvent`
- `EventType`
- `WebsiteEventMenu`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Online Event Booths - Models and Relations
class EventEvent
class EventType
class WebsiteEventMenu
class "website.event.menu" as website_event_menu
EventEvent --|> website_event_menu : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
