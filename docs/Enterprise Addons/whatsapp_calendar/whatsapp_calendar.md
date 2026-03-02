<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# WhatsApp-Calendar

- Scope: Enterprise Addons
- Source: enterprise/whatsapp_calendar
- Dependencies: [[docs/Community Addons/calendar/calendar|calendar]], [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

## Summary

Send whatsapp messages as event reminders

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `CalendarAlarm`
- `CalendarAttendee`
- `CalendarEvent`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title WhatsApp-Calendar - Models and Relations
class CalendarAlarm
class CalendarAttendee
class CalendarEvent
class "whatsapp.template" as whatsapp_template
CalendarAlarm --> whatsapp_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



