<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# event.registration.answer

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/event_registration_answer.py`
- Python classes: `EventRegistrationAnswer`
- Description: Event Registration Answer

## Field footprint

- Detected fields: 7
- Field types: `Many2one` x 5, `Selection` x 1, `Text` x 1
- Relation fields: 5

## Sample fields

- `event_id`: `Many2one` (comodel `event.event`, related `registration_id.event_id`)
- `partner_id`: `Many2one` (comodel `res.partner`, related `registration_id.partner_id`)
- `question_id`: `Many2one` (comodel `event.question`)
- `question_type`: `Selection` (related `question_id.question_type`)
- `registration_id`: `Many2one` (comodel `event.registration`)
- `value_answer_id`: `Many2one` (comodel `event.question.answer`)
- `value_text_box`: `Text` (comodel `Text answer`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_display_name`
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
title event.registration.answer - Direct Relations
class "event.registration.answer" as event_registration_answer
class "event.event" as event_event
class "event.question" as event_question
class "event.question.answer" as event_question_answer
class "event.registration" as event_registration
class "res.partner" as res_partner
event_registration_answer --> event_question : question_id
event_registration_answer --> event_registration : registration_id
event_registration_answer --> res_partner : partner_id
event_registration_answer --> event_event : event_id
event_registration_answer --> event_question_answer : value_answer_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/event/Models]]

<!-- GENERATED:MODEL -->
