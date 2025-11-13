<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# WhatsApp Messaging

- Version: v18
- Category: enterprise
- Source: enterprise18/whatsapp
- Dependencies: [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/phone_validation/phone_validation|phone_validation]]

## Summary

Text your Contacts on WhatsApp

## XML Artifacts (detected)

- Views: 22
- Actions: 5
- Menus: 5
- Rules (ir.rule): 14
- Access CSV entries: 14

## Detected Models

- `DiscussChannel`
- `DiscussChannelMember`
- `ir.actions.server`
- `MailMessage`
- `ResPartner`
- `ResUsersSettings`
- `whatsapp.account`
- `whatsapp.message`
- `whatsapp.template`
- `whatsapp.template.button`
- `whatsapp.template.variable`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title WhatsApp Messaging - Models and Relations
class DiscussChannel
class DiscussChannelMember
class "ir.actions.server" as ir_actions_server
class MailMessage
class ResPartner
class ResUsersSettings
class "whatsapp.account" as whatsapp_account
class "whatsapp.message" as whatsapp_message
class "whatsapp.template" as whatsapp_template
class "whatsapp.template.button" as whatsapp_template_button
class "whatsapp.template.variable" as whatsapp_template_variable
class "mail.message" as mail_message
DiscussChannel --> mail_message : many2one
class "res.partner" as res_partner
DiscussChannel --> res_partner : many2one
DiscussChannel --> whatsapp_account : many2one
ir_actions_server --> whatsapp_template : many2one
MailMessage --|> whatsapp_message : one2many
class "res.company" as res_company
whatsapp_account .. res_company : many2many
class "res.users" as res_users
whatsapp_account .. res_users : many2many
whatsapp_message --> whatsapp_template : many2one
whatsapp_message --> whatsapp_account : many2one
whatsapp_message --> whatsapp_message : many2one
whatsapp_message --> mail_message : many2one
whatsapp_template --> whatsapp_account : many2one
class "ir.model" as ir_model
whatsapp_template --> ir_model : many2one
whatsapp_template .. res_users : many2many
class "ir.attachment" as ir_attachment
whatsapp_template .. ir_attachment : many2many
class "ir.actions.report" as ir_actions_report
whatsapp_template --> ir_actions_report : many2one
whatsapp_template --|> whatsapp_template_variable : one2many
whatsapp_template --|> whatsapp_template_button : one2many
whatsapp_template_button --> whatsapp_template : many2one
whatsapp_template_button --|> whatsapp_template_variable : one2many
whatsapp_template_variable --> whatsapp_template_button : many2one
whatsapp_template_variable --> whatsapp_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
