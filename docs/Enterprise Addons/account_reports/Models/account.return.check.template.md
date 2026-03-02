<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.return.check.template

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/account_return.py`
- Python classes: `AccountReturnCheckTemplate`
- Description: Account Return Check Template

## Field footprint

- Detected fields: 14
- Field types: `Char` x 6, `Many2many` x 1, `Many2one` x 3, `Selection` x 3, `Text` x 1
- Relation fields: 4

## Sample fields

- `action_id`: `Many2one` (comodel `ir.actions.actions`)
- `activity_type`: `Many2one` (comodel `mail.activity.type`)
- `additional_action_context`: `Char`
- `additional_action_domain`: `Char`
- `additional_action_params`: `Char`
- `code`: `Char`
- `country_ids`: `Many2many` (comodel `res.country`)
- `cycle`: `Selection`
- `description`: `Text`
- `domain`: `Char`
- `model`: `Selection`
- `name`: `Char`
- `return_type`: `Many2one` (comodel `account.return.type`)
- `type`: `Selection`

## Method hints

- Detected methods: 1
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
title account.return.check.template - Direct Relations
class "account.return.check.template" as account_return_check_template
class "account.return.type" as account_return_type
class "ir.actions.actions" as ir_actions_actions
class "mail.activity.type" as mail_activity_type
class "res.country" as res_country
account_return_check_template --> account_return_type : return_type
account_return_check_template .. res_country : country_ids
account_return_check_template --> ir_actions_actions : action_id
account_return_check_template --> mail_activity_type : activity_type
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Models]]

<!-- GENERATED:MODEL -->
