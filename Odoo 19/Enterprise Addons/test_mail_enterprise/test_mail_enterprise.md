<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Mail Tests (Enterprise)

- Version: v19
- Category: enterprise
- Source: enterprise19/test_mail_enterprise
- Dependencies: [[Odoo 19/Enterprise Addons/ai/ai|ai]], [[Odoo 19/Enterprise Addons/documents/documents|documents]], [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/mail_bot/mail_bot|mail_bot]], [[Odoo 19/Enterprise Addons/mail_enterprise/mail_enterprise|mail_enterprise]], [[Odoo 19/Community Addons/mass_mailing/mass_mailing|mass_mailing]], [[Odoo 19/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]], [[Odoo 19/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]], [[Odoo 19/Enterprise Addons/marketing_automation_sms/marketing_automation_sms|marketing_automation_sms]], [[Odoo 19/Enterprise Addons/mail_mobile/mail_mobile|mail_mobile]], [[Odoo 19/Community Addons/portal/portal|portal]], [[Odoo 19/Community Addons/rating/rating|rating]], [[Odoo 19/Community Addons/snailmail/snailmail|snailmail]], [[Odoo 19/Community Addons/sms/sms|sms]], [[Odoo 19/Community Addons/test_mail/test_mail|test_mail]], [[Odoo 19/Community Addons/test_mail_full/test_mail_full|test_mail_full]], [[Odoo 19/Community Addons/test_mass_mailing/test_mass_mailing|test_mass_mailing]], [[Odoo 19/Community Addons/test_mail_sms/test_mail_sms|test_mail_sms]], [[Odoo 19/Enterprise Addons/voip/voip|voip]], [[Odoo 19/Enterprise Addons/test_whatsapp/test_whatsapp|test_whatsapp]]

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


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mail Tests (Enterprise) - Models and Relations
class "mail.test.activity.bl.sms.voip" as mail_test_activity_bl_sms_voip
class "res.partner" as res_partner
mail_test_activity_bl_sms_voip --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
