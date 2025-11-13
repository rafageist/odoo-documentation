<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Timesheet and Planning

- Version: v19
- Category: enterprise
- Source: enterprise19/project_timesheet_forecast
- Dependencies: [[Odoo 19/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]], [[Odoo 19/Enterprise Addons/project_forecast/project_forecast|project_forecast]]

## Summary

Compare timesheets and plannings

## XML Artifacts (detected)

- Views: 12
- Actions: 8
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `IrUiMenu`
- `PlanningSlot`
- `ProjectProject`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Timesheet and Planning - Models and Relations
class IrUiMenu
class PlanningSlot
class ProjectProject
class "account.analytic.line" as account_analytic_line
PlanningSlot .. account_analytic_line : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
