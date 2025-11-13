<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Schedule push notifications on attendees

- Version: v18
- Category: enterprise
- Source: enterprise18/website_event_social
- Dependencies: [[Odoo 18/Community Addons/website_event/website_event|website_event]], [[Odoo 18/Enterprise Addons/social_push_notifications/social_push_notifications|social_push_notifications]]

## Summary

Bridge module to push notifications to event attendees

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `EventSocial`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Schedule push notifications on attendees - Models and Relations
class EventSocial
class ResPartner
class "event.registration" as event_registration
ResPartner --|> event_registration : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
