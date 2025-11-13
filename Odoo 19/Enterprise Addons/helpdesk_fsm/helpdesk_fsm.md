<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Helpdesk FSM

- Version: v19
- Category: enterprise
- Source: enterprise19/helpdesk_fsm
- Dependencies: [[Odoo 19/Enterprise Addons/project_helpdesk/project_helpdesk|project_helpdesk]], [[Odoo 19/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]]

## Summary

Allow generating fsm tasks from ticket

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `HelpdeskTeam`
- `HelpdeskTicket`
- `ProjectTask`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk FSM - Models and Relations
class HelpdeskTeam
class HelpdeskTicket
class ProjectTask
class "project.project" as project_project
HelpdeskTeam --> project_project : many2one
class "project.task" as project_task
HelpdeskTicket --|> project_task : one2many
class "helpdesk.ticket" as helpdesk_ticket
ProjectTask --> helpdesk_ticket : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
