<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.product

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/product_product.py`
- Python classes: `ProductProduct`

## Field footprint

- Detected fields: 8
- Field types: `Char` x 2, `Float` x 1, `Many2one` x 3, `Monetary` x 1, `One2many` x 1
- Relation fields: 4

## Sample fields

- `base_unit_count`: `Float`
- `base_unit_id`: `Many2one` (comodel `website.base.unit`)
- `base_unit_name`: `Char` (compute `_compute_base_unit_name`)
- `base_unit_price`: `Monetary` (compute `_compute_base_unit_price`)
- `product_variant_image_ids`: `One2many` (comodel `product.image`)
- `variant_ribbon_id`: `Many2one` (comodel `product.ribbon`)
- `website_id`: `Many2one` (related `product_tmpl_id.website_id`)
- `website_url`: `Char` (compute `_compute_product_website_url`)

## Method hints

- Detected methods: 17
- Action methods: none
- Compute methods: `_compute_base_unit_name`, `_compute_base_unit_price`, `_compute_product_website_url`
- Onchange methods: `_onchange_public_categ_ids`

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
title product.product - Direct Relations
class "product.product" as product_product
class "product.image" as product_image
class "product.ribbon" as product_ribbon
class "website.base.unit" as website_base_unit
product_product --> product_ribbon : variant_ribbon_id
product_product --|> product_image : product_variant_image_ids
product_product --> website_base_unit : base_unit_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Models]]

<!-- GENERATED:MODEL -->
