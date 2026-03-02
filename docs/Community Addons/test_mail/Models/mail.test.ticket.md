<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mail.test.ticket

- Module: [[docs/Community Addons/test_mail/test_mail|test_mail]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mail_test_ticket.py`
- Python classes: `MailTestTicket`
- Description: Ticket-like model
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 9
- Field types: `Char` x 3, `Datetime` x 1, `Integer` x 1, `Many2one` x 4
- Relation fields: 4

## Sample fields

- `container_id`: `Many2one` (comodel `mail.test.container`)
- `count`: `Integer`
- `customer_id`: `Many2one` (comodel `res.partner`)
- `datetime`: `Datetime`
- `email_from`: `Char`
- `mail_template`: `Many2one` (comodel `mail.template`)
- `name`: `Char`
- `phone_number`: `Char`
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 7
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
title mail.test.ticket - Direct Relations
class "mail.test.ticket" as mail_test_ticket
class "mail.template" as mail_template
class "mail.test.container" as mail_test_container
class "res.partner" as res_partner
class "res.users" as res_users
mail_test_ticket --> mail_template : mail_template
mail_test_ticket --> res_partner : customer_id
mail_test_ticket --> res_users : user_id
mail_test_ticket --> mail_test_container : container_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/test_mail/Models]]

<!-- GENERATED:MODEL -->
