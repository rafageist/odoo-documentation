<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Barcode

- Version: v19
- Category: enterprise
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
