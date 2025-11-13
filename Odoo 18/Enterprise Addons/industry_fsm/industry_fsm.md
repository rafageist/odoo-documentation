<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Field Service

- Version: v18
- Category: enterprise
- Source: enterprise18/industry_fsm
- Dependencies: [[Odoo 18/Enterprise Addons/project_enterprise/project_enterprise|project_enterprise]], [[Odoo 18/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]], [[Odoo 18/Community Addons/base_geolocalize/base_geolocalize|base_geolocalize]]

## Summary

Schedule and track onsite operations, time and material

## XML Artifacts (detected)

- Views: 58
- Actions: 139
- Menus: 21
- Rules (ir.rule): 2
- Access CSV entries: 4

## Detected Models

- `IrActionsReport`
- `IrUiMenu`
- `Project`
- `Task`
- `ProjectTaskRecurrence`
- `ProjectTaskType`
- `res.company`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Field Service - Models and Relations
class IrActionsReport
class IrUiMenu
class Project
class Task
class ProjectTaskRecurrence
class ProjectTaskType
class "res.company" as res_company
class ResPartner
class "res.country" as res_country
Task --> res_country : many2one
class "res.country.state" as res_country_state
Task --> res_country_state : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
