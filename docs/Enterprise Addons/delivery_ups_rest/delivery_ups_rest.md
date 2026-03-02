<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# UPS Shipping

- Scope: Enterprise Addons
- Source: enterprise/delivery_ups_rest
- Dependencies: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[docs/Community Addons/mail/mail|mail]]

## Summary

Send your shippings through UPS and track them online. This new version of the UPS connector is compatiblewith the newest version of the UPS REST APIs available at https://developer.ups.com/

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DeliveryCarrier`
- `PaymentProvider`
- `StockPackageType`
- `ResPartner`
- `SaleOrder`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title UPS Shipping - Models and Relations
class DeliveryCarrier
class PaymentProvider
class StockPackageType
class ResPartner
class SaleOrder
class "stock.package.type" as stock_package_type
DeliveryCarrier --> stock_package_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



