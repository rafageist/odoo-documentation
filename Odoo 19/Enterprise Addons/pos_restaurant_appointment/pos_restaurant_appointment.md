<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Point of Sale Restaurant Appointment

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/pos_restaurant_appointment
- Dependencies: [[Odoo 19/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[Odoo 19/Enterprise Addons/pos_appointment/pos_appointment|pos_appointment]]

## Summary

This module lets you manage online reservations for restaurant tables

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `appointment.resource`
- `calendar.event`
- `RestaurantTable`
- `PosSession`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Point of Sale Restaurant Appointment - Models and Relations
class "appointment.resource" as appointment_resource
class "calendar.event" as calendar_event
class RestaurantTable
class PosSession
class "restaurant.table" as restaurant_table
appointment_resource --|> restaurant_table : one2many
RestaurantTable --> appointment_resource : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

