<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# United States Postal Service (USPS) Shipping (Legacy)

- Scope: Enterprise Addons
- Source: enterprise/delivery_usps
- Dependencies: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[docs/Community Addons/mail/mail|mail]]

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
!include ../../../templates/DiagramStyles.puml
title United States Postal Service (USPS) Shipping (Legacy) - Models and Relations
class DeliveryCarrier
class "res.partner" as res_partner
DeliveryCarrier --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



