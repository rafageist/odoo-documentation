<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# coupon.share

- Module: [[docs/Community Addons/website_sale_loyalty/website_sale_loyalty|website_sale_loyalty]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/coupon_share.py`
- Python classes: `CouponShare`
- Description: Create links that apply a coupon and redirect to a specific page

## Field footprint

- Detected fields: 7
- Field types: `Char` x 3, `Many2one` x 4
- Relation fields: 4

## Sample fields

- `coupon_id`: `Many2one` (comodel `loyalty.card`)
- `program_id`: `Many2one` (comodel `loyalty.program`)
- `program_website_id`: `Many2one` (comodel `website`, related `program_id.website_id`)
- `promo_code`: `Char` (compute `_compute_promo_code`)
- `redirect`: `Char`
- `share_link`: `Char` (compute `_compute_share_link`)
- `website_id`: `Many2one` (comodel `website`)

## Method hints

- Detected methods: 7
- Action methods: `action_generate_short_link`
- Compute methods: `_compute_promo_code`, `_compute_share_link`
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
title coupon.share - Direct Relations
class "coupon.share" as coupon_share
class "loyalty.card" as loyalty_card
class "loyalty.program" as loyalty_program
class "website" as website
coupon_share --> website : website_id
coupon_share --> loyalty_card : coupon_id
coupon_share --> loyalty_program : program_id
coupon_share --> website : program_website_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website_sale_loyalty/Models]]

<!-- GENERATED:MODEL -->
