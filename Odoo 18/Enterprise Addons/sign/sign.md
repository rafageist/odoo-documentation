<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Sign

- Version: v18
- Category: enterprise
- Source: enterprise18/sign
- Dependencies: [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/attachment_indexation/attachment_indexation|attachment_indexation]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/sms/sms|sms]]

## Summary

Send documents to sign online and handle filled copies

## XML Artifacts (detected)

- Views: 29
- Actions: 15
- Menus: 12
- Rules (ir.rule): 17
- Access CSV entries: 16

## Detected Models

- `MailActivityType`
- `Company`
- `ResPartner`
- `ResUsers`
- `sign.log`
- `sign.request`
- `sign.request.item`
- `sign.request.item.value`
- `sign.template`
- `sign.template.tag`
- `sign.item.option`
- `sign.item.radio.set`
- `sign.item`
- `sign.item.type`
- `sign.item.role`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sign - Models and Relations
class MailActivityType
class Company
class ResPartner
class ResUsers
class "sign.log" as sign_log
class "sign.request" as sign_request
class "sign.request.item" as sign_request_item
class "sign.request.item.value" as sign_request_item_value
class "sign.template" as sign_template
class "sign.template.tag" as sign_template_tag
class "sign.item.option" as sign_item_option
class "sign.item.radio.set" as sign_item_radio_set
class "sign.item" as sign_item
class "sign.item.type" as sign_item_type
class "sign.item.role" as sign_item_role
MailActivityType --> sign_template : many2one
sign_log --> sign_request : many2one
sign_log --> sign_request_item : many2one
class "res.users" as res_users
sign_log --> res_users : many2one
class "res.partner" as res_partner
sign_log --> res_partner : many2one
sign_request --> sign_template : many2one
sign_request --|> sign_request_item : one2many
sign_request .. res_users : many2many
class "res.company" as res_company
sign_request --> res_company : many2one
sign_request --|> sign_log : one2many
sign_request .. sign_template_tag : many2many
sign_request .. res_partner : many2many
class "ir.attachment" as ir_attachment
sign_request .. ir_attachment : many2many
sign_request .. ir_attachment : many2many
sign_request_item --> res_partner : many2one
sign_request_item --> sign_request : many2one
sign_request_item --|> sign_request_item_value : one2many
sign_request_item --> sign_item_role : many2one
sign_request_item_value --> sign_request_item : many2one
sign_request_item_value --> sign_item : many2one
sign_template --> ir_attachment : many2one
sign_template --|> sign_item : one2many
sign_template .. res_users : many2many
sign_template --> res_users : many2one
sign_template --|> sign_request : one2many
sign_template .. sign_template_tag : many2many
sign_template .. res_users : many2many
class "res.groups" as res_groups
sign_template .. res_groups : many2many
sign_item_radio_set --|> sign_item : one2many
sign_item --> sign_template : many2one
sign_item --> sign_item_type : many2one
sign_item --> sign_item_role : many2one
sign_item .. sign_item_option : many2many
sign_item --> sign_item_radio_set : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
