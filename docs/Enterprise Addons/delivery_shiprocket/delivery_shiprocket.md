<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Shiprocket Shipping

- Scope: Enterprise Addons
- Source: enterprise/delivery_shiprocket
- Dependencies: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[docs/Community Addons/mail/mail|mail]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



