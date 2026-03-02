<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# product.template

- Module: [[docs/Enterprise Addons/pos_urban_piper/pos_urban_piper|pos_urban_piper]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/product.py`
- Python classes: `ProductTemplate`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 2, `Many2many` x 2, `One2many` x 1, `Selection` x 1
- Relation fields: 3

## Sample fields

- `is_alcoholic_on_urbanpiper`: `Boolean`
- `is_recommended_on_urbanpiper`: `Boolean`
- `urban_piper_status_ids`: `One2many` (comodel `product.urban.piper.status`)
- `urbanpiper_meal_type`: `Selection`
- `urbanpiper_pos_config_ids`: `Many2many` (comodel `pos.config`)
- `urbanpiper_pos_platform_ids`: `Many2many` (comodel `pos.delivery.provider`, compute `_compute_urbanpiper_pos_platform_ids`, store `True`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_urbanpiper_pos_platform_ids`
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
title product.template - Direct Relations
class "product.template" as product_template
class "pos.config" as pos_config
class "pos.delivery.provider" as pos_delivery_provider
class "product.urban.piper.status" as product_urban_piper_status
product_template .. pos_config : urbanpiper_pos_config_ids
product_template .. pos_delivery_provider : urbanpiper_pos_platform_ids
product_template --|> product_urban_piper_status : urban_piper_status_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_urban_piper/Models]]

<!-- GENERATED:MODEL -->
