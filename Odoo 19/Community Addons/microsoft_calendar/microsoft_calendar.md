<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Outlook Calendar

- Version: v19
- Category: community
- Source: odoo19/addons/microsoft_calendar
- Dependencies: [[Odoo 19/Community Addons/microsoft_account/microsoft_account|microsoft_account]], [[Odoo 19/Community Addons/calendar/calendar|calendar]]
## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `calendar.event`
- `CalendarAttendee`
- `calendar.recurrence`
- `ResUsers`
- `ResUsersSettings`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Outlook Calendar - Models and Relations
class "calendar.event" as calendar_event
class CalendarAttendee
class "calendar.recurrence" as calendar_recurrence
class ResUsers
class ResUsersSettings
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
