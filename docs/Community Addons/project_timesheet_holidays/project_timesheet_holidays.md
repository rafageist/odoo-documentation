<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Timesheet when on Time Off

- Scope: Community Addons
- Source: odoo/addons/project_timesheet_holidays
- Dependencies: [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]], [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





