<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.report.send

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/account_report_send.py`
- Python classes: `AccountReportSend`
- Description: Account Report Send

## Field footprint

- Detected fields: 17
- Field types: `Boolean` x 6, `Char` x 2, `Html` x 1, `Json` x 3, `Many2many` x 2, `Many2one` x 2, `Selection` x 1
- Relation fields: 4

## Sample fields

- `account_report_id`: `Many2one` (comodel `account.report`)
- `checkbox_download`: `Boolean`
- `checkbox_send_mail`: `Boolean`
- `display_mail_composer`: `Boolean` (compute `_compute_send_mail_extra_fields`)
- `enable_download`: `Boolean`
- `enable_send_mail`: `Boolean`
- `mail_attachments_widget`: `Json` (compute `_compute_mail_attachments_widget`, store `True`)
- `mail_body`: `Html` (compute `_compute_mail_subject_body`, store `True`)
- `mail_lang`: `Char` (compute `_compute_mail_lang`)
- `mail_partner_ids`: `Many2many` (comodel `res.partner`, compute `_compute_mail_partner_ids`, store `True`)
- `mail_subject`: `Char` (compute `_compute_mail_subject_body`, store `True`)
- `mail_template_id`: `Many2one` (comodel `mail.template`)
- `mode`: `Selection` (compute `_compute_mode`, store `True`)
- `partner_ids`: `Many2many` (comodel `res.partner`, compute `_compute_partner_ids`)
- `report_options`: `Json`
- `send_mail_readonly`: `Boolean` (compute `_compute_send_mail_extra_fields`)
- `warnings`: `Json` (compute `_compute_warnings`)

## Method hints

- Detected methods: 17
- Action methods: `action_send_and_print`
- Compute methods: `_compute_mail_attachments_widget`, `_compute_mail_lang`, `_compute_mail_partner_ids`, `_compute_mail_subject_body`, `_compute_mode`, `_compute_partner_ids`, `_compute_send_mail_extra_fields`, `_compute_warnings`
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
title account.report.send - Direct Relations
class "account.report.send" as account_report_send
class "account.report" as account_report
class "mail.template" as mail_template
class "res.partner" as res_partner
account_report_send .. res_partner : partner_ids
account_report_send --> mail_template : mail_template_id
account_report_send --> account_report : account_report_id
account_report_send .. res_partner : mail_partner_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Models]]

<!-- GENERATED:MODEL -->
