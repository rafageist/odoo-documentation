<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sale.commission.plan.target.forecast

- Module: [[docs/Enterprise Addons/sale_commission/sale_commission|sale_commission]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `model/commission_plan_target_forecast.py`
- Python classes: `SaleCommissionPlanTargetForecast`
- Description: Commission Plan Target Forecast

## Field footprint

- Detected fields: 7
- Field types: `Many2one` x 5, `Monetary` x 1, `Text` x 1
- Relation fields: 5

## Sample fields

- `amount`: `Monetary` (comodel `Forecast`)
- `currency_id`: `Many2one` (comodel `res.currency`, related `plan_id.currency_id`)
- `notes`: `Text` (comodel `Notes`)
- `plan_id`: `Many2one` (comodel `sale.commission.plan`)
- `target_id`: `Many2one` (comodel `sale.commission.plan.target`)
- `team_id`: `Many2one` (comodel `crm.team`, related `user_id.sale_team_id`, store `True`)
- `user_id`: `Many2one` (comodel `res.users`)

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
title sale.commission.plan.target.forecast - Direct Relations
class "sale.commission.plan.target.forecast" as sale_commission_plan_target_forecast
class "crm.team" as crm_team
class "res.currency" as res_currency
class "res.users" as res_users
class "sale.commission.plan" as sale_commission_plan
class "sale.commission.plan.target" as sale_commission_plan_target
sale_commission_plan_target_forecast --> sale_commission_plan : plan_id
sale_commission_plan_target_forecast --> sale_commission_plan_target : target_id
sale_commission_plan_target_forecast --> res_users : user_id
sale_commission_plan_target_forecast --> crm_team : team_id
sale_commission_plan_target_forecast --> res_currency : currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_commission/Models]]

<!-- GENERATED:MODEL -->
