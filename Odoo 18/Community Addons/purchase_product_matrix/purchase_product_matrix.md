<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Purchase Matrix

- Version: v18
- Category: community
- Source: odoo/addons/purchase_product_matrix
- Dependencies: [[Odoo 18/Community Addons/purchase/purchase|purchase]], [[Odoo 18/Community Addons/product_matrix/product_matrix|product_matrix]]

## Summary

Add variants to your purchase orders through an Order Grid Entry.

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PurchaseOrder`
- `PurchaseOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Purchase Matrix - Models and Relations
class PurchaseOrder
class PurchaseOrderLine
class "product.template" as product_template
PurchaseOrder --> product_template : many2one
PurchaseOrderLine --> product_template : many2one
class "product.template.attribute.value" as product_template_attribute_value
PurchaseOrderLine .. product_template_attribute_value : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
