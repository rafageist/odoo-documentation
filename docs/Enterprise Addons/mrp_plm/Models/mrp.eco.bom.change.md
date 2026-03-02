<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# mrp.eco.bom.change

- Module: [[docs/Enterprise Addons/mrp_plm/mrp_plm|mrp_plm]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/mrp_eco.py`
- Python classes: `MrpEcoBomChange`
- Description: ECO BoM changes

## Field footprint

- Detected fields: 18
- Field types: `Boolean` x 1, `Char` x 2, `Float` x 3, `Many2one` x 11, `Selection` x 1
- Relation fields: 11

## Sample fields

- `bom_line_id`: `Many2one` (comodel `mrp.bom.line`)
- `byproduct_id`: `Many2one` (comodel `mrp.bom.byproduct`)
- `change_type`: `Selection`
- `company_id`: `Many2one` (related `eco_id.company_id`)
- `conflict`: `Boolean`
- `eco_id`: `Many2one` (comodel `mrp.eco`)
- `eco_rebase_id`: `Many2one` (comodel `mrp.eco`)
- `new_operation_id`: `Many2one` (comodel `mrp.routing.workcenter`)
- `new_product_qty`: `Float` (comodel `New revision quantity`)
- `new_uom_id`: `Many2one` (comodel `uom.uom`)
- `old_operation_id`: `Many2one` (comodel `mrp.routing.workcenter`)
- `old_product_qty`: `Float` (comodel `Previous revision quantity`)
- `old_uom_id`: `Many2one` (comodel `uom.uom`)
- `operation_change`: `Char` (compute `_compute_change`)
- `product_id`: `Many2one` (comodel `product.product`)
- `rebase_id`: `Many2one` (comodel `mrp.eco`)
- `uom_change`: `Char` (comodel `Unit`, compute `_compute_change`)
- `upd_product_qty`: `Float` (comodel `Quantity`, compute `_compute_upd_product_qty`, store `True`)

## Method hints

- Detected methods: 4
- Action methods: `action_open_byproduct_change`, `action_open_component_change`
- Compute methods: `_compute_change`, `_compute_upd_product_qty`
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
title mrp.eco.bom.change - Direct Relations
class "mrp.eco.bom.change" as mrp_eco_bom_change
class "mrp.bom.byproduct" as mrp_bom_byproduct
class "mrp.bom.line" as mrp_bom_line
class "mrp.eco" as mrp_eco
class "mrp.routing.workcenter" as mrp_routing_workcenter
class "product.product" as product_product
class "uom.uom" as uom_uom
mrp_eco_bom_change --> mrp_eco : eco_id
mrp_eco_bom_change --> mrp_eco : eco_rebase_id
mrp_eco_bom_change --> mrp_eco : rebase_id
mrp_eco_bom_change --> product_product : product_id
mrp_eco_bom_change --> uom_uom : old_uom_id
mrp_eco_bom_change --> uom_uom : new_uom_id
mrp_eco_bom_change --> mrp_routing_workcenter : old_operation_id
mrp_eco_bom_change --> mrp_routing_workcenter : new_operation_id
mrp_eco_bom_change --> mrp_bom_line : bom_line_id
mrp_eco_bom_change --> mrp_bom_byproduct : byproduct_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_plm/Models]]

<!-- GENERATED:MODEL -->
