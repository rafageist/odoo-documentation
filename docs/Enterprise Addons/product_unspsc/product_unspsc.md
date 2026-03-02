<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# UNSPSC product codes

- Scope: Enterprise Addons
- Source: enterprise/product_unspsc
- Dependencies: [[docs/Community Addons/account/account|account]]

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
!include ../../../templates/DiagramStyles.puml
title UNSPSC product codes - Models and Relations
class ProductTemplate
class UomUom
class "product.unspsc.code" as product_unspsc_code
ProductTemplate --> product_unspsc_code : many2one
UomUom --> product_unspsc_code : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



