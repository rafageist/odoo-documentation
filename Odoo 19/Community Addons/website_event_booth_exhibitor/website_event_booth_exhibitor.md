<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Booths/Exhibitors Bridge

- Version: v19
- Category: community
- Source: odoo19/addons/website_event_booth_exhibitor
- Dependencies: [[Odoo 19/Community Addons/website_event_exhibitor/website_event_exhibitor|website_event_exhibitor]], [[Odoo 19/Community Addons/website_event_booth/website_event_booth|website_event_booth]]

## Summary

Event Booths, automatically create a sponsor.

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `EventBooth`
- `EventBoothCategory`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Booths/Exhibitors Bridge - Models and Relations
class EventBooth
class EventBoothCategory
class "event.sponsor" as event_sponsor
EventBooth --> event_sponsor : many2one
class "event.sponsor.type" as event_sponsor_type
EventBoothCategory --> event_sponsor_type : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
