---
tags: [v18, community, inventory, stock, analysis]
status: draft
---

# Stock Module (`stock`)

> **Summary:** Core inventory module providing pickings, stock moves, locations, quants, routes, and procurement triggers. Refer to `[[Odoo 18/Core/Processes/Inventory]]` for the overarching flow; this note focuses on module-specific configuration and extensions.

## 1. Principal models

| Model | File | Responsibilities |
|-------|------|------------------|
| `stock.picking` | `addons/stock/models/stock_picking.py` | High-level transfer document; groups stock moves by operation type. |
| `stock.move` | `addons/stock/models/stock_move.py` | Unit of stock movement; manages reservations, procurement, and valuation. |
| `stock.move.line` | `addons/stock/models/stock_move_line.py` | Operational detail (lot, package, owner) enabling barcode/warehouse scans. |
| `stock.quant` | `addons/stock/models/stock_quant.py` | Onhand/reserved quantities per location/lot. |
| `stock.location` | `addons/stock/models/stock_location.py` | Warehouse structure and rules. |
| `stock.rule`, `procurement.group` | `addons/stock/models/procurement.py` | Defines push/pull routes and demand fulfilment logic. |

## 2. Picking states

| State | Meaning |
|-------|---------|
| `draft` | Draft transfer. |
| `waiting`, `confirmed` | Waiting for availability or ready after reservation. |
| `assigned` | Components reserved & ready. |
| `in_progress` | Pick in progress (internal moves). |
| `done` | Completed transfer. |
| `cancel` | Cancelled transfer. |

## 3. Procurement routes
- Default warehouse routes: one-step, two-step, three-step transfers (picking types).
- Custom routes on products/locations. Methods: `push`, `pull`, `buy`, `manufacture`, `make_to_order`.
- Scheduler (`stock.scheduler.compute`) executes procurements, generating flows (purchase, manufacturing, transfer).

## 4. Reservation & availability
- `_action_assign` reserves quants; partial reservations create backorders.
- `stock.move` lazily creates move lines, allowing manual adjustments.
- Negative stock allowed per location (`allow_negative_stock`).

## 5. Integration points
- **Sales:** `sale_stock` auto-creates delivery pickings, updates delivered quantities. See `[[Odoo 18/Core/Processes/Sales]]`.
- **Purchases:** `purchase_stock` generates incoming receipts.
- **Accounting:** `stock_account` ensures valuation entries.
- **Manufacturing:** `mrp` relies on stock routes for component consumption/production.

## 6. Configuration
- Warehouse setup: `stock.warehouse` define steps; `res.config.settings` toggles multi-warehouse, routes, lots.
- Delivery lead times (customer/vendor) configured on product/partner.
- Scrap management via `stock.scrap`; inventory adjustments via `stock.quant`.

## 7. To-do (Issue #20)
- [ ] Include examples of custom routes (push/pull) diagram.
- [ ] Add details on scheduler configuration (reordering rules).
- [ ] Link to barcode/wave picking modules when documented.

## Navigation
- **Parent:** [[Odoo 18/Community Addons/Inventory/Inventory]]
