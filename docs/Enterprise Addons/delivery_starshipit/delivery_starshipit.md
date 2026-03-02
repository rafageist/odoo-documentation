<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Starshipit Shipping

- Scope: Enterprise Addons
- Source: enterprise/delivery_starshipit
- Dependencies: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `DeliveryCarrier`
- `StockPackageType`
- `StockPicking`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



