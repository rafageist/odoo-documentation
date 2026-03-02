<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.return.picking.line

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/stock_picking_return.py`
- Python classes: `StockReturnPickingLine`
- Description: Return Picking Line

## Field footprint

- Detected fields: 6
- Field types: `Float` x 2, `Many2one` x 4
- Relation fields: 4

## Sample fields

- `move_id`: `Many2one` (comodel `stock.move`)
- `move_quantity`: `Float` (related `move_id.quantity`)
- `product_id`: `Many2one` (comodel `product.product`)
- `quantity`: `Float` (comodel `Quantity`)
- `uom_id`: `Many2one` (comodel `uom.uom`, compute `_compute_uom_id`)
- `wizard_id`: `Many2one` (comodel `stock.return.picking`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_uom_id`
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
title stock.return.picking.line - Direct Relations
class "stock.return.picking.line" as stock_return_picking_line
class "product.product" as product_product
class "stock.move" as stock_move
class "stock.return.picking" as stock_return_picking
class "uom.uom" as uom_uom
stock_return_picking_line --> product_product : product_id
stock_return_picking_line --> uom_uom : uom_id
stock_return_picking_line --> stock_return_picking : wizard_id
stock_return_picking_line --> stock_move : move_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
