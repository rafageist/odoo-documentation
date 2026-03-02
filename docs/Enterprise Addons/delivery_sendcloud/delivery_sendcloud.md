<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sendcloud Shipping

- Scope: Enterprise Addons
- Source: enterprise/delivery_sendcloud
- Dependencies: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[docs/Community Addons/mail/mail|mail]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



