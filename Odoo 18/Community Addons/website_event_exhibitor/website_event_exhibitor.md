<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Event Exhibitors

- Version: v18
- Category: community
- Source: odoo/addons/website_event_exhibitor
- Dependencies: [[Odoo 18/Community Addons/website_event_jitsi/website_event_jitsi|website_event_jitsi]]

## Summary

Event: manage sponsors and exhibitors

## XML Artifacts (detected)

- Views: 9
- Actions: 3
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 6

## Detected Models

- `EventEvent`
- `event.sponsor`
- `event.sponsor.type`
- `EventType`
- `EventMenu`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Event Exhibitors - Models and Relations
class EventEvent
class "event.sponsor" as event_sponsor
class "event.sponsor.type" as event_sponsor_type
class EventType
class EventMenu
EventEvent --|> event_sponsor : one2many
class "website.event.menu" as website_event_menu
EventEvent --|> website_event_menu : one2many
class "event.event" as event_event
event_sponsor --> event_event : many2one
event_sponsor --> event_sponsor_type : many2one
class "res.partner" as res_partner
event_sponsor --> res_partner : many2one
class "res.country" as res_country
event_sponsor --> res_country : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
