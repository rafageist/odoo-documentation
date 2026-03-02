<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Barcode

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/stock_barcode
- Dependencies: [[Odoo 19/Community Addons/stock/stock|stock]], [[Odoo 19/Community Addons/web_tour/web_tour|web_tour]], [[Odoo 19/Enterprise Addons/web_mobile/web_mobile|web_mobile]]

## Summary

Use barcode scanners to process logistics operations

## XML Artifacts (detected)

- Views: 20
- Actions: 8
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `ProductProduct`
- `ProductUom`
- `ResPartner`
- `StockLocation`
- `StockLot`
- `StockMove`
- `StockMoveLine`
- `StockPackage`
- `StockPackageType`
- `StockPicking`
- `StockPickingType`
- `StockQuant`
- `stock.scrap`
- `StockWarehouse`
- `UomUom`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Barcode - Models and Relations
class ProductProduct
class ProductUom
class ResPartner
class StockLocation
class StockLot
class StockMove
class StockMoveLine
class StockPackage
class StockPackageType
class StockPicking
class StockPickingType
class StockQuant
class "stock.scrap" as stock_scrap
class StockWarehouse
class UomUom
class "stock.location" as stock_location
StockMoveLine --> stock_location : many2one
StockMoveLine --> stock_location : many2one
class "stock.quant" as stock_quant
StockMoveLine --|> stock_quant : one2many
class "uom.uom" as uom_uom
StockMoveLine --> uom_uom : many2one
class "stock.package" as stock_package
StockMoveLine --> stock_package : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

## Curated analysis

### Functional role
- `stock_barcode` is the mobile execution layer for warehouse work: receipts, transfers, packages, lots, scrap, and location scans are driven from fast scanner-oriented screens.
- It extends the community stock engine rather than replacing it, so the operational value comes from speed and device ergonomics on top of the same reservation logic.

### Operational footprint
- `controllers/stock_barcode.py` exposes the barcode endpoints, while the model extensions adapt stock pickings, move lines, packages, and EPC encoding to scanning flows.
- The frontend is asset-heavy and depends on `web_mobile`, so behavior in real handheld devices matters as much as server-side model logic.

### Evidence
- Source files: `enterprise19/stock_barcode/controllers/stock_barcode.py`, `enterprise19/stock_barcode/models/stock_picking.py`, `enterprise19/stock_barcode/models/stock_move_line.py`
- UI and device flows: `enterprise19/stock_barcode/views/stock_barcode_views.xml`, `enterprise19/stock_barcode/wizard/stock_backorder_confirmation.py`, `enterprise19/stock_barcode/static/src/**/*`
- Tests: `enterprise19/stock_barcode/tests/test_controller.py`, `enterprise19/stock_barcode/tests/test_barcode.py`, `enterprise19/stock_barcode/tests/test_barcode_client_action_picking.py`

### Related notes
- `[[Odoo 19/Community Addons/stock/stock|stock]]`
- `[[Odoo 19/Core/Processes/Inventory/Inventory]]`

### Rollout and migration concerns
- Scanner formats, GS1 rules, and package or lot requirements should be validated with the exact warehouse flows in use, not only with demo data.
- Mobile-device rollout needs operational testing on network coverage, camera scanners, and multi-company context because those conditions shape the real barcode experience.
- Odoo 18 comparison backlog was retired on 2026-03-02; keep this note focused on Odoo 19 behavior.


