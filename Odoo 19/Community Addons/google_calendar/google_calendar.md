<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Google Calendar

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/google_calendar
- Dependencies: [[Odoo 19/Community Addons/google_account/google_account|google_account]], [[Odoo 19/Community Addons/calendar/calendar|calendar]]

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
title Google Calendar - Models and Relations
class "calendar.event" as calendar_event
class CalendarAttendee
class "calendar.recurrence" as calendar_recurrence
class ResUsers
class ResUsersSettings
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


