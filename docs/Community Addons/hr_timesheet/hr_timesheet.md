<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Task Logs

- Scope: Community Addons
- Source: odoo/addons/hr_timesheet
- Dependencies: [[docs/Community Addons/hr/hr|hr]], [[docs/Community Addons/hr_hourly_cost/hr_hourly_cost|hr_hourly_cost]], [[docs/Community Addons/analytic/analytic|analytic]], [[docs/Community Addons/project/project|project]], [[docs/Community Addons/uom/uom|uom]]

## Summary

Track employee time on tasks

## XML Artifacts (detected)

- Views: 54
- Actions: 44
- Menus: 11
- Rules (ir.rule): 9
- Access CSV entries: 7

## Detected Models

- `account.analytic.line.calendar.employee`
- `AccountAnalyticApplicability`
- `HrEmployee`
- `HrEmployeePublic`
- `AccountAnalyticLine`
- `IrUiMenu`
- `ProjectCollaborator`
- `ProjectProject`
- `ProjectTask`
- `ProjectUpdate`
- `ResCompany`
- `UomUom`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Task Logs - Models and Relations
class "account.analytic.line.calendar.employee" as account_analytic_line_calendar_employee
class AccountAnalyticApplicability
class HrEmployee
class HrEmployeePublic
class AccountAnalyticLine
class IrUiMenu
class ProjectCollaborator
class ProjectProject
class ProjectTask
class ProjectUpdate
class ResCompany
class UomUom
class "res.users" as res_users
account_analytic_line_calendar_employee --> res_users : many2one
class "hr.employee" as hr_employee
account_analytic_line_calendar_employee --> hr_employee : many2one
class "project.task" as project_task
AccountAnalyticLine --> project_task : many2one
AccountAnalyticLine --> project_task : many2one
class "project.project" as project_project
AccountAnalyticLine --> project_project : many2one
AccountAnalyticLine --> hr_employee : many2one
class "hr.department" as hr_department
AccountAnalyticLine --> hr_department : many2one
AccountAnalyticLine --> hr_employee : many2one
class "uom.uom" as uom_uom
AccountAnalyticLine --> uom_uom : many2one
class "project.milestone" as project_milestone
AccountAnalyticLine --> project_milestone : many2one
class "res.partner" as res_partner
AccountAnalyticLine .. res_partner : many2many
class "account.analytic.line" as account_analytic_line
ProjectProject --|> account_analytic_line : one2many
ProjectProject --> uom_uom : many2one
ProjectTask --|> account_analytic_line : one2many
ProjectUpdate --> uom_uom : many2one
ResCompany --> uom_uom : many2one
ResCompany --> uom_uom : many2one
ResCompany --> project_project : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





