<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Point of Sale Restaurant Appointment

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_restaurant_appointment
- Dependencies: [[Odoo 18/Enterprise Addons/appointment/appointment|appointment]], [[Odoo 18/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]]

## Summary

This module lets you manage online reservations for restaurant tables

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `appointment.resource`
- `calendar.event`
- `PosConfig`
- `RestaurantTable`
- `PosSession`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Point of Sale Restaurant Appointment - Models and Relations
class "appointment.resource" as appointment_resource
class "calendar.event" as calendar_event
class PosConfig
class RestaurantTable
class PosSession
class "restaurant.table" as restaurant_table
appointment_resource --|> restaurant_table : one2many
class "appointment.type" as appointment_type
PosConfig --> appointment_type : many2one
RestaurantTable --> appointment_resource : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
