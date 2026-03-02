<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# PoS Pricer

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/pos_pricer
- Dependencies: [[Odoo 19/Community Addons/product/product|product]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Display and change your products information on electronic Pricer tags

## XML Artifacts (detected)

- Views: 5
- Actions: 2
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `PosConfig`
- `pricer.store`
- `pricer.tag`
- `ProductProduct`
- `ProductTemplate`
- `StockMove`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title PoS Pricer - Models and Relations
class PosConfig
class "pricer.store" as pricer_store
class "pricer.tag" as pricer_tag
class ProductProduct
class ProductTemplate
class StockMove
class "product.product" as product_product
pricer_store --|> product_product : one2many
pricer_store --|> pricer_tag : one2many
pricer_tag --> product_product : many2one
pricer_tag --> pricer_store : many2one
ProductProduct --> pricer_store : many2one
ProductProduct --|> pricer_tag : one2many
class "product.pricelist" as product_pricelist
ProductProduct --> product_pricelist : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

