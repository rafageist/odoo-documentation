<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Display Working Hours in Calendar

- Version: v18
- Category: community
- Source: odoo/addons/hr_calendar
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]], [[Odoo 18/Community Addons/calendar/calendar|calendar]]
## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `CalendarEvent`
- `Partner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Display Working Hours in Calendar - Models and Relations
class CalendarEvent
class Partner
class "res.partner" as res_partner
CalendarEvent .. res_partner : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
