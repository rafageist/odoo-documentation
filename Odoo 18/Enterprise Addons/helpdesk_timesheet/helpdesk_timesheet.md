<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Helpdesk Timesheet

- Version: v18
- Category: enterprise
- Source: enterprise18/helpdesk_timesheet
- Dependencies: [[Odoo 18/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]], [[Odoo 18/Enterprise Addons/project_helpdesk/project_helpdesk|project_helpdesk]]

## Summary

Project, Tasks, Timesheet

## XML Artifacts (detected)

- Views: 23
- Actions: 11
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 6

## Detected Models

- `AccountAnalyticLine`
- `HelpdeskTeam`
- `helpdesk.ticket`
- `Project`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk Timesheet - Models and Relations
class AccountAnalyticLine
class HelpdeskTeam
class "helpdesk.ticket" as helpdesk_ticket
class Project
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
Project --|> helpdesk_ticket : one2many
class "helpdesk.team" as helpdesk_team
Project --|> helpdesk_team : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
