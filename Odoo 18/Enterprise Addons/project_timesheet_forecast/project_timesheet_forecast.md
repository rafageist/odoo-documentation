<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Timesheet and Planning

- Version: v18
- Category: enterprise
- Source: enterprise18/project_timesheet_forecast
- Dependencies: [[Odoo 18/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]], [[Odoo 18/Enterprise Addons/project_forecast/project_forecast|project_forecast]]

## Summary

Compare timesheets and plannings

## XML Artifacts (detected)

- Views: 12
- Actions: 8
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `AccountAnalyticLine`
- `IrUiMenu`
- `Project`
- `Forecast`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Timesheet and Planning - Models and Relations
class AccountAnalyticLine
class IrUiMenu
class Project
class Forecast
class "planning.slot" as planning_slot
AccountAnalyticLine --> planning_slot : many2one
class "account.analytic.line" as account_analytic_line
Forecast .. account_analytic_line : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
