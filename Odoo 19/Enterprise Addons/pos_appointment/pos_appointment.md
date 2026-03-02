<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Point of Sale Appointment

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/pos_appointment
- Dependencies: [[Odoo 19/Enterprise Addons/appointment/appointment|appointment]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

This module lets you manage online reservations for PoS

## XML Artifacts (detected)

- Views: 7
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AppointmentType`
- `calendar.event`
- `PosConfig`
- `PosSession`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Point of Sale Appointment - Models and Relations
class AppointmentType
class "calendar.event" as calendar_event
class PosConfig
class PosSession
class "appointment.type" as appointment_type
PosConfig --> appointment_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

