<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.replenishment.option

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/stock_replenishment_info.py`
- Python classes: `StockReplenishmentOption`
- Description: Stock warehouse replenishment option

## Field footprint

- Detected fields: 10
- Field types: `Char` x 3, `Float` x 2, `Many2one` x 5
- Relation fields: 5

## Sample fields

- `free_qty`: `Float` (compute `_compute_free_qty`)
- `lead_time`: `Char` (compute `_compute_lead_time`)
- `location_id`: `Many2one` (comodel `stock.location`, related `warehouse_id.lot_stock_id`)
- `product_id`: `Many2one` (comodel `product.product`)
- `qty_to_order`: `Float` (related `replenishment_info_id.qty_to_order`)
- `replenishment_info_id`: `Many2one` (comodel `stock.replenishment.info`)
- `route_id`: `Many2one` (comodel `stock.route`)
- `uom`: `Char` (related `product_id.uom_name`)
- `warehouse_id`: `Many2one` (comodel `stock.warehouse`, related `route_id.supplier_wh_id`)
- `warning_message`: `Char` (compute `_compute_warning_message`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_free_qty`, `_compute_lead_time`, `_compute_warning_message`
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
title stock.replenishment.option - Direct Relations
class "stock.replenishment.option" as stock_replenishment_option
class "product.product" as product_product
class "stock.location" as stock_location
class "stock.replenishment.info" as stock_replenishment_info
class "stock.route" as stock_route
class "stock.warehouse" as stock_warehouse
stock_replenishment_option --> stock_route : route_id
stock_replenishment_option --> product_product : product_id
stock_replenishment_option --> stock_replenishment_info : replenishment_info_id
stock_replenishment_option --> stock_location : location_id
stock_replenishment_option --> stock_warehouse : warehouse_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
