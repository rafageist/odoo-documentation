<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# POS Tyro

- Scope: Enterprise Addons
- Source: enterprise/pos_tyro
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Integrate your POS with a Tyro payment terminal (AU)

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PosConfig`
- `PosPaymentMethod`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title POS Tyro - Models and Relations
class PosConfig
class PosPaymentMethod
class "product.product" as product_product
PosPaymentMethod --> product_product : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



