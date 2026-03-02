<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sdd.mandate.send

- Module: [[docs/Enterprise Addons/account_sepa_direct_debit/account_sepa_direct_debit|account_sepa_direct_debit]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/sdd_mandate_send.py`
- Python classes: `SddMandateSend`
- Description: SDD Mandate Send
- Inherits: `mail.composer.mixin`

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 2, `Json` x 1, `Many2many` x 1, `Many2one` x 5
- Relation fields: 6

## Sample fields

- `author_id`: `Many2one` (comodel `res.partner`)
- `checkbox_download`: `Boolean`
- `checkbox_send_mail`: `Boolean`
- `company_id`: `Many2one` (comodel `res.company`, compute `_compute_company_id`, store `True`)
- `mandate_id`: `Many2one` (comodel `sdd.mandate`)
- `partner_id`: `Many2one` (related `mandate_id.partner_id`)
- `recipient_ids`: `Many2many` (comodel `res.partner`, compute `_compute_recipient_ids`)
- `template_id`: `Many2one` (comodel `mail.template`)
- `warnings`: `Json` (compute `_compute_warnings`)

## Method hints

- Detected methods: 8
- Action methods: `action_send_and_print`
- Compute methods: `_compute_body`, `_compute_company_id`, `_compute_recipient_ids`, `_compute_subject`, `_compute_warnings`
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
title sdd.mandate.send - Direct Relations
class "sdd.mandate.send" as sdd_mandate_send
class "mail.template" as mail_template
class "res.company" as res_company
class "res.partner" as res_partner
class "sdd.mandate" as sdd_mandate
sdd_mandate_send --> res_company : company_id
sdd_mandate_send --> sdd_mandate : mandate_id
sdd_mandate_send --> mail_template : template_id
sdd_mandate_send --> res_partner : author_id
sdd_mandate_send .. res_partner : recipient_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_sepa_direct_debit/Models]]

<!-- GENERATED:MODEL -->
