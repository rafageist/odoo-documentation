<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Italy - Stock DDT

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_it_stock_ddt
- Dependencies: [[Odoo 19/Community Addons/l10n_it_edi/l10n_it_edi|l10n_it_edi]], [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 19/Community Addons/stock_account/stock_account|stock_account]]

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `StockPicking`
- `StockPickingType`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Italy - Stock DDT - Models and Relations
class AccountMove
class StockPicking
class StockPickingType
class "stock.picking" as stock_picking
AccountMove .. stock_picking : many2many
class "ir.sequence" as ir_sequence
StockPickingType --> ir_sequence : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


