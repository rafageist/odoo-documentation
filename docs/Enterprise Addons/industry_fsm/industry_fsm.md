<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Field Service

- Scope: Enterprise Addons
- Source: enterprise/industry_fsm
- Dependencies: [[docs/Enterprise Addons/project_enterprise/project_enterprise|project_enterprise]], [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]], [[docs/Community Addons/base_geolocalize/base_geolocalize|base_geolocalize]]

## Summary

Schedule and track onsite operations, time and material

## XML Artifacts (detected)

- Views: 55
- Actions: 150
- Menus: 21
- Rules (ir.rule): 2
- Access CSV entries: 4

## Detected Models

- `AccountAnalyticLine`
- `IrActionsReport`
- `IrUiMenu`
- `ProjectProject`
- `ProjectTask`
- `ProjectTaskRecurrence`
- `ProjectTaskType`
- `RatingRating`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Field Service - Models and Relations
class AccountAnalyticLine
class IrActionsReport
class IrUiMenu
class ProjectProject
class ProjectTask
class ProjectTaskRecurrence
class ProjectTaskType
class RatingRating
class ResCompany
class ResPartner
class "res.country" as res_country
ProjectTask --> res_country : many2one
class "res.country.state" as res_country_state
ProjectTask --> res_country_state : many2one
class "project.project" as project_project
RatingRating --> project_project : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



