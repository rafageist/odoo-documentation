<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Stock - Maintenance

- Scope: Community Addons
- Source: odoo/addons/stock_maintenance
- Dependencies: [[docs/Community Addons/stock/stock|stock]], [[docs/Community Addons/maintenance/maintenance|maintenance]]

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
!include ../../../templates/DiagramStyles.puml
title Stock - Maintenance - Models and Relations
class MaintenanceEquipment
class StockLocation
class "stock.location" as stock_location
MaintenanceEquipment --> stock_location : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




