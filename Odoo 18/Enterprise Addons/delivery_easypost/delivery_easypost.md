<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Easypost Shipping

- Version: v18
- Category: enterprise
- Source: enterprise18/delivery_easypost
- Dependencies: [[Odoo 18/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 18/Community Addons/mail/mail|mail]]
## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `DeliverCarrier`
- `easypost.service`
- `PackageType`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Easypost Shipping - Models and Relations
class DeliverCarrier
class "easypost.service" as easypost_service
class PackageType
class StockPicking
class "stock.package.type" as stock_package_type
DeliverCarrier --> stock_package_type : many2one
DeliverCarrier --> easypost_service : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
