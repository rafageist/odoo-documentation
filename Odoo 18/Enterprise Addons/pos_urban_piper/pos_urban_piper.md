<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Point of Sale - UrbanPiper

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_urban_piper
- Dependencies: [[Odoo 18/Enterprise Addons/pos_preparation_display/pos_preparation_display|pos_preparation_display]]
## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `IrConfigParameter`
- `PosConfig`
- `pos.delivery.provider`
- `PosOrder`
- `PosPayment`
- `PosPaymentMethod`
- `PosSession`
- `PosPreparationDisplayOrder`
- `ProductTemplate`
- `ProductPricelist`
- `product.urban.piper.status`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Point of Sale - UrbanPiper - Models and Relations
class IrConfigParameter
class PosConfig
class "pos.delivery.provider" as pos_delivery_provider
class PosOrder
class PosPayment
class PosPaymentMethod
class PosSession
class PosPreparationDisplayOrder
class ProductTemplate
class ProductPricelist
class "product.urban.piper.status" as product_urban_piper_status
class "product.pricelist" as product_pricelist
PosConfig --> product_pricelist : many2one
class "account.fiscal.position" as account_fiscal_position
PosConfig --> account_fiscal_position : many2one
class "pos.payment.method" as pos_payment_method
PosConfig .. pos_payment_method : many2many
PosConfig .. pos_delivery_provider : many2many
class "res.country" as res_country
pos_delivery_provider .. res_country : many2many
PosOrder --> pos_delivery_provider : many2one
PosPaymentMethod --> pos_delivery_provider : many2one
class "pos.config" as pos_config
ProductTemplate .. pos_config : many2many
ProductTemplate --|> product_urban_piper_status : one2many
product_urban_piper_status --> pos_config : many2one
class "product.template" as product_template
product_urban_piper_status --> product_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
