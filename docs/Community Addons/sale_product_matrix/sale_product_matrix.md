<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sale Matrix

- Scope: Community Addons
- Source: odoo/addons/sale_product_matrix
- Dependencies: [[docs/Community Addons/sale/sale|sale]], [[docs/Community Addons/product_matrix/product_matrix|product_matrix]]

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
!include ../../../templates/DiagramStyles.puml
title Sale Matrix - Models and Relations
class ProductTemplate
class SaleOrder
class SaleOrderLine
class "product.template" as product_template
SaleOrder --> product_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




