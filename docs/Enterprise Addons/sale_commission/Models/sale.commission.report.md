<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sale.commission.report

- Module: [[docs/Enterprise Addons/sale_commission/sale_commission|sale_commission]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/commission_report.py`
- Python classes: `SaleCommissionReport`
- Description: Sales Commission Report

## Field footprint

- Detected fields: 15
- Field types: `Date` x 3, `Float` x 1, `Many2one` x 6, `Monetary` x 4, `Text` x 1
- Relation fields: 6

## Sample fields

- `achieved`: `Monetary` (comodel `Achieved`)
- `achieved_rate`: `Float` (comodel `Achieved Rate`)
- `commission`: `Monetary` (comodel `Commission`)
- `company_id`: `Many2one` (comodel `res.company`)
- `currency_id`: `Many2one` (comodel `res.currency`)
- `date_from`: `Date` (related `target_id.date_from`)
- `date_to`: `Date` (related `target_id.date_to`)
- `forecast`: `Monetary` (comodel `Forecast`)
- `forecast_id`: `Many2one` (comodel `sale.commission.plan.target.forecast`)
- `notes`: `Text` (related `forecast_id.notes`)
- `payment_date`: `Date` (comodel `Payment Date`)
- `plan_id`: `Many2one` (comodel `sale.commission.plan`)
- `target_amount`: `Monetary` (comodel `Target Amount`)
- `target_id`: `Many2one` (comodel `sale.commission.plan.target`)
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 8
- Action methods: `action_achievement_detail`
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
title sale.commission.report - Direct Relations
class "sale.commission.report" as sale_commission_report
class "res.company" as res_company
class "res.currency" as res_currency
class "res.users" as res_users
class "sale.commission.plan" as sale_commission_plan
class "sale.commission.plan.target" as sale_commission_plan_target
class "sale.commission.plan.target.forecast" as sale_commission_plan_target_forecast
sale_commission_report --> sale_commission_plan_target : target_id
sale_commission_report --> sale_commission_plan : plan_id
sale_commission_report --> res_users : user_id
sale_commission_report --> res_currency : currency_id
sale_commission_report --> res_company : company_id
sale_commission_report --> sale_commission_plan_target_forecast : forecast_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_commission/Models]]

<!-- GENERATED:MODEL -->
