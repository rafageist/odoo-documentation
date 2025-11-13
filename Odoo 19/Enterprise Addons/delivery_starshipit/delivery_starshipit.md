<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Starshipit Shipping

- Version: v19
- Category: enterprise
- Source: enterprise19/delivery_starshipit
- Dependencies: [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]]
## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `DeliveryCarrier`
- `StockPackageType`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Starshipit Shipping - Models and Relations
class DeliveryCarrier
class StockPackageType
class StockPicking
class "stock.package.type" as stock_package_type
DeliveryCarrier --> stock_package_type : many2one
class "res.partner" as res_partner
DeliveryCarrier --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
