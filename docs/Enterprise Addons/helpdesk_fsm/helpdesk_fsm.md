<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk FSM

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_fsm
- Dependencies: [[docs/Enterprise Addons/project_helpdesk/project_helpdesk|project_helpdesk]], [[docs/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



