<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# POS - Sales

- Scope: Community Addons
- Source: odoo/addons/pos_sale
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Community Addons/sale_management/sale_management|sale_management]]

## Summary

Link module between Point of Sale and Sales

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `CrmTeam`
- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `PosSession`
- `ProductTemplate`
- `ResPartner`
- `sale.order`
- `sale.order.line`
- `StockPicking`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title POS - Sales - Models and Relations
class AccountMove
class CrmTeam
class PosConfig
class PosOrder
class PosOrderLine
class PosSession
class ProductTemplate
class ResPartner
class "sale.order" as sale_order
class "sale.order.line" as sale_order_line
class StockPicking
class "pos.config" as pos_config
CrmTeam --|> pos_config : one2many
class "crm.team" as crm_team
PosConfig --> crm_team : many2one
class "product.product" as product_product
PosConfig --> product_product : many2one
PosOrder --> crm_team : many2one
PosOrderLine --> sale_order : many2one
PosOrderLine --> sale_order_line : many2one
PosSession --> crm_team : many2one
class "pos.order.line" as pos_order_line
sale_order --|> pos_order_line : one2many
sale_order_line --|> pos_order_line : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





