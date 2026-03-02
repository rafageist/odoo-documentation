<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Timesheets

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/timesheet_grid
- Dependencies: [[Odoo 19/Enterprise Addons/project_enterprise/project_enterprise|project_enterprise]], [[Odoo 19/Enterprise Addons/web_grid/web_grid|web_grid]], [[Odoo 19/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]], [[Odoo 19/Enterprise Addons/timer/timer|timer]], [[Odoo 19/Community Addons/hr_org_chart/hr_org_chart|hr_org_chart]]

## Summary

Track employee time on tasks

## XML Artifacts (detected)

- Views: 33
- Actions: 26
- Menus: 3
- Rules (ir.rule): 2
- Access CSV entries: 2

## Detected Models

- `account.analytic.line`
- `HrEmployee`
- `HrEmployeePublic`
- `IrModuleModule`
- `project.project`
- `project.task`
- `ResCompany`
- `ResUsers`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Timesheets - Models and Relations
class "account.analytic.line" as account_analytic_line
class HrEmployee
class HrEmployeePublic
class IrModuleModule
class "project.project" as project_project
class "project.task" as project_task
class ResCompany
class ResUsers
class "res.users" as res_users
HrEmployee --> res_users : many2one
HrEmployeePublic --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

