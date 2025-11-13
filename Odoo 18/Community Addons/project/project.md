<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Project

- Version: v18
- Category: community
- Source: odoo/addons/project
- Dependencies: [[Odoo 18/Community Addons/analytic/analytic|analytic]], [[Odoo 18/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/rating/rating|rating]], [[Odoo 18/Community Addons/resource/resource|resource]], [[Odoo 18/Community Addons/web/web|web]], [[Odoo 18/Community Addons/web_tour/web_tour|web_tour]], [[Odoo 18/Community Addons/digest/digest|digest]]

## Summary

Organize and plan your projects

## XML Artifacts (detected)

- Views: 96
- Actions: 94
- Menus: 18
- Rules (ir.rule): 31
- Access CSV entries: 47

## Detected Models

- `AccountAnalyticAccount`
- `Digest`
- `IrUiMenu`
- `MailMessage`
- `project.collaborator`
- `project.milestone`
- `project.project`
- `project.project.stage`
- `project.tags`
- `project.task`
- `project.task.recurrence`
- `project.task.stage.personal`
- `project.task.type`
- `project.update`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Project - Models and Relations
class AccountAnalyticAccount
class Digest
class IrUiMenu
class MailMessage
class "project.collaborator" as project_collaborator
class "project.milestone" as project_milestone
class "project.project" as project_project
class "project.project.stage" as project_project_stage
class "project.tags" as project_tags
class "project.task" as project_task
class "project.task.recurrence" as project_task_recurrence
class "project.task.stage.personal" as project_task_stage_personal
class "project.task.type" as project_task_type
class "project.update" as project_update
class ResPartner
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
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
