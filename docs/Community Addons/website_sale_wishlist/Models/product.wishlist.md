<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.wishlist

- Module: [[docs/Community Addons/website_sale_wishlist/website_sale_wishlist|website_sale_wishlist]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/product_wishlist.py`
- Python classes: `ProductWishlist`
- Description: Product Wishlist

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 1, `Many2one` x 5, `Monetary` x 1
- Relation fields: 5

## Sample fields

- `active`: `Boolean`
- `currency_id`: `Many2one` (comodel `res.currency`, related `website_id.currency_id`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `price`: `Monetary`
- `pricelist_id`: `Many2one` (comodel `product.pricelist`)
- `product_id`: `Many2one` (comodel `product.product`)
- `website_id`: `Many2one` (comodel `website`)

## Method hints

- Detected methods: 4
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
title product.wishlist - Direct Relations
class "product.wishlist" as product_wishlist
class "product.pricelist" as product_pricelist
class "product.product" as product_product
class "res.currency" as res_currency
class "res.partner" as res_partner
class "website" as website
product_wishlist --> res_partner : partner_id
product_wishlist --> product_product : product_id
product_wishlist --> res_currency : currency_id
product_wishlist --> product_pricelist : pricelist_id
product_wishlist --> website : website_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website_sale_wishlist/Models]]

<!-- GENERATED:MODEL -->
