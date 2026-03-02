
<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Click & Collect

- Scope: Community Addons
- Source: odoo/addons/website_sale_collect
- Dependencies: [[docs/Community Addons/base_geolocalize/base_geolocalize|base_geolocalize]], [[docs/Community Addons/payment_custom/payment_custom|payment_custom]], [[docs/Community Addons/website_sale_stock/website_sale_stock|website_sale_stock]]

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DeliveryCarrier`
- `PaymentProvider`
- `PaymentTransaction`
- `ProductTemplate`
- `SaleOrder`
- `StockWarehouse`
- `Website`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Click & Collect - Models and Relations
class DeliveryCarrier
class PaymentProvider
class PaymentTransaction
class ProductTemplate
class SaleOrder
class StockWarehouse
class Website
class "stock.warehouse" as stock_warehouse
DeliveryCarrier .. stock_warehouse : many2many
class "resource.calendar" as resource_calendar
StockWarehouse --> resource_calendar : many2one
class "delivery.carrier" as delivery_carrier
Website --> delivery_carrier : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

