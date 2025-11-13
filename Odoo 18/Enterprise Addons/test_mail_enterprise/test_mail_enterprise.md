<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Mail Tests (Enterprise)

- Version: v18
- Category: enterprise
- Source: enterprise18/test_mail_enterprise
- Dependencies: [[Odoo 18/Enterprise Addons/documents/documents|documents]], [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/mail_bot/mail_bot|mail_bot]], [[Odoo 18/Enterprise Addons/mail_enterprise/mail_enterprise|mail_enterprise]], [[Odoo 18/Community Addons/mass_mailing/mass_mailing|mass_mailing]], [[Odoo 18/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]], [[Odoo 18/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]], [[Odoo 18/Enterprise Addons/marketing_automation_sms/marketing_automation_sms|marketing_automation_sms]], [[Odoo 18/Enterprise Addons/mail_mobile/mail_mobile|mail_mobile]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/rating/rating|rating]], [[Odoo 18/Community Addons/snailmail/snailmail|snailmail]], [[Odoo 18/Community Addons/sms/sms|sms]], [[Odoo 18/Community Addons/test_mail/test_mail|test_mail]], [[Odoo 18/Community Addons/test_mail_full/test_mail_full|test_mail_full]], [[Odoo 18/Community Addons/test_mass_mailing/test_mass_mailing|test_mass_mailing]], [[Odoo 18/Community Addons/test_mail_sms/test_mail_sms|test_mail_sms]], [[Odoo 18/Enterprise Addons/voip/voip|voip]], [[Odoo 18/Enterprise Addons/test_whatsapp/test_whatsapp|test_whatsapp]]

## Summary

Mail Tests: performances and tests specific to mail with all sub-modules

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `mail.test.activity.bl.sms.voip`
- `IrAttachment`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mail Tests (Enterprise) - Models and Relations
class "mail.test.activity.bl.sms.voip" as mail_test_activity_bl_sms_voip
class IrAttachment
class "res.partner" as res_partner
mail_test_activity_bl_sms_voip --> res_partner : many2one
class "documents.document" as documents_document
IrAttachment --|> documents_document : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
