<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# SMS gateway

- Scope: Community Addons
- Source: odoo/addons/sms
- Dependencies: base (not documented), [[docs/Community Addons/iap_mail/iap_mail|iap_mail]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/phone_validation/phone_validation|phone_validation]]

## Summary

SMS Text Messaging

## XML Artifacts (detected)

- Views: 18
- Actions: 8
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 13

## Detected Models

- `IapAccount`
- `IrActionsServer`
- `IrModel`
- `MailFollowers`
- `MailMessage`
- `MailNotification`
- `ResCompany`
- `sms.sms`
- `sms.template`
- `sms.tracker`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title SMS gateway - Models and Relations
class IapAccount
class IrActionsServer
class IrModel
class MailFollowers
class MailMessage
class MailNotification
class ResCompany
class "sms.sms" as sms_sms
class "sms.template" as sms_template
class "sms.tracker" as sms_tracker
IrActionsServer --> sms_template : many2one
MailNotification --> sms_sms : many2one
MailNotification --|> sms_tracker : one2many
class "res.partner" as res_partner
sms_sms --> res_partner : many2one
class "mail.message" as mail_message
sms_sms --> mail_message : many2one
sms_sms --> sms_tracker : many2one
class "ir.model" as ir_model
sms_template --> ir_model : many2one
class "ir.actions.act_window" as ir_actions_act_window
sms_template --> ir_actions_act_window : many2one
class "mail.notification" as mail_notification
sms_tracker --> mail_notification : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




