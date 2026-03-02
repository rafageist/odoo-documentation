<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Purchase Matrix

- Scope: Community Addons
- Source: odoo/addons/purchase_product_matrix
- Dependencies: [[docs/Community Addons/purchase/purchase|purchase]], [[docs/Community Addons/product_matrix/product_matrix|product_matrix]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





