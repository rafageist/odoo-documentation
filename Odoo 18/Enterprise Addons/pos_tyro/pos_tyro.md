<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# POS Tyro

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_tyro
- Dependencies: [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
