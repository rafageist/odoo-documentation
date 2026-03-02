<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Documents

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/documents
- Dependencies: base (not documented), [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/portal/portal|portal]], [[Odoo 19/Enterprise Addons/web_enterprise/web_enterprise|web_enterprise]], [[Odoo 19/Community Addons/attachment_indexation/attachment_indexation|attachment_indexation]], [[Odoo 19/Community Addons/digest/digest|digest]]

## Summary

Collect, organize and share documents.

## XML Artifacts (detected)

- Views: 28
- Actions: 13
- Menus: 9
- Rules (ir.rule): 11
- Access CSV entries: 25

## Detected Models

- `documents.access`
- `documents.access.tracking`
- `documents.document`
- `documents.redirect`
- `documents.tag`
- `IrActionsServer`
- `IrAttachment`
- `IrEmbeddedActions`
- `MailActivity`
- `MailActivityType`
- `Company`
- `ResPartner`
- `ResUsers`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Models and Relations
class "documents.access" as documents_access
class "documents.access.tracking" as documents_access_tracking
class "documents.document" as documents_document
class "documents.redirect" as documents_redirect
class "documents.tag" as documents_tag
class IrActionsServer
class IrAttachment
class IrEmbeddedActions
class MailActivity
class MailActivityType
class Company
class ResPartner
class ResUsers
documents_access --> documents_document : many2one
class "res.partner" as res_partner
documents_access --> res_partner : many2one
class "res.users" as res_users
documents_access_tracking --> res_users : many2one
class "ir.attachment" as ir_attachment
documents_document --> ir_attachment : many2one
documents_document .. ir_attachment : many2many
documents_document --> documents_document : many2one
documents_document --> res_users : many2one
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
IrAttachment --|> documents_document : one2many
MailActivityType .. documents_tag : many2many
MailActivityType --> documents_document : many2one
ResPartner --|> documents_document : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

