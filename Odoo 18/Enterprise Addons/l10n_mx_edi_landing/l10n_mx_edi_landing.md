<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Odoo Mexico Localization for Stock/Landing

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_mx_edi_landing
- Dependencies: [[Odoo 18/Community Addons/stock_landed_costs/stock_landed_costs|stock_landed_costs]], [[Odoo 18/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 18/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 18/Enterprise Addons/l10n_mx_edi_extended/l10n_mx_edi_extended|l10n_mx_edi_extended]]

## Summary

Generate Electronic Invoice with custom numbers

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `StockLandedCost`
- `StockMove`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Odoo Mexico Localization for Stock/Landing - Models and Relations
class AccountMove
class StockLandedCost
class StockMove
class "stock.move" as stock_move
StockMove .. stock_move : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
