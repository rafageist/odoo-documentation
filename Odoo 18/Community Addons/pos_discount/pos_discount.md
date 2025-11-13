<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Point of Sale Discounts

- Version: v18
- Category: community
- Source: odoo/addons/pos_discount
- Dependencies: [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Simple Discounts in the Point of Sale 

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PosConfig`
- `ProductProduct`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Point of Sale Discounts - Models and Relations
class PosConfig
class ProductProduct
class "product.product" as product_product
PosConfig --> product_product : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
