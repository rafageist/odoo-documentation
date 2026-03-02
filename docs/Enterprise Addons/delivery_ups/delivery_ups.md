<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# UPS Shipping (Legacy)

- Scope: Enterprise Addons
- Source: enterprise/delivery_ups
- Dependencies: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[docs/Community Addons/mail/mail|mail]]

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DeliveryCarrier`
- `PaymentProvider`
- `ResPartner`
- `SaleOrder`
- `StockPackageType`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title UPS Shipping (Legacy) - Models and Relations
class DeliveryCarrier
class PaymentProvider
class ResPartner
class SaleOrder
class StockPackageType
class "stock.package.type" as stock_package_type
DeliveryCarrier --> stock_package_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



