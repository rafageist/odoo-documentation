<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Point of Sale Discounts

- Version: v19
- Category: community
- Source: odoo19/addons/pos_discount
- Dependencies: [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

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
- `ProductTemplate`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Point of Sale Discounts - Models and Relations
class PosConfig
class ProductTemplate
class "product.product" as product_product
PosConfig --> product_product : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
