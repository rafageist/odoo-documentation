<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Google Calendar

- Version: v18
- Category: community
- Source: odoo/addons/google_calendar
- Dependencies: [[Odoo 18/Community Addons/google_account/google_account|google_account]], [[Odoo 18/Community Addons/calendar/calendar|calendar]]
## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `calendar.event`
- `calendar.attendee`
- `calendar.recurrence`
- `User`
- `ResUsersSettings`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Google Calendar - Models and Relations
class "calendar.event" as calendar_event
class "calendar.attendee" as calendar_attendee
class "calendar.recurrence" as calendar_recurrence
class User
class ResUsersSettings
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
