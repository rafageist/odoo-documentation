<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Product Availability

- Version: v18
- Category: community
- Source: odoo/addons/website_sale_stock
- Dependencies: [[Odoo 18/Community Addons/website_sale/website_sale|website_sale]], [[Odoo 18/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 18/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

## Summary

Manage product inventory & availability

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProductCombo`
- `ProductProduct`
- `ProductTemplate`
- `SaleOrder`
- `SaleOrderLine`
- `StockPicking`
- `Website`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Product Availability - Models and Relations
class ProductCombo
class ProductProduct
class ProductTemplate
class SaleOrder
class SaleOrderLine
class StockPicking
class Website
class "res.partner" as res_partner
ProductProduct .. res_partner : many2many
class website
StockPicking --> website : many2one
class "stock.warehouse" as stock_warehouse
Website --> stock_warehouse : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
