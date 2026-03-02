<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.lot

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/stock_lot.py`
- Python classes: `StockLot`
- Description: Lot/Serial
- Inherits: `mail.activity.mixin`, `mail.thread`

## Field footprint

- Detected fields: 14
- Field types: `Boolean` x 1, `Char` x 2, `Float` x 1, `Html` x 1, `Integer` x 1, `Many2many` x 2, `Many2one` x 4, `One2many` x 1, `Properties` x 1
- Relation fields: 7

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`, compute `_compute_company_id`, store `True`)
- `delivery_count`: `Integer` (comodel `Delivery order count`, compute `_compute_delivery_ids`)
- `delivery_ids`: `Many2many` (comodel `stock.picking`, compute `_compute_delivery_ids`)
- `display_complete`: `Boolean` (compute `_compute_display_complete`)
- `location_id`: `Many2one` (comodel `stock.location`, compute `_compute_single_location`, store `True`)
- `lot_properties`: `Properties` (comodel `Properties`)
- `name`: `Char` (comodel `Lot/Serial Number`, compute `_compute_name`, store `True`)
- `note`: `Html`
- `partner_ids`: `Many2many` (comodel `res.partner`, compute `_compute_partner_ids`)
- `product_id`: `Many2one` (comodel `product.product`)
- `product_qty`: `Float` (comodel `On Hand Quantity`, compute `_product_qty`)
- `product_uom_id`: `Many2one` (comodel `uom.uom`, related `product_id.uom_id`)
- `quant_ids`: `One2many` (comodel `stock.quant`)
- `ref`: `Char` (comodel `Internal Reference`)

## Method hints

- Detected methods: 23
- Action methods: `action_lot_open_quants`, `action_lot_open_transfers`
- Compute methods: `_compute_company_id`, `_compute_delivery_ids`, `_compute_display_complete`, `_compute_name`, `_compute_partner_ids`, `_compute_single_location`
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
title stock.lot - Direct Relations
class "stock.lot" as stock_lot
class "product.product" as product_product
class "res.company" as res_company
class "res.partner" as res_partner
class "stock.location" as stock_location
class "stock.picking" as stock_picking
class "stock.quant" as stock_quant
class "uom.uom" as uom_uom
stock_lot --> product_product : product_id
stock_lot --> uom_uom : product_uom_id
stock_lot --|> stock_quant : quant_ids
stock_lot --> res_company : company_id
stock_lot .. stock_picking : delivery_ids
stock_lot .. res_partner : partner_ids
stock_lot --> stock_location : location_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
