<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# esg.carbon.emission.report

- Module: [[docs/Enterprise Addons/esg/esg|esg]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/esg_carbon_emission_report.py`
- Python classes: `EsgCarbonEmissionReport`
- Description: ESG Carbon Emissions Report

## Field footprint

- Detected fields: 22
- Field types: `Date` x 2, `Float` x 4, `Integer` x 1, `Many2many` x 1, `Many2one` x 9, `Monetary` x 1, `Selection` x 2, `Text` x 2
- Relation fields: 10

## Sample fields

- `account_id`: `Many2one` (comodel `account.account`)
- `activity_type_ids`: `Many2many` (comodel `esg.activity.type`, related `esg_emission_factor_id.activity_type_ids`)
- `company_id`: `Many2one` (comodel `res.company`)
- `compute_method`: `Selection` (related `esg_emission_factor_id.compute_method`)
- `currency_id`: `Many2one` (comodel `res.currency`, compute `_compute_currency_id`, store `True`)
- `database_id`: `Many2one` (related `esg_emission_factor_id.database_id`)
- `date`: `Date`
- `date_end`: `Date`
- `esg_emission_factor_id`: `Many2one` (comodel `esg.emission.factor`)
- `esg_emissions_value`: `Float`
- `esg_emissions_value_t`: `Float`
- `esg_uncertainty_absolute_value`: `Float`
- `esg_uncertainty_value`: `Float` (related `esg_emission_factor_id.esg_uncertainty_value`)
- `move_id`: `Many2one` (comodel `account.move`)
- `name`: `Text`
- `note`: `Text`
- `partner_id`: `Many2one` (related `move_id.partner_id`)
- `price_subtotal`: `Monetary`
- `quantity`: `Integer`
- `scope`: `Selection` (related `source_id.scope`)

## Method hints

- Detected methods: 8
- Action methods: `action_open_emission_form`
- Compute methods: `_compute_currency_id`, `_compute_uom_id`
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
title esg.carbon.emission.report - Direct Relations
class "esg.carbon.emission.report" as esg_carbon_emission_report
class "account.account" as account_account
class "account.move" as account_move
class "esg.activity.type" as esg_activity_type
class "esg.emission.factor" as esg_emission_factor
class "res.company" as res_company
class "res.currency" as res_currency
class "uom.uom" as uom_uom
esg_carbon_emission_report --> esg_emission_factor : esg_emission_factor_id
esg_carbon_emission_report --> account_move : move_id
esg_carbon_emission_report --> uom_uom : uom_id
esg_carbon_emission_report --> res_currency : currency_id
esg_carbon_emission_report --> res_company : company_id
esg_carbon_emission_report --> account_account : account_id
esg_carbon_emission_report .. esg_activity_type : activity_type_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg/Models]]

<!-- GENERATED:MODEL -->
