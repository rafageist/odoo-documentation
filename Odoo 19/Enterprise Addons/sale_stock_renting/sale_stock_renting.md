<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Rental Stock Management

- Version: v19
- Category: enterprise
- Source: enterprise19/sale_stock_renting
- Dependencies: [[Odoo 19/Enterprise Addons/sale_renting/sale_renting|sale_renting]], [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]]

## Summary

Allows use of stock application to manage rentals inventory

## XML Artifacts (detected)

- Views: 12
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
- `SaleOrderLine`
- `StockLot`
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
class SaleOrderLine
class StockLot
class StockMove
class StockWarehouseOrderpoint
class StockWarehouse
class "stock.location" as stock_location
ResCompany --> stock_location : many2one
class "stock.lot" as stock_lot
SaleOrderLine .. stock_lot : many2many
SaleOrderLine .. stock_lot : many2many
SaleOrderLine .. stock_lot : many2many
SaleOrderLine .. stock_lot : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
