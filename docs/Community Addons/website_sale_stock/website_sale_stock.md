<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Product Availability

- Scope: Community Addons
- Source: odoo/addons/website_sale_stock
- Dependencies: [[docs/Community Addons/website_sale/website_sale|website_sale]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]], [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



