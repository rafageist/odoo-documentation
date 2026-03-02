<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Calendar - SMS

- Scope: Community Addons
- Source: odoo/addons/calendar_sms
- Dependencies: [[docs/Community Addons/calendar/calendar|calendar]], [[docs/Community Addons/sms/sms|sms]]

## Summary

Send text messages as event reminders

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `CalendarAlarm`
- `CalendarEvent`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Calendar - SMS - Models and Relations
class CalendarAlarm
class CalendarEvent
class "sms.template" as sms_template
CalendarAlarm --> sms_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





