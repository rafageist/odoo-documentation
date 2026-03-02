<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sale.order.line

- Module: [[docs/Enterprise Addons/sale_stock_renting/sale_stock_renting|sale_stock_renting]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/sale_order_line.py`
- Python classes: `SaleOrderLine`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Many2many` x 4, `Selection` x 1
- Relation fields: 4

## Sample fields

- `available_reserved_lots`: `Boolean` (compute `_compute_available_reserved_lots`)
- `pickedup_lot_ids`: `Many2many` (comodel `stock.lot`)
- `reserved_lot_ids`: `Many2many` (comodel `stock.lot`)
- `returned_lot_ids`: `Many2many` (comodel `stock.lot`)
- `tracking`: `Selection` (related `product_id.tracking`)
- `unavailable_lot_ids`: `Many2many` (comodel `stock.lot`, compute `_compute_unavailable_lots`, store `False`)

## Method hints

- Detected methods: 22
- Action methods: none
- Compute methods: `_compute_available_reserved_lots`, `_compute_qty_at_date`, `_compute_qty_delivered_method`, `_compute_reservation_begin`, `_compute_unavailable_lots`
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
title sale.order.line - Direct Relations
class "sale.order.line" as sale_order_line
class "stock.lot" as stock_lot
sale_order_line .. stock_lot : reserved_lot_ids
sale_order_line .. stock_lot : pickedup_lot_ids
sale_order_line .. stock_lot : returned_lot_ids
sale_order_line .. stock_lot : unavailable_lot_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_stock_renting/Models]]

<!-- GENERATED:MODEL -->
