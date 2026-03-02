<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# WhatsApp-Calendar

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/whatsapp_calendar
- Dependencies: [[Odoo 19/Community Addons/calendar/calendar|calendar]], [[Odoo 19/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

