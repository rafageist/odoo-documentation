<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Italy - Stock DDT

- Scope: Community Addons
- Source: odoo/addons/l10n_it_stock_ddt
- Dependencies: [[docs/Community Addons/l10n_it_edi/l10n_it_edi|l10n_it_edi]], [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[docs/Community Addons/stock_account/stock_account|stock_account]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





