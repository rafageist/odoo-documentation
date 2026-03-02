<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.feed

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/product_feed.py`
- Python classes: `ProductFeed`
- Description: Product Feed
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 12
- Field types: `Binary` x 1, `Char` x 3, `Date` x 1, `Datetime` x 1, `Many2many` x 2, `Many2one` x 3, `Selection` x 1
- Relation fields: 5

## Sample fields

- `access_token`: `Char`
- `cache_expiry`: `Datetime`
- `feed_cache`: `Binary` (compute `_compute_feed_cache`, store `True`)
- `lang_id`: `Many2one` (comodel `res.lang`, compute `_compute_lang_id`, store `True`)
- `last_notification_date`: `Date`
- `name`: `Char`
- `pricelist_id`: `Many2one` (comodel `product.pricelist`)
- `product_category_ids`: `Many2many` (comodel `product.public.category`)
- `target`: `Selection`
- `url`: `Char` (compute `_compute_url`)
- `website_id`: `Many2one` (comodel `website`)
- `website_lang_ids`: `Many2many` (related `website_id.language_ids`)

## Method hints

- Detected methods: 16
- Action methods: `action_invalidate_cache`
- Compute methods: `_compute_feed_cache`, `_compute_lang_id`, `_compute_url`
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
title product.feed - Direct Relations
class "product.feed" as product_feed
class "product.pricelist" as product_pricelist
class "product.public.category" as product_public_category
class "res.lang" as res_lang
class "website" as website
product_feed --> website : website_id
product_feed --> product_pricelist : pricelist_id
product_feed --> res_lang : lang_id
product_feed .. product_public_category : product_category_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Models]]

<!-- GENERATED:MODEL -->
