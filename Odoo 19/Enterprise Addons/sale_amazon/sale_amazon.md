<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Amazon Connector

- Version: v19
- Category: enterprise
- Source: enterprise19/sale_amazon
- Dependencies: [[Odoo 19/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

## Summary

Import Amazon orders and sync deliveries

## XML Artifacts (detected)

- Views: 17
- Actions: 4
- Menus: 3
- Rules (ir.rule): 2
- Access CSV entries: 4

## Detected Models

- `amazon.account`
- `amazon.marketplace`
- `amazon.offer`
- `ProductProduct`
- `ProductTemplate`
- `ResPartner`
- `SaleOrder`
- `SaleOrderLine`
- `StockMove`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Amazon Connector - Models and Relations
class "amazon.account" as amazon_account
class "amazon.marketplace" as amazon_marketplace
class "amazon.offer" as amazon_offer
class ProductProduct
class ProductTemplate
class ResPartner
class SaleOrder
class SaleOrderLine
class StockMove
class StockPicking
class "res.company" as res_company
amazon_account --> res_company : many2one
amazon_account --|> amazon_offer : one2many
amazon_account --> amazon_marketplace : many2one
amazon_account .. amazon_marketplace : many2many
amazon_account .. amazon_marketplace : many2many
class "product.product" as product_product
amazon_account .. product_product : many2many
class "res.users" as res_users
amazon_account --> res_users : many2one
class "crm.team" as crm_team
amazon_account --> crm_team : many2one
class "stock.location" as stock_location
amazon_account --> stock_location : many2one
amazon_offer --> amazon_account : many2one
amazon_offer --> amazon_marketplace : many2one
amazon_offer --> product_product : many2one
SaleOrderLine --> amazon_offer : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
