<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# POS Pricer

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_pricer
- Dependencies: [[Odoo 18/Community Addons/product/product|product]], [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Display and change your products information on electronic Pricer tags

## XML Artifacts (detected)

- Views: 5
- Actions: 2
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountTax`
- `PricerPosConfig`
- `pricer.store`
- `pricer.tag`
- `PricerProductProduct`
- `PricerProductSupplierInfo`
- `PricerProductTemplate`
- `PricerResPartner`
- `PricerStockMove`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title POS Pricer - Models and Relations
class AccountTax
class PricerPosConfig
class "pricer.store" as pricer_store
class "pricer.tag" as pricer_tag
class PricerProductProduct
class PricerProductSupplierInfo
class PricerProductTemplate
class PricerResPartner
class PricerStockMove
class "product.product" as product_product
pricer_store --|> product_product : one2many
pricer_store --|> pricer_tag : one2many
pricer_tag --> product_product : many2one
pricer_tag --> pricer_store : many2one
PricerProductProduct --> pricer_store : many2one
PricerProductProduct --|> pricer_tag : one2many
class "product.pricelist" as product_pricelist
PricerProductProduct --> product_pricelist : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
