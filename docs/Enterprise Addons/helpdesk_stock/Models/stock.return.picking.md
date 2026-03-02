<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# stock.return.picking

- Module: [[docs/Enterprise Addons/helpdesk_stock/helpdesk_stock|helpdesk_stock]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `wizard/stock_picking_return.py`
- Python classes: `StockReturnPicking`

## Field footprint

- Detected fields: 6
- Field types: `Many2many` x 2, `Many2one` x 4
- Relation fields: 6

## Sample fields

- `partner_id`: `Many2one` (comodel `res.partner`, related `ticket_id.partner_id`)
- `picking_id`: `Many2one` (compute `_compute_picking_id`, store `True`)
- `sale_order_id`: `Many2one` (comodel `sale.order`, compute `_compute_sale_order_id`)
- `suitable_picking_ids`: `Many2many` (comodel `stock.picking`, compute `_compute_suitable_picking_ids`)
- `suitable_sale_order_ids`: `Many2many` (comodel `sale.order`, compute `_compute_suitable_sale_orders`)
- `ticket_id`: `Many2one` (comodel `helpdesk.ticket`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_picking_id`, `_compute_sale_order_id`, `_compute_suitable_picking_ids`, `_compute_suitable_sale_orders`
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
title stock.return.picking - Direct Relations
class "stock.return.picking" as stock_return_picking
class "helpdesk.ticket" as helpdesk_ticket
class "res.partner" as res_partner
class "sale.order" as sale_order
class "stock.picking" as stock_picking
stock_return_picking --> res_partner : partner_id
stock_return_picking --> helpdesk_ticket : ticket_id
stock_return_picking --> sale_order : sale_order_id
stock_return_picking .. stock_picking : suitable_picking_ids
stock_return_picking .. sale_order : suitable_sale_order_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_stock/Models]]

<!-- GENERATED:MODEL -->
