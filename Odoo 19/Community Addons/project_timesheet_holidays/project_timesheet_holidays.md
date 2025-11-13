<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Timesheet when on Time Off

- Version: v19
- Category: community
- Source: odoo19/addons/project_timesheet_holidays
- Dependencies: [[Odoo 19/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]], [[Odoo 19/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

## Summary

Schedule timesheet when on time off

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountAnalyticLine`
- `HrEmployee`
- `HrLeave`
- `ProjectTask`
- `ResourceCalendarLeaves`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Timesheet when on Time Off - Models and Relations
class AccountAnalyticLine
class HrEmployee
class HrLeave
class ProjectTask
class ResourceCalendarLeaves
class ResCompany
class "hr.leave" as hr_leave
AccountAnalyticLine --> hr_leave : many2one
class "resource.calendar.leaves" as resource_calendar_leaves
AccountAnalyticLine --> resource_calendar_leaves : many2one
class "account.analytic.line" as account_analytic_line
HrLeave --|> account_analytic_line : one2many
ResourceCalendarLeaves --|> account_analytic_line : one2many
class "project.task" as project_task
ResCompany --> project_task : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
