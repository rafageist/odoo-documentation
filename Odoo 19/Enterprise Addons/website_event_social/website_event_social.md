<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Schedule push notifications on attendees

- Version: v19
- Category: enterprise
- Source: enterprise19/website_event_social
- Dependencies: [[Odoo 19/Community Addons/website_event/website_event|website_event]], [[Odoo 19/Enterprise Addons/social_push_notifications/social_push_notifications|social_push_notifications]]

## Summary

Bridge module to push notifications to event attendees

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `EventEvent`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Schedule push notifications on attendees - Models and Relations
class EventEvent
class ResPartner
class "event.registration" as event_registration
ResPartner --|> event_registration : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
