<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# product.pricing

- Module: [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/product_pricing.py`
- Python classes: `ProductPricing`
- Description: Pricing rule of rental products

## Field footprint

- Detected fields: 9
- Field types: `Char` x 2, `Many2many` x 1, `Many2one` x 5, `Monetary` x 1
- Relation fields: 6

## Sample fields

- `company_id`: `Many2one` (related `pricelist_id.company_id`)
- `currency_id`: `Many2one` (comodel `res.currency`, compute `_compute_currency_id`, store `True`)
- `description`: `Char` (compute `_compute_description`)
- `name`: `Char` (related `recurrence_id.duration_display`)
- `price`: `Monetary`
- `pricelist_id`: `Many2one` (comodel `product.pricelist`)
- `product_template_id`: `Many2one` (comodel `product.template`)
- `product_variant_ids`: `Many2many` (comodel `product.product`)
- `recurrence_id`: `Many2one` (comodel `sale.temporal.recurrence`)

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_currency_id`, `_compute_description`, `_compute_duration_vals`, `_compute_price`
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
title product.pricing - Direct Relations
class "product.pricing" as product_pricing
class "product.pricelist" as product_pricelist
class "product.product" as product_product
class "product.template" as product_template
class "res.currency" as res_currency
class "sale.temporal.recurrence" as sale_temporal_recurrence
product_pricing --> sale_temporal_recurrence : recurrence_id
product_pricing --> res_currency : currency_id
product_pricing --> product_template : product_template_id
product_pricing .. product_product : product_variant_ids
product_pricing --> product_pricelist : pricelist_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_renting/Models]]

<!-- GENERATED:MODEL -->
