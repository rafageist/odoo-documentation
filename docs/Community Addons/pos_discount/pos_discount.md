<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Point of Sale Discounts

- Scope: Community Addons
- Source: odoo/addons/pos_discount
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

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
!include ../../../templates/DiagramStyles.puml
title Point of Sale Discounts - Models and Relations
class PosConfig
class ProductTemplate
class "product.product" as product_product
PosConfig --> product_product : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





