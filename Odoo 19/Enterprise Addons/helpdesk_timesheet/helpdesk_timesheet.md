<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Helpdesk Timesheet

- Version: v19
- Category: enterprise
- Source: enterprise19/helpdesk_timesheet
- Dependencies: [[Odoo 19/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]], [[Odoo 19/Enterprise Addons/project_helpdesk/project_helpdesk|project_helpdesk]]

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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
