<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Point of Sale Appointment

- Scope: Enterprise Addons
- Source: enterprise/pos_appointment
- Dependencies: [[docs/Enterprise Addons/appointment/appointment|appointment]], [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



