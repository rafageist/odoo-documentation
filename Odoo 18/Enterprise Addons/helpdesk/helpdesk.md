<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Helpdesk

- Version: v18
- Category: enterprise
- Source: enterprise18/helpdesk
- Dependencies: [[Odoo 18/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/utm/utm|utm]], [[Odoo 18/Community Addons/rating/rating|rating]], [[Odoo 18/Community Addons/web_tour/web_tour|web_tour]], [[Odoo 18/Enterprise Addons/web_cohort/web_cohort|web_cohort]], [[Odoo 18/Community Addons/resource/resource|resource]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/digest/digest|digest]]

## Summary

Track, prioritize, and solve customer tickets

## XML Artifacts (detected)

- Views: 72
- Actions: 96
- Menus: 16
- Rules (ir.rule): 13
- Access CSV entries: 21

## Detected Models

- `Digest`
- `helpdesk.sla`
- `helpdesk.sla.status`
- `helpdesk.stage`
- `helpdesk.tag`
- `helpdesk.team`
- `helpdesk.ticket`
- `IrModuleModule`
- `IrUiMenu`
- `MailMessage`
- `ResCompany`
- `ResPartner`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk - Models and Relations
class Digest
class "helpdesk.sla" as helpdesk_sla
class "helpdesk.sla.status" as helpdesk_sla_status
class "helpdesk.stage" as helpdesk_stage
class "helpdesk.tag" as helpdesk_tag
class "helpdesk.team" as helpdesk_team
class "helpdesk.ticket" as helpdesk_ticket
class IrModuleModule
class IrUiMenu
class MailMessage
class ResCompany
class ResPartner
class ResUsers
helpdesk_sla --> helpdesk_team : many2one
helpdesk_sla .. helpdesk_tag : many2many
helpdesk_sla --> helpdesk_stage : many2one
helpdesk_sla .. helpdesk_stage : many2many
class "res.partner" as res_partner
helpdesk_sla .. res_partner : many2many
class "res.company" as res_company
helpdesk_sla --> res_company : many2one
helpdesk_sla_status --> helpdesk_ticket : many2one
helpdesk_sla_status --> helpdesk_sla : many2one
helpdesk_sla_status --> helpdesk_stage : many2one
helpdesk_stage .. helpdesk_team : many2many
class "mail.template" as mail_template
helpdesk_stage --> mail_template : many2one
helpdesk_team --> res_company : many2one
helpdesk_team .. helpdesk_stage : many2many
class "res.users" as res_users
helpdesk_team .. res_users : many2many
helpdesk_team --|> helpdesk_ticket : one2many
class "resource.calendar" as resource_calendar
helpdesk_team --> resource_calendar : many2one
helpdesk_team .. helpdesk_stage : many2many
helpdesk_team --> helpdesk_stage : many2one
helpdesk_ticket --> helpdesk_team : many2one
helpdesk_ticket .. helpdesk_tag : many2many
helpdesk_ticket .. res_users : many2many
helpdesk_ticket --> res_users : many2one
helpdesk_ticket --> res_partner : many2one
helpdesk_ticket .. helpdesk_ticket : many2many
helpdesk_ticket --> helpdesk_stage : many2one
helpdesk_ticket .. helpdesk_sla : many2many
helpdesk_ticket --|> helpdesk_sla_status : one2many
ResPartner .. helpdesk_sla : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
