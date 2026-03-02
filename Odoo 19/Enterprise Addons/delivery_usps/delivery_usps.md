<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# United States Postal Service (USPS) Shipping (Legacy)

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/delivery_usps
- Dependencies: [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 19/Community Addons/mail/mail|mail]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DeliveryCarrier`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title United States Postal Service (USPS) Shipping (Legacy) - Models and Relations
class DeliveryCarrier
class "res.partner" as res_partner
DeliveryCarrier --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

