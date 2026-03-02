<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# purchase.order.line

- Module: [[docs/Community Addons/purchase_product_matrix/purchase_product_matrix|purchase_product_matrix]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/purchase.py`
- Python classes: `PurchaseOrderLine`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 1, `Many2many` x 2, `Many2one` x 1
- Relation fields: 3

## Sample fields

- `is_configurable_product`: `Boolean` (comodel `Is the product configurable?`, related `product_template_id.has_configurable_attributes`)
- `product_no_variant_attribute_value_ids`: `Many2many` (comodel `product.template.attribute.value`)
- `product_template_attribute_value_ids`: `Many2many` (related `product_id.product_template_attribute_value_ids`)
- `product_template_id`: `Many2one` (comodel `product.template`, related `product_id.product_tmpl_id`)

## Method hints

- Detected methods: 1
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
title purchase.order.line - Direct Relations
class "purchase.order.line" as purchase_order_line
class "product.template" as product_template
class "product.template.attribute.value" as product_template_attribute_value
purchase_order_line --> product_template : product_template_id
purchase_order_line .. product_template_attribute_value : product_no_variant_attribute_value_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/purchase_product_matrix/Models]]

<!-- GENERATED:MODEL -->
