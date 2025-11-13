<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Meeting Rooms

- Version: v18
- Category: enterprise
- Source: enterprise18/room
- Dependencies: [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Enterprise Addons/web_gantt/web_gantt|web_gantt]]

## Summary

Manage Meeting Rooms

## XML Artifacts (detected)

- Views: 11
- Actions: 2
- Menus: 3
- Rules (ir.rule): 2
- Access CSV entries: 5

## Detected Models

- `room.booking`
- `room.office`
- `room.room`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Meeting Rooms - Models and Relations
class "room.booking" as room_booking
class "room.office" as room_office
class "room.room" as room_room
room_booking --> room_room : many2one
class "res.users" as res_users
room_booking --> res_users : many2one
class "res.company" as res_company
room_office --> res_company : many2one
room_room --> room_office : many2one
room_room --|> room_booking : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
