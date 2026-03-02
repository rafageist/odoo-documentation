<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Timesheet and Planning

- Scope: Enterprise Addons
- Source: enterprise/project_timesheet_forecast
- Dependencies: [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]], [[docs/Enterprise Addons/project_forecast/project_forecast|project_forecast]]

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
!include ../../../templates/DiagramStyles.puml
title Timesheet and Planning - Models and Relations
class IrUiMenu
class PlanningSlot
class ProjectProject
class "account.analytic.line" as account_analytic_line
PlanningSlot .. account_analytic_line : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



