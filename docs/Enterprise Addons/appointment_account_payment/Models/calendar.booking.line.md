<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# calendar.booking.line

- Module: [[docs/Enterprise Addons/appointment_account_payment/appointment_account_payment|appointment_account_payment]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/calendar_booking_line.py`
- Python classes: `CalendarBookingLine`
- Description: Meeting User/Resource Booking

## Field footprint

- Detected fields: 5
- Field types: `Integer` x 2, `Many2one` x 3
- Relation fields: 3

## Sample fields

- `appointment_resource_id`: `Many2one` (comodel `appointment.resource`)
- `appointment_user_id`: `Many2one` (comodel `res.users`, related `calendar_booking_id.staff_user_id`)
- `calendar_booking_id`: `Many2one` (comodel `calendar.booking`)
- `capacity_reserved`: `Integer` (comodel `Capacity Reserved`)
- `capacity_used`: `Integer` (comodel `Capacity Used`)

## Method hints

- Detected methods: 0
- Action methods: none
- Compute methods: none
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
title calendar.booking.line - Direct Relations
class "calendar.booking.line" as calendar_booking_line
class "appointment.resource" as appointment_resource
class "calendar.booking" as calendar_booking
class "res.users" as res_users
calendar_booking_line --> appointment_resource : appointment_resource_id
calendar_booking_line --> res_users : appointment_user_id
calendar_booking_line --> calendar_booking : calendar_booking_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment_account_payment/Models]]

<!-- GENERATED:MODEL -->
