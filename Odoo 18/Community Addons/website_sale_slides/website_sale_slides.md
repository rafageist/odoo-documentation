<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Sell Courses

- Version: v18
- Category: community
- Source: odoo/addons/website_sale_slides
- Dependencies: [[Odoo 18/Community Addons/website_slides/website_slides|website_slides]], [[Odoo 18/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Sell your courses online

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Product`
- `ProductTemplate`
- `SaleOrder`
- `Channel`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sell Courses - Models and Relations
class Product
class ProductTemplate
class SaleOrder
class Channel
class "slide.channel" as slide_channel
Product --|> slide_channel : one2many
class "product.product" as product_product
Channel --> product_product : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
