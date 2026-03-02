<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sell Courses

- Scope: Community Addons
- Source: odoo/addons/website_sale_slides
- Dependencies: [[docs/Community Addons/website_slides/website_slides|website_slides]], [[docs/Community Addons/website_sale/website_sale|website_sale]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




