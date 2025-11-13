<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# FEDEX Locations for Website Delivery

- Version: v18
- Category: enterprise
- Source: enterprise18/website_sale_fedex
- Dependencies: [[Odoo 18/Enterprise Addons/delivery_fedex/delivery_fedex|delivery_fedex]], [[Odoo 18/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Allows website customers to choose delivery pick-up points

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProviderFedex`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title FEDEX Locations for Website Delivery - Models and Relations
class ProviderFedex
class "uom.uom" as uom_uom
ProviderFedex --> uom_uom : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
