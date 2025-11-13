<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Sendcloud Shipping

- Version: v18
- Category: enterprise
- Source: enterprise18/delivery_sendcloud
- Dependencies: [[Odoo 18/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 18/Community Addons/mail/mail|mail]]
## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `DeliveryCarrier`
- `sendcloud.shipping.product`
- `PackageType`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sendcloud Shipping - Models and Relations
class DeliveryCarrier
class "sendcloud.shipping.product" as sendcloud_shipping_product
class PackageType
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
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
