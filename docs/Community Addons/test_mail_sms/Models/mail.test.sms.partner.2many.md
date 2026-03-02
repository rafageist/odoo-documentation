<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mail.test.sms.partner.2many

- Module: [[docs/Community Addons/test_mail_sms/test_mail_sms|test_mail_sms]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/test_mail_sms_models.py`
- Python classes: `MailTestSmsPartner2many`
- Description: Chatter Model for SMS Gateway (M2M Partners only)
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 1, `Many2many` x 1
- Relation fields: 1

## Sample fields

- `customer_ids`: `Many2many` (comodel `res.partner`)
- `name`: `Char`
- `opt_out`: `Boolean`

## Method hints

- Detected methods: 2
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
title mail.test.sms.partner.2many - Direct Relations
class "mail.test.sms.partner.2many" as mail_test_sms_partner_2many
class "res.partner" as res_partner
mail_test_sms_partner_2many .. res_partner : customer_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/test_mail_sms/Models]]

<!-- GENERATED:MODEL -->
