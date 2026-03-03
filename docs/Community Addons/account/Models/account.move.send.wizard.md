<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.move.send.wizard

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/account_move_send_wizard.py`
- Python classes: `AccountMoveSendWizard`
- Description: Account Move Send Wizard
- Inherits: `account.move.send`, `mail.composer.mixin`

## Field footprint

- Detected fields: 18
- Field types: `Boolean` x 1, `Char` x 3, `Json` x 6, `Many2many` x 1, `Many2one` x 4, `One2many` x 1, `Selection` x 1, `Text` x 1
- Relation fields: 6

## Sample fields

- `alerts`: `Json` (compute `_compute_alerts`)
- `available_pdf_report_ids`: `One2many` (comodel `ir.actions.report`, compute `_compute_available_pdf_report_ids`)
- `company_id`: `Many2one` (comodel `res.company`, related `move_id.company_id`)
- `display_pdf_report_id`: `Boolean` (compute `_compute_display_pdf_report_id`)
- `extra_edi_checkboxes`: `Json` (compute `_compute_extra_edi_checkboxes`, store `True`)
- `extra_edis`: `Json` (compute `_compute_extra_edis`)
- `invoice_edi_format`: `Selection` (compute `_compute_invoice_edi_format`)
- `lang`: `Char` (compute `_compute_lang`)
- `mail_attachments_widget`: `Json` (compute `_compute_mail_attachments_widget`, store `True`)
- `mail_partner_ids`: `Many2many` (comodel `res.partner`, compute `_compute_mail_partners`, store `True`)
- `model`: `Char` (comodel `Related Document Model`, compute `_compute_model`, store `True`)
- `move_id`: `Many2one` (comodel `account.move`)
- `pdf_report_id`: `Many2one` (comodel `ir.actions.report`, compute `_compute_pdf_report_id`, store `True`)
- `res_ids`: `Text` (comodel `Related Document IDs`, compute `_compute_res_ids`, store `True`)
- `sending_method_checkboxes`: `Json` (compute `_compute_sending_method_checkboxes`, store `True`)
- `sending_methods`: `Json` (compute `_compute_sending_methods`)
- `template_id`: `Many2one` (compute `_compute_template_id`, store `True`)
- `template_name`: `Char` (comodel `Template Name`)

## Method hints

- Detected methods: 31
- Action methods: `action_send_and_print`
- Compute methods: `_compute_alerts`, `_compute_available_pdf_report_ids`, `_compute_body`, `_compute_can_edit_body`, `_compute_display_pdf_report_id`, `_compute_extra_edi_checkboxes`, `_compute_extra_edis`, `_compute_invoice_edi_format`, and 11 more
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
title account.move.send.wizard - Direct Relations
class "account.move.send.wizard" as account_move_send_wizard
class "account.move" as account_move
class "ir.actions.report" as ir_actions_report
class "res.company" as res_company
class "res.partner" as res_partner
account_move_send_wizard --> account_move : move_id
account_move_send_wizard --> res_company : company_id
account_move_send_wizard --> ir_actions_report : pdf_report_id
account_move_send_wizard --|> ir_actions_report : available_pdf_report_ids
account_move_send_wizard .. res_partner : mail_partner_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/account/Models]]

<!-- GENERATED:MODEL -->
