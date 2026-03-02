<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Product Comparison

- Scope: Community Addons
- Source: odoo/addons/website_sale_comparison
- Dependencies: [[docs/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Allow shoppers to compare products based on their attributes

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `ProductAttribute`
- `product.attribute.category`
- `ProductProduct`
- `ProductTemplateAttributeLine`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Product Comparison - Models and Relations
class ProductAttribute
class "product.attribute.category" as product_attribute_category
class ProductProduct
class ProductTemplateAttributeLine
ProductAttribute --> product_attribute_category : many2one
class "product.attribute" as product_attribute
product_attribute_category --|> product_attribute : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



