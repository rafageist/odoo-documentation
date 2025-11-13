<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Members

- Version: v18
- Category: community
- Source: odoo/addons/membership
- Dependencies: [[Odoo 18/Community Addons/account/account|account]]
## XML Artifacts (detected)

- Views: 12
- Actions: 10
- Menus: 5
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `membership.membership_line`
- `Partner`
- `Product`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Members - Models and Relations
class AccountMove
class AccountMoveLine
class "membership.membership_line" as membership_membership_line
class Partner
class Product
class "res.partner" as res_partner
membership_membership_line --> res_partner : many2one
class "product.product" as product_product
membership_membership_line --> product_product : many2one
class "account.move.line" as account_move_line
membership_membership_line --> account_move_line : many2one
class "account.move" as account_move
membership_membership_line --> account_move : many2one
class "res.company" as res_company
membership_membership_line --> res_company : many2one
Partner --> res_partner : many2one
Partner --|> membership_membership_line : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
