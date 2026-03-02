<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# commission.rule

- Module: [[docs/Enterprise Addons/partner_commission/partner_commission|partner_commission]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/commission_plan.py`
- Python classes: `CommissionRule`
- Description: Commission rules management.

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 1, `Float` x 2, `Integer` x 1, `Many2one` x 5
- Relation fields: 5

## Sample fields

- `category_id`: `Many2one` (comodel `product.category`)
- `is_capped`: `Boolean` (comodel `Capped`)
- `max_commission`: `Float` (comodel `Max Commission`)
- `plan_id`: `Many2one` (comodel `commission.plan`)
- `pricelist_id`: `Many2one` (comodel `product.pricelist`)
- `product_id`: `Many2one` (comodel `product.product`)
- `rate`: `Float` (comodel `Rate`)
- `sequence`: `Integer`
- `template_id`: `Many2one` (comodel `sale.order.template`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: none
- Onchange methods: `_onchange_is_capped`

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
title commission.rule - Direct Relations
class "commission.rule" as commission_rule
class "commission.plan" as commission_plan
class "product.category" as product_category
class "product.pricelist" as product_pricelist
class "product.product" as product_product
class "sale.order.template" as sale_order_template
commission_rule --> commission_plan : plan_id
commission_rule --> product_category : category_id
commission_rule --> product_product : product_id
commission_rule --> sale_order_template : template_id
commission_rule --> product_pricelist : pricelist_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/partner_commission/Models]]

<!-- GENERATED:MODEL -->
