<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# slide.channel

- Module: [[docs/Community Addons/website_sale_slides/website_sale_slides|website_sale_slides]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/slide_channel.py`
- Python classes: `SlideChannel`

## Field footprint

- Detected fields: 4
- Field types: `Many2one` x 2, `Monetary` x 1, `Selection` x 1
- Relation fields: 2

## Sample fields

- `currency_id`: `Many2one` (related `product_id.currency_id`)
- `enroll`: `Selection`
- `product_id`: `Many2one` (comodel `product.product`)
- `product_sale_revenues`: `Monetary` (compute `_compute_product_sale_revenues`)

## Method hints

- Detected methods: 6
- Action methods: `action_view_sales`
- Compute methods: `_compute_product_sale_revenues`
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
title slide.channel - Direct Relations
class "slide.channel" as slide_channel
class "product.product" as product_product
slide_channel --> product_product : product_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website_sale_slides/Models]]

<!-- GENERATED:MODEL -->
