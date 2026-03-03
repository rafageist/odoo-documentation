<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.fiscal.position

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/partner.py`
- Python classes: `AccountFiscalPosition`
- Description: Fiscal Position

## Field footprint

- Detected fields: 22
- Field types: `Binary` x 2, `Boolean` x 4, `Char` x 5, `Html` x 1, `Integer` x 2, `Many2many` x 2, `Many2one` x 4, `One2many` x 1, `Selection` x 1
- Relation fields: 7

## Sample fields

- `account_ids`: `One2many` (comodel `account.fiscal.position.account`)
- `account_map`: `Binary` (compute `_compute_account_map`)
- `active`: `Boolean`
- `auto_apply`: `Boolean`
- `company_country_id`: `Many2one` (related `company_id.account_fiscal_country_id`)
- `company_id`: `Many2one` (comodel `res.company`)
- `country_group_id`: `Many2one` (comodel `res.country.group`)
- `country_id`: `Many2one` (comodel `res.country`)
- `fiscal_country_codes`: `Char` (related `company_country_id.code`)
- `foreign_vat`: `Char`
- `foreign_vat_header_mode`: `Selection` (compute `_compute_foreign_vat_header_mode`)
- `is_domestic`: `Boolean` (compute `_compute_is_domestic`, store `True`)
- `name`: `Char`
- `note`: `Html` (comodel `Notes`)
- `sequence`: `Integer`
- `state_ids`: `Many2many` (comodel `res.country.state`)
- `states_count`: `Integer` (compute `_compute_states_count`)
- `tax_ids`: `Many2many` (comodel `account.tax`)
- `tax_map`: `Binary` (compute `_compute_tax_map`)
- `vat_required`: `Boolean`

## Method hints

- Detected methods: 21
- Action methods: `action_create_foreign_taxes`, `action_open_related_taxes`
- Compute methods: `_compute_account_map`, `_compute_foreign_vat_header_mode`, `_compute_is_domestic`, `_compute_states_count`, `_compute_tax_map`
- Onchange methods: `_onchange_country_group_id`, `_onchange_country_id`, `_onchange_foreign_vat`

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
title account.fiscal.position - Direct Relations
class "account.fiscal.position" as account_fiscal_position
class "account.fiscal.position.account" as account_fiscal_position_account
class "account.tax" as account_tax
class "res.company" as res_company
class "res.country" as res_country
class "res.country.group" as res_country_group
class "res.country.state" as res_country_state
account_fiscal_position --> res_company : company_id
account_fiscal_position --|> account_fiscal_position_account : account_ids
account_fiscal_position .. account_tax : tax_ids
account_fiscal_position --> res_country : country_id
account_fiscal_position --> res_country_group : country_group_id
account_fiscal_position .. res_country_state : state_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/account/Models]]

<!-- GENERATED:MODEL -->
