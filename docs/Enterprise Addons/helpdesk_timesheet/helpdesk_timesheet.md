<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk Timesheet

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_timesheet
- Dependencies: [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]], [[docs/Enterprise Addons/project_helpdesk/project_helpdesk|project_helpdesk]]

## Summary

Project, Tasks, Timesheet

## XML Artifacts (detected)

- Views: 25
- Actions: 11
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 5

## Detected Models

- `AccountAnalyticLine`
- `HelpdeskTeam`
- `helpdesk.ticket`
- `ProjectProject`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Helpdesk Timesheet - Models and Relations
class AccountAnalyticLine
class HelpdeskTeam
class "helpdesk.ticket" as helpdesk_ticket
class ProjectProject
AccountAnalyticLine --> helpdesk_ticket : many2one
class "project.project" as project_project
HelpdeskTeam --> project_project : many2one
class "uom.uom" as uom_uom
HelpdeskTeam --> uom_uom : many2one
helpdesk_ticket --> project_project : many2one
class "account.analytic.line" as account_analytic_line
helpdesk_ticket --|> account_analytic_line : one2many
class "account.analytic.account" as account_analytic_account
helpdesk_ticket --> account_analytic_account : many2one
ProjectProject --|> helpdesk_ticket : one2many
class "helpdesk.team" as helpdesk_team
ProjectProject --|> helpdesk_team : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




