<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Maintenance - HR

- Version: v18
- Category: community
- Source: odoo/addons/hr_maintenance
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]], [[Odoo 18/Community Addons/maintenance/maintenance|maintenance]]

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
- `Users`
- `Employee`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Maintenance - HR - Models and Relations
class MaintenanceEquipment
class MaintenanceRequest
class Users
class Employee
class "hr.employee" as hr_employee
MaintenanceEquipment --> hr_employee : many2one
class "hr.department" as hr_department
MaintenanceEquipment --> hr_department : many2one
MaintenanceRequest --> hr_employee : many2one
class "maintenance.equipment" as maintenance_equipment
Users --|> maintenance_equipment : one2many
Employee --|> maintenance_equipment : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
