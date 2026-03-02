<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/stock_accountant/stock_accountant|stock_accountant]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 5
- Field types: `Many2one` x 2, `Selection` x 3
- Relation fields: 2

## Sample fields

- `cost_method`: `Selection` (related `company_id.cost_method`)
- `inventory_period`: `Selection` (related `company_id.inventory_period`)
- `stock_journal`: `Many2one` (comodel `account.journal`, related `company_id.account_stock_journal_id`)
- `stock_valuation_account_id`: `Many2one` (comodel `account.account`, related `company_id.account_stock_valuation_id`)
- `valuation_method`: `Selection` (related `company_id.inventory_valuation`)

## Method hints

- Detected methods: 1
- Action methods: `action_stock_open_valued_locations`
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
res_config_settings --> account_journal : stock_journal
res_config_settings --> account_account : stock_valuation_account_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_accountant/Models]]

<!-- GENERATED:MODEL -->
