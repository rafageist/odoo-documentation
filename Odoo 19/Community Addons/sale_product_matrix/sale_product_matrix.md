<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Sale Matrix

- Version: v19
- Category: community
- Source: odoo19/addons/sale_product_matrix
- Dependencies: [[Odoo 19/Community Addons/sale/sale|sale]], [[Odoo 19/Community Addons/product_matrix/product_matrix|product_matrix]]

## Summary

Add variants to Sales Order through a grid entry.

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProductTemplate`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sale Matrix - Models and Relations
class ProductTemplate
class SaleOrder
class SaleOrderLine
class "product.template" as product_template
SaleOrder --> product_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
