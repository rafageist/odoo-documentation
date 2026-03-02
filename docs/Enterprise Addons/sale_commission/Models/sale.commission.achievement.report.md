<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sale.commission.achievement.report

- Module: [[docs/Enterprise Addons/sale_commission/sale_commission|sale_commission]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/achievement_report.py`
- Python classes: `SaleCommissionAchievementReport`
- Description: Sales Achievement Report

## Field footprint

- Detected fields: 15
- Field types: `Char` x 1, `Date` x 1, `Float` x 2, `Many2one` x 7, `Many2oneReference` x 1, `Monetary` x 3
- Relation fields: 7

## Sample fields

- `achieved`: `Monetary` (comodel `Achieved`)
- `commission_rate`: `Float` (comodel `Commission Rate`)
- `commission_target_amount`: `Monetary`
- `company_id`: `Many2one` (comodel `res.company`)
- `currency_id`: `Many2one` (comodel `res.currency`)
- `date`: `Date`
- `partner_id`: `Many2one` (comodel `res.partner`)
- `plan_id`: `Many2one` (comodel `sale.commission.plan`)
- `related_res_id`: `Many2oneReference` (comodel `Related`)
- `related_res_model`: `Char`
- `target_amount`: `Monetary`
- `target_id`: `Many2one` (comodel `sale.commission.plan.target`)
- `target_rate`: `Float` (comodel `Achieved Rate`)
- `team_id`: `Many2one` (comodel `crm.team`)
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 34
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
title sale.commission.achievement.report - Direct Relations
class "sale.commission.achievement.report" as sale_commission_achievement_report
class "crm.team" as crm_team
class "res.company" as res_company
class "res.currency" as res_currency
class "res.partner" as res_partner
class "res.users" as res_users
class "sale.commission.plan" as sale_commission_plan
class "sale.commission.plan.target" as sale_commission_plan_target
sale_commission_achievement_report --> sale_commission_plan_target : target_id
sale_commission_achievement_report --> sale_commission_plan : plan_id
sale_commission_achievement_report --> res_users : user_id
sale_commission_achievement_report --> crm_team : team_id
sale_commission_achievement_report --> res_currency : currency_id
sale_commission_achievement_report --> res_company : company_id
sale_commission_achievement_report --> res_partner : partner_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_commission/Models]]

<!-- GENERATED:MODEL -->
