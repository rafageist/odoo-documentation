<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Easypost Shipping

- Scope: Enterprise Addons
- Source: enterprise/delivery_easypost
- Dependencies: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[docs/Community Addons/mail/mail|mail]]

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `DeliveryCarrier`
- `easypost.service`
- `StockPackageType`
- `StockPicking`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Easypost Shipping - Models and Relations
class DeliveryCarrier
class "easypost.service" as easypost_service
class StockPackageType
class StockPicking
class "stock.package.type" as stock_package_type
DeliveryCarrier --> stock_package_type : many2one
DeliveryCarrier --> easypost_service : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



