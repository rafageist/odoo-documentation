<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# loyalty.rule

- Module: [[docs/Community Addons/loyalty/loyalty|loyalty]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/loyalty_rule.py`
- Python classes: `LoyaltyRule`
- Description: Loyalty Rule

## Field footprint

- Detected fields: 19
- Field types: `Boolean` x 3, `Char` x 3, `Float` x 1, `Integer` x 1, `Many2many` x 1, `Many2one` x 5, `Monetary` x 1, `Selection` x 4
- Relation fields: 6

## Sample fields

- `active`: `Boolean`
- `code`: `Char` (compute `_compute_code`, store `True`)
- `company_id`: `Many2one` (related `program_id.company_id`, store `True`)
- `currency_id`: `Many2one` (related `program_id.currency_id`)
- `minimum_amount`: `Monetary`
- `minimum_amount_tax_mode`: `Selection`
- `minimum_qty`: `Integer`
- `mode`: `Selection` (compute `_compute_mode`, store `True`)
- `product_category_id`: `Many2one` (comodel `product.category`)
- `product_domain`: `Char`
- `product_ids`: `Many2many` (comodel `product.product`)
- `product_tag_id`: `Many2one` (comodel `product.tag`)
- `program_id`: `Many2one` (comodel `loyalty.program`)
- `program_type`: `Selection` (related `program_id.program_type`)
- `reward_point_amount`: `Float`
- `reward_point_mode`: `Selection`
- `reward_point_name`: `Char` (related `program_id.portal_point_name`)
- `reward_point_split`: `Boolean`
- `user_has_debug`: `Boolean` (compute `_compute_user_has_debug`)

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_amount`, `_compute_code`, `_compute_mode`, `_compute_user_has_debug`
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
title loyalty.rule - Direct Relations
class "loyalty.rule" as loyalty_rule
class "loyalty.program" as loyalty_program
class "product.category" as product_category
class "product.product" as product_product
class "product.tag" as product_tag
loyalty_rule --> loyalty_program : program_id
loyalty_rule .. product_product : product_ids
loyalty_rule --> product_category : product_category_id
loyalty_rule --> product_tag : product_tag_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/loyalty/Models]]

<!-- GENERATED:MODEL -->
