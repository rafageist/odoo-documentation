<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mailing.contact

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mailing_contact.py`
- Python classes: `MailingContact`
- Description: Mailing Contact
- Inherits: `mail.thread.blacklist`, `properties.base.definition.mixin`

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 1, `Char` x 5, `Many2many` x 2, `Many2one` x 1, `One2many` x 1
- Relation fields: 4

## Sample fields

- `company_name`: `Char`
- `country_id`: `Many2one` (comodel `res.country`)
- `email`: `Char` (comodel `Email`)
- `first_name`: `Char` (comodel `First Name`)
- `last_name`: `Char` (comodel `Last Name`)
- `list_ids`: `Many2many` (comodel `mailing.list`)
- `name`: `Char` (comodel `Name`, compute `_compute_name`, store `True`)
- `opt_out`: `Boolean` (comodel `Opt Out`, compute `_compute_opt_out`)
- `subscription_ids`: `One2many` (comodel `mailing.subscription`)
- `tag_ids`: `Many2many` (comodel `res.partner.category`)

## Method hints

- Detected methods: 13
- Action methods: `action_add_to_mailing_list`, `action_import`
- Compute methods: `_compute_name`, `_compute_opt_out`
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
title mailing.contact - Direct Relations
class "mailing.contact" as mailing_contact
class "mailing.list" as mailing_list
class "mailing.subscription" as mailing_subscription
class "res.country" as res_country
class "res.partner.category" as res_partner_category
mailing_contact .. mailing_list : list_ids
mailing_contact --|> mailing_subscription : subscription_ids
mailing_contact --> res_country : country_id
mailing_contact .. res_partner_category : tag_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Models]]

<!-- GENERATED:MODEL -->
