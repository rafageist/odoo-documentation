<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Stock - Maintenance

- Version: v19
- Category: community
- Source: odoo19/addons/stock_maintenance
- Dependencies: [[Odoo 19/Community Addons/stock/stock|stock]], [[Odoo 19/Community Addons/maintenance/maintenance|maintenance]]

## Summary

See lots used in maintenance

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `MaintenanceEquipment`
- `StockLocation`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Stock - Maintenance - Models and Relations
class MaintenanceEquipment
class StockLocation
class "stock.location" as stock_location
MaintenanceEquipment --> stock_location : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
