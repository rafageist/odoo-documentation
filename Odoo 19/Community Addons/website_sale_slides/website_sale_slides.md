<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Sell Courses

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/website_sale_slides
- Dependencies: [[Odoo 19/Community Addons/website_slides/website_slides|website_slides]], [[Odoo 19/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Sell your courses online

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProductProduct`
- `ProductTemplate`
- `SaleOrder`
- `SaleOrderLine`
- `SlideChannel`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sell Courses - Models and Relations
class ProductProduct
class ProductTemplate
class SaleOrder
class SaleOrderLine
class SlideChannel
class "slide.channel" as slide_channel
ProductProduct --|> slide_channel : one2many
class "product.product" as product_product
SlideChannel --> product_product : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

