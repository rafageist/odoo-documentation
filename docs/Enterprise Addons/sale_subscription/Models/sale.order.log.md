<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sale.order.log

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/sale_order_log.py`
- Python classes: `SaleOrderLog`
- Description: Sale Order Log

## Field footprint

- Detected fields: 13
- Field types: `Date` x 2, `Many2one` x 7, `Monetary` x 2, `Selection` x 2
- Relation fields: 7

## Sample fields

- `amount_signed`: `Monetary`
- `company_id`: `Many2one` (comodel `res.company`, related `order_id.company_id`, store `True`)
- `currency_id`: `Many2one` (comodel `res.currency`, related `order_id.currency_id`, store `True`)
- `effective_date`: `Date`
- `event_date`: `Date`
- `event_type`: `Selection`
- `order_id`: `Many2one` (comodel `sale.order`)
- `origin_order_id`: `Many2one` (comodel `sale.order`, compute `_compute_origin_order_id`, store `True`)
- `plan_id`: `Many2one` (comodel `sale.subscription.plan`, related `order_id.plan_id`, store `True`)
- `recurring_monthly`: `Monetary`
- `subscription_state`: `Selection`
- `team_id`: `Many2one` (comodel `crm.team`, related `order_id.team_id`, store `True`)
- `user_id`: `Many2one` (comodel `res.users`, related `order_id.user_id`, store `True`)

## Method hints

- Detected methods: 13
- Action methods: none
- Compute methods: `_compute_display_name`, `_compute_origin_order_id`
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
title sale.order.log - Direct Relations
class "sale.order.log" as sale_order_log
class "crm.team" as crm_team
class "res.company" as res_company
class "res.currency" as res_currency
class "res.users" as res_users
class "sale.order" as sale_order
class "sale.subscription.plan" as sale_subscription_plan
sale_order_log --> sale_order : order_id
sale_order_log --> res_users : user_id
sale_order_log --> crm_team : team_id
sale_order_log --> sale_subscription_plan : plan_id
sale_order_log --> res_company : company_id
sale_order_log --> res_currency : currency_id
sale_order_log --> sale_order : origin_order_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Models]]

<!-- GENERATED:MODEL -->
