<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Timesheets

- Scope: Enterprise Addons
- Source: enterprise/timesheet_grid
- Dependencies: [[docs/Enterprise Addons/project_enterprise/project_enterprise|project_enterprise]], [[docs/Enterprise Addons/web_grid/web_grid|web_grid]], [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]], [[docs/Enterprise Addons/timer/timer|timer]], [[docs/Community Addons/hr_org_chart/hr_org_chart|hr_org_chart]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




