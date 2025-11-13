<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Odoo Mexico Localization for Stock/Landing

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_mx_edi_landing
- Dependencies: [[Odoo 19/Community Addons/stock_landed_costs/stock_landed_costs|stock_landed_costs]], [[Odoo 19/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 19/Enterprise Addons/l10n_mx_edi_extended/l10n_mx_edi_extended|l10n_mx_edi_extended]]

## Summary

Generate Electronic Invoice with custom numbers

## XML Artifacts (detected)

- Views: 7
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `ProductTemplate`
- `SaleOrderLine`
- `StockLandedCost`
- `StockLot`
- `StockMoveLine`
- `StockQuant`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Odoo Mexico Localization for Stock/Landing - Models and Relations
class AccountMove
class AccountMoveLine
class ProductTemplate
class SaleOrderLine
class StockLandedCost
class StockLot
class StockMoveLine
class StockQuant
class "stock.landed.cost" as stock_landed_cost
StockLot --> stock_landed_cost : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
