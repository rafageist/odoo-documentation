<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Click & Collect

- Version: v18
- Category: community
- Source: odoo/addons/website_sale_collect
- Dependencies: [[Odoo 18/Community Addons/base_geolocalize/base_geolocalize|base_geolocalize]], [[Odoo 18/Community Addons/payment_custom/payment_custom|payment_custom]], [[Odoo 18/Community Addons/website_sale_stock/website_sale_stock|website_sale_stock]]
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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
