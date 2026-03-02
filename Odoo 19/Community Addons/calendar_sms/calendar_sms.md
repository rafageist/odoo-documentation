<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Calendar - SMS

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/calendar_sms
- Dependencies: [[Odoo 19/Community Addons/calendar/calendar|calendar]], [[Odoo 19/Community Addons/sms/sms|sms]]

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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


