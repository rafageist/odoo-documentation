<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Product Availability

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/website_sale_stock
- Dependencies: [[Odoo 19/Community Addons/website_sale/website_sale|website_sale]], [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

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
- `ProductFeed`
- `ProductProduct`
- `ProductRibbon`
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
class ProductFeed
class ProductProduct
class ProductRibbon
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

