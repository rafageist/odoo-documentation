<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Project

- Scope: Community Addons
- Source: odoo/addons/project
- Dependencies: [[docs/Community Addons/analytic/analytic|analytic]], [[docs/Community Addons/base_setup/base_setup|base_setup]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/rating/rating|rating]], [[docs/Community Addons/resource/resource|resource]], [[docs/Community Addons/web/web|web]], [[docs/Community Addons/web_tour/web_tour|web_tour]], [[docs/Community Addons/digest/digest|digest]]

## Summary

Organize and plan your projects

## XML Artifacts (detected)

- Views: 112
- Actions: 109
- Menus: 19
- Rules (ir.rule): 31
- Access CSV entries: 54

## Detected Models

- `AccountAnalyticAccount`
- `DigestDigest`
- `IrUiMenu`
- `MailMessage`
- `project.collaborator`
- `project.milestone`
- `project.project`
- `project.project.stage`
- `project.role`
- `project.tags`
- `project.task`
- `project.task.recurrence`
- `project.task.stage.personal`
- `project.task.type`
- `project.update`
- `ResPartner`
- `ResUsers`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Project - Models and Relations
class AccountAnalyticAccount
class DigestDigest
class IrUiMenu
class MailMessage
class "project.collaborator" as project_collaborator
class "project.milestone" as project_milestone
class "project.project" as project_project
class "project.project.stage" as project_project_stage
class "project.role" as project_role
class "project.tags" as project_tags
class "project.task" as project_task
class "project.task.recurrence" as project_task_recurrence
class "project.task.stage.personal" as project_task_stage_personal
class "project.task.type" as project_task_type
class "project.update" as project_update
class ResPartner
class ResUsers
AccountAnalyticAccount --|> project_project : one2many
project_collaborator --> project_project : many2one
class "res.partner" as res_partner
project_collaborator --> res_partner : many2one
project_milestone --> project_project : many2one
project_milestone --|> project_task : one2many
project_project --> res_partner : many2one
class "res.company" as res_company
project_project --> res_company : many2one
class "res.currency" as res_currency
project_project --> res_currency : many2one
class "account.analytic.account" as account_analytic_account
project_project --> account_analytic_account : many2one
class "res.users" as res_users
project_project .. res_users : many2many
project_project --|> project_task : one2many
class "resource.calendar" as resource_calendar
project_project --> resource_calendar : many2one
project_project .. project_task_type : many2many
project_project --|> project_task : one2many
project_project --> res_users : many2one
project_project .. project_tags : many2many
project_project --|> project_collaborator : one2many
project_project --> project_project_stage : many2one
project_project --|> project_update : one2many
project_project --> project_update : many2one
project_project --|> project_milestone : one2many
project_project --> project_milestone : many2one
class "mail.template" as mail_template
project_project_stage --> mail_template : many2one
project_project_stage --> res_company : many2one
project_tags .. project_project : many2many
project_tags .. project_task : many2many
project_task --> project_task_type : many2one
project_task .. project_tags : many2many
project_task --> project_project : many2one
project_task .. project_role : many2many
project_task .. res_users : many2many
project_task .. project_task_type : many2many
project_task --> project_task_stage_personal : many2one
project_task --> project_task_type : many2one
project_task --> res_partner : many2one
project_task --> res_company : many2one
class "ir.attachment" as ir_attachment
project_task --|> ir_attachment : one2many
project_task --> ir_attachment : many2one
project_task --> project_task : many2one
project_task --|> project_task : one2many
project_task --> project_milestone : many2one
project_task .. project_task : many2many
project_task .. project_task : many2many
project_task --> project_task_recurrence : many2one
project_task_recurrence --|> project_task : one2many
project_task_stage_personal --> project_task : many2one
project_task_stage_personal --> res_users : many2one
project_task_stage_personal --> project_task_type : many2one
project_task_type .. project_project : many2many
project_task_type --> mail_template : many2one
project_task_type --> mail_template : many2one
project_task_type --> res_users : many2one
project_update --> res_users : many2one
project_update --> project_project : many2one
ResPartner --|> project_project : one2many
ResPartner --|> project_task : one2many
ResUsers .. project_project : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




## Curated analysis

### Functional role
- `project` is the services execution workspace: projects, tasks, updates, milestones, roles, collaborators, and portal sharing all converge here.
- It is one of the clearest examples of a module that mixes business flow, mail/thread behavior, ratings, portal access, and reporting in the same functional surface.

### Operational footprint
- `project_project.py`, `project_task.py`, and `project_update.py` hold the core orchestration for project state, task lifecycle, and stakeholder updates.
- The module ships broad UI and security coverage, including burndown reporting, sharing views, cron data, and a dense set of record rules in `security/project_security.xml`.

### Evidence
- Source files: `odoo19/addons/project/models/project_project.py`, `odoo19/addons/project/models/project_task.py`, `odoo19/addons/project/models/project_update.py`
- UI and automation: `odoo19/addons/project/views/project_project_views.xml`, `odoo19/addons/project/views/project_task_views.xml`, `odoo19/addons/project/data/ir_cron_data.xml`
- Security and tests: `odoo19/addons/project/security/project_security.xml`, `odoo19/addons/project/tests/test_access_rights.py`, `odoo19/addons/project/tests/test_burndown_chart.py`

### Related notes
- `[[docs/Core/Processes/Projects/Projects]]`
- `[[docs/Community Addons/portal/portal|portal]]`

### Risks and follow-up
- Access control is a first-class concern here; portal sharing and collaborator rules need to be reviewed before exposing customer projects externally.
- The analytic-account link means configuration mistakes can leak into billing, profitability, and resource reporting even when users think they are only moving tasks.
- Legacy comparison backlog was retired on 2026-03-02; keep this note focused on the current codebase.


