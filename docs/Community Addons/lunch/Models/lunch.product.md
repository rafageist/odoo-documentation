<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# lunch.product

- Module: [[docs/Community Addons/lunch/lunch|lunch]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/lunch_product.py`
- Python classes: `LunchProduct`
- Description: Lunch Product
- Inherits: `image.mixin`

## Field footprint

- Detected fields: 15
- Field types: `Boolean` x 3, `Char` x 1, `Date` x 2, `Float` x 1, `Html` x 1, `Image` x 1, `Many2many` x 1, `Many2one` x 5
- Relation fields: 6

## Sample fields

- `active`: `Boolean`
- `category_id`: `Many2one` (comodel `lunch.product.category`)
- `company_id`: `Many2one` (comodel `res.company`, related `supplier_id.company_id`, store `True`)
- `currency_id`: `Many2one` (comodel `res.currency`, related `company_id.currency_id`)
- `description`: `Html` (comodel `Description`)
- `favorite_user_ids`: `Many2many` (comodel `res.users`)
- `is_available_at`: `Many2one` (comodel `lunch.location`, compute `_compute_is_available_at`)
- `is_favorite`: `Boolean` (compute `_compute_is_favorite`)
- `is_new`: `Boolean` (compute `_compute_is_new`)
- `last_order_date`: `Date` (compute `_compute_last_order_date`)
- `name`: `Char` (comodel `Product Name`)
- `new_until`: `Date` (comodel `New Until`)
- `price`: `Float` (comodel `Price`)
- `product_image`: `Image` (compute `_compute_product_image`)
- `supplier_id`: `Many2one` (comodel `lunch.supplier`)

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_is_available_at`, `_compute_is_favorite`, `_compute_is_new`, `_compute_last_order_date`, `_compute_product_image`
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
title lunch.product - Direct Relations
class "lunch.product" as lunch_product
class "lunch.location" as lunch_location
class "lunch.product.category" as lunch_product_category
class "lunch.supplier" as lunch_supplier
class "res.company" as res_company
class "res.currency" as res_currency
class "res.users" as res_users
lunch_product --> lunch_product_category : category_id
lunch_product --> lunch_supplier : supplier_id
lunch_product --> res_company : company_id
lunch_product --> res_currency : currency_id
lunch_product .. res_users : favorite_user_ids
lunch_product --> lunch_location : is_available_at
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/lunch/Models]]

<!-- GENERATED:MODEL -->
