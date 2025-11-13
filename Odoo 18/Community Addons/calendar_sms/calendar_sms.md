<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Calendar - SMS

- Version: v18
- Category: community
- Source: odoo/addons/calendar_sms
- Dependencies: [[Odoo 18/Community Addons/calendar/calendar|calendar]], [[Odoo 18/Community Addons/sms/sms|sms]]

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
!include ../../../Templates/DiagramStyles.puml
title Calendar - SMS - Models and Relations
class CalendarAlarm
class CalendarEvent
class "sms.template" as sms_template
CalendarAlarm --> sms_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
