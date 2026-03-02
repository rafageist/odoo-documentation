<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Point of Sale Restaurant Appointment

- Scope: Enterprise Addons
- Source: enterprise/pos_restaurant_appointment
- Dependencies: [[docs/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[docs/Enterprise Addons/pos_appointment/pos_appointment|pos_appointment]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



