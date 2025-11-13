<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Shiprocket Shipping

- Version: v18
- Category: enterprise
- Source: enterprise18/delivery_shiprocket
- Dependencies: [[Odoo 18/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 18/Community Addons/mail/mail|mail]]
## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 8

## Detected Models

- `DeliverCarrier`
- `shiprocket.channel`
- `shiprocket.courier`
- `PackageType`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Shiprocket Shipping - Models and Relations
class DeliverCarrier
class "shiprocket.channel" as shiprocket_channel
class "shiprocket.courier" as shiprocket_courier
class PackageType
class StockPicking
DeliverCarrier --> shiprocket_channel : many2one
DeliverCarrier .. shiprocket_courier : many2many
class "stock.package.type" as stock_package_type
DeliverCarrier --> stock_package_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
