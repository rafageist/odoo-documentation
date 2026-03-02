<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/l10n_nl_reports/l10n_nl_reports|l10n_nl_reports]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 3
- Field types: `Many2one` x 3
- Relation fields: 3

## Sample fields

- `l10n_nl_reports_sbr_cert_id`: `Many2one` (related `company_id.l10n_nl_reports_sbr_cert_id`)
- `l10n_nl_rounding_difference_loss_account_id`: `Many2one` (comodel `account.account`, related `company_id.l10n_nl_rounding_difference_loss_account_id`)
- `l10n_nl_rounding_difference_profit_account_id`: `Many2one` (comodel `account.account`, related `company_id.l10n_nl_rounding_difference_profit_account_id`)

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
res_config_settings --> account_account : l10n_nl_rounding_difference_loss_account_id
res_config_settings --> account_account : l10n_nl_rounding_difference_profit_account_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_nl_reports/Models]]

<!-- GENERATED:MODEL -->
