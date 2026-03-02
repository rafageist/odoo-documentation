<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Envia Shipping

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/delivery_envia
- Dependencies: [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 19/Community Addons/base_address_extended/base_address_extended|base_address_extended]], [[Odoo 19/Community Addons/phone_validation/phone_validation|phone_validation]]

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `DeliverCarrier`
- `StockPackageType`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Envia Shipping - Models and Relations
class DeliverCarrier
class StockPackageType
class "stock.package.type" as stock_package_type
DeliverCarrier --> stock_package_type : many2one
class "res.currency" as res_currency
DeliverCarrier --> res_currency : many2one
class "res.country" as res_country
DeliverCarrier --> res_country : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

