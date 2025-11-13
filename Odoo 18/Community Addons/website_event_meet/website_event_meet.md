<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Event Meeting / Rooms

- Version: v18
- Category: community
- Source: odoo/addons/website_event_meet
- Dependencies: [[Odoo 18/Community Addons/website_event_jitsi/website_event_jitsi|website_event_jitsi]]

## Summary

Event: meeting and chat rooms

## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 6

## Detected Models

- `Event`
- `event.meeting.room`
- `EventType`
- `EventMenu`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Event Meeting / Rooms - Models and Relations
class Event
class "event.meeting.room" as event_meeting_room
class EventType
class EventMenu
Event --|> event_meeting_room : one2many
class "event.event" as event_event
event_meeting_room --> event_event : many2one
class "chat.room" as chat_room
event_meeting_room --> chat_room : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
