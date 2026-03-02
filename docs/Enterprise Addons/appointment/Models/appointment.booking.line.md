<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# appointment.booking.line

- Module: [[docs/Enterprise Addons/appointment/appointment|appointment]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/appointment_booking_line.py`
- Python classes: `AppointmentBookingLine`
- Description: Appointment Booking Line

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 1, `Datetime` x 2, `Integer` x 2, `Many2one` x 4
- Relation fields: 4

## Sample fields

- `active`: `Boolean` (related `calendar_event_id.active`)
- `appointment_resource_id`: `Many2one` (comodel `appointment.resource`)
- `appointment_type_id`: `Many2one` (comodel `appointment.type`, related `calendar_event_id.appointment_type_id`, store `True`)
- `appointment_user_id`: `Many2one` (comodel `res.users`, related `calendar_event_id.user_id`)
- `calendar_event_id`: `Many2one` (comodel `calendar.event`)
- `capacity_reserved`: `Integer` (comodel `Capacity Reserved`)
- `capacity_used`: `Integer` (comodel `Capacity Used`, compute `_compute_capacity_used`, store `True`)
- `event_start`: `Datetime` (comodel `Booking Start`, related `calendar_event_id.start`, store `True`)
- `event_stop`: `Datetime` (comodel `Booking End`, related `calendar_event_id.stop`, store `True`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_capacity_used`
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title appointment.booking.line - Direct Relations
class "appointment.booking.line" as appointment_booking_line
class "appointment.resource" as appointment_resource
class "appointment.type" as appointment_type
class "calendar.event" as calendar_event
class "res.users" as res_users
appointment_booking_line --> appointment_resource : appointment_resource_id
appointment_booking_line --> res_users : appointment_user_id
appointment_booking_line --> appointment_type : appointment_type_id
appointment_booking_line --> calendar_event : calendar_event_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment/Models]]

<!-- GENERATED:MODEL -->
