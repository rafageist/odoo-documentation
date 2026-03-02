<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Maintenance - HR

- Scope: Community Addons
- Source: odoo/addons/hr_maintenance
- Dependencies: [[docs/Community Addons/hr/hr|hr]], [[docs/Community Addons/maintenance/maintenance|maintenance]]

## Summary

Equipment, Assets, Internal Hardware, Allocation Tracking

## XML Artifacts (detected)

- Views: 11
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `MaintenanceEquipment`
- `MaintenanceRequest`
- `HrEmployee`
- `HrEmployeePublic`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Maintenance - HR - Models and Relations
class MaintenanceEquipment
class MaintenanceRequest
class HrEmployee
class HrEmployeePublic
class "hr.employee" as hr_employee
MaintenanceEquipment --> hr_employee : many2one
class "hr.department" as hr_department
MaintenanceEquipment --> hr_department : many2one
MaintenanceRequest --> hr_employee : many2one
class "maintenance.equipment" as maintenance_equipment
HrEmployee --|> maintenance_equipment : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





