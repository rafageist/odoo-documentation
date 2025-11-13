<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Timesheets

- Version: v18
- Category: enterprise
- Source: enterprise18/timesheet_grid
- Dependencies: [[Odoo 18/Enterprise Addons/project_enterprise/project_enterprise|project_enterprise]], [[Odoo 18/Enterprise Addons/web_grid/web_grid|web_grid]], [[Odoo 18/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]], [[Odoo 18/Enterprise Addons/timer/timer|timer]], [[Odoo 18/Community Addons/hr_org_chart/hr_org_chart|hr_org_chart]]

## Summary

Track employee time on tasks

## XML Artifacts (detected)

- Views: 31
- Actions: 24
- Menus: 3
- Rules (ir.rule): 2
- Access CSV entries: 2

## Detected Models

- `account.analytic.line`
- `Employee`
- `HrEmployeePublic`
- `IrModuleModule`
- `project.project`
- `Company`
- `User`
- `project.task`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Timesheets - Models and Relations
class "account.analytic.line" as account_analytic_line
class Employee
class HrEmployeePublic
class IrModuleModule
class "project.project" as project_project
class Company
class User
class "project.task" as project_task
class "res.users" as res_users
Employee --> res_users : many2one
HrEmployeePublic --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
