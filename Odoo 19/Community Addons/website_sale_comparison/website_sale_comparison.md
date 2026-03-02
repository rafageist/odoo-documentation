<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Product Comparison

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/website_sale_comparison
- Dependencies: [[Odoo 19/Community Addons/website_sale/website_sale|website_sale]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

