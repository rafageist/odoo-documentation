<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# POS Tyro

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/pos_tyro
- Dependencies: [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

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
!include ../../../Templates/DiagramStyles.puml
title POS Tyro - Models and Relations
class PosConfig
class PosPaymentMethod
class "product.product" as product_product
PosPaymentMethod --> product_product : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

