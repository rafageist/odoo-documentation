<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Rental Stock Management

- Version: v18
- Category: enterprise
- Source: enterprise18/sale_stock_renting
- Dependencies: [[Odoo 18/Enterprise Addons/sale_renting/sale_renting|sale_renting]], [[Odoo 18/Community Addons/sale_stock/sale_stock|sale_stock]]

## Summary

Allows use of stock application to manage rentals inventory

## XML Artifacts (detected)

- Views: 10
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `ProductProduct`
- `ProductTemplate`
- `ResCompany`
- `SaleOrder`
- `RentalOrderLine`
- `ProductionLot`
- `StockMove`
- `StockWarehouseOrderpoint`
- `StockWarehouse`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Rental Stock Management - Models and Relations
class AccountMove
class AccountMoveLine
class ProductProduct
class ProductTemplate
class ResCompany
class SaleOrder
class RentalOrderLine
class ProductionLot
class StockMove
class StockWarehouseOrderpoint
class StockWarehouse
class "stock.location" as stock_location
ResCompany --> stock_location : many2one
class "stock.lot" as stock_lot
RentalOrderLine .. stock_lot : many2many
RentalOrderLine .. stock_lot : many2many
RentalOrderLine .. stock_lot : many2many
RentalOrderLine .. stock_lot : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
