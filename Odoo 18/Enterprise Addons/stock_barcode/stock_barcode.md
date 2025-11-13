<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Barcode

- Version: v18
- Category: enterprise
- Source: enterprise18/stock_barcode
- Dependencies: [[Odoo 18/Community Addons/stock/stock|stock]], [[Odoo 18/Community Addons/web_tour/web_tour|web_tour]], [[Odoo 18/Enterprise Addons/web_mobile/web_mobile|web_mobile]]

## Summary

Use barcode scanners to process logistics operations

## XML Artifacts (detected)

- Views: 19
- Actions: 8
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `ProductPackaging`
- `Product`
- `Partner`
- `Location`
- `StockLot`
- `StockMove`
- `StockMoveLine`
- `PackageType`
- `StockPicking`
- `StockPickingType`
- `StockQuant`
- `QuantPackage`
- `stock.scrap`
- `StockWarehouse`
- `UoM`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Barcode - Models and Relations
class ProductPackaging
class Product
class Partner
class Location
class StockLot
class StockMove
class StockMoveLine
class PackageType
class StockPicking
class StockPickingType
class StockQuant
class QuantPackage
class "stock.scrap" as stock_scrap
class StockWarehouse
class UoM
class "stock.location" as stock_location
StockMoveLine --> stock_location : many2one
StockMoveLine --> stock_location : many2one
class "stock.quant" as stock_quant
StockMoveLine --|> stock_quant : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
