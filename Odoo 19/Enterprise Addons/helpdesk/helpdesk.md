<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Helpdesk

- Version: v19
- Category: enterprise
- Source: enterprise19/helpdesk
- Dependencies: [[Odoo 19/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/utm/utm|utm]], [[Odoo 19/Community Addons/rating/rating|rating]], [[Odoo 19/Community Addons/web_tour/web_tour|web_tour]], [[Odoo 19/Enterprise Addons/web_cohort/web_cohort|web_cohort]], [[Odoo 19/Community Addons/resource/resource|resource]], [[Odoo 19/Community Addons/portal/portal|portal]], [[Odoo 19/Community Addons/digest/digest|digest]]

## Summary

Track, prioritize, and solve customer tickets

## XML Artifacts (detected)

- Views: 74
- Actions: 97
- Menus: 16
- Rules (ir.rule): 13
- Access CSV entries: 22

## Detected Models

- `DigestDigest`
- `helpdesk.sla`
- `helpdesk.sla.status`
- `helpdesk.stage`
- `helpdesk.tag`
- `helpdesk.tag.assignment`
- `helpdesk.team`
- `helpdesk.ticket`
- `IrModuleModule`
- `IrUiMenu`
- `MailMessage`
- `RatingRating`
- `ResCompany`
- `ResPartner`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk - Models and Relations
class DigestDigest
class "helpdesk.sla" as helpdesk_sla
class "helpdesk.sla.status" as helpdesk_sla_status
class "helpdesk.stage" as helpdesk_stage
class "helpdesk.tag" as helpdesk_tag
class "helpdesk.tag.assignment" as helpdesk_tag_assignment
class "helpdesk.team" as helpdesk_team
class "helpdesk.ticket" as helpdesk_ticket
class IrModuleModule
class IrUiMenu
class MailMessage
class RatingRating
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
helpdesk_tag_assignment --> helpdesk_team : many2one
helpdesk_tag_assignment --> helpdesk_tag : many2one
class "res.users" as res_users
helpdesk_tag_assignment .. res_users : many2many
helpdesk_team --> res_company : many2one
helpdesk_team .. helpdesk_stage : many2many
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
RatingRating --> helpdesk_ticket : many2one
ResPartner .. helpdesk_sla : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
