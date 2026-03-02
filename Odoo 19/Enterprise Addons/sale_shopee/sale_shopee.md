<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Shopee Connector

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/sale_shopee
- Dependencies: [[Odoo 19/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

## Summary

Import Shopee orders and sync deliveries

## XML Artifacts (detected)

- Views: 13
- Actions: 6
- Menus: 3
- Rules (ir.rule): 2
- Access CSV entries: 3

## Detected Models

- `ProductProduct`
- `ResPartner`
- `SaleOrder`
- `shopee.account`
- `shopee.item`
- `shopee.shop`
- `StockMove`
- `StockPicking`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Shopee Connector - Models and Relations
class ProductProduct
class ResPartner
class SaleOrder
class "shopee.account" as shopee_account
class "shopee.item" as shopee_item
class "shopee.shop" as shopee_shop
class StockMove
class StockPicking
SaleOrder --> shopee_shop : many2one
class "res.company" as res_company
shopee_account .. res_company : many2many
shopee_account --|> shopee_shop : one2many
shopee_item --> shopee_shop : many2one
class "product.product" as product_product
shopee_item --> product_product : many2one
shopee_shop --> shopee_account : many2one
shopee_shop --|> shopee_item : one2many
class "res.users" as res_users
shopee_shop --> res_users : many2one
class "crm.team" as crm_team
shopee_shop --> crm_team : many2one
shopee_shop --> res_company : many2one
class "stock.location" as stock_location
shopee_shop --> stock_location : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

