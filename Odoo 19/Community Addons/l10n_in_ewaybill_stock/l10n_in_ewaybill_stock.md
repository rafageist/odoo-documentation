<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Indian - E-waybill Stock

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_in_ewaybill_stock
- Dependencies: [[Odoo 19/Community Addons/l10n_in_stock/l10n_in_stock|l10n_in_stock]], [[Odoo 19/Community Addons/l10n_in_ewaybill/l10n_in_ewaybill|l10n_in_ewaybill]]
## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `L10nInEwaybill`
- `StockMove`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indian - E-waybill Stock - Models and Relations
class L10nInEwaybill
class StockMove
class StockPicking
class "stock.picking" as stock_picking
L10nInEwaybill --> stock_picking : many2one
class "account.fiscal.position" as account_fiscal_position
L10nInEwaybill --> account_fiscal_position : many2one
class "account.tax" as account_tax
StockMove .. account_tax : many2many
class "l10n.in.ewaybill" as l10n_in_ewaybill
StockPicking --|> l10n_in_ewaybill : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
