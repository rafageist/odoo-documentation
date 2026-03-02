<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Fedex Shipping (Legacy)

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/delivery_fedex
- Dependencies: [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 19/Community Addons/mail/mail|mail]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DeliveryCarrier`
- `StockPackageType`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Fedex Shipping (Legacy) - Models and Relations
class DeliveryCarrier
class StockPackageType
class "stock.package.type" as stock_package_type
DeliveryCarrier --> stock_package_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


