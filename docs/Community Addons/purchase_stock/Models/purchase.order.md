<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# purchase.order

- Module: [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/purchase_order.py`
- Python classes: `PurchaseOrder`

## Field footprint

- Detected fields: 11
- Field types: `Boolean` x 1, `Char` x 1, `Datetime` x 1, `Float` x 1, `Integer` x 1, `Many2many` x 2, `Many2one` x 2, `Selection` x 2
- Relation fields: 4

## Sample fields

- `default_location_dest_id_usage`: `Selection` (related `picking_type_id.default_location_dest_id.usage`)
- `dest_address_id`: `Many2one` (comodel `res.partner`, compute `_compute_dest_address_id`, store `True`)
- `effective_date`: `Datetime` (comodel `Arrival`, compute `_compute_effective_date`, store `True`)
- `incoming_picking_count`: `Integer` (comodel `Incoming Shipment count`, compute `_compute_incoming_picking_count`)
- `incoterm_location`: `Char`
- `is_shipped`: `Boolean` (compute `_compute_is_shipped`)
- `on_time_rate`: `Float` (related `partner_id.on_time_rate`)
- `picking_ids`: `Many2many` (comodel `stock.picking`, compute `_compute_picking_ids`, store `True`)
- `picking_type_id`: `Many2one` (comodel `stock.picking.type`)
- `receipt_status`: `Selection` (compute `_compute_receipt_status`, store `True`)
- `reference_ids`: `Many2many` (comodel `stock.reference`)

## Method hints

- Detected methods: 33
- Action methods: `action_add_from_catalog`, `action_purchase_order_suggest`, `action_view_picking`
- Compute methods: `_compute_dest_address_id`, `_compute_effective_date`, `_compute_incoming_picking_count`, `_compute_is_shipped`, `_compute_picking_ids`, `_compute_receipt_status`
- Onchange methods: `_onchange_company_id`

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
title purchase.order - Direct Relations
class "purchase.order" as purchase_order
class "res.partner" as res_partner
class "stock.picking" as stock_picking
class "stock.picking.type" as stock_picking_type
class "stock.reference" as stock_reference
purchase_order .. stock_picking : picking_ids
purchase_order --> res_partner : dest_address_id
purchase_order --> stock_picking_type : picking_type_id
purchase_order .. stock_reference : reference_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/purchase_stock/Models]]

<!-- GENERATED:MODEL -->
