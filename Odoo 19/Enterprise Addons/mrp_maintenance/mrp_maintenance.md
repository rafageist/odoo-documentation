<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Maintenance - MRP

- Version: v19
- Category: enterprise
- Source: enterprise19/mrp_maintenance
- Dependencies: [[Odoo 19/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]], [[Odoo 19/Community Addons/stock_maintenance/stock_maintenance|stock_maintenance]]

## Summary

Schedule and manage maintenance on machine and tools.

## XML Artifacts (detected)

- Views: 11
- Actions: 3
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `MaintenanceStage`
- `mrp.workcenter`
- `MaintenanceEquipment`
- `MaintenanceRequest`
- `MrpProduction`
- `MrpWorkorder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Maintenance - MRP - Models and Relations
class MaintenanceStage
class "mrp.workcenter" as mrp_workcenter
class MaintenanceEquipment
class MaintenanceRequest
class MrpProduction
class MrpWorkorder
class "maintenance.equipment" as maintenance_equipment
mrp_workcenter --|> maintenance_equipment : one2many
class "maintenance.request" as maintenance_request
mrp_workcenter --|> maintenance_request : one2many
MaintenanceEquipment --> mrp_workcenter : many2one
class "mrp.production" as mrp_production
MaintenanceRequest --> mrp_production : many2one
class "mrp.workorder" as mrp_workorder
MaintenanceRequest --> mrp_workorder : many2one
MaintenanceRequest --> mrp_workcenter : many2one
class "resource.calendar.leaves" as resource_calendar_leaves
MaintenanceRequest .. resource_calendar_leaves : many2many
MrpProduction --|> maintenance_request : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
