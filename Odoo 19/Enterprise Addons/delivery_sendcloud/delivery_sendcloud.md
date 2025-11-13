<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Sendcloud Shipping

- Version: v19
- Category: enterprise
- Source: enterprise19/delivery_sendcloud
- Dependencies: [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 19/Community Addons/mail/mail|mail]]
## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `DeliveryCarrier`
- `sendcloud.shipping.product`
- `StockPackageType`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sendcloud Shipping - Models and Relations
class DeliveryCarrier
class "sendcloud.shipping.product" as sendcloud_shipping_product
class StockPackageType
class StockPicking
class "res.country" as res_country
DeliveryCarrier --> res_country : many2one
class "stock.package.type" as stock_package_type
DeliveryCarrier --> stock_package_type : many2one
DeliveryCarrier --> sendcloud_shipping_product : many2one
DeliveryCarrier --> sendcloud_shipping_product : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
