<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# UPS Shipping

- Version: v18
- Category: enterprise
- Source: enterprise18/delivery_ups_rest
- Dependencies: [[Odoo 18/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 18/Community Addons/mail/mail|mail]]

## Summary

Send your shippings through UPS and track them online. This new version of the UPS connector is compatiblewith the newest version of the UPS REST APIs available at https://developer.ups.com/

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProviderUPS`
- `ProductPackaging`
- `ResPartner`
- `SaleOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title UPS Shipping - Models and Relations
class ProviderUPS
class ProductPackaging
class ResPartner
class SaleOrder
class "stock.package.type" as stock_package_type
ProviderUPS --> stock_package_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
