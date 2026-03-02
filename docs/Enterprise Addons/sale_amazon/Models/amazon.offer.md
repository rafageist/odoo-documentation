<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# amazon.offer

- Module: [[docs/Enterprise Addons/sale_amazon/sale_amazon|sale_amazon]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/amazon_offer.py`
- Python classes: `AmazonOffer`
- Description: Amazon Offer

## Field footprint

- Detected fields: 11
- Field types: `Boolean` x 1, `Char` x 2, `Many2many` x 1, `Many2one` x 5, `Selection` x 2
- Relation fields: 6

## Sample fields

- `account_id`: `Many2one` (comodel `amazon.account`)
- `active_marketplace_ids`: `Many2many` (related `account_id.active_marketplace_ids`)
- `amazon_channel`: `Selection`
- `amazon_feed_ref`: `Char`
- `amazon_sync_status`: `Selection`
- `company_id`: `Many2one` (related `account_id.company_id`)
- `marketplace_id`: `Many2one` (comodel `amazon.marketplace`)
- `product_id`: `Many2one` (comodel `product.product`)
- `product_template_id`: `Many2one` (related `product_id.product_tmpl_id`, store `True`)
- `sku`: `Char`
- `sync_stock`: `Boolean` (compute `_compute_sync_stock`, store `True`)

## Method hints

- Detected methods: 12
- Action methods: `action_view_online`
- Compute methods: `_compute_sync_stock`
- Onchange methods: `_onchange_product_id`

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
title amazon.offer - Direct Relations
class "amazon.offer" as amazon_offer
class "amazon.account" as amazon_account
class "amazon.marketplace" as amazon_marketplace
class "product.product" as product_product
amazon_offer --> amazon_account : account_id
amazon_offer --> amazon_marketplace : marketplace_id
amazon_offer --> product_product : product_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_amazon/Models]]

<!-- GENERATED:MODEL -->
