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

## Curated analysis

### Functional role
- `documents` turns `ir.attachment` into an enterprise document workspace with folders, tags, requests, sharing links, and access tracking.
- It is as much a governance layer as a UI module because it redefines how attachments are organized, exposed, and audited.

### Operational footprint
- `documents_document.py`, `documents_access.py`, and `ir_attachment.py` are the core files for document records, sharing rules, and attachment behavior.
- Controllers and wizards cover portal access, document requests, bulk operations, and sharing flows, while cron and data files preload tags, aliases, and request behavior.

### Evidence
- Source files: `enterprise19/documents/models/documents_document.py`, `enterprise19/documents/models/documents_access.py`, `enterprise19/documents/models/ir_attachment.py`
- UI and flows: `enterprise19/documents/views/documents_document_views.xml`, `enterprise19/documents/views/documents_access_views.xml`, `enterprise19/documents/wizard/documents_sharing.py`
- Tests: `enterprise19/documents/tests/test_documents_access.py`, `enterprise19/documents/tests/test_attachment_access.py`, `enterprise19/documents/tests/test_attachment_split.py`

### Related notes
- `[[Odoo 19/Core/Infrastructure/Files]]`
- `[[Odoo 19/Enterprise Addons/knowledge/knowledge|knowledge]]`

### Rollout and migration concerns
- Document permissions must be reviewed before importing historical attachments because access propagation and portal exposure are built into the model, not layered on later.
- PDF split and merge operations change attachment ownership and traceability, so retention and audit expectations should be validated during rollout.
- Odoo 18 comparison backlog was retired on 2026-03-02; keep this note focused on Odoo 19 behavior.

