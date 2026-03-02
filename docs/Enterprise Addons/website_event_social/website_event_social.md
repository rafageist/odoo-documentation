<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Schedule push notifications on attendees

- Scope: Enterprise Addons
- Source: enterprise/website_event_social
- Dependencies: [[docs/Community Addons/website_event/website_event|website_event]], [[docs/Enterprise Addons/social_push_notifications/social_push_notifications|social_push_notifications]]

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
!include ../../../templates/DiagramStyles.puml
title Schedule push notifications on attendees - Models and Relations
class EventEvent
class ResPartner
class "event.registration" as event_registration
ResPartner --|> event_registration : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



