<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# FEDEX Locations for Website Delivery

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/website_sale_fedex
- Dependencies: [[Odoo 19/Enterprise Addons/delivery_fedex/delivery_fedex|delivery_fedex]], [[Odoo 19/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Allows website customers to choose delivery pick-up points

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
title FEDEX Locations for Website Delivery - Models and Relations
class DeliveryCarrier
class "uom.uom" as uom_uom
DeliveryCarrier --> uom_uom : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

