<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# appointment.answer.input

- Module: [[docs/Enterprise Addons/appointment/appointment|appointment]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/appointment_answer.py`
- Python classes: `AppointmentAnswerInput`
- Description: Appointment Answer Inputs

## Field footprint

- Detected fields: 7
- Field types: `Many2one` x 5, `Selection` x 1, `Text` x 1
- Relation fields: 5

## Sample fields

- `appointment_type_id`: `Many2one` (comodel `appointment.type`)
- `calendar_event_id`: `Many2one` (comodel `calendar.event`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `question_id`: `Many2one` (comodel `appointment.question`)
- `question_type`: `Selection` (related `question_id.question_type`)
- `value_answer_id`: `Many2one` (comodel `appointment.answer`)
- `value_text_box`: `Text` (comodel `Text Answer`)

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
title appointment.answer.input - Direct Relations
class "appointment.answer.input" as appointment_answer_input
class "appointment.answer" as appointment_answer
class "appointment.question" as appointment_question
class "appointment.type" as appointment_type
class "calendar.event" as calendar_event
class "res.partner" as res_partner
appointment_answer_input --> appointment_question : question_id
appointment_answer_input --> appointment_answer : value_answer_id
appointment_answer_input --> appointment_type : appointment_type_id
appointment_answer_input --> calendar_event : calendar_event_id
appointment_answer_input --> res_partner : partner_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment/Models]]

<!-- GENERATED:MODEL -->
