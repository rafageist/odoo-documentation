<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Rental Stock Management

- Scope: Enterprise Addons
- Source: enterprise/sale_stock_renting
- Dependencies: [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]]

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
- `StockPicking`
- `StockWarehouse`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
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
class StockPicking
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




