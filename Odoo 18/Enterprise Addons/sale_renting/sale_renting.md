<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Rental

- Version: v18
- Category: enterprise
- Source: enterprise18/sale_renting
- Dependencies: [[Odoo 18/Community Addons/sale/sale|sale]]

## Summary

Manage rental contracts, deliveries and returns

## XML Artifacts (detected)

- Views: 26
- Actions: 25
- Menus: 13
- Rules (ir.rule): 2
- Access CSV entries: 13

## Detected Models

- `Pricelist`
- `product.pricing`
- `ProductProduct`
- `ProductTemplate`
- `ResCompany`
- `SaleOrder`
- `SaleOrderLine`
- `sale.temporal.recurrence`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Rental - Models and Relations
class Pricelist
class "product.pricing" as product_pricing
class ProductProduct
class ProductTemplate
class ResCompany
class SaleOrder
class SaleOrderLine
class "sale.temporal.recurrence" as sale_temporal_recurrence
Pricelist --|> product_pricing : one2many
product_pricing --> sale_temporal_recurrence : many2one
class "res.currency" as res_currency
product_pricing --> res_currency : many2one
class "product.template" as product_template
product_pricing --> product_template : many2one
class "product.product" as product_product
product_pricing .. product_product : many2many
class "product.pricelist" as product_pricelist
product_pricing --> product_pricelist : many2one
ProductTemplate --|> product_pricing : one2many
ResCompany --> product_product : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
