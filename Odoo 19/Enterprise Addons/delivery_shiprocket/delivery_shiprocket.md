<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Shiprocket Shipping

- Version: v19
- Category: enterprise
- Source: enterprise19/delivery_shiprocket
- Dependencies: [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 19/Community Addons/mail/mail|mail]]
## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 8

## Detected Models

- `DeliveryCarrier`
- `PaymentProvider`
- `shiprocket.channel`
- `shiprocket.courier`
- `StockPackageType`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Shiprocket Shipping - Models and Relations
class DeliveryCarrier
class PaymentProvider
class "shiprocket.channel" as shiprocket_channel
class "shiprocket.courier" as shiprocket_courier
class StockPackageType
class StockPicking
DeliveryCarrier --> shiprocket_channel : many2one
DeliveryCarrier .. shiprocket_courier : many2many
class "stock.package.type" as stock_package_type
DeliveryCarrier --> stock_package_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
