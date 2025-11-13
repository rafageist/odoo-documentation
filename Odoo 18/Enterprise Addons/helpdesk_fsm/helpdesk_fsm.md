<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Helpdesk FSM

- Version: v18
- Category: enterprise
- Source: enterprise18/helpdesk_fsm
- Dependencies: [[Odoo 18/Enterprise Addons/project_helpdesk/project_helpdesk|project_helpdesk]], [[Odoo 18/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]]

## Summary

Allow generating fsm tasks from ticket

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `HelpdeskTeam`
- `HelpdeskTicket`
- `Task`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk FSM - Models and Relations
class HelpdeskTeam
class HelpdeskTicket
class Task
class "project.project" as project_project
HelpdeskTeam --> project_project : many2one
class "project.task" as project_task
HelpdeskTicket --|> project_task : one2many
class "helpdesk.ticket" as helpdesk_ticket
Task --> helpdesk_ticket : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
