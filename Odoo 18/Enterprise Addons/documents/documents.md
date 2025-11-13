<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Documents

- Version: v18
- Category: enterprise
- Source: enterprise18/documents
- Dependencies: base (not documented), [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Enterprise Addons/web_enterprise/web_enterprise|web_enterprise]], [[Odoo 18/Community Addons/attachment_indexation/attachment_indexation|attachment_indexation]], [[Odoo 18/Community Addons/digest/digest|digest]]

## Summary

Collect, organize and share documents.

## XML Artifacts (detected)

- Views: 23
- Actions: 19
- Menus: 9
- Rules (ir.rule): 10
- Access CSV entries: 18

## Detected Models

- `documents.access`
- `documents.document`
- `documents.redirect`
- `documents.tag`
- `IrActionsServer`
- `IrAttachment`
- `MailActivity`
- `MailActivityType`
- `Company`
- `Partner`
- `res.users`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Models and Relations
class "documents.access" as documents_access
class "documents.document" as documents_document
class "documents.redirect" as documents_redirect
class "documents.tag" as documents_tag
class IrActionsServer
class IrAttachment
class MailActivity
class MailActivityType
class Company
class Partner
class "res.users" as res_users
documents_access --> documents_document : many2one
class "res.partner" as res_partner
documents_access --> res_partner : many2one
class "ir.attachment" as ir_attachment
documents_document --> ir_attachment : many2one
documents_document .. ir_attachment : many2many
documents_document --> documents_document : many2one
documents_document --|> documents_document : one2many
documents_document .. res_users : many2many
documents_document .. documents_tag : many2many
documents_document --> res_partner : many2one
documents_document --> res_users : many2one
documents_document --> res_users : many2one
class "mail.activity" as mail_activity
documents_document --> mail_activity : many2one
documents_document --> res_partner : many2one
documents_document --|> documents_access : one2many
documents_document --> documents_document : many2one
documents_document --|> documents_document : one2many
class "res.company" as res_company
documents_document --> res_company : many2one
class "mail.activity.type" as mail_activity_type
documents_document --> mail_activity_type : many2one
documents_document --> res_users : many2one
class "ir.embedded.actions" as ir_embedded_actions
documents_document .. ir_embedded_actions : many2many
documents_document .. documents_tag : many2many
documents_redirect --> documents_document : many2one
documents_tag .. documents_document : many2many
MailActivityType .. documents_tag : many2many
MailActivityType --> documents_document : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
