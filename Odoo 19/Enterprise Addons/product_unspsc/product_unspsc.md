<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# UNSPSC product codes

- Version: v19
- Category: enterprise
- Source: enterprise19/product_unspsc
- Dependencies: [[Odoo 19/Community Addons/account/account|account]]

## Summary

UNSPSC product codes

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `ProductTemplate`
- `UomUom`
- `product.unspsc.code`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title UNSPSC product codes - Models and Relations
class ProductTemplate
class UomUom
class "product.unspsc.code" as product_unspsc_code
ProductTemplate --> product_unspsc_code : many2one
UomUom --> product_unspsc_code : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
