<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/account_intrastat/account_intrastat|account_intrastat]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Many2one` x 4
- Relation fields: 4

## Sample fields

- `company_country_id`: `Many2one` (comodel `res.country`, related `company_id.account_fiscal_country_id`)
- `has_country_regions`: `Boolean` (compute `_compute_has_country_regions`)
- `intrastat_default_invoice_transaction_code_id`: `Many2one` (comodel `account.intrastat.code`, related `company_id.intrastat_default_invoice_transaction_code_id`)
- `intrastat_default_refund_transaction_code_id`: `Many2one` (comodel `account.intrastat.code`, related `company_id.intrastat_default_refund_transaction_code_id`)
- `intrastat_region_id`: `Many2one` (comodel `account.intrastat.code`, related `company_id.intrastat_region_id`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_has_country_regions`
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
class "account.intrastat.code" as account_intrastat_code
class "res.country" as res_country
res_config_settings --> res_country : company_country_id
res_config_settings --> account_intrastat_code : intrastat_default_invoice_transaction_code_id
res_config_settings --> account_intrastat_code : intrastat_default_refund_transaction_code_id
res_config_settings --> account_intrastat_code : intrastat_region_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_intrastat/Models]]

<!-- GENERATED:MODEL -->
