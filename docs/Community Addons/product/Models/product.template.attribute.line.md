<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.template.attribute.line

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/product_template_attribute_line.py`
- Python classes: `ProductTemplateAttributeLine`
- Description: Product Template Attribute Line

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 1, `Integer` x 2, `Many2many` x 1, `Many2one` x 2, `One2many` x 1
- Relation fields: 4

## Sample fields

- `active`: `Boolean`
- `attribute_id`: `Many2one` (comodel `product.attribute`)
- `product_template_value_ids`: `One2many` (comodel `product.template.attribute.value`)
- `product_tmpl_id`: `Many2one` (comodel `product.template`)
- `sequence`: `Integer` (comodel `Sequence`)
- `value_count`: `Integer` (compute `_compute_value_count`, store `True`)
- `value_ids`: `Many2many` (comodel `product.attribute.value`)

## Method hints

- Detected methods: 10
- Action methods: `action_open_attribute_values`
- Compute methods: `_compute_value_count`
- Onchange methods: `_onchange_attribute_id`

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
title product.template.attribute.line - Direct Relations
class "product.template.attribute.line" as product_template_attribute_line
class "product.attribute" as product_attribute
class "product.attribute.value" as product_attribute_value
class "product.template" as product_template
class "product.template.attribute.value" as product_template_attribute_value
product_template_attribute_line --> product_template : product_tmpl_id
product_template_attribute_line --> product_attribute : attribute_id
product_template_attribute_line .. product_attribute_value : value_ids
product_template_attribute_line --|> product_template_attribute_value : product_template_value_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/product/Models]]

<!-- GENERATED:MODEL -->
