<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Google Calendar

- Scope: Community Addons
- Source: odoo/addons/google_calendar
- Dependencies: [[docs/Community Addons/google_account/google_account|google_account]], [[docs/Community Addons/calendar/calendar|calendar]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





