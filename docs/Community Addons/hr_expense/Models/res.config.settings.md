<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.config.settings

- Module: [[docs/Community Addons/hr_expense/hr_expense|hr_expense]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 4, `Char` x 1, `Many2many` x 1, `Many2one` x 2
- Relation fields: 3

## Sample fields

- `company_expense_allowed_payment_method_line_ids`: `Many2many` (comodel `account.payment.method.line`, related `company_id.company_expense_allowed_payment_method_line_ids`)
- `expense_journal_id`: `Many2one` (comodel `account.journal`, related `company_id.expense_journal_id`)
- `hr_expense_alias_domain_id`: `Many2one` (comodel `mail.alias.domain`, compute `_compute_hr_expense_alias_domain_id`)
- `hr_expense_alias_prefix`: `Char` (comodel `Default Alias Name for Expenses`, compute `_compute_hr_expense_alias_prefix`, store `True`)
- `hr_expense_use_mailgateway`: `Boolean`
- `module_hr_expense_extract`: `Boolean`
- `module_hr_expense_stripe`: `Boolean`
- `module_hr_payroll_expense`: `Boolean`

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_hr_expense_alias_domain_id`, `_compute_hr_expense_alias_prefix`
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
title res.config.settings - Direct Relations
class "res.config.settings" as res_config_settings
class "account.journal" as account_journal
class "account.payment.method.line" as account_payment_method_line
class "mail.alias.domain" as mail_alias_domain
res_config_settings --> mail_alias_domain : hr_expense_alias_domain_id
res_config_settings --> account_journal : expense_journal_id
res_config_settings .. account_payment_method_line : company_expense_allowed_payment_method_line_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_expense/Models]]

<!-- GENERATED:MODEL -->
