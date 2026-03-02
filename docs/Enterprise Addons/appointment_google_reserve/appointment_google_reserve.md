
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Appointment Google Reserve

- Scope: Enterprise Addons
- Source: enterprise/appointment_google_reserve
- Dependencies: [[docs/Enterprise Addons/appointment/appointment|appointment]]

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AppointmentResource`
- `AppointmentType`
- `CalendarEvent`
- `google.reserve.merchant`
- `ResourceCalendarLeaves`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Appointment Google Reserve - Models and Relations
class AppointmentResource
class AppointmentType
class CalendarEvent
class "google.reserve.merchant" as google_reserve_merchant
class ResourceCalendarLeaves
AppointmentType --> google_reserve_merchant : many2one
class "appointment.type" as appointment_type
google_reserve_merchant --|> appointment_type : one2many
class "res.partner" as res_partner
google_reserve_merchant --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

