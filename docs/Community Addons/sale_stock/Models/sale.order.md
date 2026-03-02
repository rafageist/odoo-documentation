<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# sale.order

- Module: [[docs/Community Addons/sale_stock/sale_stock|sale_stock]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/sale_order.py`
- Python classes: `SaleOrder`

## Field footprint

- Detected fields: 13
- Field types: `Boolean` x 2, `Char` x 2, `Datetime` x 2, `Integer` x 1, `Many2many` x 1, `Many2one` x 2, `One2many` x 1, `Selection` x 2
- Relation fields: 4

## Sample fields

- `delivery_count`: `Integer` (compute `_compute_picking_ids`)
- `delivery_status`: `Selection` (compute `_compute_delivery_status`, store `True`)
- `effective_date`: `Datetime` (comodel `Effective Date`, compute `_compute_effective_date`, store `True`)
- `expected_date`: `Datetime`
- `incoterm`: `Many2one` (comodel `account.incoterms`)
- `incoterm_location`: `Char`
- `json_popover`: `Char` (comodel `JSON data for the popover widget`, compute `_compute_json_popover`)
- `late_availability`: `Boolean` (compute `_compute_late_availability`)
- `picking_ids`: `One2many` (comodel `stock.picking`)
- `picking_policy`: `Selection`
- `show_json_popover`: `Boolean` (comodel `Has late picking`, compute `_compute_json_popover`)
- `stock_reference_ids`: `Many2many` (comodel `stock.reference`)
- `warehouse_id`: `Many2one` (comodel `stock.warehouse`, compute `_compute_warehouse_id`, store `True`)

## Method hints

- Detected methods: 20
- Action methods: `action_view_delivery`
- Compute methods: `_compute_delivery_status`, `_compute_effective_date`, `_compute_expected_date`, `_compute_json_popover`, `_compute_late_availability`, `_compute_picking_ids`, `_compute_warehouse_id`
- Onchange methods: `_onchange_partner_shipping_id`

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
title sale.order - Direct Relations
class "sale.order" as sale_order
class "account.incoterms" as account_incoterms
class "stock.picking" as stock_picking
class "stock.reference" as stock_reference
class "stock.warehouse" as stock_warehouse
sale_order --> account_incoterms : incoterm
sale_order --> stock_warehouse : warehouse_id
sale_order --|> stock_picking : picking_ids
sale_order .. stock_reference : stock_reference_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/sale_stock/Models]]

<!-- GENERATED:MODEL -->
