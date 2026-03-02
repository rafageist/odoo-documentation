<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sign

- Scope: Enterprise Addons
- Source: enterprise/sign
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/attachment_indexation/attachment_indexation|attachment_indexation]], [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/sms/sms|sms]], [[docs/Community Addons/certificate/certificate|certificate]]

## Summary

Send and request electronic signatures.

## XML Artifacts (detected)

- Views: 31
- Actions: 13
- Menus: 11
- Rules (ir.rule): 25
- Access CSV entries: 19

## Detected Models

- `MailActivityType`
- `ResCompany`
- `ResPartner`
- `ResUsers`
- `sign.completed.document`
- `sign.document`
- `sign.item`
- `sign.item.option`
- `sign.item.radio.set`
- `sign.item.role`
- `sign.item.type`
- `sign.log`
- `sign.request`
- `sign.request.item`
- `sign.request.item.value`
- `sign.template`
- `sign.template.tag`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Sign - Models and Relations
class MailActivityType
class ResCompany
class ResPartner
class ResUsers
class "sign.completed.document" as sign_completed_document
class "sign.document" as sign_document
class "sign.item" as sign_item
class "sign.item.option" as sign_item_option
class "sign.item.radio.set" as sign_item_radio_set
class "sign.item.role" as sign_item_role
class "sign.item.type" as sign_item_type
class "sign.log" as sign_log
class "sign.request" as sign_request
class "sign.request.item" as sign_request_item
class "sign.request.item.value" as sign_request_item_value
class "sign.template" as sign_template
class "sign.template.tag" as sign_template_tag
MailActivityType --> sign_template : many2one
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
sign_completed_document --> sign_request : many2one
sign_completed_document --> sign_document : many2one
class "ir.attachment" as ir_attachment
sign_document --> ir_attachment : many2one
sign_document --> sign_template : many2one
sign_document --|> sign_item : one2many
sign_item --> sign_document : many2one
sign_item --> sign_template : many2one
sign_item --> sign_item_type : many2one
sign_item --> sign_item_role : many2one
sign_item .. sign_item_option : many2many
sign_item --> sign_item_radio_set : many2one
sign_item_radio_set --|> sign_item : one2many
class "res.partner" as res_partner
sign_item_role --> res_partner : many2one
class "ir.model" as ir_model
sign_item_type --> ir_model : many2one
sign_log --> sign_request : many2one
sign_log --> sign_request_item : many2one
class "res.users" as res_users
sign_log --> res_users : many2one
sign_log --> res_partner : many2one
sign_request --> sign_template : many2one
sign_request --|> sign_request_item : one2many
sign_request .. sign_document : many2many
sign_request --|> sign_completed_document : one2many
sign_request .. res_users : many2many
class "res.company" as res_company
sign_request --> res_company : many2one
sign_request --|> sign_log : one2many
sign_request .. sign_template_tag : many2many
sign_request .. res_partner : many2many
sign_request .. ir_attachment : many2many
sign_request .. ir_attachment : many2many
sign_request_item --> res_partner : many2one
sign_request_item --> sign_request : many2one
sign_request_item --|> sign_request_item_value : one2many
sign_request_item --> sign_item_role : many2one
sign_request_item_value --> sign_request_item : many2one
sign_request_item_value --> sign_item : many2one
sign_template --|> sign_document : one2many
sign_template --|> sign_item : one2many
sign_template .. res_users : many2many
sign_template --> res_users : many2one
sign_template --|> sign_request : one2many
sign_template .. sign_template_tag : many2many
sign_template .. res_users : many2many
class "res.groups" as res_groups
sign_template .. res_groups : many2many
sign_template --> ir_model : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



