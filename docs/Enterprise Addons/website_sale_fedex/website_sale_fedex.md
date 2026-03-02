
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# FEDEX Locations for Website Delivery

- Scope: Enterprise Addons
- Source: enterprise/website_sale_fedex
- Dependencies: [[docs/Enterprise Addons/delivery_fedex/delivery_fedex|delivery_fedex]], [[docs/Community Addons/website_sale/website_sale|website_sale]]

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
!include ../../../templates/DiagramStyles.puml
title FEDEX Locations for Website Delivery - Models and Relations
class DeliveryCarrier
class "uom.uom" as uom_uom
DeliveryCarrier --> uom_uom : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

