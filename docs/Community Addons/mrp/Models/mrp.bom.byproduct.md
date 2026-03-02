<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mrp.bom.byproduct

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mrp_bom.py`
- Python classes: `MrpBomByproduct`
- Description: Byproduct

## Field footprint

- Detected fields: 11
- Field types: `Float` x 2, `Integer` x 1, `Many2many` x 2, `Many2one` x 5, `One2many` x 1
- Relation fields: 8

## Sample fields

- `allowed_operation_ids`: `One2many` (comodel `mrp.routing.workcenter`, related `bom_id.operation_ids`)
- `bom_id`: `Many2one` (comodel `mrp.bom`)
- `bom_product_template_attribute_value_ids`: `Many2many` (comodel `product.template.attribute.value`)
- `company_id`: `Many2one` (related `bom_id.company_id`, store `True`)
- `cost_share`: `Float` (comodel `Cost Share (%)`)
- `operation_id`: `Many2one` (comodel `mrp.routing.workcenter`)
- `possible_bom_product_template_attribute_value_ids`: `Many2many` (related `bom_id.possible_product_template_attribute_value_ids`)
- `product_id`: `Many2one` (comodel `product.product`)
- `product_qty`: `Float` (comodel `Quantity`)
- `product_uom_id`: `Many2one` (comodel `uom.uom`, compute `_compute_product_uom_id`, store `True`)
- `sequence`: `Integer` (comodel `Sequence`)

## Method hints

- Detected methods: 4
- Action methods: `action_add_from_catalog`
- Compute methods: `_compute_product_uom_id`
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
title mrp.bom.byproduct - Direct Relations
class "mrp.bom.byproduct" as mrp_bom_byproduct
class "mrp.bom" as mrp_bom
class "mrp.routing.workcenter" as mrp_routing_workcenter
class "product.product" as product_product
class "product.template.attribute.value" as product_template_attribute_value
class "uom.uom" as uom_uom
mrp_bom_byproduct --> product_product : product_id
mrp_bom_byproduct --> uom_uom : product_uom_id
mrp_bom_byproduct --> mrp_bom : bom_id
mrp_bom_byproduct --|> mrp_routing_workcenter : allowed_operation_ids
mrp_bom_byproduct --> mrp_routing_workcenter : operation_id
mrp_bom_byproduct .. product_template_attribute_value : bom_product_template_attribute_value_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Models]]

<!-- GENERATED:MODEL -->
