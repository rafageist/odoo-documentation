<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Point of Sale Settle Due

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/pos_settle_due
- Dependencies: [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 19/Enterprise Addons/account_followup/account_followup|account_followup]]

## Summary

Settle partner's due in the POS UI.

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `ir.ui.view`
- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `PosSession`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Point of Sale Settle Due - Models and Relations
class AccountMove
class "ir.ui.view" as ir_ui_view
class PosConfig
class PosOrder
class PosOrderLine
class PosSession
class ResCompany
class ResPartner
class "pos.order.line" as pos_order_line
AccountMove --|> pos_order_line : one2many
class "product.product" as product_product
PosConfig --> product_product : many2one
PosConfig --> product_product : many2one
PosConfig --> product_product : many2one
PosOrder --|> pos_order_line : one2many
class "res.partner" as res_partner
PosOrder --> res_partner : many2one
class "pos.order" as pos_order
PosOrderLine --> pos_order : many2one
class "account.move" as account_move
PosOrderLine --> account_move : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

