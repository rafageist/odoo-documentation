<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account_followup.followup.line

- Module: [[docs/Enterprise Addons/account_followup/account_followup|account_followup]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/account_followup.py`
- Python classes: `Account_FollowupFollowupLine`
- Description: Follow-up Criteria

## Field footprint

- Detected fields: 15
- Field types: `Boolean` x 5, `Char` x 2, `Integer` x 1, `Many2many` x 1, `Many2one` x 4, `Selection` x 1, `Text` x 1
- Relation fields: 5

## Sample fields

- `activity_default_responsible_type`: `Selection`
- `activity_note`: `Text`
- `activity_summary`: `Char`
- `activity_type_id`: `Many2one` (comodel `mail.activity.type`)
- `additional_follower_ids`: `Many2many` (comodel `res.users`)
- `auto_execute`: `Boolean`
- `company_id`: `Many2one` (comodel `res.company`)
- `create_activity`: `Boolean`
- `delay`: `Integer` (comodel `Due Days`)
- `join_invoices`: `Boolean`
- `mail_template_id`: `Many2one` (comodel `mail.template`)
- `name`: `Char` (comodel `Description`)
- `send_email`: `Boolean` (comodel `Email`)
- `send_sms`: `Boolean` (comodel `SMS`)
- `sms_template_id`: `Many2one` (comodel `sms.template`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: none
- Onchange methods: `_onchange_auto_execute`

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
title account_followup.followup.line - Direct Relations
class "account_followup.followup.line" as account_followup_followup_line
class "mail.activity.type" as mail_activity_type
class "mail.template" as mail_template
class "res.company" as res_company
class "res.users" as res_users
class "sms.template" as sms_template
account_followup_followup_line --> res_company : company_id
account_followup_followup_line --> mail_template : mail_template_id
account_followup_followup_line .. res_users : additional_follower_ids
account_followup_followup_line --> sms_template : sms_template_id
account_followup_followup_line --> mail_activity_type : activity_type_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_followup/Models]]

<!-- GENERATED:MODEL -->
