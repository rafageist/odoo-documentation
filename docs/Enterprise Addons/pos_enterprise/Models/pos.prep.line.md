<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# pos.prep.line

- Module: [[docs/Enterprise Addons/pos_enterprise/pos_enterprise|pos_enterprise]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/pos_prep_line.py`
- Python classes: `PosPrepLine`
- Description: Pos Preparation Line
- Inherits: `pos.load.mixin`

## Field footprint

- Detected fields: 11
- Field types: `Char` x 3, `Float` x 2, `Many2many` x 1, `Many2one` x 4, `One2many` x 1
- Relation fields: 6

## Sample fields

- `attribute_value_ids`: `Many2many` (comodel `product.template.attribute.value`)
- `cancelled`: `Float` (comodel `Quantity of cancelled product`)
- `combo_line_ids`: `One2many` (comodel `pos.prep.line`)
- `combo_parent_id`: `Many2one` (comodel `pos.prep.line`)
- `customer_note`: `Char`
- `internal_note`: `Char`
- `pos_order_line_id`: `Many2one` (comodel `pos.order.line`)
- `pos_order_line_uuid`: `Char`
- `prep_order_id`: `Many2one` (comodel `pos.prep.order`)
- `product_id`: `Many2one` (comodel `product.product`)
- `quantity`: `Float` (comodel `Quantity`)

## Method hints

- Detected methods: 0
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
title pos.prep.line - Direct Relations
class "pos.prep.line" as pos_prep_line
class "pos.order.line" as pos_order_line
class "pos.prep.line" as pos_prep_line
class "pos.prep.order" as pos_prep_order
class "product.product" as product_product
class "product.template.attribute.value" as product_template_attribute_value
pos_prep_line --> pos_prep_order : prep_order_id
pos_prep_line --> product_product : product_id
pos_prep_line .. product_template_attribute_value : attribute_value_ids
pos_prep_line --|> pos_prep_line : combo_line_ids
pos_prep_line --> pos_prep_line : combo_parent_id
pos_prep_line --> pos_order_line : pos_order_line_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_enterprise/Models]]

<!-- GENERATED:MODEL -->
