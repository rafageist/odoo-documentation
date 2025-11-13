<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Task Logs

- Version: v18
- Category: community
- Source: odoo/addons/hr_timesheet
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]], [[Odoo 18/Community Addons/hr_hourly_cost/hr_hourly_cost|hr_hourly_cost]], [[Odoo 18/Community Addons/analytic/analytic|analytic]], [[Odoo 18/Community Addons/project/project|project]], [[Odoo 18/Community Addons/uom/uom|uom]]

## Summary

Track employee time on tasks

## XML Artifacts (detected)

- Views: 48
- Actions: 42
- Menus: 11
- Rules (ir.rule): 9
- Access CSV entries: 6

## Detected Models

- `AccountAnalyticApplicability`
- `HrEmployee`
- `AccountAnalyticLine`
- `IrUiMenu`
- `ProjectCollaborator`
- `Project`
- `project.task`
- `ProjectUpdate`
- `ResCompany`
- `Uom`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Task Logs - Models and Relations
class AccountAnalyticApplicability
class HrEmployee
class AccountAnalyticLine
class IrUiMenu
class ProjectCollaborator
class Project
class "project.task" as project_task
class ProjectUpdate
class ResCompany
class Uom
AccountAnalyticLine --> project_task : many2one
AccountAnalyticLine --> project_task : many2one
class "project.project" as project_project
AccountAnalyticLine --> project_project : many2one
class "hr.employee" as hr_employee
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
Project --|> account_analytic_line : one2many
Project --> uom_uom : many2one
project_task --|> account_analytic_line : one2many
ProjectUpdate --> uom_uom : many2one
ResCompany --> uom_uom : many2one
ResCompany --> uom_uom : many2one
ResCompany --> project_project : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
