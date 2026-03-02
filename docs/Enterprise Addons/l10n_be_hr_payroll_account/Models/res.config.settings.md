<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_account/l10n_be_hr_payroll_account|l10n_be_hr_payroll_account]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 4
- Field types: `Many2one` x 4
- Relation fields: 4

## Sample fields

- `exemption_bachelor_account_id`: `Many2one` (comodel `account.account`, related `company_id.exemption_bachelor_account_id`)
- `exemption_bachelor_capping_account_id`: `Many2one` (comodel `account.account`, related `company_id.exemption_bachelor_capping_account_id`)
- `exemption_doctor_master_account_id`: `Many2one` (comodel `account.account`, related `company_id.exemption_doctor_master_account_id`)
- `exemption_journal_id`: `Many2one` (comodel `account.journal`, related `company_id.exemption_journal_id`)

## Method hints

- Detected methods: 0
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
title res.config.settings - Direct Relations
class "res.config.settings" as res_config_settings
class "account.account" as account_account
class "account.journal" as account_journal
res_config_settings --> account_account : exemption_doctor_master_account_id
res_config_settings --> account_account : exemption_bachelor_account_id
res_config_settings --> account_account : exemption_bachelor_capping_account_id
res_config_settings --> account_journal : exemption_journal_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_account/Models]]

<!-- GENERATED:MODEL -->
