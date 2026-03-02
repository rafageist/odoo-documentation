<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Point of Sale - UrbanPiper

- Scope: Enterprise Addons
- Source: enterprise/pos_urban_piper
- Dependencies: [[docs/Enterprise Addons/pos_enterprise/pos_enterprise|pos_enterprise]], [[docs/Community Addons/pos_discount/pos_discount|pos_discount]]

## XML Artifacts (detected)

- Views: 7
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 7

## Detected Models

- `IrConfig_Parameter`
- `PosCategory`
- `PosConfig`
- `pos.delivery.provider`
- `PosOrder`
- `PosPayment`
- `PosPaymentMethod`
- `PosPrepDisplay`
- `PosPrepOrder`
- `PosSession`
- `ProductTemplate`
- `ProductPricelist`
- `product.urban.piper.status`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Point of Sale - UrbanPiper - Models and Relations
class IrConfig_Parameter
class PosCategory
class PosConfig
class "pos.delivery.provider" as pos_delivery_provider
class PosOrder
class PosPayment
class PosPaymentMethod
class PosPrepDisplay
class PosPrepOrder
class PosSession
class ProductTemplate
class ProductPricelist
class "product.urban.piper.status" as product_urban_piper_status
class ResCompany
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
ProductTemplate .. pos_delivery_provider : many2many
ProductTemplate --|> product_urban_piper_status : one2many
product_urban_piper_status --> pos_config : many2one
class "product.template" as product_template
product_urban_piper_status --> product_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




