<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Timesheet when on Time Off

- Version: v18
- Category: community
- Source: odoo/addons/project_timesheet_holidays
- Dependencies: [[Odoo 18/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]], [[Odoo 18/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

## Summary

Schedule timesheet when on time off

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountAnalyticLine`
- `Employee`
- `HolidaysType`
- `Holidays`
- `Task`
- `ResourceCalendarLeaves`
- `Company`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Timesheet when on Time Off - Models and Relations
class AccountAnalyticLine
class Employee
class HolidaysType
class Holidays
class Task
class ResourceCalendarLeaves
class Company
class "hr.leave" as hr_leave
AccountAnalyticLine --> hr_leave : many2one
class "resource.calendar.leaves" as resource_calendar_leaves
AccountAnalyticLine --> resource_calendar_leaves : many2one
class "project.project" as project_project
HolidaysType --> project_project : many2one
class "project.task" as project_task
HolidaysType --> project_task : many2one
class "account.analytic.line" as account_analytic_line
Holidays --|> account_analytic_line : one2many
ResourceCalendarLeaves --|> account_analytic_line : one2many
Company --> project_task : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
